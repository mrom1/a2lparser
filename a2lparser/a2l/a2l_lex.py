#######################################################################################
# a2lparser: https://github.com/mrom1/a2lparser                                       #
# author: https://github.com/mrom1                                                    #
#                                                                                     #
# This file is part of the a2lparser package.                                         #
#                                                                                     #
# a2lparser is free software: you can redistribute it and/or modify it                #
# under the terms of the GNU General Public License as published by the               #
# Free Software Foundation, either version 3 of the License, or (at your option)      #
# any later version.                                                                  #
#                                                                                     #
# a2lparser is distributed in the hope that it will be useful,                        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY      #
# or FITNESS FOR A PARTICULAR PURPOSE.                                                #
# See the GNU General Public License for more details.                                #
#                                                                                     #
# You should have received a copy of the GNU General Public License                   #
# along with a2lparser. If not, see <https://www.gnu.org/licenses/>.                  #
#######################################################################################


import re
from ply.lex import lex, LexToken, TOKEN
from a2lparser import A2L_GENERATED_FILES_DIR
from a2lparser.a2l.lex.lexer_regex import LexerRegex
from a2lparser.a2l.lex.lexer_keywords import LexerKeywords


class A2LLex:
    """
    Lexer class for the A2L parser.
    An object of this class may be passed to the ply yacc object as the lexer for parsing.

    Usage:
        >>> lexer = A2LLex()
        >>> y = yacc(...)
        >>> y.parse(lexer=lexer, input=...)
    """

    ###########################
    # Tokens of the A2L Lexer #
    ###########################
    tokens_meta = [
        "ID",
        "BEGIN",
        "END",
        "A2ML_CONTENT",
    ]
    tokens_datatypes = [
        "STRING_LITERAL",
        "INT_CONST_DEC",
        "INT_CONST_HEX",
        "FLOAT_CONST",
        "HEX_FLOAT_CONST",
    ]
    tokens = (
        tokens_meta
        + tokens_datatypes
        + LexerKeywords.keywords_enum
        + LexerKeywords.keywords_section
        + LexerKeywords.keywords_type
        + LexerKeywords.keywords_datatypes
    )
    t_STRING_LITERAL = LexerRegex.string_literal
    t_ignore = " \t\r"

    def __init__(
        self,
        debug: bool = False,
        optimize: bool = True,
        lex_table_file: str = "_a2l_lex_tables",
        generated_files_dir: str = str(A2L_GENERATED_FILES_DIR),
    ) -> None:
        """
        A2L Lexer Constructor.
        Builds an instance of the ply lex object with an A2L configuration.

        Args:
            - debug: will output debug information from ply
            - optimize: optimize flag for the ply lexer
            - lex_table_file: the name of the lex table file
            - generated_files_dir: the directory to write the generated files to
        """
        self.last_token: LexToken = None
        self.progressbar = None
        self.lexer = lex(
            module=self,
            debug=debug,
            optimize=optimize,
            lextab=lex_table_file,
            outputdir=generated_files_dir,
        )

    def token(self) -> LexToken:
        """
        Returns the current token which the lexer processes.
        """
        token = self.lexer.token()
        if token:
            self.last_token = token
        return token

    def get_current_line_position(self) -> int:
        """
        Get the current line number.
        """
        return self.lexer.lineno

    def reset_line_position(self) -> None:
        """
        Resets the current line number of the lexer to 1.
        """
        self.lexer.lineno = 1

    def set_line_position(self, lineno) -> None:
        """
        Sets the current line number to lineno.
        """
        self.lexer.lineno = lineno

    def input(self, text) -> None:
        """
        Passes the input text to the lexer.
        """
        self.lexer.input(text)

    def _error_handling(self, msg, token) -> None:
        """
        This function is called when an error occurs.
        Error handling is to report the error and skip the token.
        """
        self.lexer.skip(1)

    # Disable warning for snake case style, as we want the tokens to be uppercase.
    # pylint: disable=C0103
    def t_error(self, t):
        """
        Triggers when a token could not be interpreted.
        """
        msg = f"Illegal character {repr(t.value[0])}"
        self._error_handling(msg, t)

    @TOKEN(LexerRegex.a2ml_content)
    def t_A2ML_CONTENT(self, t):
        """
        Triggers on any content between /begin A2ML and /end A2ML.
        """
        # Adjusting line counter of the lexer
        lines = t.value.count("\n")
        self.lexer.lineno += lines
        # Pattern for finding and filtering out the /begin and /end A2ML tags
        pattern = r"/\s*(?:begin|BEGIN)\s+A2ML|/\s*(?:end|END)\s+A2ML"
        # Perform a case-insensitive split using re.split
        parts = re.split(pattern, t.value, flags=re.IGNORECASE)
        t.value = parts[1].strip() if len(parts) >= 3 else ""
        # Update progressbar with skipped lines
        if self.progressbar:
            self.progressbar(lines, skipped=True)  # pylint: disable=E1102
        return t

    @TOKEN(LexerRegex.begin_section)
    def t_BEGIN(self, t):
        """
        Triggers when a begin tag token is encountered.
        """
        return t

    @TOKEN(LexerRegex.end_section)
    def t_END(self, t):
        """
        Triggers when a end tag token is encountered.
        """
        return t

    @TOKEN(LexerRegex.newline)
    def t_NEWLINE(self, t):
        """
        Triggered when a newline token has been parsed.
        Will call the progressbar to advance if one has been defined.
        """
        self.lexer.lineno += len(t.value)
        if self.progressbar:
            self.progressbar()  # pylint: disable=E1102

    @TOKEN(
        r"\b("
        + r"|".join(LexerKeywords.keywords_type + LexerKeywords.keywords_enum + LexerKeywords.keywords_datatypes)
        + r")\b"
    )
    def t_KEYWORD_TYPE(self, t):
        """
        Sets the type of the token to the specific keyword found.
        """
        t.type = t.value
        return t

    @TOKEN(r"\b(" + r"|".join(LexerKeywords.keywords_section) + r")\b")
    def t_KEYWORD_SECTION(self, t):
        """
        Sets the type of the token to the specific keyword found.
        """
        t.type = t.value
        return t

    @TOKEN(LexerRegex.identifier)
    def t_ID(self, t):
        """
        Returns a ident token which represents any string, like a name, data etc.
        """
        return t

    @TOKEN(LexerRegex.floating_constant)
    def t_FLOAT_CONST(self, t):
        """
        Returns a floating constant token like 3.14.
        """
        return t

    @TOKEN(LexerRegex.hex_floating_constant)
    def t_HEX_FLOAT_CONST(self, t):
        """
        Returns a hex floating constant token.
        """
        return t

    @TOKEN(LexerRegex.hex_constant)
    def t_INT_CONST_HEX(self, t):
        """
        Returns an integer hexadecimal token like 0x44886600.
        """
        return t

    @TOKEN(LexerRegex.decimal_constant)
    def t_INT_CONST_DEC(self, t):
        """
        Returns a decimal number token.
        """
        return t

    @TOKEN(LexerRegex.comment_singleline)
    def t_COMMENT_SINGLELINE(self, t):
        """
        Any single line comments like "// comment" will be ignored.
        """

    @TOKEN(LexerRegex.comment_multiline)
    def t_COMMENT_MULTILINE(self, t):
        """
        Any multi line comments like "/* comment */" will be ignored.
        """

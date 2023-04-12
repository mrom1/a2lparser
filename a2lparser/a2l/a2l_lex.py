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


from ply.lex import lex, LexToken, TOKEN
from a2lparser import A2L_GENERATED_FILES_DIR
from a2l.lex.lexer_regex import LexerRegex
from a2l.lex.lexer_keywords import LexerKeywords


class A2LLex:
    """
    Lexer class for the A2L parser.
    An object of this class may be passed to the ply yacc object as the lexer for parsing.

    Usage:
        >>> lexer = A2LLex()
        >>> y = yacc(...)
        >>> y.parse(lexer=lexer, input=...)
    """

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
        self.last_token: LexToken
        self.progressbar = None
        self.lexer = lex(
            module=self,
            debug=debug,
            optimize=optimize,
            lextab=lex_table_file,
            outputdir=generated_files_dir,
        )
        self.lexer.lineno = 1

    def token(self) -> LexToken:
        """
        Retruns the current token the lexer processes.
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

    def _error_handling(self, msg, token) -> None:  # pylint: disable=W0613
        """
        This function is called when an error occurs.
        Error handling is to report the error and skip the token.
        """
        self.lexer.skip(1)

    tokens_meta = ["ID", "BEGIN", "END", "STRING_LITERAL", "INT_CONST_DEC", "INT_CONST_HEX", "FLOAT_CONST", "HEX_FLOAT_CONST"]
    tokens = tokens_meta + LexerKeywords.keywords_section + LexerKeywords.keywords_type
    t_STRING_LITERAL = LexerRegex.string_literal
    t_ignore = " \t\r"

    # Disable docstring and camel case
    # pylint: disable=C0103, C0116
    @TOKEN(LexerRegex.newline)
    def t_NEWLINE(self, t):
        self.lexer.lineno += len(t.value)
        if self.progressbar:
            self.progressbar()  # pylint: disable=E1102

    @TOKEN(LexerRegex.identifier)
    def t_ID(self, t):
        return t

    @TOKEN(LexerRegex.floating_constant)
    def t_FLOAT_CONST(self, t):
        return t

    @TOKEN(LexerRegex.hex_floating_constant)
    def t_HEX_FLOAT_CONST(self, t):
        return t

    @TOKEN(LexerRegex.hex_constant)
    def t_INT_CONST_HEX(self, t):
        return t

    @TOKEN(LexerRegex.decimal_constant)
    def t_INT_CONST_DEC(self, t):
        return t

    @TOKEN(LexerRegex.begin_section)
    def t_BEGIN(self, t):
        return t

    @TOKEN(LexerRegex.end_section)
    def t_END(self, t):
        return t

    @TOKEN(LexerRegex.comment_singleline)
    def t_COMMENT_SINGLELINE(self, t):
        pass

    @TOKEN(LexerRegex.comment_multiline)
    def t_COMMENT_MULTILINE(self, t):
        pass

    def t_error(self, t):
        msg = f"Illegal character {repr(t.value[0])}"
        self._error_handling(msg, t)

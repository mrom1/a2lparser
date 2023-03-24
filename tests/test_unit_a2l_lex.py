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


from a2lparser.a2l.a2l_lex import A2LLex


def test_a2l_lexer_data_types():
    """
    Testing the A2L Lexer for detection of various data types.
    """
    decimal_constants = ["123", "-456", "0"]
    float_constants = ["3.1415", "-128.12", "0.0"]
    hex_constants = ["0x12AB", "0XFF", "0xfeed", "0xbeef1234"]
    exp_constants = ["1.23E-4", "2.1e+6", "-1.4e+21"]

    lexer = A2LLex()

    for decimal_constant in decimal_constants:
        lexer.reset_line_number()
        lexer.input(decimal_constant)
        token = lexer.token()
        assert token
        assert token.type == "INT_CONST_DEC"  # type: ignore
        assert token.value == decimal_constant  # type: ignore

    for float_constant in float_constants:
        lexer.reset_line_number()
        lexer.input(float_constant)
        token = lexer.token()
        assert token
        assert token.type == "FLOAT_CONST"  # type: ignore
        assert token.value == float_constant  # type: ignore

    for hex_constant in hex_constants:
        lexer.reset_line_number()
        lexer.input(hex_constant)
        token = lexer.token()
        assert token
        assert token.type == "INT_CONST_HEX"  # type: ignore
        assert token.value == hex_constant  # type: ignore

    for exp_constant in exp_constants:
        lexer.reset_line_number()
        lexer.input(exp_constant)
        token = lexer.token()
        assert token
        assert token.type == "FLOAT_CONST"  # type: ignore
        assert token.value == exp_constant  # type: ignore


def test_a2l_lexer_singleline_comment():
    """
    Testing the A2L Lexer for detection of single line comments.
    """
    singleline_comment = "3.23e-9 // !@: 0x1212DD08 - Some comment."
    lexer = A2LLex()

    tokens = []
    lexer.input(singleline_comment)
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)

    # If parsed successfully only the number should have been detected.
    # Everything after '//' should have been ignored.
    assert len(tokens) == 1
    assert tokens[0].type == "FLOAT_CONST"
    assert tokens[0].value == "3.23e-9"


def test_a2l_lexer_multiline_comment():
    """
    Testing the A2L Lexer for detection of multi line comments.
    """
    multiline_comment = """
    -2.41e+16
    /*
    This is a multi-line comment
    that spans multiple lines.
    0xAAEEDDEE
    It can include whitespace and other
    special characters &%\\!.
    */
    0xFF24A8DD
    """
    lexer = A2LLex()

    tokens = []
    lexer.input(multiline_comment)
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)

    assert len(tokens) > 0

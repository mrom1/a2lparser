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


def test_a2l_lexer_singleline_comment():
    """
    Testing the A2L Lexer for detection of single line comments.
    """
    singleline_comment = "3.23e-9 // !@: 0x1212DD08 - Some comment."
    lexer = A2LLex()

    tokens = []
    lexer.input(singleline_comment)
    while True:
        if token := lexer.token():
            tokens.append(token)
        else:
            break
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
        if token := lexer.token():
            tokens.append(token)
        else:
            break
    # The multi line comment and everything in it should have been ignored
    # so only the two token numbers should be recognized in the string.
    assert tokens
    assert len(tokens) == 2

    # First parsed token should be '-2.41e+16'
    assert tokens[0].type == "FLOAT_CONST"
    assert tokens[0].value == "-2.41e+16"

    # Second parsed token should be '0xFF24A8DD'
    assert tokens[1].type == "INT_CONST_HEX"
    assert tokens[1].value == "0xFF24A8DD"

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
        lexer.input(decimal_constant)
        token = lexer.token()
        assert token
        assert token.type == "INT_CONST_DEC"  # type: ignore
        assert token.value == decimal_constant  # type: ignore

    for float_constant in float_constants:
        lexer.input(float_constant)
        token = lexer.token()
        assert token
        assert token.type == "FLOAT_CONST"  # type: ignore
        assert token.value == float_constant  # type: ignore

    for hex_constant in hex_constants:
        lexer.input(hex_constant)
        token = lexer.token()
        assert token
        assert token.type == "INT_CONST_HEX"  # type: ignore
        assert token.value == hex_constant  # type: ignore

    for exp_constant in exp_constants:
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

    # The multi line comment and everything in it should have been ignored
    # so only the two token numbers should be recognized in the string.
    assert len(tokens) > 0
    assert len(tokens) == 2

    # First parsed token should be '-2.41e+16'
    assert tokens[0].type == "FLOAT_CONST"
    assert tokens[0].value == "-2.41e+16"

    # Second parsed token should be '0xFF24A8DD'
    assert tokens[1].type == "INT_CONST_HEX"
    assert tokens[1].value == "0xFF24A8DD"


def test_a2l_lexer_newline():
    """
    Testing the A2L Lexer for detection of newlines.
    """
    multliline_string = """

    3
    4

    6
    7
    8



    12

    14
    15
    """
    lexer = A2LLex()

    lexer.input(multliline_string)
    while True:
        token = lexer.token()
        if not token:
            break
        assert token.value == str(lexer.get_current_line_position())  # type: ignore


def test_a2l_lexer_begin_end_section():
    """
    Testing the A2L Lexer for detecting a A2L section.
    """
    empty_block = "/begin /end"
    empty_block_keyword = """
    /begin MEASUREMENT
    /end MEASUREMENT
    """
    project_block = """
    /begin project
        PROJECT "My Project"
        VERSION "1.0"
    /end project
    """
    lexer = A2LLex()

    tokens = []
    lexer.input(empty_block)
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
    assert len(tokens) == 2
    assert tokens[0].type == "BEGIN"
    assert tokens[1].type == "END"

    tokens = []
    lexer.input(empty_block_keyword)
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
    assert len(tokens) == 4
    assert tokens[0].type == "BEGIN"
    assert tokens[1].type == "KEYWORD"
    assert tokens[1].value == "MEASUREMENT"
    assert tokens[2].type == "END"
    assert tokens[3].type == "KEYWORD"
    assert tokens[3].value == "MEASUREMENT"

    tokens = []
    lexer.input(project_block)
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
    assert len(tokens) == 8
    assert tokens[0].type == "BEGIN"
    assert tokens[1].type == "KEYWORD"
    assert tokens[1].value == "PROJECT"
    assert tokens[2].type == "ID"
    assert tokens[2].value == "PROJECT"
    assert tokens[3].type == "STRING_LITERAL"
    assert tokens[3].value == '"My Project"'
    assert tokens[4].type == "ID"
    assert tokens[4].value == "VERSION"
    assert tokens[5].type == "STRING_LITERAL"
    assert tokens[5].value == '"1.0"'
    assert tokens[6].type == "END"
    assert tokens[7].type == "KEYWORD"
    assert tokens[7].value == "PROJECT"


def test_a2l_lexer_begin_end_section_whitespace():
    """
    Testing that the begin and end sections can include whitespace characters.
    """
    empty_block_no_whitespace = """
    /begin COMPU_METHOD
    /end compu_method
    """
    empty_block_whitespace = """
    / begin
    / end
    """
    project_block = """
    /  begin project PROJECT "Example Project"
       version "1.0.0"
    /end PROJECT
    """
    lexer = A2LLex()

    tokens = []
    lexer.input(empty_block_no_whitespace)
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
    assert len(tokens) == 4
    assert tokens[0].type == "BEGIN"
    assert tokens[1].type == "KEYWORD"
    assert tokens[1].value == "COMPU_METHOD"
    assert tokens[2].type == "END"
    assert tokens[3].type == "KEYWORD"
    assert tokens[3].value == "COMPU_METHOD"

    tokens = []
    lexer.input(empty_block_whitespace)
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
    assert len(tokens) == 2
    assert tokens[0].type == "BEGIN"
    assert tokens[1].type == "END"

    tokens = []
    lexer.input(project_block)
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
    assert len(tokens) == 8
    assert tokens[0].type == "BEGIN"
    assert tokens[1].type == "KEYWORD"
    assert tokens[1].value == "PROJECT"
    assert tokens[2].type == "ID"
    assert tokens[2].value == "PROJECT"
    assert tokens[3].type == "STRING_LITERAL"
    assert tokens[3].value == '"Example Project"'
    assert tokens[4].type == "ID"
    assert tokens[4].value == "version"
    assert tokens[5].type == "STRING_LITERAL"
    assert tokens[5].value == '"1.0.0"'
    assert tokens[6].type == "END"
    assert tokens[7].type == "KEYWORD"
    assert tokens[7].value == "PROJECT"

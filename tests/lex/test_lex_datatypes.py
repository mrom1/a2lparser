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


import pytest
from a2lparser.a2l.a2l_lex import A2LLex


@pytest.mark.parametrize("decimal_constant", ["123", "-456", "0", "08001", "-01234", "+22"])
def test_lex_datatypes_decimal_constants(decimal_constant):
    """
    Testing the A2L Lexer for detection of decimal numbers.
    """
    lexer = A2LLex()
    lexer.input(decimal_constant)
    token = lexer.token()
    assert token
    assert token.type == "INT_CONST_DEC"
    assert token.value == decimal_constant


@pytest.mark.parametrize("float_constant", ["3.1415", "-128.12", "0.0"])
def test_lex_datatypes_float_constants(float_constant):
    """
    Testing the A2L Lexer for detection of float numbers.
    """
    lexer = A2LLex()
    lexer.input(float_constant)
    token = lexer.token()
    assert token
    assert token.type == "FLOAT_CONST"
    assert token.value == float_constant


@pytest.mark.parametrize("hex_constant", ["0x12AB", "0XFF", "0xfeed", "0xbeef1234"])
def test_lex_datatypes_hex_constants(hex_constant):
    """
    Testing the A2L Lexer for detection of hexadecimal numbers.
    """
    lexer = A2LLex()
    lexer.input(hex_constant)
    token = lexer.token()
    assert token
    assert token.type == "INT_CONST_HEX"
    assert token.value == hex_constant


@pytest.mark.parametrize("exp_constant", ["1.23E-4", "2.1e+6", "-1.4e+21"])
def test_lex_datatypes_exp_constants(exp_constant):
    """
    Testing the A2L Lexer for detection of numbers written with the exponential format.
    """
    lexer = A2LLex()
    lexer.input(exp_constant)
    token = lexer.token()
    assert token
    assert token.type == "FLOAT_CONST"
    assert token.value == exp_constant


@pytest.mark.parametrize(
    "string_literal",
    [
        '"Some test string"',
        '"Some string with a weird escape character\tin it."',
    ],
)
def test_lex_datatypes_string_literals(string_literal):
    """
    Testing the A2L Lexer for detection of numbers written with the exponential format.
    """
    lexer = A2LLex()
    lexer.input(string_literal)
    token = lexer.token()
    assert token
    assert token.type == "STRING_LITERAL"
    assert token.value == string_literal

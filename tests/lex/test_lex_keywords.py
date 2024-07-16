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
from a2lparser.a2l.lex.lexer_keywords import LexerKeywords


@pytest.mark.parametrize("keyword_section", LexerKeywords.keywords_section)
def test_lex_keywords_sections(keyword_section):
    """
    Test the correct interpretation of the tags in a A2L file defining a section.
    A section is defined by being encloused with a "BEGIN" and an "END" tag.

    Example:
        /begin MEASUREMENT
        /end MEASUREMENT
    """
    lexer = A2LLex()
    lexer.input(keyword_section)
    token = lexer.token()
    assert token
    assert token.type == keyword_section


@pytest.mark.parametrize("keyword_type", LexerKeywords.keywords_type)
def test_lex_keywords_types(keyword_type):
    """
    Test the correct interpretation of keyword tags defining types in an A2L file.
    """
    lexer = A2LLex()
    lexer.input(keyword_type)
    token = lexer.token()
    assert token
    assert token.type == keyword_type


@pytest.mark.parametrize("keyword_enum", LexerKeywords.keywords_enum)
def test_lex_keywords_enums(keyword_enum):
    """
    Test the correct interpretation of enum types in an A2L file.
    """
    lexer = A2LLex()
    lexer.input(keyword_enum)
    token = lexer.token()
    assert token


@pytest.mark.parametrize("keyword_datatype", LexerKeywords.keywords_datatypes)
def test_lex_keywords_datatypes(keyword_datatype):
    """
    Test the correct interpretation of data types in an A2L file.
    """
    lexer = A2LLex()
    lexer.input(keyword_datatype)
    token = lexer.token()
    assert token

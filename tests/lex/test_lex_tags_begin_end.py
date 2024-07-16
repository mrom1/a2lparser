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


@pytest.mark.parametrize(
    "begin_tag",
    [
        "/BEGIN",
        "/begin",
        "/ BEGIN",
        "/ begin",
        "/    BEGIN",
        "/      begin",
        " /BEGIN",
        " /begin",
        " /  BEGIN",
        "  / begin",
        " / BEGIN  ",
        " / begin  ",
    ],
)
def test_lex_tags_begin(begin_tag):
    """
    Testing the A2L Lexer for detection of the A2L "BEGIN" tag with whitespaces.
    """
    lexer = A2LLex()
    lexer.input(begin_tag)
    token = lexer.token()
    assert token
    assert token.type == "BEGIN"


@pytest.mark.parametrize(
    "end_tag",
    [
        "/END",
        "/end",
        "/ END",
        "/ end",
        "/    END",
        "/      end",
        " /END",
        " /end",
        " /  END",
        "  / end",
        " / END  ",
        " / end  ",
    ],
)
def test_lex_tags_end(end_tag):
    """
    Testing the A2L Lexer for detection of the A2L "END" tag with whitespaces.
    """
    lexer = A2LLex()
    lexer.input(end_tag)
    token = lexer.token()
    assert token
    assert token.type == "END"


@pytest.mark.parametrize(
    "begin_end_tag",
    [
        "/BEGIN /END",
        "/BEGIN/END",
        "/begin /end",
        "/begin/end",
        "/  BEGIN / END",
        "/ begin /  end",
        "  /BEGIN/END",
        "/  begin/end",
    ],
)
def test_lex_tags_begin_end(begin_end_tag):
    """
    Testing the A2L Lexer for detection of A2L "BEGIN" and "END" tags.
    """
    tokens = []
    lexer = A2LLex()
    lexer.input(begin_end_tag)
    while True:
        if token := lexer.token():
            tokens.append(token)
        else:
            break
    token = lexer.token()
    assert tokens
    assert len(tokens) == 2
    assert tokens[0].type == "BEGIN"
    assert tokens[1].type == "END"

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
from a2lparser.a2l.a2l_validator import A2LValidator


@pytest.mark.parametrize("line, expected_line", [
    ("/begin PROJECT // This is a comment", "/begin PROJECT"),
    ("/begin PROJECT//No space between comment", "/begin PROJECT"),
    ("/begin PROJECT //No space after comment", "/begin PROJECT"),
    ("// /begin PROJECT // This is a comment", ""),
])
def test_validator_inline_comment(line, expected_line):
    """
    Test that a C-Style inline comment ("//") is removed correctly.
    """
    validator = A2LValidator()
    parsed_line = validator._remove_comments(line)
    assert parsed_line == expected_line


@pytest.mark.parametrize("line, expected_line", [
    ("/begin PROJECT /* in between */ /begin HEADER", "/begin PROJECT /begin HEADER"),
    ("/begin PROJECT/*No space between comment*/", "/begin PROJECT"),
    ("/begin PROJECT /*No space after comment*/", "/begin PROJECT"),
    ("/begin PROJECT /* comment\n/begin MODULE /* nested\nEnd of comment.*/\n/*END PROJECT*//end PROJECT",
     "/begin PROJECT /end PROJECT"),
    ("/* /begin PROJECT /* This is a comment */", "")]
)
def test_validator_multiline_comment(line, expected_line):
    """
    Test that a C-Style multiline comment ("/*") is removed correctly.
    """
    validator = A2LValidator()
    parsed_line = validator._remove_comments(line)
    assert parsed_line == expected_line


@pytest.mark.parametrize("line, expected_line", [
    ("/begin PROJECT \"test\"", "/begin PROJECT \"test\""),
    ("/begin PROJECT 'test'", "/begin PROJECT 'test'"),
    ("/begin PROJECT /* some \"string literal\"*/ /end PROJECT", "/begin PROJECT /end PROJECT"),
    ("/begin TEXT 'text // containing /* comments */' /end TEXT", "/begin TEXT 'text // containing /* comments */' /end TEXT"),
    ("/begin TEXT \"text // /* comment */\" /end TEXT", "/begin TEXT \"text // /* comment */\" /end TEXT"),
    ("/begin MODULE /*\"String inside comment\"*/ /end MODULE", "/begin MODULE /end MODULE"),
    ("/begin PROJECT /* 'String inside comment' */ /end PROJECT", "/begin PROJECT /end PROJECT"),
])
def test_validator_string_literals(line, expected_line):
    """
    Test that comment tokens are allowed in string literals.
    """
    validator = A2LValidator()
    parsed_line = validator._remove_comments(line)
    assert parsed_line == expected_line

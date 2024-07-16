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


def test_validator_with_valid_content_simple():
    """
    Test that valid A2L sections pass syntax validation without any error.
    """
    a2l_string = """\
    /begin PROJECT "test"
    /begin MOD_PAR "module"
    /begin CHARACTERISTIC foo
    /end CHARACTERISTIC
    /end MOD_PAR
    /end PROJECT
    """
    A2LValidator().validate(a2l_string)


def test_validator_with_missing_end_statement():
    """
    Tests detection of a missing end statement.
    """
    a2l_string = """\
    /begin PROJECT "test"
    /begin MOD_PAR "module"
    /begin CHARACTERISTIC foo
    /end MOD_PAR
    """
    with pytest.raises(A2LValidator.A2LValidationError) as ex:
        A2LValidator().validate(a2l_string)
    assert len(ex.value.errors) == 4
    assert ex.value.errors[0] == "Detected unexpected end of section on '/end MOD_PAR' at line 4."
    assert ex.value.errors[1] == "Detected unclosed section 'CHARACTERISTIC' starting at line 3."
    assert ex.value.errors[2] == "Detected unclosed section 'MOD_PAR' starting at line 2."
    assert ex.value.errors[3] == "Detected unclosed section 'PROJECT' starting at line 1."


def test_validator_with_missing_begin_statement():
    """
    Tests detection of a missing begin statement.
    """
    a2l_string = """\
    /begin PROJECT "test"
    /begin MOD_PAR "module"
    /end CHARACTERISTIC
    /end MOD_PAR
    /end PROJECT
    """
    with pytest.raises(A2LValidator.A2LValidationError) as ex:
        A2LValidator().validate(a2l_string)
    assert len(ex.value.errors) == 1
    assert ex.value.errors[0] == "Detected unexpected end of section on '/end CHARACTERISTIC' at line 3."


def test_validator_with_nested_structure_error():
    """
    Tests detection of an invalid open / close structure.
    """
    a2l_string = """\
    /begin PROJECT "test"
        /begin MOD_PAR "module"
        /begin CHARACTERISTIC foo
            /begin CURVE foo_curve
        /end CHARACTERISTIC
            /end CURVE
        /end MOD_PAR
    /end PROJECT
    """
    with pytest.raises(A2LValidator.A2LValidationError) as ex:
        A2LValidator().validate(a2l_string)
    assert ex

    assert ex.value.errors[0] == "Detected unexpected end of section on '/end CHARACTERISTIC' at line 5."
    assert ex.value.errors[1] == "Detected unexpected end of section on '/end MOD_PAR' at line 7."
    assert ex.value.errors[2] == "Detected unexpected end of section on '/end PROJECT' at line 8."
    assert ex.value.errors[3] == "Detected unclosed section 'CHARACTERISTIC' starting at line 3."
    assert ex.value.errors[4] == "Detected unclosed section 'MOD_PAR' starting at line 2."
    assert ex.value.errors[5] == "Detected unclosed section 'PROJECT' starting at line 1."


def test_validator_complex_comment_section_valid():
    """
    Tests more complex comments with nested A2L Keywords in them.
    """
    a2l_string = """
    /begin PROJECT "test"
    /begin MODULE M_TEST "test"
    /****************/
    ///begin A2ML
    /****************/
    /BEGIN BLOB TEST_BLOB ""
        /* Test value */
        0x0 1
    /END BLOB
    /****************/
    /*/end A2ML     */
    /****************/
    /end MODULE
    /end PROJECT
    """
    A2LValidator().validate(a2l_string)


def test_validator_complex_comment_section_invalid():
    """
    Tests more complex comments with nested A2L Keywords in them.
    """
    a2l_string = """
    /begin PROJECT "test"
    /begin MODULE M_TEST "test"

    ///begin A2ML

    /****************/
    /* BLOB         */
    /****************/
        /BEGIN BLOB TEST_BLOB ""
            /* Test value */
            0x0 1
        /END BLOB

    /****************/
    /end A2ML
    /****************/
    /end MODULE
    /end PROJECT
    """
    with pytest.raises(A2LValidator.A2LValidationError) as ex:
        A2LValidator().validate(a2l_string)
    assert ex

    assert ex.value.errors[0] == "Detected unexpected end of section on '/end A2ML' at line 16."

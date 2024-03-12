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
    Test that a valid A2L file passes syntax validation without errors.
    """
    a2l_string = """\
    /begin PROJECT "test"
    /begin MOD_PAR "module"
    /begin CHARACTERISTIC foo
    /end CHARACTERISTIC
    /end MOD_PAR
    /end PROJECT
    """
    assert A2LValidator().validate(a2l_string) is None


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
    assert ex.value.errors[0] == "Invalid \"/end MOD_PAR\" found at line 4. Last found section CHARACTERISTIC at line 3."
    assert ex.value.errors[1] == "Found \"/begin PROJECT\" tag without matching /end tag at line 1."
    assert ex.value.errors[2] == "Found \"/begin MOD_PAR\" tag without matching /end tag at line 2."
    assert ex.value.errors[3] == "Found \"/begin CHARACTERISTIC\" tag without matching /end tag at line 3."


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
    assert ex.value.errors[0] == "Invalid \"/end CHARACTERISTIC\" found at line 3. Last found section MOD_PAR at line 2."


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

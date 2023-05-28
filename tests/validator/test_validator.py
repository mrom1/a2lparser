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


def test_validator_with_valid_file():
    """
    Test that a valid A2L file passes syntax validation without errors.
    """
    a2l_string = """\
    /begin PROJECT "test"
    /begin MOD_PAR "module"
    /begin CHARACTERISTIC foo
    /end CHARACTERISTIC
    /end MOD_PAR
    /end PROJECT"""
    assert A2LValidator.validate_syntax(a2l_string) is None


def test_validator_with_missing_end_statement():
    """
    Tests detection of a missing end statement.
    """
    a2l_string = """\
    /begin PROJECT "test"
    /begin MOD_PAR "module"
    /begin CHARACTERISTIC foo
    /end MOD_PAR"""
    with pytest.raises(A2LValidator.A2LValidationError) as ex:
        A2LValidator.validate_syntax(a2l_string)
    assert ex.value.errors[0]
    assert ex.value.errors[0] == "Found /end mod_par tag without matching /begin characteristic tag at line 4, column 5."
    assert ex.value.errors[1]
    assert ex.value.errors[1] == "Found /begin mod_par tag without matching /end tag at line 2, column 5."


def test_validator_with_missing_begin_statement():
    """
    Tests detection of a missing begin statement.
    """
    a2l_string = """\
    /begin PROJECT "test"
    /begin MOD_PAR "module"
    /end CHARACTERISTIC
    /end MOD_PAR
    /end PROJECT"""
    with pytest.raises(A2LValidator.A2LValidationError) as ex:
        A2LValidator.validate_syntax(a2l_string)
    assert ex


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
    /end PROJECT"""
    with pytest.raises(A2LValidator.A2LValidationError) as ex:
        A2LValidator.validate_syntax(a2l_string)
    assert ex

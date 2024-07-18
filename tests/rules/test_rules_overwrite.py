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


from a2lparser.a2l.a2l_yacc import A2LYacc


def test_rules_overwrite_minimal():
    """
    Test A2L OVERWRITE section.
    """
    overwrite_minimal = """
    /begin OVERWRITE
        MyMap 1 // overruling the X axis of
    /end OVERWRITE
    """
    ast = A2LYacc().generate_ast(overwrite_minimal)
    assert ast

    overwrite = ast["OVERWRITE"]
    assert overwrite["Name"] == "MyMap"
    assert overwrite["AxisNumber"] == "1"


def test_rules_overwrite_full():
    """
    Test A2L OVERWRITE section.
    """
    overwrite_full = """
    /begin OVERWRITE
        XcpInstance 3
        CONVERSION ConversionMethod1
        EXTENDED_LIMITS 0 200
        FORMAT "%.2f"
        INPUT_QUANTITY Speed2
        LIMITS 0 160
        MONOTONY STRICT_DECREASE
        PHYS_UNIT "km/h"
    /end OVERWRITE
    """
    ast = A2LYacc().generate_ast(overwrite_full)
    assert ast

    overwrite = ast["OVERWRITE"]
    assert overwrite["Name"] == "XcpInstance"
    assert overwrite["AxisNumber"] == "3"
    assert overwrite["CONVERSION"] == "ConversionMethod1"
    assert overwrite["EXTENDED_LIMITS"] == {"LowerLimit": "0", "UpperLimit": "200"}
    assert overwrite["FORMAT"] == '"%.2f"'
    assert overwrite["INPUT_QUANTITY"] == "Speed2"
    assert overwrite["LIMITS"] == {"LowerLimit": "0", "UpperLimit": "160"}
    assert overwrite["MONOTONY"] == "STRICT_DECREASE"
    assert overwrite["PHYS_UNIT"] == '"km/h"'

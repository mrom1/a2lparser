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


def test_rules_typedef_measurement_minimal():
    """
    Test A2L TYPEDEF_MEASUREMENT section.
    """
    typedef_measurement_minimal = """
    /begin TYPEDEF_MEASUREMENT
        T_Register // type name
        "register content" // description
        UWORD // data type
        RegisterConversion // conversion method
        1 // resolution
        0 // accuracy
        0 // lower limit
        4294967295 // upper limit
    /end TYPEDEF_MEASUREMENT
    """
    ast = A2LYacc().generate_ast(typedef_measurement_minimal)
    assert ast

    typedef_measurement = ast["TYPEDEF_MEASUREMENT"]
    assert typedef_measurement
    assert typedef_measurement["Name"] == "T_Register"
    assert typedef_measurement["LongIdentifier"] == '"register content"'
    assert typedef_measurement["Datatype"] == "UWORD"
    assert typedef_measurement["CONVERSION"] == "RegisterConversion"
    assert typedef_measurement["Resolution"] == "1"
    assert typedef_measurement["Accuracy"] == "0"
    assert typedef_measurement["LowerLimit"] == "0"
    assert typedef_measurement["UpperLimit"] == "4294967295"


def test_rules_typedef_measurement_full():
    """
    Test A2L TYPEDEF_MEASUREMENT section.
    """
    typedef_measurement_full = """
    /begin TYPEDEF_MEASUREMENT
        T_Register // type name
        "register content" // description
        UWORD // data type
        RegisterConversion // conversion method
        1 // resolution
        0 // accuracy
        0 // lower limit
        4294967295 // upper limit
        ADDRESS_TYPE PLONGLONG
        /begin BIT_OPERATION
            LEFT_SHIFT 4
            SIGN_EXTEND
        /end BIT_OPERATION
        BIT_MASK 0x0F
        BYTE_ORDER MSB_LAST_MSW_FIRST
        DISCRETE
        ERROR_MASK 0xCC000000
        FORMAT "10e-5f"
        LAYOUT ALTERNATE_WITH_Y
        MATRIX_DIM 1
        PHYS_UNIT "V"
    /end TYPEDEF_MEASUREMENT
    """
    ast = A2LYacc().generate_ast(typedef_measurement_full)
    assert ast

    typedef_measurement = ast["TYPEDEF_MEASUREMENT"]
    assert typedef_measurement
    assert typedef_measurement["Name"] == "T_Register"
    assert typedef_measurement["LongIdentifier"] == '"register content"'
    assert typedef_measurement["Datatype"] == "UWORD"
    assert typedef_measurement["Resolution"] == "1"
    assert typedef_measurement["Accuracy"] == "0"
    assert typedef_measurement["LowerLimit"] == "0"
    assert typedef_measurement["UpperLimit"] == "4294967295"
    assert typedef_measurement["CONVERSION"] == "RegisterConversion"
    assert typedef_measurement["BIT_MASK"] == "0x0F"
    assert typedef_measurement["ADDRESS_TYPE"] == "PLONGLONG"
    assert typedef_measurement["BYTE_ORDER"] == "MSB_LAST_MSW_FIRST"
    assert typedef_measurement["DISCRETE"] is True
    assert typedef_measurement["ERROR_MASK"] == "0xCC000000"
    assert typedef_measurement["FORMAT"] == '"10e-5f"'
    assert typedef_measurement["LAYOUT"] == "ALTERNATE_WITH_Y"
    assert typedef_measurement["MATRIX_DIM"] == ["1"]
    assert typedef_measurement["PHYS_UNIT"] == '"V"'
    assert typedef_measurement["BIT_OPERATION"] == {
        "LEFT_SHIFT": {"Bitcount": "4"},
        "SIGN_EXTEND": {"Boolean": True},
    }

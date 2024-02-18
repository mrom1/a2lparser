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


def test_rules_typedef_characteristic_minimal():
    """
    Test A2L TYPEDEF_CHARACTERISTIC section.
    """
    typedef_characteristic_minimal = """
    /begin TYPEDEF_CHARACTERISTIC
        T_TIME_MS // type name
        "time in ms" // description
        VALUE // object type
        RL_VALUE_ULONG // record layout
        100.0 // maxdiff
        NO_COMPU_METHOD // no conversion
        10 // lower limit
        65535 // upper limit
    /end TYPEDEF_CHARACTERISTIC
    """
    ast = A2LYacc().generate_ast(typedef_characteristic_minimal)
    assert ast

    typedef_characteristic = ast["TYPEDEF_CHARACTERISTIC"]
    assert typedef_characteristic
    assert typedef_characteristic["Name"] == "T_TIME_MS"
    assert typedef_characteristic["LongIdentifier"] == '"time in ms"'
    assert typedef_characteristic["Type"] == "VALUE"
    assert typedef_characteristic["RecordLayout"] == "RL_VALUE_ULONG"
    assert typedef_characteristic["MaxDiff"] == "100.0"
    assert typedef_characteristic["CONVERSION"] == "NO_COMPU_METHOD"
    assert typedef_characteristic["LowerLimit"] == "10"
    assert typedef_characteristic["UpperLimit"] == "65535"


def test_rules_typedef_characteristic_full():
    """
    Test A2L TYPEDEF_CHARACTERISTIC section.
    """
    typedef_characteristic_full = """
    /begin TYPEDEF_CHARACTERISTIC
        T_TIME_MS // type name
        "time in ms" // description
        VALUE // object type
        RL_VALUE_ULONG // record layout
        100.0 // maxdiff
        CONV_DMMAX // reference to conversion method
        10 // lower limit
        65535 // upper limit
        PHYS_UNIT "ms" // physical unit
        BYTE_ORDER MSB_LAST_MSW_FIRST
        BIT_MASK 0xC
        EXTENDED_LIMITS 0 3500
        /begin AXIS_DESCR CURVE_AXIS /* N axis points */
            N /* Reference to input quantity */
            CONV_STD /* Conversion */
            50 /* Max.number of axis points*/
            0.0 /* Lower limit */
            5000.0 /* Upper limit*/
            STEP_SIZE 25.0 /* Axis: maximum gradient*/
        /end AXIS_DESCR
        FORMAT "%0.01f"
        STEP_SIZE 0.01
        MATRIX_DIM 2 3 4
        NUMBER 7
        ENCODING UTF32
        /begin AXIS_DESCR STD_AXIS /* Standard axis points */
            N /* Reference to input quantity */
            CONV_N /* Conversion */
            5 /* Max.number of axis points*/
            0.0 /* Lower limit */
            1000.0 /* Upper limit*/
            MAX_GRAD 20.0 /* Axis: maximum gradient*/
        /end AXIS_DESCR
    /end TYPEDEF_CHARACTERISTIC
    """
    ast = A2LYacc(debug=True).generate_ast(typedef_characteristic_full)
    assert ast

    typedef_characteristic = ast["TYPEDEF_CHARACTERISTIC"]
    assert typedef_characteristic
    assert typedef_characteristic["Name"] == "T_TIME_MS"
    assert typedef_characteristic["LongIdentifier"] == '"time in ms"'
    assert typedef_characteristic["Type"] == "VALUE"
    assert typedef_characteristic["RecordLayout"] == "RL_VALUE_ULONG"
    assert typedef_characteristic["MaxDiff"] == "100.0"
    assert typedef_characteristic["LowerLimit"] == "10"
    assert typedef_characteristic["UpperLimit"] == "65535"
    assert typedef_characteristic["CONVERSION"] == "CONV_DMMAX"
    assert typedef_characteristic["PHYS_UNIT"] == '"ms"'
    assert typedef_characteristic["BYTE_ORDER"] == "MSB_LAST_MSW_FIRST"
    assert typedef_characteristic["BIT_MASK"] == "0xC"
    assert typedef_characteristic["EXTENDED_LIMITS"] == {"LowerLimit": "0", "UpperLimit": "3500"}
    assert typedef_characteristic["NUMBER"] == "7"
    assert typedef_characteristic["FORMAT"] == '"%0.01f"'
    assert typedef_characteristic["MATRIX_DIM"] == ["2", "3", "4"]
    assert typedef_characteristic["STEP_SIZE"] == "0.01"
    assert typedef_characteristic["ENCODING"] == "UTF32"

    assert len(typedef_characteristic["AXIS_DESCR"]) == 2
    axis_descr_1 = typedef_characteristic["AXIS_DESCR"][0]
    axis_descr_2 = typedef_characteristic["AXIS_DESCR"][1]

    assert axis_descr_1
    assert axis_descr_1["Attribute"] == "CURVE_AXIS"
    assert axis_descr_1["InputQuantity"] == "N"
    assert axis_descr_1["MaxAxisPoints"] == "50"
    assert axis_descr_1["LowerLimit"] == "0.0"
    assert axis_descr_1["UpperLimit"] == "5000.0"
    assert axis_descr_1["CONVERSION"] == "CONV_STD"
    assert axis_descr_1["STEP_SIZE"] == "25.0"

    assert axis_descr_2
    assert axis_descr_2["Attribute"] == "STD_AXIS"
    assert axis_descr_2["InputQuantity"] == "N"
    assert axis_descr_2["MaxAxisPoints"] == "5"
    assert axis_descr_2["LowerLimit"] == "0.0"
    assert axis_descr_2["UpperLimit"] == "1000.0"
    assert axis_descr_2["CONVERSION"] == "CONV_N"
    assert axis_descr_2["MAX_GRAD"] == "20.0"

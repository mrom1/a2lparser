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


def test_rules_measurement():
    """
    Tests parsing a valid "MEASUREMENT" block.
    """
    measurement_block = """
    /begin MEASUREMENT xxx4b4b52c91215c8.xc33258c9abefff4284.x87f0.x871bxxx "ex1"
        SWORD NO_FORMULA 0 0 -32768 32767
        BIT_MASK 0xFFFF
        BYTE_ORDER MSB_FIRST
        ECU_ADDRESS 0x2DDDD
        ECU_ADDRESS_EXTENSION 0x0
        FORMAT "%.3"
        DISCRETE
        /begin IF_DATA CANAPE_EXT
            100
            LINK_MAP "xxx79c13e523bc16dfbba3285.x794ec36d9751f96100fb3400ff.x79f0cb.x791bcbxxx" 0x2D474 0x0 0 0x0 1 0xCF 0x0
            DISPLAY 0 -36044.75 36043.75
        /end IF_DATA
        /begin IF_DATA CANAPE
            DISPLAY 0 -36044.75 36043.75
        /end IF_DATA
        ERROR_MASK 0x00000001
        LAYOUT ALTERNATE_WITH_Y
        MATRIX_DIM 2 4 3
        MAX_REFRESH 998 2
        PHYS_UNIT "Nm"
        READ_WRITE
        REF_MEMORY_SEGMENT Data1
        /begin ANNOTATION
            ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_1"
            ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_1"
            /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_1"
            /end ANNOTATION_TEXT
        /end ANNOTATION
        /begin ANNOTATION
            ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_2"
            ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_2"
            /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_2"
            /end ANNOTATION_TEXT
        /end ANNOTATION
        /begin VIRTUAL
            PHI_BASIS
            PHI_CORR
        /end VIRTUAL
        SYMBOL_LINK
            "_VehicleSpeed" /* Symbol name */
            0 /* Offset */
    /end MEASUREMENT
    """
    parser = A2LYacc()
    ast = parser.generate_ast(measurement_block)
    assert ast

    measurement = ast["MEASUREMENT"]
    assert measurement
    assert measurement["Name"] == "xxx4b4b52c91215c8.xc33258c9abefff4284.x87f0.x871bxxx"
    assert measurement["LongIdentifier"] == '"ex1"'
    assert measurement["Datatype"] == "SWORD"
    assert measurement["CONVERSION"] == "NO_FORMULA"
    assert measurement["Resolution"] == "0"
    assert measurement["Accuracy"] == "0"
    assert measurement["LowerLimit"] == "-32768"
    assert measurement["UpperLimit"] == "32767"
    assert measurement["BIT_MASK"] == "0xFFFF"
    assert measurement["BYTE_ORDER"] == "MSB_FIRST"
    assert measurement["DISCRETE"] is True
    assert measurement["ECU_ADDRESS"] == "0x2DDDD"
    assert measurement["ECU_ADDRESS_EXTENSION"] == "0x0"
    assert measurement["ERROR_MASK"] == "0x00000001"

    assert len(measurement["IF_DATA"]) == 2

    assert measurement["IF_DATA"][0]["Name"] == "CANAPE_EXT"
    assert len(measurement["IF_DATA"][0]["DataParams"]) == 14

    assert measurement["IF_DATA"][1]["Name"] == "CANAPE"
    assert len(measurement["IF_DATA"][1]["DataParams"]) == 4

    assert len(measurement["ANNOTATION"]) == 2

    assert measurement["ANNOTATION"][0]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_BLOCK_1"'
    assert measurement["ANNOTATION"][0]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_BLOCK_1"'
    assert len(measurement["ANNOTATION"][0]["ANNOTATION_TEXT"]) == 1

    assert measurement["ANNOTATION"][1]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_BLOCK_2"'
    assert measurement["ANNOTATION"][1]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_BLOCK_2"'
    assert len(measurement["ANNOTATION"][1]["ANNOTATION_TEXT"]) == 1


def test_rules_in_measurement():
    """
    Tests a A2L IN_MEASUREMENT section.
    """
    in_measurement_input = """
    /begin IN_MEASUREMENT 
        WHEEL_REVOLUTIONS
        ENGINE_SPEED
        RESOLUTION_TICKS
    /end IN_MEASUREMENT
    """
    ast = A2LYacc().generate_ast(in_measurement_input)
    assert ast

    in_measurement = ast["IN_MEASUREMENT"]
    assert in_measurement
    assert in_measurement["Identifier"] == ['WHEEL_REVOLUTIONS', 'ENGINE_SPEED', 'RESOLUTION_TICKS']


def test_rules_out_measurement():
    """
    Tests a A2L OUT_MEASUREMENT section.
    """
    out_measurement_input = """
    /begin OUT_MEASUREMENT OK_FLAG
        SENSOR_FLAG
        FAILURE_FLAG
        GLOBAL_FLAG
    /end OUT_MEASUREMENT
    """
    ast = A2LYacc().generate_ast(out_measurement_input)
    assert ast

    out_measurement = ast["OUT_MEASUREMENT"]
    assert out_measurement
    assert out_measurement["Identifier"] == ['OK_FLAG', 'SENSOR_FLAG', 'FAILURE_FLAG', 'GLOBAL_FLAG']

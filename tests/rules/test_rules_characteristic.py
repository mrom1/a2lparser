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


def test_rules_characteristic():
    """
    Tests parsing a valid "CHARACTERISTIC" block.
    """
    characteristic_block = """
    /begin CHARACTERISTIC
        PUMKF /* name */
        "Pump characteristic map" /* long identifier */
        MAP /* type */
        0x7140 /* address */
        DAMOS_KF /* deposit */
        100.0 /* maxdiff */
        R_VOLTAGE /* conversion */
        0.0 /* lower limit */
        5000.0 /* upper limit */
        BIT_MASK 0x40
        BYTE_ORDER MSB_LAST
        CALIBRATION_ACCESS OFFLINE_CALIBRATION
        COMPARISON_QUANTITY COMPARISON_QUANTITY_NAME
        DISCRETE
        DISPLAY_IDENTIFIER load_engine
        FORMAT "%0.2"
        ECU_ADDRESS_EXTENSION 2
        EXTENDED_LIMITS 0 4000.0
        /begin DEPENDENT_CHARACTERISTIC
            "sin(X1)"
            BETA
        /end DEPENDENT_CHARACTERISTIC
        REF_MEMORY_SEGMENT Data1
        /begin FUNCTION_LIST
            ID_ADJUSTM
            FL_ADJUSTM
            SPEED_LIM
        /end FUNCTION_LIST
        GUARD_RAILS
        MATRIX_DIM 2 4 3
        /begin MAP_LIST
            one two three
        /end MAP_LIST
        NUMBER 123123123
        MAX_REFRESH 3 15
        PHYS_UNIT "Nm"
        READ_ONLY
        STEP_SIZE 3
        /begin IF_DATA
            DIM
            EXTERNAL
            INDIRECT
        /end IF_DATA
        SYMBOL_LINK
            "_VehicleSpeed" /* Symbol name */
            0 /* Offset */
        /begin ANNOTATION
            ANNOTATION_LABEL "ANNOTATION_LABEL_CHARACTERISTIC_1"
            ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_CHARACTERISTIC_1"
        /end ANNOTATION
        /begin ANNOTATION
            ANNOTATION_LABEL "ANNOTATION_LABEL_CHARACTERISTIC_2"
            ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_CHARACTERISTIC_2"
            /begin ANNOTATION_TEXT "ANNOTATION_TEXT_CHARACERISTIC"
            /end ANNOTATION_TEXT
        /end ANNOTATION
        /begin AXIS_DESCR STD_AXIS /* Standard axis points */
            N /* Reference to input quantity */
            CONV_N /* Conversion */
            14 /* Max.number of axis points*/
            0.0 /* Lower limit */
            5800.0 /* Upper limit*/
            /begin ANNOTATION
                ANNOTATION_LABEL "AXIS_DESCR_LABEL_BLOCK_1"
                ANNOTATION_ORIGIN "AXIS_DESCR_ORIGIN_BLOCK_1"
                /begin ANNOTATION_TEXT "AXIS_DESCR_TEXT_BLOCK_1"
                /end ANNOTATION_TEXT
            /end ANNOTATION
            MAX_GRAD 20.0 /* Axis: maximum gradient*/
            AXIS_PTS_REF GRP_N
            BYTE_ORDER MSB_LAST
            FIX_AXIS_PAR 0 4 6
            FIX_AXIS_PAR_DIST 0 100 8
            /begin FIX_AXIS_PAR_LIST
                2 5 9
            /end FIX_AXIS_PAR_LIST
            CURVE_AXIS_REF SPD_NORM
            DEPOSIT ABSOLUTE
            /begin ANNOTATION
                ANNOTATION_LABEL "AXIS_DESCR_LABEL_BLOCK_2"
                ANNOTATION_ORIGIN "AXIS_DESCR_ORIGIN_BLOCK_2"
                /begin ANNOTATION_TEXT "AXIS_DESCR_TEXT_BLOCK_2"
                /end ANNOTATION_TEXT
            /end ANNOTATION
            EXTENDED_LIMITS 0 6000.0
            PHYS_UNIT "Nm"
            READ_ONLY
            STEP_SIZE 0.025
            FORMAT "%4.2"
            MONOTONY MON_INCREASE
        /end AXIS_DESCR
        /begin AXIS_DESCR
            /* description of Y-axis points */
            STD_AXIS /* standard axis points */
            AMOUNT /* reference to input quantity */
            CON_ME /* conversion */
            17 /* maximum number of axis points*/
            0.0 /* lower limit */
            43.0 /* upper limit */
        /end AXIS_DESCR
        /begin VIRTUAL_CHARACTERISTIC
            "sin(X1)"
            B
        /end VIRTUAL_CHARACTERISTIC
    /end CHARACTERISTIC
    """
    parser = A2LYacc()
    ast = parser.generate_ast(characteristic_block)
    assert ast

    characteristic = ast["CHARACTERISTIC"]
    assert characteristic
    assert characteristic["Name"] == "PUMKF"
    assert characteristic["LongIdentifier"] == '"Pump characteristic map"'
    assert characteristic["Type"] == "MAP"
    assert characteristic["Address"] == "0x7140"
    assert characteristic["Deposit_Ref"] == "DAMOS_KF"
    assert characteristic["MaxDiff"] == "100.0"
    assert characteristic["Conversion"] == "R_VOLTAGE"
    assert characteristic["LowerLimit"] == "0.0"
    assert characteristic["UpperLimit"] == "5000.0"
    assert characteristic["BIT_MASK"] == "0x40"
    assert characteristic["BYTE_ORDER"] == "MSB_LAST"
    assert characteristic["CALIBRATION_ACCESS"] == "OFFLINE_CALIBRATION"
    assert characteristic["COMPARISON_QUANTITY"] == "COMPARISON_QUANTITY_NAME"
    assert characteristic["DISCRETE"] is True
    assert characteristic["DISPLAY_IDENTIFIER"] == "load_engine"
    assert characteristic["ECU_ADDRESS_EXTENSION"] == "2"
    assert characteristic["FORMAT"] == '"%0.2"'
    assert characteristic["GUARD_RAILS"] is True
    assert characteristic["NUMBER"] == "123123123"
    assert characteristic["PHYS_UNIT"] == '"Nm"'
    assert characteristic["READ_ONLY"] is True
    assert characteristic["REF_MEMORY_SEGMENT"] == "Data1"
    assert characteristic["STEP_SIZE"] == "3"
    assert characteristic["DEPENDENT_CHARACTERISTIC"]["FORMULA"] == '"sin(X1)"'
    assert characteristic["DEPENDENT_CHARACTERISTIC"]["CHARACTERISTIC"] == ["BETA"]
    assert characteristic["EXTENDED_LIMITS"]["LowerLimit"] == "0"
    assert characteristic["EXTENDED_LIMITS"]["UpperLimit"] == "4000.0"
    assert characteristic["FUNCTION_LIST"]["Name"] == ["ID_ADJUSTM", "FL_ADJUSTM", "SPEED_LIM"]
    assert characteristic["MAP_LIST"]["Name"] == ["one", "two", "three"]
    assert characteristic["MATRIX_DIM"]["xDim"] == "2"
    assert characteristic["MATRIX_DIM"]["yDim"] == "4"
    assert characteristic["MATRIX_DIM"]["zDim"] == "3"
    assert characteristic["MAX_REFRESH"]["ScalingUnit"] == "3"
    assert characteristic["MAX_REFRESH"]["Rate"] == "15"
    assert characteristic["SYMBOL_LINK"]["SymbolName"] == '"_VehicleSpeed"'
    assert characteristic["SYMBOL_LINK"]["Offset"] == "0"
    assert characteristic["VIRTUAL_CHARACTERISTIC"]["FORMULA"] == '"sin(X1)"'
    assert characteristic["VIRTUAL_CHARACTERISTIC"]["CHARACTERISTIC"] == ["B"]
    assert len(characteristic["ANNOTATION"]) == 2
    assert characteristic["ANNOTATION"][0]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_CHARACTERISTIC_1"'
    assert characteristic["ANNOTATION"][0]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_CHARACTERISTIC_1"'
    assert characteristic["ANNOTATION"][1]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_CHARACTERISTIC_2"'
    assert characteristic["ANNOTATION"][1]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_CHARACTERISTIC_2"'
    assert characteristic["ANNOTATION"][1]["ANNOTATION_TEXT"] == ['"ANNOTATION_TEXT_CHARACERISTIC"']
    assert len(characteristic["AXIS_DESCR"]) == 2
    assert characteristic["AXIS_DESCR"][0]["Attribute"] == "STD_AXIS"
    assert characteristic["AXIS_DESCR"][0]["InputQuantity"] == "N"
    assert characteristic["AXIS_DESCR"][0]["Conversion"] == "CONV_N"
    assert characteristic["AXIS_DESCR"][0]["MaxAxisPoints"] == "14"
    assert characteristic["AXIS_DESCR"][0]["LowerLimit"] == "0.0"
    assert characteristic["AXIS_DESCR"][0]["UpperLimit"] == "5800.0"
    assert characteristic["AXIS_DESCR"][0]["AXIS_PTS_REF"] == "GRP_N"
    assert characteristic["AXIS_DESCR"][0]["BYTE_ORDER"] == "MSB_LAST"
    assert characteristic["AXIS_DESCR"][0]["CURVE_AXIS_REF"] == "SPD_NORM"
    assert characteristic["AXIS_DESCR"][0]["DEPOSIT"] == "ABSOLUTE"
    assert characteristic["AXIS_DESCR"][0]["FORMAT"] == '"%4.2"'
    assert characteristic["AXIS_DESCR"][0]["MAX_GRAD"] == "20.0"
    assert characteristic["AXIS_DESCR"][0]["MONOTONY"] == "MON_INCREASE"
    assert characteristic["AXIS_DESCR"][0]["PHYS_UNIT"] == '"Nm"'
    assert characteristic["AXIS_DESCR"][0]["READ_ONLY"] is True
    assert characteristic["AXIS_DESCR"][0]["STEP_SIZE"] == "0.025"
    assert characteristic["AXIS_DESCR"][0]["EXTENDED_LIMITS"]["LowerLimit"] == "0"
    assert characteristic["AXIS_DESCR"][0]["EXTENDED_LIMITS"]["UpperLimit"] == "6000.0"
    assert characteristic["AXIS_DESCR"][0]["FIX_AXIS_PAR"]["Offset"] == "0"
    assert characteristic["AXIS_DESCR"][0]["FIX_AXIS_PAR"]["Shift"] == "4"
    assert characteristic["AXIS_DESCR"][0]["FIX_AXIS_PAR"]["Numberapo"] == "6"
    assert characteristic["AXIS_DESCR"][0]["FIX_AXIS_PAR_DIST"]["Offset"] == "0"
    assert characteristic["AXIS_DESCR"][0]["FIX_AXIS_PAR_DIST"]["Distance"] == "100"
    assert characteristic["AXIS_DESCR"][0]["FIX_AXIS_PAR_DIST"]["Numberapo"] == "8"
    assert characteristic["AXIS_DESCR"][0]["FIX_AXIS_PAR_LIST"]["AxisPts_Value"] == ["2", "5", "9"]
    assert len(characteristic["AXIS_DESCR"][0]["ANNOTATION"]) == 2
    assert characteristic["AXIS_DESCR"][0]["ANNOTATION"][0]["ANNOTATION_LABEL"] == '"AXIS_DESCR_LABEL_BLOCK_1"'
    assert characteristic["AXIS_DESCR"][0]["ANNOTATION"][0]["ANNOTATION_ORIGIN"] == '"AXIS_DESCR_ORIGIN_BLOCK_1"'
    assert characteristic["AXIS_DESCR"][0]["ANNOTATION"][0]["ANNOTATION_TEXT"] == ['"AXIS_DESCR_TEXT_BLOCK_1"']
    assert characteristic["AXIS_DESCR"][0]["ANNOTATION"][1]["ANNOTATION_LABEL"] == '"AXIS_DESCR_LABEL_BLOCK_2"'
    assert characteristic["AXIS_DESCR"][0]["ANNOTATION"][1]["ANNOTATION_ORIGIN"] == '"AXIS_DESCR_ORIGIN_BLOCK_2"'
    assert characteristic["AXIS_DESCR"][0]["ANNOTATION"][1]["ANNOTATION_TEXT"] == ['"AXIS_DESCR_TEXT_BLOCK_2"']
    assert characteristic["AXIS_DESCR"][1]["Attribute"] == "STD_AXIS"
    assert characteristic["AXIS_DESCR"][1]["InputQuantity"] == "AMOUNT"
    assert characteristic["AXIS_DESCR"][1]["Conversion"] == "CON_ME"
    assert characteristic["AXIS_DESCR"][1]["MaxAxisPoints"] == "17"
    assert characteristic["AXIS_DESCR"][1]["LowerLimit"] == "0.0"
    assert characteristic["AXIS_DESCR"][1]["UpperLimit"] == "43.0"
    assert characteristic["IF_DATA"]["DataParams"] == ["EXTERNAL", "INDIRECT"]

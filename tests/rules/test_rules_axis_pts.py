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


def test_rules_axis_pts():
    """
    Tests parsing a valid "AXIS_PTS" block.
    """
    axis_pts_block = """
    /begin AXIS_PTS STV_N /* name */
        "axis points distribution speed" /* long identifier */
        0x9876 /* address */
        N /* input quantity */
        DAMOS_SST /* deposit */
        100.0 /* maxdiff */
        R_SPEED /* conversion */
        21 /* maximum number of axis points */
        0.0 /* lower limit */
        5800.0 /* upper limit */
        /begin ANNOTATION
            ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_1"
            ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_1"
            /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_1"
            /end ANNOTATION_TEXT
        /end ANNOTATION
        GUARD_RAILS /* uses guard rails*/
        REF_MEMORY_SEGMENT Data3
        /begin FUNCTION_LIST
            ID_ADJUSTM
            FL_ADJUSTM
            SPEED_LIM
        /end FUNCTION_LIST
        /begin IF_DATA
            ASAP1B_EXAMPLE /* Name of device */
            /* interface-specific parameters described in A2ML */
            /begin DP_BLOB
                0x12129977
                0xFF
            /end DP_BLOB
            /* interface-specific parameters described in A2ML */
            /begin PA_BLOB
                "Pumpenkennfeld"
                1
                2
                17
            /end PA_BLOB
        /end IF_DATA
        CALIBRATION_ACCESS CALIBRATION
        /begin ANNOTATION
            ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_2"
            ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_2"
            /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_2"
            /end ANNOTATION_TEXT
        /end ANNOTATION
        BYTE_ORDER MSB_LAST
        DISPLAY_IDENTIFIER load_engine
        STEP_SIZE 0.025
        FORMAT "%4.2"
        PHYS_UNIT "Nm"
        ECU_ADDRESS_EXTENSION 2
        MAX_REFRESH 3 10
        MODEL_LINK "axis_points/STV_N.obj"
        READ_ONLY
        SYMBOL_LINK
            "_VehicleSpeed" /* Symbol name */
            0 /* Offset */
        MONOTONY MON_INCREASE
        DEPOSIT ABSOLUTE
        EXTENDED_LIMITS 0 6000.0
        /begin IF_DATA
            ASAP1B_EXAMPLE /* Name of device */
            "TEST_STRING"
            0x0123212 /* some address */
            TEST_IDENT
        /end IF_DATA
    /end AXIS_PTS
    """
    parser = A2LYacc()
    ast = parser.generate_ast(axis_pts_block)
    assert ast

    axis_pts = ast["AXIS_PTS"]
    assert axis_pts
    assert axis_pts["Name"] == "STV_N"
    assert axis_pts["LongIdentifier"] == '"axis points distribution speed"'
    assert axis_pts["Address"] == "0x9876"
    assert axis_pts["InputQuantity"] == "N"
    assert axis_pts["Deposit_Ref"] == "DAMOS_SST"
    assert axis_pts["MaxDiff"] == "100.0"
    assert axis_pts["CONVERSION"] == "R_SPEED"
    assert axis_pts["MaxAxisPoints"] == "21"
    assert axis_pts["LowerLimit"] == "0.0"
    assert axis_pts["UpperLimit"] == "5800.0"
    assert axis_pts["BYTE_ORDER"] == "MSB_LAST"
    assert axis_pts["CALIBRATION_ACCESS"] == "CALIBRATION"
    assert axis_pts["DISPLAY_IDENTIFIER"] == "load_engine"
    assert axis_pts["DEPOSIT"] == "ABSOLUTE"
    assert axis_pts["ECU_ADDRESS_EXTENSION"] == "2"
    assert axis_pts["FORMAT"] == '"%4.2"'
    assert axis_pts["GUARD_RAILS"] is True
    assert axis_pts["MAX_REFRESH"] == {"Rate": "10", "ScalingUnit": "3"}
    assert axis_pts["MONOTONY"] == "MON_INCREASE"
    assert axis_pts["PHYS_UNIT"] == '"Nm"'
    assert axis_pts["READ_ONLY"] is True
    assert axis_pts["REF_MEMORY_SEGMENT"] == "Data3"
    assert axis_pts["STEP_SIZE"] == "0.025"
    assert axis_pts["EXTENDED_LIMITS"]["LowerLimit"] == "0"
    assert axis_pts["EXTENDED_LIMITS"]["UpperLimit"] == "6000.0"
    assert axis_pts["FUNCTION_LIST"]["Name"] == ["ID_ADJUSTM", "FL_ADJUSTM", "SPEED_LIM"]
    assert axis_pts["SYMBOL_LINK"]["SymbolName"] == '"_VehicleSpeed"'
    assert axis_pts["SYMBOL_LINK"]["Offset"] == "0"
    assert axis_pts["ANNOTATION"][0]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_BLOCK_1"'
    assert axis_pts["ANNOTATION"][0]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_BLOCK_1"'
    assert axis_pts["ANNOTATION"][0]["ANNOTATION_TEXT"] == ['"ANNOTATION_TEXT_BLOCK_1"']
    assert axis_pts["ANNOTATION"][1]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_BLOCK_2"'
    assert axis_pts["ANNOTATION"][1]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_BLOCK_2"'
    assert axis_pts["ANNOTATION"][1]["ANNOTATION_TEXT"] == ['"ANNOTATION_TEXT_BLOCK_2"']
    assert axis_pts["IF_DATA"][0]["Name"] == "ASAP1B_EXAMPLE"
    assert axis_pts["IF_DATA"][0]["If_Data_Block"][0]["Name"] == "DP_BLOB"
    assert axis_pts["IF_DATA"][0]["If_Data_Block"][0]["DataParams"] == ["0x12129977", "0xFF"]
    assert axis_pts["IF_DATA"][0]["If_Data_Block"][1]["Name"] == "PA_BLOB"
    assert axis_pts["IF_DATA"][0]["If_Data_Block"][1]["DataParams"] == ['"Pumpenkennfeld"', "1", "2", "17"]
    assert axis_pts["IF_DATA"][1]["DataParams"] == ['"TEST_STRING"', "0x0123212", "TEST_IDENT"]

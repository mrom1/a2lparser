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


def test_rules_module():
    """
    Tests parsing a valid "MODULE" block.
    """
    module_block = """
    /begin MODULE
        _default_ModuleName
        "_default_ModuleLongIdentifier"

        /begin AXIS_PTS STV_N "first block" 0x9876 N DAMOS_SST 100.0 R_SPEED 21 0.0 5800.0
        /end AXIS_PTS
        /begin AXIS_PTS STV_N "first block" 0x9876 N DAMOS_SST 100.0 R_SPEED 21 0.0 5800.0
        /end AXIS_PTS

        /begin CHARACTERISTIC PUMKF "Pump characteristic map" MAP 0x7140 DAMOS_KF 100.0 R_VOLTAGE 0.0 5000.0
        /end CHARACTERISTIC
        /begin CHARACTERISTIC PUMKF "Characteristic map" MAP 0xFFFF DAMOS_KF 124.0 R_VOLTAGE 0.0 1000.0
        /end CHARACTERISTIC

        /begin COMPU_METHOD CM_N_SB_03 "CM_Force" TAB_INTP "%3.41" "N"
        /end COMPU_METHOD
        /begin COMPU_METHOD CM_V_SB_06 "CM_Voltage" TAB_INTP "%12.3" "V"
        /end COMPU_METHOD

        /begin COMPU_TAB TT  "conversion table for oil temperatures" TAB_NOINTP 7
            1 4.3 2 4.7 3 5.8 4 14.2 5 16.8 6 17.2 7 19.4 /* value pairs */
        /end COMPU_TAB
        /begin COMPU_TAB TT  "conversion table for oil temperatures" TAB_NOINTP 7
            1 4.3 2 4.7 3 5.8 4 14.2 5 16.8 6 17.2 7 19.4 /* value pairs */
        /end COMPU_TAB

        /begin COMPU_VTAB CM_BuiltInDTypeId "LONG" TAB_VERB 9
          0 "SS_DOUBLE"
          1 "SS_SINGLE"
        /end COMPU_VTAB
        /begin COMPU_VTAB CM_BuiltInDTypeId "LONG" TAB_VERB 9
          0 "SS_DOUBLE"
          1 "SS_SINGLE"
        /end COMPU_VTAB

        /begin COMPU_VTAB_RANGE SAR_ASS_REQ_AX "Active assistant"
            33
            0 0 "IDLE"
            1 1 "NDEF1"
            2 2 "ACTV"
        /end COMPU_VTAB_RANGE
        /begin COMPU_VTAB_RANGE SAR_ASS_REQ_AX "Active assistant"
            399
            3 3 "XT_ACTV"
            64 255 "not defined"
        /end COMPU_VTAB_RANGE

        /begin FRAME ABS_ADJUSTM "function group ABS adjustment" 3 2
        /end FRAME
        /begin FRAME ABS_ADJUSTN "function group ABS" 8 4
        /end FRAME

        /begin FUNCTION CalcStopDynDecel "IDENT_LNG"
        /end FUNCTION
        /begin FUNCTION CalcStartIncr "IDENT_BYTE"
        /end FUNCTION

        /begin GROUP CUSTSWC "Subsys"
        /end GROUP
        /begin GROUP CUSTBSW "Subsystem"
        /end GROUP

        /begin IF_DATA XCP LINK_MAP ref_name 0x003432
        /end IF_DATA
        /begin IF_DATA CANAPE STATIC ref_name 0xFF
        /end IF_DATA

        /begin MEASUREMENT measurement_1 "ID" SWORD DC_PCT_100 1 100. -327.68 327.67
        /end MEASUREMENT
        /begin MEASUREMENT measurement_2 "ID" UBYTE DC_PCT_100 1 100. -327.68 327.67
        /end MEASUREMENT

        /begin RECORD_LAYOUT record_layout_1
        /end RECORD_LAYOUT
        /begin RECORD_LAYOUT record_layout_2
        /end RECORD_LAYOUT

        /begin UNIT kms_per_hour
            "derived unit for velocity: kilometres per hour"
            "[km/h]"
            DERIVED
        /end UNIT
        /begin UNIT kms_per_hour
            "derived unit for velocity: kilometres per hour"
            "[km/h]"
            DERIVED
        /end UNIT

        /begin USER_RIGHTS user_group_1
        /end USER_RIGHTS
        /begin USER_RIGHTS user_group_2
        /end USER_RIGHTS

        /begin MOD_COMMON "_default_ModCommonComment"
        /end MOD_COMMON

        /begin MOD_PAR "_default_ModParComment"
        /end MOD_PAR
    /end MODULE
    """
    parser = A2LYacc()
    ast = parser.generate_ast(module_block)
    assert ast

    # Module
    module = ast["MODULE"]
    assert module
    assert module["Name"] == "_default_ModuleName"
    assert module["LongIdentifier"] == '"_default_ModuleLongIdentifier"'
    assert module["MOD_COMMON"]["Comment"] == '"_default_ModCommonComment"'
    assert module["MOD_PAR"]["Comment"] == '"_default_ModParComment"'

    # AXIS_PTS
    assert len(module["AXIS_PTS"]) == 2
    assert module["AXIS_PTS"][0]["Name"] == "STV_N"
    assert module["AXIS_PTS"][0]["LongIdentifier"] == '"first block"'
    assert module["AXIS_PTS"][0]["Address"] == "0x9876"
    assert module["AXIS_PTS"][0]["InputQuantity"] == "N"
    assert module["AXIS_PTS"][0]["Deposit_Ref"] == "DAMOS_SST"
    assert module["AXIS_PTS"][0]["MaxDiff"] == "100.0"
    assert module["AXIS_PTS"][0]["Conversion"] == "R_SPEED"
    assert module["AXIS_PTS"][0]["MaxAxisPoints"] == "21"
    assert module["AXIS_PTS"][0]["LowerLimit"] == "0.0"
    assert module["AXIS_PTS"][0]["UpperLimit"] == "5800.0"

    assert module["AXIS_PTS"][1]["Name"] == "STV_N"
    assert module["AXIS_PTS"][1]["LongIdentifier"] == '"first block"'
    assert module["AXIS_PTS"][1]["Address"] == "0x9876"
    assert module["AXIS_PTS"][1]["InputQuantity"] == "N"
    assert module["AXIS_PTS"][1]["Deposit_Ref"] == "DAMOS_SST"
    assert module["AXIS_PTS"][1]["MaxDiff"] == "100.0"
    assert module["AXIS_PTS"][1]["Conversion"] == "R_SPEED"
    assert module["AXIS_PTS"][1]["MaxAxisPoints"] == "21"
    assert module["AXIS_PTS"][1]["LowerLimit"] == "0.0"
    assert module["AXIS_PTS"][1]["UpperLimit"] == "5800.0"

    # CHARACTERISTIC
    assert len(module["CHARACTERISTIC"]) == 2
    assert module["CHARACTERISTIC"][0]["Name"] == "PUMKF"
    assert module["CHARACTERISTIC"][0]["LongIdentifier"] == '"Pump characteristic map"'
    assert module["CHARACTERISTIC"][0]["Type"] == "MAP"
    assert module["CHARACTERISTIC"][0]["Address"] == "0x7140"
    assert module["CHARACTERISTIC"][0]["Deposit_Ref"] == "DAMOS_KF"
    assert module["CHARACTERISTIC"][0]["MaxDiff"] == "100.0"
    assert module["CHARACTERISTIC"][0]["Conversion"] == "R_VOLTAGE"
    assert module["CHARACTERISTIC"][0]["LowerLimit"] == "0.0"
    assert module["CHARACTERISTIC"][0]["UpperLimit"] == "5000.0"
    assert module["CHARACTERISTIC"][1]["Name"] == "PUMKF"
    assert module["CHARACTERISTIC"][1]["LongIdentifier"] == '"Characteristic map"'
    assert module["CHARACTERISTIC"][1]["Type"] == "MAP"
    assert module["CHARACTERISTIC"][1]["Address"] == "0xFFFF"
    assert module["CHARACTERISTIC"][1]["Deposit_Ref"] == "DAMOS_KF"
    assert module["CHARACTERISTIC"][1]["MaxDiff"] == "124.0"
    assert module["CHARACTERISTIC"][1]["Conversion"] == "R_VOLTAGE"
    assert module["CHARACTERISTIC"][1]["LowerLimit"] == "0.0"
    assert module["CHARACTERISTIC"][1]["UpperLimit"] == "1000.0"

    # COMPU_METHOD
    assert len(module["COMPU_METHOD"]) == 2
    assert module["COMPU_METHOD"][0]["Name"] == "CM_N_SB_03"
    assert module["COMPU_METHOD"][0]["LongIdentifier"] == '"CM_Force"'
    assert module["COMPU_METHOD"][0]["ConversionType"] == "TAB_INTP"
    assert module["COMPU_METHOD"][0]["FORMAT"] == '"%3.41"'
    assert module["COMPU_METHOD"][0]["UNIT"] == '"N"'
    assert module["COMPU_METHOD"][1]["Name"] == "CM_V_SB_06"
    assert module["COMPU_METHOD"][1]["LongIdentifier"] == '"CM_Voltage"'
    assert module["COMPU_METHOD"][1]["ConversionType"] == "TAB_INTP"
    assert module["COMPU_METHOD"][1]["FORMAT"] == '"%12.3"'
    assert module["COMPU_METHOD"][1]["UNIT"] == '"V"'

    # COMPU_TAB
    assert len(module["COMPU_TAB"]) == 2
    assert module["COMPU_TAB"][0]["Name"] == "TT"
    assert module["COMPU_TAB"][0]["LongIdentifier"] == '"conversion table for oil temperatures"'
    assert module["COMPU_TAB"][0]["ConversionType"] == "TAB_NOINTP"
    assert module["COMPU_TAB"][0]["NumberValuePairs"] == "7"
    assert len(module["COMPU_TAB"][0]["Axis_Points"]) == 7
    assert module["COMPU_TAB"][0]["Axis_Points"] == [
        ["1", "4.3"],
        ["2", "4.7"],
        ["3", "5.8"],
        ["4", "14.2"],
        ["5", "16.8"],
        ["6", "17.2"],
        ["7", "19.4"],
    ]
    assert module["COMPU_TAB"][1]["Name"] == "TT"
    assert module["COMPU_TAB"][1]["LongIdentifier"] == '"conversion table for oil temperatures"'
    assert module["COMPU_TAB"][1]["ConversionType"] == "TAB_NOINTP"
    assert module["COMPU_TAB"][1]["NumberValuePairs"] == "7"
    assert len(module["COMPU_TAB"][1]["Axis_Points"]) == 7
    assert module["COMPU_TAB"][1]["Axis_Points"] == [
        ["1", "4.3"],
        ["2", "4.7"],
        ["3", "5.8"],
        ["4", "14.2"],
        ["5", "16.8"],
        ["6", "17.2"],
        ["7", "19.4"],
    ]

    # COMPU_VTAB assertions
    assert module["COMPU_VTAB"]
    assert len(module["COMPU_VTAB"]) == 2
    assert module["COMPU_VTAB"][0]["Name"] == "CM_BuiltInDTypeId"
    assert module["COMPU_VTAB"][0]["LongIdentifier"] == '"LONG"'
    assert module["COMPU_VTAB"][0]["ConversionType"] == "TAB_VERB"
    assert module["COMPU_VTAB"][0]["NumberValuePairs"] == "9"
    assert len(module["COMPU_VTAB"][0]["InVal_OutVal"]) == 2
    assert module["COMPU_VTAB"][0]["InVal_OutVal"][0] == ["0", '"SS_DOUBLE"']
    assert module["COMPU_VTAB"][0]["InVal_OutVal"][1] == ["1", '"SS_SINGLE"']
    assert module["COMPU_VTAB"][1]["Name"] == "CM_BuiltInDTypeId"
    assert module["COMPU_VTAB"][1]["LongIdentifier"] == '"LONG"'
    assert module["COMPU_VTAB"][1]["ConversionType"] == "TAB_VERB"
    assert module["COMPU_VTAB"][1]["NumberValuePairs"] == "9"
    assert len(module["COMPU_VTAB"][1]["InVal_OutVal"]) == 2
    assert module["COMPU_VTAB"][1]["InVal_OutVal"][0] == ["0", '"SS_DOUBLE"']
    assert module["COMPU_VTAB"][1]["InVal_OutVal"][1] == ["1", '"SS_SINGLE"']

    # COMPU_VTAB_RANGE asserts
    assert len(module["COMPU_VTAB_RANGE"]) == 2
    assert module["COMPU_VTAB_RANGE"][0]["Name"] == "SAR_ASS_REQ_AX"
    assert module["COMPU_VTAB_RANGE"][0]["LongIdentifier"] == '"Active assistant"'
    assert module["COMPU_VTAB_RANGE"][0]["NumberValueTriples"] == "33"
    assert len(module["COMPU_VTAB_RANGE"][0]["InVal_MinMax_OutVal"]) == 3
    assert module["COMPU_VTAB_RANGE"][0]["InVal_MinMax_OutVal"] == [
        ["0", "0", '"IDLE"'],
        ["1", "1", '"NDEF1"'],
        ["2", "2", '"ACTV"'],
    ]
    assert module["COMPU_VTAB_RANGE"][1]["Name"] == "SAR_ASS_REQ_AX"
    assert module["COMPU_VTAB_RANGE"][1]["LongIdentifier"] == '"Active assistant"'
    assert module["COMPU_VTAB_RANGE"][1]["NumberValueTriples"] == "399"
    assert len(module["COMPU_VTAB_RANGE"][1]["InVal_MinMax_OutVal"]) == 2
    assert module["COMPU_VTAB_RANGE"][1]["InVal_MinMax_OutVal"] == [
        ["3", "3", '"XT_ACTV"'],
        ["64", "255", '"not defined"'],
    ]

    # FRAME asserts
    assert len(module["FRAME"]) == 2
    assert module["FRAME"][0]["Name"] == "ABS_ADJUSTM"
    assert module["FRAME"][0]["LongIdentifier"] == '"function group ABS adjustment"'
    assert module["FRAME"][0]["ScalingUnit"] == "3"
    assert module["FRAME"][0]["Rate"] == "2"
    assert module["FRAME"][1]["Name"] == "ABS_ADJUSTN"
    assert module["FRAME"][1]["LongIdentifier"] == '"function group ABS"'
    assert module["FRAME"][1]["ScalingUnit"] == "8"
    assert module["FRAME"][1]["Rate"] == "4"

    # FUNCTION asserts
    assert len(module["FUNCTION"]) == 2
    assert module["FUNCTION"][0]["Name"] == "CalcStopDynDecel"
    assert module["FUNCTION"][0]["LongIdentifier"] == '"IDENT_LNG"'
    assert module["FUNCTION"][1]["Name"] == "CalcStartIncr"
    assert module["FUNCTION"][1]["LongIdentifier"] == '"IDENT_BYTE"'

    # GROUP asserts
    assert len(module["GROUP"]) == 2
    assert module["GROUP"][0]["GroupName"] == "CUSTSWC"
    assert module["GROUP"][0]["GroupLongIdentifier"] == '"Subsys"'
    assert module["GROUP"][1]["GroupName"] == "CUSTBSW"
    assert module["GROUP"][1]["GroupLongIdentifier"] == '"Subsystem"'

    # IF_DATA asserts
    assert len(module["IF_DATA"]) == 2
    assert module["IF_DATA"][0]["Name"] == "XCP"
    assert module["IF_DATA"][0]["DataParams"] == ["LINK_MAP", "ref_name", "0x003432"]
    assert module["IF_DATA"][1]["Name"] == "CANAPE"
    assert module["IF_DATA"][1]["DataParams"] == ["STATIC", "ref_name", "0xFF"]

    # MEASUREMENT asserts
    assert len(module["MEASUREMENT"]) == 2
    assert module["MEASUREMENT"][0]["Name"] == "measurement_1"
    assert module["MEASUREMENT"][0]["LongIdentifier"] == '"ID"'
    assert module["MEASUREMENT"][0]["Datatype"] == "SWORD"
    assert module["MEASUREMENT"][0]["Conversion"] == "DC_PCT_100"
    assert module["MEASUREMENT"][0]["Resolution"] == "1"
    assert module["MEASUREMENT"][0]["Accuracy"] == "100."
    assert module["MEASUREMENT"][0]["LowerLimit"] == "-327.68"
    assert module["MEASUREMENT"][0]["UpperLimit"] == "327.67"
    assert module["MEASUREMENT"][1]["Name"] == "measurement_2"
    assert module["MEASUREMENT"][1]["LongIdentifier"] == '"ID"'
    assert module["MEASUREMENT"][1]["Datatype"] == "UBYTE"
    assert module["MEASUREMENT"][1]["Conversion"] == "DC_PCT_100"
    assert module["MEASUREMENT"][1]["Resolution"] == "1"
    assert module["MEASUREMENT"][1]["Accuracy"] == "100."
    assert module["MEASUREMENT"][1]["LowerLimit"] == "-327.68"
    assert module["MEASUREMENT"][0]["UpperLimit"] == "327.67"

    # RECORD_LAYOUT asserts
    assert len(module["RECORD_LAYOUT"]) == 2
    assert module["RECORD_LAYOUT"][0]["Name"] == "record_layout_1"
    assert module["RECORD_LAYOUT"][1]["Name"] == "record_layout_2"

    # UNIT asserts
    assert len(module["UNIT"]) == 2
    assert module["UNIT"][0]["Name"] == "kms_per_hour"
    assert module["UNIT"][0]["LongIdentifier"] == '"derived unit for velocity: kilometres per hour"'
    assert module["UNIT"][0]["Display"] == '"[km/h]"'
    assert module["UNIT"][0]["Type"] == "DERIVED"
    assert module["UNIT"][1]["Name"] == "kms_per_hour"
    assert module["UNIT"][1]["LongIdentifier"] == '"derived unit for velocity: kilometres per hour"'
    assert module["UNIT"][1]["Display"] == '"[km/h]"'
    assert module["UNIT"][1]["Type"] == "DERIVED"

    # USER_RIGHTS asserts
    assert len(module["USER_RIGHTS"]) == 2
    assert module["USER_RIGHTS"][0]["UserLevelId"] == "user_group_1"
    assert module["USER_RIGHTS"][1]["UserLevelId"] == "user_group_2"

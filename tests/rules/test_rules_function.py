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


def test_rules_function():
    """
    Tests parsing a valid "FUNCTION" block.
    """
    function_block = """
    /begin FUNCTION
        Sssm140_CalcStopDynDecel
        "IDENT_LNG"
        FUNCTION_VERSION "BG5.0815"
        /begin IF_DATA MAP_REF_ADDR
            LINK_MAP ref_name 0x003432
        /end IF_DATA
        /begin SUB_FUNCTION
            CalcDynDecelState
            CalcStopDynDecel
            Sssm313_AEB_disabled
            Sssm314_AEB_enabled
            Sssm37_Subsystem
        /end SUB_FUNCTION
        /begin AR_COMPONENT
            "ApplicationSwComponentType"
            AR_PROTOTYPE_OF "HANDLE"
        /end AR_COMPONENT
        /begin LOC_MEASUREMENT
            SsmInLastWinsThreshold
            SsmInThrottlePedalPosition
        /end LOC_MEASUREMENT
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
        /begin DEF_CHARACTERISTIC
            INJECTION_CURVE
            DELAY_FACTOR
        /end DEF_CHARACTERISTIC
        /begin IN_MEASUREMENT
            WHEEL_REVOLUTIONS
            ENGINE_SPEED
        /end IN_MEASUREMENT
        /begin OUT_MEASUREMENT
            OK_FLAG
            SENSOR_FLAG
        /end OUT_MEASUREMENT
        /begin IF_DATA XCP_REF_ADDR
            XCP_REF_MAP 0x00332266
        /end IF_DATA
        /begin REF_CHARACTERISTIC
            ENG_SPEED_CORR_CURVE
            ENG_SPEED_CORR_CURVE_STD
        /end REF_CHARACTERISTIC
    /end FUNCTION
    """
    parser = A2LYacc()
    ast = parser.generate_ast(function_block)
    assert ast

    function = ast["FUNCTION"]
    assert function
    assert function["Name"] == "Sssm140_CalcStopDynDecel"
    assert function["LongIdentifier"] == '"IDENT_LNG"'
    assert function["FUNCTION_VERSION"] == '"BG5.0815"'
    assert function["DEF_CHARACTERISTIC"]["Identifier"] == ["INJECTION_CURVE", "DELAY_FACTOR"]
    assert function["IN_MEASUREMENT"]["Identifier"] == ["WHEEL_REVOLUTIONS", "ENGINE_SPEED"]
    assert function["LOC_MEASUREMENT"]["Identifier"] == [
        "SsmInLastWinsThreshold",
        "SsmInThrottlePedalPosition",
    ]
    assert function["OUT_MEASUREMENT"]["Identifier"] == ["OK_FLAG", "SENSOR_FLAG"]
    assert function["REF_CHARACTERISTIC"]["Identifier"] == [
        "ENG_SPEED_CORR_CURVE",
        "ENG_SPEED_CORR_CURVE_STD",
    ]
    assert function["AR_COMPONENT"]["ComponentType"] == '"ApplicationSwComponentType"'
    assert function["AR_COMPONENT"]["AR_PROTOTYPE_OF"] == '"HANDLE"'
    assert function["ANNOTATION"][0]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_BLOCK_1"'
    assert function["ANNOTATION"][0]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_BLOCK_1"'
    assert function["ANNOTATION"][0]["ANNOTATION_TEXT"] == ['"ANNOTATION_TEXT_BLOCK_1"']
    assert function["ANNOTATION"][1]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_BLOCK_2"'
    assert function["ANNOTATION"][1]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_BLOCK_2"'
    assert function["ANNOTATION"][1]["ANNOTATION_TEXT"] == ['"ANNOTATION_TEXT_BLOCK_2"']
    assert function["SUB_FUNCTION"]["Identifier"] == [
        "CalcDynDecelState",
        "CalcStopDynDecel",
        "Sssm313_AEB_disabled",
        "Sssm314_AEB_enabled",
        "Sssm37_Subsystem",
    ]
    assert len(function["IF_DATA"]) == 2
    if_data_map = function["IF_DATA"][0]
    if_data_xcp = function["IF_DATA"][1]
    assert if_data_map
    assert if_data_xcp
    assert if_data_map["Name"] == "MAP_REF_ADDR"
    assert if_data_map["DataParams"] == ["LINK_MAP", "ref_name", "0x003432"]
    assert if_data_xcp["Name"] == "XCP_REF_ADDR"
    assert if_data_xcp["DataParams"] == ["XCP_REF_MAP", "0x00332266"]

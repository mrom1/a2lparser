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


def test_rules_group():
    """
    Tests parsing a valid "GROUP" block.
    """
    group_block = """
    /begin GROUP
        CUSTBSW
        "Subsystem"
        ROOT
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
        /begin SUB_GROUP
            AAS
            LRG
            Sar
        /end SUB_GROUP
        /begin REF_MEASUREMENT
            CustBsw_Init_Current_Loop
            CustBsw_Init_Previous_Loop
        /end REF_MEASUREMENT
        /begin REF_CHARACTERISTIC
            ENG_SPEED_CORR_CURVE
            XAS_ENG_SPEED_CORR_CURVE
        /end REF_CHARACTERISTIC
        /begin FUNCTION_LIST
            ID_ADJUSTM
            FL_ADJUSTM
            SPEED_LIM
        /end FUNCTION_LIST
        /begin IF_DATA MAP_REF_ADDR
            LINK_MAP ref_name 0x003432
        /end IF_DATA
        /begin IF_DATA XCP_REF_ADDR
            XCP_REF_MAP 0x00332266
        /end IF_DATA
    /end GROUP
    """
    parser = A2LYacc()
    ast = parser.generate_ast(group_block)
    assert ast

    group = ast["GROUP"]
    assert group
    assert group["GroupName"] == "CUSTBSW"
    assert group["GroupLongIdentifier"] == '"Subsystem"'
    assert group["ROOT"] is True
    assert group["FUNCTION_LIST"]["Name"] == ["ID_ADJUSTM", "FL_ADJUSTM", "SPEED_LIM"]
    assert group["REF_CHARACTERISTIC"]["Identifier"] == [
        "ENG_SPEED_CORR_CURVE",
        "XAS_ENG_SPEED_CORR_CURVE",
    ]
    assert group["REF_MEASUREMENT"]["Identifier"] == [
        "CustBsw_Init_Current_Loop",
        "CustBsw_Init_Previous_Loop",
    ]
    assert group["SUB_GROUP"]["Identifier"] == ["AAS", "LRG", "Sar"]
    assert group["ANNOTATION"][0]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_BLOCK_1"'
    assert group["ANNOTATION"][0]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_BLOCK_1"'
    assert group["ANNOTATION"][0]["ANNOTATION_TEXT"] == ['"ANNOTATION_TEXT_BLOCK_1"']
    assert group["ANNOTATION"][1]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_BLOCK_2"'
    assert group["ANNOTATION"][1]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_BLOCK_2"'
    assert group["ANNOTATION"][1]["ANNOTATION_TEXT"] == ['"ANNOTATION_TEXT_BLOCK_2"']
    assert len(group["IF_DATA"]) == 2
    if_data_map = group["IF_DATA"][0]
    if_data_xcp = group["IF_DATA"][1]
    assert if_data_map
    assert if_data_xcp
    assert if_data_map["Name"] == "MAP_REF_ADDR"
    assert if_data_map["DataParams"] == ["LINK_MAP", "ref_name", "0x003432"]
    assert if_data_xcp["Name"] == "XCP_REF_ADDR"
    assert if_data_xcp["DataParams"] == ["XCP_REF_MAP", "0x00332266"]

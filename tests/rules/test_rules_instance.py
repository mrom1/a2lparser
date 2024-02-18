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


def test_rules_instance_minimal():
    """
    Test A2L instance section.
    """
    instance_minimal = """
    /begin INSTANCE
        Bravo // instance name
        "" // instance description
        Alpha // reference to type definition
        0x1800 // start address of instance
    /end INSTANCE
    """
    ast = A2LYacc().generate_ast(instance_minimal)
    assert ast

    instance = ast["INSTANCE"]
    assert instance

    assert instance["Name"] == "Bravo"
    assert instance["LongIdentifier"] == '""'
    assert instance["TypedefName"] == "Alpha"
    assert instance["Address"] == "0x1800"


def test_rules_instance_full():
    """
    Test A2L instance section.
    """
    instance_full = """
    /begin INSTANCE
        Bravo // instance name
        "" // instance description
        Alpha // reference to type definition
        0x1800 // start address of instance
        ADDRESS_TYPE PLONG
        /BEGIN ANNOTATION
            ANNOTATION_LABEL "INSTANCE_ANNOTATION"
        /end ANNOTATION
        CALIBRATION_ACCESS OFFLINE_CALIBRATION
        DISPLAY_IDENTIFIER INSTANCE_DISPLAY
        ECU_ADDRESS_EXTENSION 14
        LAYOUT ALTERNATE_WITH_X
        /begin IF_DATA MAP_REF_ADDR
            LINK_MAP ref_name 0x003432
        /end IF_DATA
        /begin IF_DATA XCP_REF_ADDR
            XCP_REF_MAP 0x00332266
        /end IF_DATA
        /begin ANNOTATION
            /begin ANNOTATION_TEXT "INSTANCE_ANNOTATION_DESCRIPTION"
                "This is an instance description"
            /end ANNOTATION_TEXT
        /end ANNOTATION
        MATRIX_DIM 2 4
        MAX_REFRESH 120 250
        MODEL_LINK "system/referer/SwcXcpInstance.referer"
        /begin OVERWRITE
            THIS 0
        /end OVERWRITE
        READ_WRITE
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
        SYMBOL_LINK "_InstanceReference" 0
    /end INSTANCE
    """
    ast = A2LYacc(debug=True).generate_ast(instance_full)
    assert ast

    instance = ast["INSTANCE"]
    assert instance

    assert instance["Name"] == "Bravo"
    assert instance["LongIdentifier"] == '""'
    assert instance["TypedefName"] == "Alpha"
    assert instance["Address"] == "0x1800"
    assert instance["ADDRESS_TYPE"] == "PLONG"
    assert instance["CALIBRATION_ACCESS"] == "OFFLINE_CALIBRATION"
    assert instance["DISPLAY_IDENTIFIER"] == "INSTANCE_DISPLAY"
    assert instance["ECU_ADDRESS_EXTENSION"] == "14"
    assert instance["LAYOUT"] == "ALTERNATE_WITH_X"
    assert instance["MODEL_LINK"] == '"system/referer/SwcXcpInstance.referer"'
    assert instance["READ_WRITE"] is True
    assert instance["MATRIX_DIM"]["Dim"] == ['2', '4']
    assert instance["MAX_REFRESH"] == {'ScalingUnit': '120', 'Rate': '250'}
    assert instance["SYMBOL_LINK"] == {'SymbolName': '"_InstanceReference"', 'Offset': '0'}
    assert len(instance["IF_DATA"]) == 2
    if_data_map = instance["IF_DATA"][0]
    if_data_xcp = instance["IF_DATA"][1]
    assert if_data_map
    assert if_data_xcp
    assert if_data_map["Name"] == "MAP_REF_ADDR"
    assert if_data_map["DataParams"] == ['LINK_MAP', 'ref_name', '0x003432']
    assert if_data_xcp["Name"] == "XCP_REF_ADDR"
    assert if_data_xcp["DataParams"] == ['XCP_REF_MAP', '0x00332266']
    assert len(instance["ANNOTATION"]) == 2
    assert instance["ANNOTATION"][0] == {'ANNOTATION_LABEL': '"INSTANCE_ANNOTATION"'}
    assert instance["ANNOTATION"][1] == {'ANNOTATION_TEXT':
                                         ['"INSTANCE_ANNOTATION_DESCRIPTION"', '"This is an instance description"']}
    assert len(instance["OVERWRITE"]) == 2
    overwrite_1 = instance["OVERWRITE"][0]
    overwrite_2 = instance["OVERWRITE"][1]
    assert overwrite_1
    assert overwrite_2
    assert overwrite_1 == {"Name": "THIS", "AxisNumber": "0"}
    assert overwrite_2["Name"] == "XcpInstance"
    assert overwrite_2["AxisNumber"] == "3"
    assert overwrite_2["CONVERSION"] == "ConversionMethod1"
    assert overwrite_2["EXTENDED_LIMITS"] == {'LowerLimit': '0', 'UpperLimit': '200'}
    assert overwrite_2["FORMAT"] == '"%.2f"'
    assert overwrite_2["INPUT_QUANTITY"] == "Speed2"
    assert overwrite_2["LIMITS"] == {'LowerLimit': '0', 'UpperLimit': '160'}
    assert overwrite_2["MONOTONY"] == "STRICT_DECREASE"
    assert overwrite_2["PHYS_UNIT"] == '"km/h"'

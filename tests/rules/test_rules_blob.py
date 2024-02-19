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


def test_rules_blob_minimal():
    """
    Test A2L section BLOB.
    """
    blob_minimal = """
    /begin BLOB
        Data_Blob // blob name
        "binary blob for xyz" // description
        0x4477112 // start address
        1024 // number of bytes in blob
    /end BLOB
    """
    ast = A2LYacc().generate_ast(blob_minimal)

    assert ast
    blob = ast["BLOB"]

    assert blob["Name"] == "Data_Blob"
    assert blob["LongIdentifier"] == '"binary blob for xyz"'
    assert blob["Address"] == "0x4477112"
    assert blob["Size"] == "1024"


def test_rules_blob_full():
    """
    Test A2L section BLOB.
    """
    blob_full = """
    /begin BLOB
        Data_Blob // blob name
        "binary blob for xyz" // description
        0x4477112 // start address
        1024 // number of bytes in blob
        /begin IF_DATA ODB
            /begin BINARY_SOURCE "BINARY_BLOB_ARRAY"
                103
                1
                QP_BLOB 0x100 1 23
                1952251460 1020 2952232964
            /end BINARY_SOURCE
            /begin TP_BLOB "TP_BLOB_ARRAY"
                /begin TRIGGER_BLOB
                    0xFF 0x63 0xCF 0x7F 0x81 0x84
                /end TRIGGER_BLOB
                HEX_PAGE 0x400 0xAFF7C84C 0xDC
            /end TP_BLOB
        /end IF_DATA
        ADDRESS_TYPE PLONGLONG
        /begin ANNOTATION
            ANNOTATION_LABEL "Data_Blob Description"
            /begin ANNOTATION_TEXT "Data_Blob_Description"
                "Data_Blob_Placeholder"
            /end ANNOTATION_TEXT
        /end ANNOTATION
        CALIBRATION_ACCESS NOT_IN_MCD_SYSTEM
        DISPLAY_IDENTIFIER Data_Blob_Display
        ECU_ADDRESS_EXTENSION 0
        /begin ANNOTATION
            ANNOTATION_LABEL "MODEL_LINK DESCRIPTION"
            ANNOTATION_ORIGIN "MODEL_LINK ORIGIN"
            /begin ANNOTATION_TEXT "SwcBlobPlaceholder_1"
                "SwcBlobPlaceholder_2"
            /end ANNOTATION_TEXT
        /end ANNOTATION
        MAX_REFRESH 5 15
        /begin IF_DATA XCP_TEST
            0xFF 0xFF00
            /begin XCP_BLOB
                0xAAFFEE00
            /end XCP_BLOB
        /end IF_DATA
        SYMBOL_LINK "_XCP_BLOB" 256
        MODEL_LINK "binary/blobs/TP_BLOB.obj"
    /end BLOB
    """
    ast = A2LYacc().generate_ast(blob_full)
    assert ast

    blob = ast["BLOB"]
    assert blob
    assert blob["Name"] == "Data_Blob"
    assert blob["LongIdentifier"] == '"binary blob for xyz"'
    assert blob["Address"] == "0x4477112"
    assert blob["Size"] == "1024"
    assert blob["ADDRESS_TYPE"] == "PLONGLONG"
    assert blob["CALIBRATION_ACCESS"] == "NOT_IN_MCD_SYSTEM"
    assert blob["DISPLAY_IDENTIFIER"] == "Data_Blob_Display"
    assert blob["ECU_ADDRESS_EXTENSION"] == "0"
    assert blob["MAX_REFRESH"] == {'ScalingUnit': '5', 'Rate': '15'}
    assert blob["MODEL_LINK"] == '"binary/blobs/TP_BLOB.obj"'
    assert blob["SYMBOL_LINK"] == {'SymbolName': '"_XCP_BLOB"', 'Offset': '256'}
    assert blob["ANNOTATION"][0] == {'ANNOTATION_LABEL': '"Data_Blob Description"',
                                     'ANNOTATION_TEXT': ['"Data_Blob_Description"', '"Data_Blob_Placeholder"']}
    assert blob["ANNOTATION"][1] == {'ANNOTATION_LABEL': '"MODEL_LINK DESCRIPTION"',
                                     'ANNOTATION_ORIGIN': '"MODEL_LINK ORIGIN"',
                                     'ANNOTATION_TEXT': ['"SwcBlobPlaceholder_1"', '"SwcBlobPlaceholder_2"']}

    # IF_DATA Asserts
    assert len(blob["IF_DATA"]) == 2
    if_data_odb = blob["IF_DATA"][0]
    if_data_xcp = blob["IF_DATA"][1]

    assert if_data_odb
    assert if_data_xcp

    assert if_data_odb["Name"] == "ODB"
    assert len(if_data_odb["If_Data_Block"]) == 2
    assert if_data_odb["If_Data_Block"][0]["Name"] == "BINARY_SOURCE"
    assert if_data_odb["If_Data_Block"][0]["DataParams"] == ['"BINARY_BLOB_ARRAY"', '103', '1', 'QP_BLOB',
                                                             '0x100', '1', '23', '1952251460', '1020', '2952232964']
    assert if_data_odb["If_Data_Block"][1]["Name"] == "TP_BLOB"
    assert if_data_odb["If_Data_Block"][1]["DataParams"] == ['"TP_BLOB_ARRAY"', 'HEX_PAGE', '0x400', '0xAFF7C84C', '0xDC']

    assert if_data_xcp["Name"] == "XCP_TEST"
    assert if_data_xcp["DataParams"] == ['0xFF', '0xFF00']
    assert if_data_xcp["If_Data_Block"]["Name"] == "XCP_BLOB"
    assert if_data_xcp["If_Data_Block"]["DataParams"] == ['0xAAFFEE00']

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


def test_rules_if_data():
    """
    Tests parsing a valid "IF_DATA" block.
    """
    if_data_block = """
    /begin IF_DATA XCP
        IF_DATA_PARAM_TEST_FIRST
        /begin DAQ
            STATIC
            ALSLA
            /begin TIMESTAMP_SUPPORTED
                TIMESTAMP_SUPPORTED_PARAM_FIRST
                /begin EVENT
                    /begin TEST
                        TEST_PARAM_FIRST
                        /begin FOO
                            FOO
                            /begin BAR
                                BAR
                            /end BAR
                        /end FOO
                        TEST_PARAM_LAST
                    /end TEST
                    /begin X
                        X
                    /end X
                    /begin Y
                        Y
                    /end Y
                    EVENT_PARAM_END
                /end EVENT
                TIMESTAMP_SUPPORTED_PARAM_LAST
            /end TIMESTAMP_SUPPORTED
            DAQ_END
        /end DAQ
        /begin PROTOCOL_LAYER
        1 2 3
        /end PROTOCOL_LAYER
        IF_DATA_PARAM_TEST_LAST
    /end IF_DATA
    """
    parser = A2LYacc()
    ast = parser.generate_ast(if_data_block)
    assert ast

    if_data = ast["IF_DATA"]
    assert if_data
    assert if_data["Name"] == "XCP"
    assert if_data["DataParams"] == ["IF_DATA_PARAM_TEST_FIRST", "IF_DATA_PARAM_TEST_LAST"]

    # First If_Data_Block
    if_data_daq = if_data["DAQ"]
    assert if_data_daq["Name"] == "DAQ"
    assert if_data_daq["DataParams"] == ["STATIC", "ALSLA", "DAQ_END"]

    daq_timestamp_supported = if_data_daq["TIMESTAMP_SUPPORTED"]
    assert daq_timestamp_supported["Name"] == "TIMESTAMP_SUPPORTED"
    assert daq_timestamp_supported["DataParams"] == [
        "TIMESTAMP_SUPPORTED_PARAM_FIRST",
        "TIMESTAMP_SUPPORTED_PARAM_LAST",
    ]

    daq_event = daq_timestamp_supported["EVENT"]
    assert daq_event["Name"] == "EVENT"
    assert daq_event["DataParams"] == ["EVENT_PARAM_END"]

    # First nested If_Data_Block within EVENT
    daq_event_test = daq_event["TEST"]
    assert daq_event_test["Name"] == "TEST"
    assert daq_event_test["DataParams"] == ["TEST_PARAM_FIRST", "TEST_PARAM_LAST"]
    assert daq_event_test["FOO"]["Name"] == "FOO"
    assert daq_event_test["FOO"]["DataParams"] == ["FOO"]
    assert daq_event_test["FOO"]["BAR"]["Name"] == "BAR"
    assert daq_event_test["FOO"]["BAR"]["DataParams"] == ["BAR"]

    # Second nested If_Data_Block within EVENT
    daq_event_x = daq_event["X"]
    assert daq_event_x["Name"] == "X"
    assert daq_event_x["DataParams"] == ["X"]

    # Third nested If_Data_Block within EVENT
    daq_event_y = daq_event["Y"]
    assert daq_event_y["Name"] == "Y"
    assert daq_event_y["DataParams"] == ["Y"]

    # Second If_Data_Block
    protocol_layer = if_data["PROTOCOL_LAYER"]
    assert protocol_layer["Name"] == "PROTOCOL_LAYER"
    assert protocol_layer["DataParams"] == ["1", "2", "3"]


def test_rules_if_data_including_keywords():
    """
    Tests parsing a valid "IF_DATA" block including A2L keywords.
    """
    if_data_input = """
    /begin IF_DATA ETK
      /begin SOURCE  "Engine_1"
        103
        1
        QP_BLOB 0x100 1 DIRECT 23
        MEASUREMENT 1952251460 1020 2952232964 2952243268 0 0 0 15000 256 0
      /end SOURCE
      /begin SOURCE  "Engine_2"
        103
        1
        QP_BLOB 0x200 2 DIRECT 21
        MEASUREMENT 2952251460 1020 2952233996 2952244288 0 0 0 15000 256 0
      /end SOURCE
      /begin SOURCE  "Engine_3"
        103
        1
        QP_BLOB 0x300 3 DIRECT 19
        MEASUREMENT 3952251460 1020 2952235028 2952245308 0 0 0 15000 256 0
      /end SOURCE
      /begin SOURCE  "10ms_sync"
        4
        1
        QP_BLOB 0x400 7 DIRECT 11
        MEASUREMENT 4952251460 1020 2952239156 2952249388 0 0 0 10000 512 0
      /end SOURCE
      /begin SOURCE  "100ms_sync"
        5
        1
        QP_BLOB 0x500 8 DIRECT 9
        MEASUREMENT 5952251460 1020 2952241212 2952250408 0 0 0 100000 512 0
      /end SOURCE

      /begin TP_BLOB 0x1000103 INTERFACE_SPEED_100MBIT 0x0
        /begin DISTAB_CFG 0xD 0x122 0x2 0x0 0x0
          TRG_MOD 0x0
        /end DISTAB_CFG
        ETK_CFG 0x10 0x1D 0x61 0x1 0x1 0xFF
          0xFF 0x63 0xCF 0x7F 0x81 0x84 0x79
          0x64 0xB 0x65 0x8C 0x66 0xA0 0x67 0x91
        ETK_MAILBOX 0x11223344
        EXRAM    0xAFF7FF00  0xFF
        EXRAM    0xAFF7FF00  0xFF
        PAGE_SWITCH_METHOD
        0x1
        MAILBOX  0x1 0x1F4 0xAFF7C928
        AUTOSTART_BEHAVIOR ALWAYS_RP
        OCT_WORKINGPAGE  0x400 0xAFF7C84C 0xDC
      /end TP_BLOB
    /end IF_DATA
    """
    parser = A2LYacc()
    ast = parser.generate_ast(if_data_input)
    assert ast

    if_data = ast["IF_DATA"]
    assert if_data["Name"] == "ETK"
    tp_blob = if_data["TP_BLOB"]
    source_1 = if_data["SOURCE"][0]
    source_2 = if_data["SOURCE"][1]
    source_3 = if_data["SOURCE"][2]
    source_4 = if_data["SOURCE"][3]
    source_5 = if_data["SOURCE"][4]
    assert tp_blob
    assert source_1
    assert source_2
    assert source_3
    assert source_4
    assert source_5

    assert source_1["Name"] == "SOURCE"
    assert source_1["DataParams"] == [
        '"Engine_1"',
        "103",
        "1",
        "QP_BLOB",
        "0x100",
        "1",
        "DIRECT",
        "23",
        "MEASUREMENT",
        "1952251460",
        "1020",
        "2952232964",
        "2952243268",
        "0",
        "0",
        "0",
        "15000",
        "256",
        "0",
    ]
    assert source_2["Name"] == "SOURCE"
    assert source_2["DataParams"] == [
        '"Engine_2"',
        "103",
        "1",
        "QP_BLOB",
        "0x200",
        "2",
        "DIRECT",
        "21",
        "MEASUREMENT",
        "2952251460",
        "1020",
        "2952233996",
        "2952244288",
        "0",
        "0",
        "0",
        "15000",
        "256",
        "0",
    ]
    assert source_3["Name"] == "SOURCE"
    assert source_3["DataParams"] == [
        '"Engine_3"',
        "103",
        "1",
        "QP_BLOB",
        "0x300",
        "3",
        "DIRECT",
        "19",
        "MEASUREMENT",
        "3952251460",
        "1020",
        "2952235028",
        "2952245308",
        "0",
        "0",
        "0",
        "15000",
        "256",
        "0",
    ]
    assert source_4["Name"] == "SOURCE"
    assert source_4["DataParams"] == [
        '"10ms_sync"',
        "4",
        "1",
        "QP_BLOB",
        "0x400",
        "7",
        "DIRECT",
        "11",
        "MEASUREMENT",
        "4952251460",
        "1020",
        "2952239156",
        "2952249388",
        "0",
        "0",
        "0",
        "10000",
        "512",
        "0",
    ]
    assert source_5["Name"] == "SOURCE"
    assert source_5["DataParams"] == [
        '"100ms_sync"',
        "5",
        "1",
        "QP_BLOB",
        "0x500",
        "8",
        "DIRECT",
        "9",
        "MEASUREMENT",
        "5952251460",
        "1020",
        "2952241212",
        "2952250408",
        "0",
        "0",
        "0",
        "100000",
        "512",
        "0",
    ]

    assert tp_blob["Name"] == "TP_BLOB"
    assert tp_blob["DataParams"] == [
        "0x1000103",
        "INTERFACE_SPEED_100MBIT",
        "0x0",
        "ETK_CFG",
        "0x10",
        "0x1D",
        "0x61",
        "0x1",
        "0x1",
        "0xFF",
        "0xFF",
        "0x63",
        "0xCF",
        "0x7F",
        "0x81",
        "0x84",
        "0x79",
        "0x64",
        "0xB",
        "0x65",
        "0x8C",
        "0x66",
        "0xA0",
        "0x67",
        "0x91",
        "ETK_MAILBOX",
        "0x11223344",
        "EXRAM",
        "0xAFF7FF00",
        "0xFF",
        "EXRAM",
        "0xAFF7FF00",
        "0xFF",
        "PAGE_SWITCH_METHOD",
        "0x1",
        "MAILBOX",
        "0x1",
        "0x1F4",
        "0xAFF7C928",
        "AUTOSTART_BEHAVIOR",
        "ALWAYS_RP",
        "OCT_WORKINGPAGE",
        "0x400",
        "0xAFF7C84C",
        "0xDC",
    ]

    tp_blob_distab_cfg = tp_blob["DISTAB_CFG"]
    assert tp_blob_distab_cfg
    assert tp_blob_distab_cfg["Name"] == "DISTAB_CFG"
    assert tp_blob_distab_cfg["DataParams"] == [
        "0xD",
        "0x122",
        "0x2",
        "0x0",
        "0x0",
        "TRG_MOD",
        "0x0",
    ]


def test_rules_if_data_empty_ident_block():
    """
    Tests that an empty /begin /end section does not raise an error.
    """
    if_data_input = """
    /begin IF_DATA XCP
      /begin DAQ
        STATIC
        0x0004
        GRANULARITY_ENTRY_SIZE_DAQ_BYTE
        0x04
        NO_OVERLOAD_INDICATION
        /begin DAQ_LIST
          DAQ_LIST_TYPE DAQ
          MAX_ODT 0x01
          EVENT_FIXED 0x1001
          /begin PREDEFINED
            /begin ODT
              0x00
              ODT_ENTRY
              0x04
            /end ODT
          /end PREDEFINED
        /end DAQ_LIST
        /begin DAQ_LIST
          0x01
          DAQ_LIST_TYPE DAQ
          MAX_ODT 0x10
          EVENT_FIXED 0x2001
          /begin PREDEFINED
          /end PREDEFINED
        /end DAQ_LIST
        /begin DAQ_LIST
          0x02
          DAQ_LIST_TYPE DAQ
          MAX_ODT 0x00
          EVENT_FIXED 0x4001
          /begin PREDEFINED
          /end PREDEFINED
        /end DAQ_LIST
        /begin EVENT
          "1_ms_task"
          DAQ
          1
          0x00
        /end EVENT
      /end DAQ
      /begin XCP_ON_UDP_IP
        0x0001
        08007
        ADDRESS "192.168.1.101"
      /end XCP_ON_UDP_IP
    /end IF_DATA
    """
    parser = A2LYacc()
    ast = parser.generate_ast(if_data_input)
    assert ast

    if_data = ast["IF_DATA"]
    assert if_data["Name"] == "XCP"
    assert if_data["DAQ"]
    assert if_data["XCP_ON_UDP_IP"]

    daq = if_data["DAQ"]
    assert daq["Name"] == "DAQ"
    assert daq["DataParams"] == [
        "STATIC",
        "0x0004",
        "GRANULARITY_ENTRY_SIZE_DAQ_BYTE",
        "0x04",
        "NO_OVERLOAD_INDICATION",
    ]
    assert daq["DAQ_LIST"]

    daq_list = daq["DAQ_LIST"]
    assert len(daq_list) == 3
    assert daq_list[0]["Name"] == "DAQ_LIST"
    assert daq_list[0]["DataParams"] == [
        "DAQ_LIST_TYPE",
        "DAQ",
        "MAX_ODT",
        "0x01",
        "EVENT_FIXED",
        "0x1001",
    ]
    assert daq_list[0]["PREDEFINED"]
    assert daq_list[0]["PREDEFINED"]["ODT"]["DataParams"] == ["0x00", "ODT_ENTRY", "0x04"]
    assert daq_list[1]["Name"] == "DAQ_LIST"
    assert daq_list[1]["DataParams"] == [
        "0x01",
        "DAQ_LIST_TYPE",
        "DAQ",
        "MAX_ODT",
        "0x10",
        "EVENT_FIXED",
        "0x2001",
    ]
    assert daq_list[1]["PREDEFINED"]
    assert daq_list[2]["Name"] == "DAQ_LIST"
    assert daq_list[2]["DataParams"] == [
        "0x02",
        "DAQ_LIST_TYPE",
        "DAQ",
        "MAX_ODT",
        "0x00",
        "EVENT_FIXED",
        "0x4001",
    ]
    assert daq_list[2]["PREDEFINED"]

    daq_event = daq["EVENT"]
    assert daq_event
    assert daq_event["Name"] == "EVENT"
    assert daq_event["DataParams"] == ['"1_ms_task"', "DAQ", "1", "0x00"]

    xcp_on_udp_ip = if_data["XCP_ON_UDP_IP"]
    assert xcp_on_udp_ip
    assert xcp_on_udp_ip["Name"] == "XCP_ON_UDP_IP"
    assert xcp_on_udp_ip["DataParams"] == ["0x0001", "08007", "ADDRESS", '"192.168.1.101"']

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
    assert len(if_data["If_Data_Block"]) == 2

    # First If_Data_Block
    if_data_block_0 = if_data["If_Data_Block"][0]
    assert if_data_block_0["Name"] == "DAQ"
    assert if_data_block_0["DataParams"] == ["STATIC", "ALSLA", "DAQ_END"]
    assert "If_Data_Block" in if_data_block_0

    daq_if_data_block = if_data_block_0["If_Data_Block"]
    assert daq_if_data_block["Name"] == "TIMESTAMP_SUPPORTED"
    assert daq_if_data_block["DataParams"] == ["TIMESTAMP_SUPPORTED_PARAM_FIRST", "TIMESTAMP_SUPPORTED_PARAM_LAST"]
    assert "If_Data_Block" in daq_if_data_block

    event_if_data_block = daq_if_data_block["If_Data_Block"]
    assert event_if_data_block["Name"] == "EVENT"
    assert event_if_data_block["DataParams"] == ["EVENT_PARAM_END"]
    assert len(event_if_data_block["If_Data_Block"]) == 3

    # First nested If_Data_Block within EVENT
    event_if_data_block_0 = event_if_data_block["If_Data_Block"][0]
    assert event_if_data_block_0["Name"] == "TEST"
    assert event_if_data_block_0["DataParams"] == ["TEST_PARAM_FIRST", "TEST_PARAM_LAST"]
    assert "If_Data_Block" in event_if_data_block_0

    # Second nested If_Data_Block within EVENT
    event_if_data_block_1 = event_if_data_block["If_Data_Block"][1]
    assert event_if_data_block_1["Name"] == "X"
    assert event_if_data_block_1["DataParams"] == ["X"]

    # Third nested If_Data_Block within EVENT
    event_if_data_block_2 = event_if_data_block["If_Data_Block"][2]
    assert event_if_data_block_2["Name"] == "Y"
    assert event_if_data_block_2["DataParams"] == ["Y"]

    # Second If_Data_Block
    if_data_block_1 = if_data["If_Data_Block"][1]
    assert if_data_block_1["Name"] == "PROTOCOL_LAYER"
    assert if_data_block_1["DataParams"] == ["1", "2", "3"]


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
        ETK_CFG 0x10 0x1D 0x61 0x1 0x1 0xFF 0xFF 0x63 0xCF 0x7F 0x81 0x84 0x79 0x64 0xB 0x65 0x8C 0x66 0xA0 0x67 0x91
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
    assert if_data
    assert if_data["Name"] == "ETK"
    source_1 = if_data["If_Data_Block"][0]
    source_2 = if_data["If_Data_Block"][1]
    source_3 = if_data["If_Data_Block"][2]
    source_4 = if_data["If_Data_Block"][3]
    source_5 = if_data["If_Data_Block"][4]
    tp_blob = if_data["If_Data_Block"][5]
    assert source_1
    assert source_2
    assert source_3
    assert source_4
    assert source_5
    assert tp_blob

    assert source_1["Name"] == "SOURCE"
    assert source_1["DataParams"] == ['"Engine_1"', '103', '1', 'QP_BLOB', '0x100', '1', 'DIRECT', '23', 'MEASUREMENT',
                                      '1952251460', '1020', '2952232964', '2952243268', '0', '0', '0', '15000', '256', '0']
    assert source_2["Name"] == "SOURCE"
    assert source_2["DataParams"] == ['"Engine_2"', '103', '1', 'QP_BLOB', '0x200', '2', 'DIRECT', '21', 'MEASUREMENT',
                                      '2952251460', '1020', '2952233996', '2952244288', '0', '0', '0', '15000', '256', '0']
    assert source_3["Name"] == "SOURCE"
    assert source_3["DataParams"] == ['"Engine_3"', '103', '1', 'QP_BLOB', '0x300', '3', 'DIRECT', '19', 'MEASUREMENT',
                                      '3952251460', '1020', '2952235028', '2952245308', '0', '0', '0', '15000', '256', '0']
    assert source_4["Name"] == "SOURCE"
    assert source_4["DataParams"] == ['"10ms_sync"', '4', '1', 'QP_BLOB', '0x400', '7', 'DIRECT', '11', 'MEASUREMENT',
                                      '4952251460', '1020', '2952239156', '2952249388', '0', '0', '0', '10000', '512', '0']
    assert source_5["Name"] == "SOURCE"
    assert source_5["DataParams"] == ['"100ms_sync"', '5', '1', 'QP_BLOB', '0x500', '8', 'DIRECT', '9', 'MEASUREMENT',
                                      '5952251460', '1020', '2952241212', '2952250408', '0', '0', '0', '100000', '512', '0']

    assert tp_blob["Name"] == "TP_BLOB"
    assert tp_blob["DataParams"] == ['0x1000103', 'INTERFACE_SPEED_100MBIT', '0x0', 'ETK_CFG', '0x10', '0x1D', '0x61',
                                     '0x1', '0x1', '0xFF', '0xFF', '0x63', '0xCF', '0x7F', '0x81', '0x84', '0x79', '0x64',
                                     '0xB', '0x65', '0x8C', '0x66', '0xA0', '0x67', '0x91', 'ETK_MAILBOX', '0x11223344',
                                     'EXRAM', '0xAFF7FF00', '0xFF', 'EXRAM', '0xAFF7FF00', '0xFF', 'PAGE_SWITCH_METHOD', '0x1',
                                     'MAILBOX', '0x1', '0x1F4', '0xAFF7C928', 'AUTOSTART_BEHAVIOR', 'ALWAYS_RP',
                                     'OCT_WORKINGPAGE', '0x400', '0xAFF7C84C', '0xDC']

    tp_blob_distab_cfg = tp_blob["If_Data_Block"]
    assert tp_blob_distab_cfg
    assert tp_blob_distab_cfg["Name"] == "DISTAB_CFG"
    assert tp_blob_distab_cfg["DataParams"] == ['0xD', '0x122', '0x2', '0x0', '0x0', 'TRG_MOD', '0x0']

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

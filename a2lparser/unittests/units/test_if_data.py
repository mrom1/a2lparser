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


from a2lparser.unittests.testhandler import Testhandler


_TEST_IF_DATA_BLOCK = """
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

_TEST_IF_DATA_BLOCK_PARAM_ONLY = """
/begin IF_DATA CAN
    0x0001
    0x0020
    0x0300
    0x4000
/end IF_DATA
"""

_TEST_IF_DATA_BLOCK_MANDATORY_ONLY = """
/begin IF_DATA CAN
/end IF_DATA
"""

_TEST_IF_DATA_BLOCK_EMPTY = """
/begin IF_DATA
/end IF_DATA
"""


class TestIfData(Testhandler):
    def test_if_data_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_if_data_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_IF_DATA_BLOCK,
                      filelength=_TEST_IF_DATA_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)

        if_xcp = tree.find('.//If_Data')
        if_data_blocks = if_xcp.findall('.//If_Data_Block')
        if_daq = if_data_blocks[0]
        if_timestamp_supported = if_data_blocks[1]
        if_event = if_data_blocks[2]
        if_test = if_data_blocks[3]
        if_foo = if_data_blocks[4]
        if_bar = if_data_blocks[5]
        if_x = if_data_blocks[6]
        if_y = if_data_blocks[7]
        if_protocol_layer = if_data_blocks[8]

        test = if_event.findall('.//If_Data_Block')

        self.assertEqual(if_xcp.find('.//Name').text, "XCP")
        self.assertEqual(if_daq.find('.//Name').text, "DAQ")
        self.assertEqual(if_timestamp_supported.find('.//Name').text, "TIMESTAMP_SUPPORTED")
        self.assertEqual(if_event.find('.//Name').text, "EVENT")
        self.assertEqual(if_test.find('.//Name').text, "TEST")
        self.assertEqual(if_foo.find('.//Name').text, "FOO")
        self.assertEqual(if_bar.find('.//Name').text, "BAR")
        self.assertEqual(if_x.find('.//Name').text, "X")
        self.assertEqual(if_y.find('.//Name').text, "Y")
        self.assertEqual(if_protocol_layer.find('.//Name').text, "PROTOCOL_LAYER")

        self.assertEqual(if_xcp.find('.//DataParams').text, "IF_DATA_PARAM_TEST_FIRST, IF_DATA_PARAM_TEST_LAST")
        self.assertEqual(if_daq.find('.//DataParams').text, "STATIC, ALSLA, DAQ_END")
        self.assertEqual(if_timestamp_supported.find('.//DataParams').text,
                         "TIMESTAMP_SUPPORTED_PARAM_FIRST, TIMESTAMP_SUPPORTED_PARAM_LAST")
        self.assertEqual(if_event.find('.//DataParams').text, "EVENT_PARAM_END")
        self.assertEqual(if_test.find('.//DataParams').text, "TEST_PARAM_FIRST, TEST_PARAM_LAST")
        self.assertEqual(if_foo.find('.//DataParams').text, "FOO")
        self.assertEqual(if_bar.find('.//DataParams').text, "BAR")
        self.assertEqual(if_x.find('.//DataParams').text, "X")
        self.assertEqual(if_y.find('.//DataParams').text, "Y")
        self.assertEqual(if_protocol_layer.find('.//DataParams').text, "1, 2, 3")

    def test_if_data_block_param_only(self):
        p = self.param.parser
        ast = p.parse(filename="test_if_data_block_param_only",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_IF_DATA_BLOCK_PARAM_ONLY,
                      filelength=_TEST_IF_DATA_BLOCK_PARAM_ONLY.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "CAN")
        self.assertEqual(tree.find('.//DataParams').text, "0x0001, 0x0020, 0x0300, 0x4000")

    def test_if_data_block_mandatory_only(self):
        p = self.param.parser
        ast = p.parse(filename="test_if_data_block_mandatory_only",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_IF_DATA_BLOCK_MANDATORY_ONLY,
                      filelength=_TEST_IF_DATA_BLOCK_MANDATORY_ONLY.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "CAN")

    def test_if_data_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_if_data_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_IF_DATA_BLOCK_EMPTY,
                      filelength=_TEST_IF_DATA_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

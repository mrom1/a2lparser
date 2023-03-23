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


_TEST_VAR_CHARACTERISTIC_BLOCK = """
/begin VAR_CHARACTERISTIC /* define NLLM as variant coded */
		NLLM
		Gear Car /* gear box including the 2 variants "Manual" and "Automatic" */
		/begin VAR_ADDRESS
				0x8840
				0x8858
				0x8870
				0x8888
		/end VAR_ADDRESS
/end VAR_CHARACTERISTIC
"""

_TEST_VAR_CHARACTERISTIC_BLOCK_EMPTY = """
/begin VAR_CHARACTERISTIC
    /begin VAR_ADDRESS
	/end VAR_ADDRESS
/end VAR_CHARACTERISTIC
"""


class TestVarCharacteristic(Testhandler):
    def test_var_characteristic_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_var_characteristic_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_VAR_CHARACTERISTIC_BLOCK,
                      filelength=_TEST_VAR_CHARACTERISTIC_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "NLLM")
        self.assertEqual(tree.find('.//CriterionName').text, "Gear, Car")
        self.assertEqual(tree.find('.//Var_Address/Address').text, "0x8840, 0x8858, 0x8870, 0x8888")

    def test_var_characteristic_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_var_characteristic_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_VAR_CHARACTERISTIC_BLOCK_EMPTY,
                      filelength=_TEST_VAR_CHARACTERISTIC_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

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


_TEST_BIT_OPERATION_BLOCK = """
/begin BIT_OPERATION
    RIGHT_SHIFT 4 /*4 positions*/
    LEFT_SHIFT 0
    SIGN_EXTEND
/end BIT_OPERATION
"""

_TEST_BIT_OPERATION_BLOCK_EMPTY = """
/begin BIT_OPERATION
/end BIT_OPERATION
"""


class TestBitOperation(Testhandler):
    def test_bit_operation_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_bit_operation_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_BIT_OPERATION_BLOCK,
                      filelength=_TEST_BIT_OPERATION_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Bit_Operation/Right_Shift/Bitcount').text, "4")
        self.assertEqual(tree.find('.//Bit_Operation/Left_Shift/Bitcount').text, "0")
        self.assertEqual(tree.find('.//Bit_Operation/Sign_Extend/Boolean').text, "True")

    def test_bit_operation_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_bit_operation_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_BIT_OPERATION_BLOCK_EMPTY,
                      filelength=_TEST_BIT_OPERATION_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

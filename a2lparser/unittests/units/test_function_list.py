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


_TEST_FUNCTION_LIST_BLOCK = """
/begin FUNCTION_LIST
	ID_ADJUSTM
	FL_ADJUSTM
	SPEED_LIM
/end FUNCTION_LIST
"""

_TEST_FUNCTION_LIST_BLOCK_EMPTY = """
/begin FUNCTION_LIST
/end FUNCTION_LIST
"""


class TestFunctionList(Testhandler):
    def test_function_list_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_function_list_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FUNCTION_LIST_BLOCK,
                      filelength=_TEST_FUNCTION_LIST_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        function_list = tree.findall('Function_List')
        self.assertEqual(len(function_list), 1)
        self.assertEqual(function_list[0].findall('.//Name')[0].text, "ID_ADJUSTM, FL_ADJUSTM, SPEED_LIM")

    def test_function_list_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_function_list_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FUNCTION_LIST_BLOCK_EMPTY,
                      filelength=_TEST_FUNCTION_LIST_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

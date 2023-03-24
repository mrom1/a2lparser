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


_TEST_VAR_CRITERION_BLOCK = """
/begin VAR_CRITERION
		Car
		"Car body" /*Enumeration of criterion values*/
		Limousine Kombi Cabrio
		VAR_MEASUREMENT S_CAR
		VAR_SELECTION_CHARACTERISTIC V_CAR
/end VAR_CRITERION


"""

_TEST_VAR_CRITERION_BLOCK_EMPTY = """
/begin VAR_CRITERION
/end VAR_CRITERION
"""


class TestVarCriterion(Testhandler):
    def test_var_criterion_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_var_criterion_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_VAR_CRITERION_BLOCK,
                      filelength=_TEST_VAR_CRITERION_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "Car")
        self.assertEqual(tree.find('.//LongIdentifier').text, "Car body")
        self.assertEqual(tree.find('.//Value').text, "Limousine, Kombi, Cabrio")
        self.assertEqual(tree.find('.//Var_Measurement').text, "S_CAR")
        self.assertEqual(tree.find('.//Var_Selection_Characteristic').text, "V_CAR")

    def test_var_criterion_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_var_criterion_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_VAR_CRITERION_BLOCK_EMPTY,
                      filelength=_TEST_VAR_CRITERION_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validate_abstract_syntax_tree(ast), False)

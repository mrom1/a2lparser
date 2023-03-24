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


_TEST_VARIANT_CODING_BLOCK = """
/begin VARIANT_CODING
    VAR_SEPARATOR "." /* PUMKF.1 */
	VAR_NAMING NUMERIC /* variant criterion "Car body" with three variants */
	/begin VAR_CRITERION
		Car
		"Car body"
		Limousine Kombi Cabrio
		VAR_MEASUREMENT S_CAR
		VAR_SELECTION_CHARACTERISTIC V_CAR
	/end VAR_CRITERION /* variant criterion "Type of gear box" with two variants */
	/begin VAR_CRITERION
		Gear
		"Type of gear box"
		Manual Automatic
	/end VAR_CRITERION
	/begin VAR_FORBIDDEN_COMB /* forbidden: Limousine-Manual*/
		Car Limousine
		Gear Manual
	/end VAR_FORBIDDEN_COMB
	/begin VAR_FORBIDDEN_COMB /* forbidden: Cabrio-Automatic*/
		Car Cabrio
		Gear Automatic
	/end VAR_FORBIDDEN_COMB
	/begin VAR_CHARACTERISTIC
		PUMKF /*define PUMKF as variant coded*/
		Gear Car /* Gear box variants */
		/begin VAR_ADDRESS
		/end VAR_ADDRESS
	/end VAR_CHARACTERISTIC
	/begin VAR_CHARACTERISTIC
		NLLM /*define NLLM as variant coded */
		Gear Car /*car body and gear box variants*/
		/begin VAR_ADDRESS
			0x8840
			0x8858
			0x8870
			0x8888
		/end VAR_ADDRESS
	/end VAR_CHARACTERISTIC
/end VARIANT_CODING

"""

_TEST_VARIANT_CODING_BLOCK_EMPTY = """
/begin VARIANT_CODING
/end VARIANT_CODING
"""


class TestVariantCoding(Testhandler):
    def test_variant_coding_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_variant_coding_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_VARIANT_CODING_BLOCK,
                      filelength=_TEST_VARIANT_CODING_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)

        self.assertEqual(tree.find('.//Var_Separator').text, ".")
        self.assertEqual(tree.find('.//Var_Naming').text, "NUMERIC")

        var_criterions = tree.findall('.//Var_Criterion')
        self.assertEqual(len(var_criterions), 2)
        self.assertEqual(var_criterions[0].find('.//Name').text, "Car")
        self.assertEqual(var_criterions[0].find('.//LongIdentifier').text, "Car body")
        self.assertEqual(var_criterions[0].find('.//Value').text, "Limousine, Kombi, Cabrio")
        self.assertEqual(var_criterions[0].find('.//Var_Measurement').text, "S_CAR")
        self.assertEqual(var_criterions[0].find('.//Var_Selection_Characteristic').text, "V_CAR")
        self.assertEqual(var_criterions[1].find('.//Name').text, "Gear")
        self.assertEqual(var_criterions[1].find('.//LongIdentifier').text, "Type of gear box")
        self.assertEqual(var_criterions[1].find('.//Value').text, "Manual, Automatic")

        var_fordbidden_combs = tree.findall('.//Var_Forbidden_Comb')
        self.assertEqual(len(var_fordbidden_combs), 2)
        self.assertEqual(var_fordbidden_combs[0].find('.//CriterionList').text,
                         "['Car', 'Limousine'], ['Gear', 'Manual']")
        self.assertEqual(var_fordbidden_combs[1].find('.//CriterionList').text,
                         "['Car', 'Cabrio'], ['Gear', 'Automatic']")

        var_characteristics = tree.findall('.//Var_Characteristic')
        self.assertEqual(len(var_characteristics), 2)
        self.assertEqual(var_characteristics[0].find('.//Name').text, "PUMKF")
        self.assertEqual(var_characteristics[0].find('.//CriterionName').text, "Gear, Car")
        self.assertEqual(var_characteristics[1].find('.//Name').text, "NLLM")
        self.assertEqual(var_characteristics[1].find('.//CriterionName').text, "Gear, Car")
        self.assertEqual(var_characteristics[1].find('.//Var_Address/Address').text, "0x8840, 0x8858, 0x8870, 0x8888")

    def test_variant_coding_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_variant_coding_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_VARIANT_CODING_BLOCK_EMPTY,
                      filelength=_TEST_VARIANT_CODING_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validate_abstract_syntax_tree(ast), False)

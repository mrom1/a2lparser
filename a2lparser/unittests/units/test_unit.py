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


_TEST_UNIT_BLOCK = """
/begin UNIT kms_per_hour
		"derived unit for velocity: kilometres per hour"
		"[km/h]"
		DERIVED
		REF_UNIT metres_per_second
		UNIT_CONVERSION 3.6 0.0 /* y [km/h] = (60*60/1000) * x [m/s] + 0.0 */
		SI_EXPONENTS 1 2 -2 4 3 -4 -5 /*[N] = [m]*[kg]*[s]-2 */
/end UNIT
"""

_TEST_UNIT_BLOCK_EMPTY = """
/begin UNIT
/end UNIT
"""


class TestUnit(Testhandler):
    def test_unit_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_unit_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_UNIT_BLOCK,
                      filelength=_TEST_UNIT_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "kms_per_hour")
        self.assertEqual(tree.find('.//LongIdentifier').text, "derived unit for velocity: kilometres per hour")
        self.assertEqual(tree.find('.//Display').text, "[km/h]")
        self.assertEqual(tree.find('.//Type').text, "DERIVED")
        self.assertEqual(tree.find('.//Ref_Unit').text, "metres_per_second")

        self.assertEqual(tree.find('.//Unit_Conversion/Gradient').text, "3.6")
        self.assertEqual(tree.find('.//Unit_Conversion/Offset').text, "0.0")

        self.assertEqual(tree.find('.//Si_Exponents/Length').text, "1")
        self.assertEqual(tree.find('.//Si_Exponents/Mass').text, "2")
        self.assertEqual(tree.find('.//Si_Exponents/Time').text, "-2")
        self.assertEqual(tree.find('.//Si_Exponents/ElectricCurrent').text, "4")
        self.assertEqual(tree.find('.//Si_Exponents/Temperature').text, "3")
        self.assertEqual(tree.find('.//Si_Exponents/AmountOfSubstance').text, "-4")
        self.assertEqual(tree.find('.//Si_Exponents/LuminousIntensity').text, "-5")

    def test_unit_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_unit_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_UNIT_BLOCK_EMPTY,
                      filelength=_TEST_UNIT_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

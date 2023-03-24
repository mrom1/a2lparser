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


_TEST_COMPU_VTAB_RANGE_BLOCK = """
/begin COMPU_VTAB_RANGE
    SAR_ASS_REQ_AX
	"Active assistant"
	33
	0 0 "IDLE"
	1 1 "NDEF1"
	2 2 "ACTV"
	3 3 "XT_ACTV"
	64 255 "not defined"
	DEFAULT_VALUE "SNA"
/end COMPU_VTAB_RANGE
"""

_TEST_COMPU_VTAB_RANGE_BLOCK_EMPTY = """
/begin COMPU_VTAB_RANGE
/end COMPU_VTAB_RANGE
"""


class TestCompuVtabRange(Testhandler):
    def test_compu_vtab_range_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_compu_vtab_range_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_COMPU_VTAB_RANGE_BLOCK,
                      filelength=_TEST_COMPU_VTAB_RANGE_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "SAR_ASS_REQ_AX")
        self.assertEqual(tree.find('.//LongIdentifier').text, "Active assistant")
        self.assertEqual(tree.find('.//NumberValueTriples').text, "33")
        self.assertEqual(tree.find('.//InVal_MinMax_OutVal').text,
                         "['0', '0', 'IDLE'], ['1', '1', 'NDEF1'], ['2', '2', 'ACTV'], ['3', '3', 'XT_ACTV'], ['64', '255', 'not defined']")
        self.assertEqual(tree.find('.//Default_Value').text, "SNA")

    def test_compu_vtab_range_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_compu_vtab_range_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_COMPU_VTAB_RANGE_BLOCK_EMPTY,
                      filelength=_TEST_COMPU_VTAB_RANGE_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validate_abstract_syntax_tree(ast), False)

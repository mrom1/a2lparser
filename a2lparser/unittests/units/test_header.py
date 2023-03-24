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


_TEST_HEADER_BLOCK = """
/begin HEADER "see also specification XYZ of 01.02.1994"
	VERSION "BG5.0815"
	PROJECT_NO M4711Z1
/end HEADER
"""

_TEST_HEADER_BLOCK_EMPTY = """
/begin HEADER
/end HEADER
"""


class TestHeader(Testhandler):
    def test_header_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_header_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_HEADER_BLOCK,
                      filelength=_TEST_HEADER_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Comment').text, "see also specification XYZ of 01.02.1994")
        self.assertEqual(tree.find('.//Project_No').text, "M4711Z1")
        self.assertEqual(tree.find('.//Version').text, "BG5.0815")

    def test_header_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_header_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_HEADER_BLOCK_EMPTY,
                      filelength=_TEST_HEADER_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validate_abstract_syntax_tree(ast), False)

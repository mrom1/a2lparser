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


_TEST_ANNOTATION_BLOCK = """
/begin ANNOTATION
    ANNOTATION_LABEL "ANNOTATION_LABEL"
    ANNOTATION_ORIGIN "ANNOTATION_ORIGIN"
    /begin ANNOTATION_TEXT
        "STRING_LINE_1"
        "STRING_LINE_2"
    /end ANNOTATION_TEXT
/end ANNOTATION
"""

_TEST_ANNOTATION_BLOCK_EMPTY = """
/begin ANNOTATION
    /begin ANNOTATION_TEXT
    /end ANNOTATION_TEXT
    /begin ANNOTATION_TEXT
    /end ANNOTATION_TEXT
/end ANNOTATION
"""


class TestAnnotation(Testhandler):
    def test_annotation_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_annotation_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_ANNOTATION_BLOCK_EMPTY,
                      filelength=_TEST_ANNOTATION_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

    def test_annotation_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_annotation_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_ANNOTATION_BLOCK,
                      filelength=_TEST_ANNOTATION_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)

        self.assertEqual(tree.find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN")
        self.assertEqual(tree.find('.//Annotation_Label').text, "ANNOTATION_LABEL")
        self.assertEqual(tree.find('.//Annotation_Text').text, "STRING_LINE_1, STRING_LINE_2")


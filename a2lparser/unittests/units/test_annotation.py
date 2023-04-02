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


from a2lparser.a2l.parser import Parser
from a2lparser.a2l.ast.abstract_syntax_tree import AbstractSyntaxTree
from a2lparser.unittests.testhandler import Testhandler


_TEST_ANNOTATION_BLOCK = """
/begin ANNOTATION
    ANNOTATION_LABEL "valid_section_1"
    /begin ANNOTATION_TEXT
        "string_literal_1"
        "STRING_LITERAL_2"
    /end ANNOTATION_TEXT
    ANNOTATION_ORIGIN "first block origin"
/end ANNOTATION
/begin ANNOTATION
    /begin ANNOTATION_TEXT
    /end ANNOTATION_TEXT
    /begin ANNOTATION_TEXT
    /end ANNOTATION_TEXT
/end ANNOTATION
/begin ANNOTATION
    ANNOTATION_ORIGIN "ORIGIN_UNKOWN"
    ANNOTATION_LABEL "valid_section_2"
    /begin ANNOTATION_TEXT
        "SECOND_BLOCK_STRING_LINE_1"
        "SECOND_BLOCK_STRING_LINE_2"
    /end ANNOTATION_TEXT
/end ANNOTATION
/begin ANNOTATION
    ANNOTATION_LABEL "ERROR_RESOLVE_TEST_ANNOTATION"
    /begin ANNOTATION_TEXT
        "This annotation will have a syntax error"
        "The syntax error is on ANNOTATION_ORIGIN"
        "Testing error recovery mode"
    /end ANNOTATION_TEXT
    ANNOTATION_ORIGIN 0x412142 error
/end ANNOTATION
/begin ANNOTATION
    ANNOTATION_ORIGIN "SECOND_ORIGIN"
    /begin ANNOTATION_TEXT
        "last valid annotation section"
        "VALID_STRING_LITERAL"
    /end ANNOTATION_TEXT
    ANNOTATION_LABEL "valid_section_3"
/end ANNOTATION
"""


class TestAnnotation(Testhandler):
    """
    Tests the Annotation blocks of an A2L file.
    """

    def test_annotation_block(self):
        """
        Test Annotation block.
        """
        parser: Parser = self.param
        ast: AbstractSyntaxTree = parser.parse_content(_TEST_ANNOTATION_BLOCK)

        self.assertIsInstance(ast, AbstractSyntaxTree)
        annotations = ast.find_sections("annotation")
        annotations_text = ast.find_sections("annotation_text")
        print(annotations)
        print(annotations_text)
        self.assertEqual(len(ast), 3)

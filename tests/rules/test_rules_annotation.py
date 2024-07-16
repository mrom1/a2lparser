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


from a2lparser.a2l.a2l_yacc import A2LYacc


def test_rules_annotation():
    """
    Tests parsing a valid "ANNOTATION" block.
    """
    annotation_block = """
    /begin ANNOTATION
        ANNOTATION_LABEL "valid_section_1"
        /begin ANNOTATION_TEXT
            "string_literal_1"
            "STRING_LITERAL_2"
            "STRING LITERAL 3"
        /end ANNOTATION_TEXT
        ANNOTATION_ORIGIN "first block origin"
    /end ANNOTATION
    /begin ANNOTATION
        ANNOTATION_ORIGIN "SECOND_ORIGIN"
        /begin ANNOTATION_TEXT
            "SOME_CONSTANT = 0xC48800FF"
        /end ANNOTATION_TEXT
        ANNOTATION_LABEL "valid_section_2"
    /end ANNOTATION
    """
    parser = A2LYacc()
    ast = parser.generate_ast(annotation_block)
    assert ast

    annotation = ast["ANNOTATION"]
    assert len(annotation) == 2

    annotation_1 = annotation[0]
    assert annotation_1["ANNOTATION_LABEL"] == '"valid_section_1"'
    assert annotation_1["ANNOTATION_ORIGIN"] == '"first block origin"'
    assert annotation_1["ANNOTATION_TEXT"] == ['"string_literal_1"', '"STRING_LITERAL_2"', '"STRING LITERAL 3"']

    annotation_2 = annotation[1]
    assert annotation_2["ANNOTATION_LABEL"] == '"valid_section_2"'
    assert annotation_2["ANNOTATION_ORIGIN"] == '"SECOND_ORIGIN"'
    assert annotation_2["ANNOTATION_TEXT"] == ['"SOME_CONSTANT = 0xC48800FF"']

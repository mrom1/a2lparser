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
from a2lparser.a2l.config.config import Config


def test_a2l_yacc_error_resolve():
    """
    Tests error resolving in subsection.
    """
    faulty_section = """
    /begin ANNOTATION
        ANNOTATION_LABEL "ANNOTATION_LABEL"
        ANNOTATION_ORIGIN "ORIGIN_ORIGIN"
        /begin ANNOTATION_TEXT
            "STRING_LINE_1"
            "STRING_LINE_2"
            0x41feed22
        /end ANNOTATION_TEXT
        ANNOTATION_ORIGIN "ANNOTATION_ORIGIN"
    /end ANNOTATION
    /begin ANNOTATION
        ANNOTATION_ORIGIN "ORIGIN_ORIGIN"
        /begin ANNOTATION_TEXT
            "STRING_LINE_1"
            "STRING_LINE_2"
            "0x41feed22"
        /end ANNOTATION_TEXT
        ANNOTATION_ORIGIN "ANNOTATION_ORIGIN"
    /end ANNOTATION
    """
    yacc = A2LYacc(Config())
    ast = yacc.generate_ast(faulty_section)
    assert ast


def test_a2l_yacc_annotation():
    """
    Testing to parse an ANNOTATION section.
    """
    annotation_text = """
    /begin ANNOTATION
        ANNOTATION_LABEL "ANNOTATION_LABEL"
        ANNOTATION_ORIGIN "ANNOTATION_ORIGIN"
        /begin ANNOTATION_TEXT
            "STRING_LINE_1"
            "STRING_LINE_2"
        /end ANNOTATION_TEXT
    /end ANNOTATION
    """
    yacc = A2LYacc(Config())
    ast = yacc.generate_ast(annotation_text)
    print(ast)
    assert ast


def test_a2l_yacc_project_sections():
    """
    Testing to parse an empty string.
    """
    project_block = """
    /begin project
        PROJECT "My Project"
        VERSION "1.0"
    /end project
    /begin project
        PROJECT "My Other Project"
        VERSION "2.1"
    /end project
    """
    yacc = A2LYacc(Config())
    ast = yacc.generate_ast(project_block)
    assert ast
    print(ast)


def test_a2l_yacc_error_handling():
    """
    Tests the error handling of the A2L yacc parser.
    """
    sections_with_errors = """
    /begin project
        PROJECT 1.23e+6
        VERSION "1.0"
    /end project
    /begin project
        PROJECT "My Other Project"
        VERSION "2.1"
    /end project
    """
    yacc = A2LYacc(Config())
    ast = yacc.generate_ast(sections_with_errors)
    assert ast

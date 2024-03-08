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
# @TODO: Finish and add more complex error handling tests
# @TODO: test invalid quotes

from a2lparser.a2l.a2l_yacc import A2LYacc


def test_error_handling_nested_section():
    """
    This tests aims to check that an error can occur in a nested section.
    Expected behavior is for the error handling to allow all valid parts.
    """
    erroneous_input = """
    /begin MEASUREMENT
        N /* name */
        "Engine speed" /* long identifier */
        UWORD /* datatype */
        R_SPEED_3 /* conversion */
        2 /* resolution */
        2.5 /* accuracy */
        120.0 /* lower limit */
        8400.0 /* upper limit */
        /begin ANNOTATION
            ANNOTATION_LABEL "first valid label"
            /begin ANNOTATION_TEXT
                "first valid annotation text"
            /end ANNOTATION_TEXT
            ANNOTATION_ORIGIN "first valid annotation origin"
        /end ANNOTATION
        /begin ANNOTATION
            ANNOTATION_LABEL "label inside erroneous section"
            /begin ANNOTATION_TEXT
                0xee00ee00 /* ERROR PROVOKING TOKEN */
            /end ANNOTATION_TEXT
            ANNOTATION_ORIGIN "origin inside erroneous section"
        /end ANNOTATION
        /begin ANNOTATION
            ANNOTATION_LABEL "second valid label"
            /begin ANNOTATION_TEXT
                "second valid annotation text"
            /end ANNOTATION_TEXT
            ANNOTATION_ORIGIN "second valid annotation origin"
        /end ANNOTATION
        /begin FUNCTION_LIST
            ID_ADJUSTX  /* Valid function name */
            ID_ADJUSTY  /* Valid function name */
        /end FUNCTION_LIST
    /end MEASUREMENT
    """
    parser = A2LYacc()
    ast = parser.generate_ast(erroneous_input)
    assert ast

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


def test_unit_ast_error_resolve():
    """
    Tests the error resolve functionality of the parser.
    Will receive some valid and some invalid A2L blocks as input.
    """
    a2l_content = """
    ASAM VERSION "1.7.0"
    /BEGIN PROJECT
    PROJECT "My Project"
      VERSION "1.0"
    /END PROJECT
    /begin AXIS_DESCR STD_AXIS /* Standard axis points */
        N /* Reference to input quantity */
        CONV_N /* Conversion */
        14 /* Max.number of axis points*/
        0.0 /* Lower limit */
        5800.0 /* Upper limit*/
        /begin ANNOTATION
            ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_1"
            ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_1"
            /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_1"
            /end ANNOTATION_TEXT
        /end ANNOTATION
        MAX_GRAD 20.0 /* Axis: maximum gradient*/
        AXIS_PTS_REF GRP_N
        BYTE_ORDER MSB_LAST
        FIX_AXIS_PAR 0 4 6
        FIX_AXIS_PAR_DIST 0 100 8
        /begin FIX_AXIS_PAR_LIST
            2 5 9
        /end FIX_AXIS_PAR_LIST
        CURVE_AXIS_REF SPD_NORM
        DEPOSIT ABSOLUTE
        /begin ANNOTATION
            ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_2"
            ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_2"
            /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_2"
            /end ANNOTATION_TEXT
        /end ANNOTATION
        EXTENDED_LIMITS 0 6000.0
        PHYS_UNIT "Nm"
        READ_ONLY
        STEP_SIZE 0.025
        FORMAT "%4.2"
        MONOTONY MON_INCREASE
    /end AXIS_DESCR
    """
    a2l_yacc = A2LYacc()
    ast = a2l_yacc.generate_ast(a2l_content)
    assert ast

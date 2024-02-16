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


def test_rules_axis_descr():
    """
    Tests parsing a valid "AXIS_DESCR" block.
    """
    axis_descr_block = """
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
            /begin ANNOTATION_TEXT
                "ANNOTATION_TEXT_BLOCK_2_1"
                "ANNOTATION_TEXT_BLOCK_2_2"
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
    parser = A2LYacc()
    ast = parser.generate_ast(axis_descr_block)
    assert ast

    axis_descr = ast["AXIS_DESCR"]
    assert axis_descr
    assert axis_descr["Attribute"] == "STD_AXIS"
    assert axis_descr["InputQuantity"] == "N"
    assert axis_descr["CONVERSION"] == "CONV_N"
    assert axis_descr["MaxAxisPoints"] == "14"
    assert axis_descr["LowerLimit"] == "0.0"
    assert axis_descr["UpperLimit"] == "5800.0"
    assert axis_descr["AXIS_PTS_REF"] == "GRP_N"
    assert axis_descr["BYTE_ORDER"] == "MSB_LAST"
    assert axis_descr["CURVE_AXIS_REF"] == "SPD_NORM"
    assert axis_descr["DEPOSIT"] == "ABSOLUTE"
    assert axis_descr["FORMAT"] == '"%4.2"'
    assert axis_descr["MAX_GRAD"] == "20.0"
    assert axis_descr["MONOTONY"] == "MON_INCREASE"
    assert axis_descr["PHYS_UNIT"] == '"Nm"'
    assert axis_descr["READ_ONLY"] is True
    assert axis_descr["STEP_SIZE"] == "0.025"
    assert axis_descr["EXTENDED_LIMITS"]["LowerLimit"] == "0"
    assert axis_descr["EXTENDED_LIMITS"]["UpperLimit"] == "6000.0"
    assert axis_descr["EXTENDED_LIMITS"]["UpperLimit"] == "6000.0"
    assert axis_descr["FIX_AXIS_PAR"]["Offset"] == "0"
    assert axis_descr["FIX_AXIS_PAR"]["Shift"] == "4"
    assert axis_descr["FIX_AXIS_PAR"]["Numberapo"] == "6"
    assert axis_descr["FIX_AXIS_PAR_DIST"]["Offset"] == "0"
    assert axis_descr["FIX_AXIS_PAR_DIST"]["Distance"] == "100"
    assert axis_descr["FIX_AXIS_PAR_DIST"]["Numberapo"] == "8"
    assert axis_descr["FIX_AXIS_PAR_LIST"]["AxisPts_Value"] == ["2", "5", "9"]
    assert axis_descr["ANNOTATION"][0]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_BLOCK_1"'
    assert axis_descr["ANNOTATION"][0]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_BLOCK_1"'
    assert axis_descr["ANNOTATION"][0]["ANNOTATION_TEXT"] == ['"ANNOTATION_TEXT_BLOCK_1"']
    assert axis_descr["ANNOTATION"][1]["ANNOTATION_LABEL"] == '"ANNOTATION_LABEL_BLOCK_2"'
    assert axis_descr["ANNOTATION"][1]["ANNOTATION_ORIGIN"] == '"ANNOTATION_ORIGIN_BLOCK_2"'
    assert axis_descr["ANNOTATION"][1]["ANNOTATION_TEXT"] == ['"ANNOTATION_TEXT_BLOCK_2_1"', '"ANNOTATION_TEXT_BLOCK_2_2"']

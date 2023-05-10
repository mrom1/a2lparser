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


def test_rules_frame():
    """
    Tests parsing a valid "FRAME" block.
    """
    frame_block = """
    /begin FRAME ABS_ADJUSTM
        "function group ABS adjustment"
        3
        2 /* 2 msec. */
        FRAME_MEASUREMENT LOOP_COUNTER TEMPORARY_1
        /begin IF_DATA XCP
            LINK_MAP ref_name 0x003432
        /end IF_DATA
        /begin IF_DATA CANAPE
            STATIC ref_name 0xFF
        /end IF_DATA
    /end FRAME
    """
    parser = A2LYacc()
    ast = parser.generate_ast(frame_block)
    assert ast

    frame = ast["FRAME"]
    assert frame
    assert frame["Name"] == "ABS_ADJUSTM"
    assert frame["LongIdentifier"] == '"function group ABS adjustment"'
    assert frame["ScalingUnit"] == "3"
    assert frame["Rate"] == "2"
    assert frame["FRAME_MEASUREMENT"] == ["LOOP_COUNTER", "TEMPORARY_1"]
    assert frame["IF_DATA"][0]["Name"] == "XCP"
    assert frame["IF_DATA"][0]["DataParams"] == ["LINK_MAP", "ref_name", "0x003432"]
    assert frame["IF_DATA"][1]["Name"] == "CANAPE"
    assert frame["IF_DATA"][1]["DataParams"] == ["STATIC", "ref_name", "0xFF"]

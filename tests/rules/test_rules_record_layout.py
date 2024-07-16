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


def test_rules_record_layout():
    """
    Tests parsing a valid "RECORD_LAYOUT" block.
    """
    record_layout_block = """
    /begin RECORD_LAYOUT RL_MAP_SB
        ALIGNMENT_BYTE 1
        ALIGNMENT_WORD 2
        ALIGNMENT_LONG 4
        ALIGNMENT_FLOAT16_IEEE 1
        ALIGNMENT_FLOAT32_IEEE 2
        ALIGNMENT_FLOAT64_IEEE 4
        ALIGNMENT_INT64 4
        RESERVED 4 BYTE
        AXIS_PTS_X 3 ULONG INDEX_INCR DIRECT
        AXIS_PTS_Y 3 ULONG INDEX_INCR DIRECT
        AXIS_PTS_Z 3 ULONG INDEX_INCR DIRECT
        AXIS_PTS_4 3 ULONG INDEX_INCR DIRECT
        AXIS_PTS_5 3 ULONG INDEX_INCR DIRECT
        AXIS_RESCALE_X 3 UBYTE 5 INDEX_INCR DIRECT
        DIST_OP_X 21 UWORD
        DIST_OP_Y 21 UWORD
        DIST_OP_Z 21 UWORD
        DIST_OP_4 21 UWORD
        DIST_OP_5 21 UWORD
        FIX_NO_AXIS_PTS_X 17
        FIX_NO_AXIS_PTS_Y 17
        FIX_NO_AXIS_PTS_Z 17
        FIX_NO_AXIS_PTS_4 17
        FIX_NO_AXIS_PTS_5 17
        FNC_VALUES 7 SWORD COLUMN_DIR DIRECT
        IDENTIFICATION 1 UWORD
        NO_AXIS_PTS_X 2 UWORD
        NO_AXIS_PTS_Y 2 UWORD
        NO_AXIS_PTS_Z 2 UWORD
        NO_AXIS_PTS_4 2 UWORD
        NO_AXIS_PTS_5 2 UWORD
        NO_RESCALE_X 1 UBYTE
        OFFSET_X 16 UWORD
        OFFSET_Y 16 UWORD
        OFFSET_Z 16 UWORD
        OFFSET_4 16 UWORD
        OFFSET_5 16 UWORD
        RIP_ADDR_W 19 UWORD
        RIP_ADDR_X 19 UWORD
        RIP_ADDR_Y 19 UWORD
        RIP_ADDR_Z 19 UWORD
        RIP_ADDR_4 19 UWORD
        RIP_ADDR_5 19 UWORD
        SRC_ADDR_X 1 UWORD
        SRC_ADDR_Y 1 UWORD
        SRC_ADDR_Z 1 UWORD
        SRC_ADDR_4 1 UWORD
        SRC_ADDR_5 1 UWORD
        SHIFT_OP_X 21 UWORD
        SHIFT_OP_Y 21 UWORD
        SHIFT_OP_Z 21 UWORD
        SHIFT_OP_4 21 UWORD
        SHIFT_OP_5 21 UWORD
        STATIC_RECORD_LAYOUT
        STATIC_ADDRESS_OFFSETS
        RESERVED 2 BYTE
    /end RECORD_LAYOUT
    """
    parser = A2LYacc()
    ast = parser.generate_ast(record_layout_block)
    assert ast

    record_layout = ast["RECORD_LAYOUT"]
    assert record_layout

    assert record_layout["Name"] == "RL_MAP_SB"
    assert record_layout["ALIGNMENT_BYTE"] == "1"
    assert record_layout["ALIGNMENT_FLOAT16_IEEE"] == "1"
    assert record_layout["ALIGNMENT_FLOAT32_IEEE"] == "2"
    assert record_layout["ALIGNMENT_FLOAT64_IEEE"] == "4"
    assert record_layout["ALIGNMENT_INT64"] == "4"
    assert record_layout["ALIGNMENT_LONG"] == "4"
    assert record_layout["ALIGNMENT_WORD"] == "2"

    assert record_layout["FIX_NO_AXIS_PTS_X"] == "17"
    assert record_layout["FIX_NO_AXIS_PTS_Y"] == "17"
    assert record_layout["FIX_NO_AXIS_PTS_Z"] == "17"
    assert record_layout["FIX_NO_AXIS_PTS_4"] == "17"
    assert record_layout["FIX_NO_AXIS_PTS_5"] == "17"

    assert record_layout["AXIS_PTS_X"]["Position"] == "3"
    assert record_layout["AXIS_PTS_X"]["Datatype"] == "ULONG"
    assert record_layout["AXIS_PTS_X"]["IndexIncr"] == "INDEX_INCR"
    assert record_layout["AXIS_PTS_X"]["Addressing"] == "DIRECT"
    assert record_layout["AXIS_PTS_Y"]["Position"] == "3"
    assert record_layout["AXIS_PTS_Y"]["Datatype"] == "ULONG"
    assert record_layout["AXIS_PTS_Y"]["IndexIncr"] == "INDEX_INCR"
    assert record_layout["AXIS_PTS_Y"]["Addressing"] == "DIRECT"
    assert record_layout["AXIS_PTS_Z"]["Position"] == "3"
    assert record_layout["AXIS_PTS_Z"]["Datatype"] == "ULONG"
    assert record_layout["AXIS_PTS_Z"]["IndexIncr"] == "INDEX_INCR"
    assert record_layout["AXIS_PTS_Z"]["Addressing"] == "DIRECT"
    assert record_layout["AXIS_PTS_4"]["Position"] == "3"
    assert record_layout["AXIS_PTS_4"]["Datatype"] == "ULONG"
    assert record_layout["AXIS_PTS_4"]["IndexIncr"] == "INDEX_INCR"
    assert record_layout["AXIS_PTS_4"]["Addressing"] == "DIRECT"
    assert record_layout["AXIS_PTS_5"]["Position"] == "3"
    assert record_layout["AXIS_PTS_5"]["Datatype"] == "ULONG"
    assert record_layout["AXIS_PTS_5"]["IndexIncr"] == "INDEX_INCR"
    assert record_layout["AXIS_PTS_5"]["Addressing"] == "DIRECT"

    assert record_layout["AXIS_RESCALE_X"]["Position"] == "3"
    assert record_layout["AXIS_RESCALE_X"]["Datatype"] == "UBYTE"
    assert record_layout["AXIS_RESCALE_X"]["MaxNumberOfRescalePairs"] == "5"
    assert record_layout["AXIS_RESCALE_X"]["IndexIncr"] == "INDEX_INCR"
    assert record_layout["AXIS_RESCALE_X"]["Addressing"] == "DIRECT"

    assert record_layout["DIST_OP_X"]["Position"] == "21"
    assert record_layout["DIST_OP_X"]["Datatype"] == "UWORD"
    assert record_layout["DIST_OP_Y"]["Position"] == "21"
    assert record_layout["DIST_OP_Y"]["Datatype"] == "UWORD"
    assert record_layout["DIST_OP_Z"]["Position"] == "21"
    assert record_layout["DIST_OP_Z"]["Datatype"] == "UWORD"
    assert record_layout["DIST_OP_4"]["Position"] == "21"
    assert record_layout["DIST_OP_4"]["Datatype"] == "UWORD"
    assert record_layout["DIST_OP_5"]["Position"] == "21"
    assert record_layout["DIST_OP_5"]["Datatype"] == "UWORD"

    assert record_layout["FNC_VALUES"]["Position"] == "7"
    assert record_layout["FNC_VALUES"]["Datatype"] == "SWORD"
    assert record_layout["FNC_VALUES"]["IndexMode"] == "COLUMN_DIR"
    assert record_layout["FNC_VALUES"]["Addresstype"] == "DIRECT"

    assert record_layout["IDENTIFICATION"]["Position"] == "1"
    assert record_layout["IDENTIFICATION"]["Datatype"] == "UWORD"

    assert record_layout["NO_AXIS_PTS_X"]["Position"] == "2"
    assert record_layout["NO_AXIS_PTS_X"]["Datatype"] == "UWORD"
    assert record_layout["NO_AXIS_PTS_Y"]["Position"] == "2"
    assert record_layout["NO_AXIS_PTS_Y"]["Datatype"] == "UWORD"
    assert record_layout["NO_AXIS_PTS_Z"]["Position"] == "2"
    assert record_layout["NO_AXIS_PTS_Z"]["Datatype"] == "UWORD"
    assert record_layout["NO_AXIS_PTS_4"]["Position"] == "2"
    assert record_layout["NO_AXIS_PTS_4"]["Datatype"] == "UWORD"
    assert record_layout["NO_AXIS_PTS_5"]["Position"] == "2"
    assert record_layout["NO_AXIS_PTS_5"]["Datatype"] == "UWORD"

    assert record_layout["NO_RESCALE_X"]["Position"] == "1"
    assert record_layout["NO_RESCALE_X"]["Datatype"] == "UBYTE"

    assert record_layout["OFFSET_X"]["Position"] == "16"
    assert record_layout["OFFSET_X"]["Datatype"] == "UWORD"
    assert record_layout["OFFSET_Y"]["Position"] == "16"
    assert record_layout["OFFSET_Y"]["Datatype"] == "UWORD"
    assert record_layout["OFFSET_Z"]["Position"] == "16"
    assert record_layout["OFFSET_Z"]["Datatype"] == "UWORD"
    assert record_layout["OFFSET_4"]["Position"] == "16"
    assert record_layout["OFFSET_4"]["Datatype"] == "UWORD"
    assert record_layout["OFFSET_5"]["Position"] == "16"
    assert record_layout["OFFSET_5"]["Datatype"] == "UWORD"

    assert record_layout["RIP_ADDR_X"]["Position"] == "19"
    assert record_layout["RIP_ADDR_X"]["Datatype"] == "UWORD"
    assert record_layout["RIP_ADDR_Y"]["Position"] == "19"
    assert record_layout["RIP_ADDR_Y"]["Datatype"] == "UWORD"
    assert record_layout["RIP_ADDR_Z"]["Position"] == "19"
    assert record_layout["RIP_ADDR_Z"]["Datatype"] == "UWORD"
    assert record_layout["RIP_ADDR_4"]["Position"] == "19"
    assert record_layout["RIP_ADDR_4"]["Datatype"] == "UWORD"
    assert record_layout["RIP_ADDR_5"]["Position"] == "19"
    assert record_layout["RIP_ADDR_5"]["Datatype"] == "UWORD"

    assert record_layout["SRC_ADDR_X"]["Position"] == "1"
    assert record_layout["SRC_ADDR_X"]["Datatype"] == "UWORD"
    assert record_layout["SRC_ADDR_Y"]["Position"] == "1"
    assert record_layout["SRC_ADDR_Y"]["Datatype"] == "UWORD"
    assert record_layout["SRC_ADDR_Z"]["Position"] == "1"
    assert record_layout["SRC_ADDR_Z"]["Datatype"] == "UWORD"
    assert record_layout["SRC_ADDR_4"]["Position"] == "1"
    assert record_layout["SRC_ADDR_4"]["Datatype"] == "UWORD"
    assert record_layout["SRC_ADDR_5"]["Position"] == "1"
    assert record_layout["SRC_ADDR_5"]["Datatype"] == "UWORD"

    assert record_layout["SHIFT_OP_X"]["Position"] == "21"
    assert record_layout["SHIFT_OP_X"]["Datatype"] == "UWORD"
    assert record_layout["SHIFT_OP_Y"]["Position"] == "21"
    assert record_layout["SHIFT_OP_Y"]["Datatype"] == "UWORD"
    assert record_layout["SHIFT_OP_Z"]["Position"] == "21"
    assert record_layout["SHIFT_OP_Z"]["Datatype"] == "UWORD"
    assert record_layout["SHIFT_OP_4"]["Position"] == "21"
    assert record_layout["SHIFT_OP_4"]["Datatype"] == "UWORD"
    assert record_layout["SHIFT_OP_5"]["Position"] == "21"
    assert record_layout["SHIFT_OP_5"]["Datatype"] == "UWORD"

    assert len(record_layout["RESERVED"]) == 2
    assert record_layout["RESERVED"][0]["Position"] == "4"
    assert record_layout["RESERVED"][0]["DataSize"] == "BYTE"
    assert record_layout["RESERVED"][1]["Position"] == "2"
    assert record_layout["RESERVED"][1]["DataSize"] == "BYTE"

    assert record_layout["STATIC_RECORD_LAYOUT"] is True
    assert record_layout["STATIC_ADDRESS_OFFSETS"] is True

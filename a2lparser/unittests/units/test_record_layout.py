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


_TEST_FRAME_BLOCK = """
/begin RECORD_LAYOUT RL_MAP_SB
    ALIGNMENT_BYTE 1
    ALIGNMENT_WORD 2
    ALIGNMENT_LONG 4
    ALIGNMENT_FLOAT32_IEEE 2
    ALIGNMENT_FLOAT64_IEEE 4
    ALIGNMENT_INT64 4
    RESERVED 4 BYTE
    AXIS_PTS_X 3 ULONG INDEX_INCR DIRECT
    AXIS_PTS_Y 3 ULONG INDEX_INCR DIRECT
    AXIS_PTS_Z 3 ULONG INDEX_INCR DIRECT
    AXIS_PTS_Z4 3 ULONG INDEX_INCR DIRECT
    AXIS_PTS_Z5 3 ULONG INDEX_INCR DIRECT
    AXIS_RESCALE_X 3 UBYTE 5 INDEX_INCR DIRECT
    DIST_OP_X 21 UWORD
    DIST_OP_Y 21 UWORD
    DIST_OP_Z 21 UWORD
    DIST_OP_Z4 21 UWORD
    DIST_OP_Z5 21 UWORD
    FIX_NO_AXIS_PTS_X 17
    FIX_NO_AXIS_PTS_Y 17
    FIX_NO_AXIS_PTS_Z 17
    FIX_NO_AXIS_PTS_Z4 17
    FIX_NO_AXIS_PTS_Z5 17
    FNC_VALUES 7 SWORD COLUMN_DIR DIRECT
    IDENTIFICATION 1 UWORD
    NO_AXIS_PTS_X 2 UWORD
    NO_AXIS_PTS_Y 2 UWORD
    NO_AXIS_PTS_Z 2 UWORD
    NO_AXIS_PTS_Z4 2 UWORD
    NO_AXIS_PTS_Z5 2 UWORD
    NO_RESCALE_X 1 UBYTE
    OFFSET_X 16 UWORD
    OFFSET_Y 16 UWORD
    OFFSET_Z 16 UWORD
    OFFSET_Z4 16 UWORD
    OFFSET_Z5 16 UWORD
    RIP_ADDR_W 19 UWORD
    RIP_ADDR_X 19 UWORD
    RIP_ADDR_Y 19 UWORD
    RIP_ADDR_Z 19 UWORD
    RIP_ADDR_Z4 19 UWORD
    RIP_ADDR_Z5 19 UWORD
    SRC_ADDR_X 1 UWORD
    SRC_ADDR_Y 1 UWORD
    SRC_ADDR_Z 1 UWORD
    SRC_ADDR_Z4 1 UWORD
    SRC_ADDR_Z5 1 UWORD
    SHIFT_OP_X 21 UWORD
    SHIFT_OP_Y 21 UWORD
    SHIFT_OP_Z 21 UWORD
    SHIFT_OP_Z4 21 UWORD
    SHIFT_OP_Z5 21 UWORD
    STATIC_RECORD_LAYOUT
    RESERVED 2 BYTE
/end RECORD_LAYOUT
"""

_TEST_FRAME_BLOCK_EMPTY = """
/begin RECORD_LAYOUT
/end RECORD_LAYOUT
"""


class TestRecordLayout(Testhandler):
    def test_record_layout_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_record_layout_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FRAME_BLOCK,
                      filelength=_TEST_FRAME_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)

        self.assertEqual(tree.find('.//Name').text, "RL_MAP_SB")

        self.assertEqual(tree.find('.//Alignment_Byte').text, "1")
        self.assertEqual(tree.find('.//Alignment_Float32_Ieee').text, "2")
        self.assertEqual(tree.find('.//Alignment_Float64_Ieee').text, "4")
        self.assertEqual(tree.find('.//Alignment_Int64').text, "4")
        self.assertEqual(tree.find('.//Alignment_Long').text, "4")
        self.assertEqual(tree.find('.//Alignment_Word').text, "2"
                         )
        self.assertEqual(tree.find('.//Axis_Pts_X/Addressing').text, "DIRECT")
        self.assertEqual(tree.find('.//Axis_Pts_X/Datatype').text, "ULONG")
        self.assertEqual(tree.find('.//Axis_Pts_X/IndexIncr').text, "INDEX_INCR")
        self.assertEqual(tree.find('.//Axis_Pts_X/Position').text, "3")
        self.assertEqual(tree.find('.//Axis_Pts_Y/Addressing').text, "DIRECT")
        self.assertEqual(tree.find('.//Axis_Pts_Y/Datatype').text, "ULONG")
        self.assertEqual(tree.find('.//Axis_Pts_Y/IndexIncr').text, "INDEX_INCR")
        self.assertEqual(tree.find('.//Axis_Pts_Y/Position').text, "3")
        self.assertEqual(tree.find('.//Axis_Pts_Z/Addressing').text, "DIRECT")
        self.assertEqual(tree.find('.//Axis_Pts_Z/Datatype').text, "ULONG")
        self.assertEqual(tree.find('.//Axis_Pts_Z/IndexIncr').text, "INDEX_INCR")
        self.assertEqual(tree.find('.//Axis_Pts_Z/Position').text, "3")
        self.assertEqual(tree.find('.//Axis_Pts_Z4/Addressing').text, "DIRECT")
        self.assertEqual(tree.find('.//Axis_Pts_Z4/Datatype').text, "ULONG")
        self.assertEqual(tree.find('.//Axis_Pts_Z4/IndexIncr').text, "INDEX_INCR")
        self.assertEqual(tree.find('.//Axis_Pts_Z4/Position').text, "3")
        self.assertEqual(tree.find('.//Axis_Pts_Z5/Addressing').text, "DIRECT")
        self.assertEqual(tree.find('.//Axis_Pts_Z5/Datatype').text, "ULONG")
        self.assertEqual(tree.find('.//Axis_Pts_Z5/IndexIncr').text, "INDEX_INCR")
        self.assertEqual(tree.find('.//Axis_Pts_Z5/Position').text, "3")

        self.assertEqual(tree.find('.//Axis_Rescale_X/Addressing').text, "DIRECT")
        self.assertEqual(tree.find('.//Axis_Rescale_X/Datatype').text, "UBYTE")
        self.assertEqual(tree.find('.//Axis_Rescale_X/IndexIncr').text, "INDEX_INCR")
        self.assertEqual(tree.find('.//Axis_Rescale_X/Position').text, "3")
        self.assertEqual(tree.find('.//Axis_Rescale_X/MaxNumberOfRescalePairs').text, "5")

        self.assertEqual(tree.find('.//Dist_Op_X/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Dist_Op_X/Position').text, "21")
        self.assertEqual(tree.find('.//Dist_Op_Y/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Dist_Op_Y/Position').text, "21")
        self.assertEqual(tree.find('.//Dist_Op_Z/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Dist_Op_Z/Position').text, "21")
        self.assertEqual(tree.find('.//Dist_Op_Z4/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Dist_Op_Z4/Position').text, "21")
        self.assertEqual(tree.find('.//Dist_Op_Z5/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Dist_Op_Z5/Position').text, "21")

        self.assertEqual(tree.find('.//Fix_No_Axis_Pts_X').text, "17")
        self.assertEqual(tree.find('.//Fix_No_Axis_Pts_Y').text, "17")
        self.assertEqual(tree.find('.//Fix_No_Axis_Pts_Z').text, "17")
        self.assertEqual(tree.find('.//Fix_No_Axis_Pts_Z4').text, "17")
        self.assertEqual(tree.find('.//Fix_No_Axis_Pts_Z5').text, "17")

        self.assertEqual(tree.find('.//Fnc_Values/AddressType').text, "DIRECT")
        self.assertEqual(tree.find('.//Fnc_Values/Datatype').text, "SWORD")
        self.assertEqual(tree.find('.//Fnc_Values/IndexMode').text, "COLUMN_DIR")
        self.assertEqual(tree.find('.//Fnc_Values/Position').text, "7")

        self.assertEqual(tree.find('.//Identification/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Identification/Position').text, "1")

        self.assertEqual(tree.find('.//No_Axis_Pts_X/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//No_Axis_Pts_X/Position').text, "2")
        self.assertEqual(tree.find('.//No_Axis_Pts_Y/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//No_Axis_Pts_Y/Position').text, "2")
        self.assertEqual(tree.find('.//No_Axis_Pts_Z/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//No_Axis_Pts_Z/Position').text, "2")
        self.assertEqual(tree.find('.//No_Axis_Pts_Z4/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//No_Axis_Pts_Z4/Position').text, "2")
        self.assertEqual(tree.find('.//No_Axis_Pts_Z5/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//No_Axis_Pts_Z5/Position').text, "2")

        self.assertEqual(tree.find('.//No_Rescale_X/Datatype').text, "UBYTE")
        self.assertEqual(tree.find('.//No_Rescale_X/Position').text, "1")

        self.assertEqual(tree.find('.//Offset_X/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Offset_X/Position').text, "16")
        self.assertEqual(tree.find('.//Offset_Y/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Offset_Y/Position').text, "16")
        self.assertEqual(tree.find('.//Offset_Z/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Offset_Z/Position').text, "16")
        self.assertEqual(tree.find('.//Offset_Z4/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Offset_Z4/Position').text, "16")
        self.assertEqual(tree.find('.//Offset_Z5/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Offset_Z5/Position').text, "16")

        self.assertEqual(tree.find('.//Rip_Addr_W/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Rip_Addr_W/Position').text, "19")
        self.assertEqual(tree.find('.//Rip_Addr_X/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Rip_Addr_X/Position').text, "19")
        self.assertEqual(tree.find('.//Rip_Addr_Y/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Rip_Addr_Y/Position').text, "19")
        self.assertEqual(tree.find('.//Rip_Addr_Z/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Rip_Addr_Z/Position').text, "19")
        self.assertEqual(tree.find('.//Rip_Addr_Z4/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Rip_Addr_Z4/Position').text, "19")
        self.assertEqual(tree.find('.//Rip_Addr_Z5/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Rip_Addr_Z5/Position').text, "19")

        self.assertEqual(tree.find('.//Shift_Op_X/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Shift_Op_X/Position').text, "21")
        self.assertEqual(tree.find('.//Shift_Op_Y/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Shift_Op_Y/Position').text, "21")
        self.assertEqual(tree.find('.//Shift_Op_Z/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Shift_Op_Z/Position').text, "21")
        self.assertEqual(tree.find('.//Shift_Op_Z4/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Shift_Op_Z4/Position').text, "21")
        self.assertEqual(tree.find('.//Shift_Op_Z5/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Shift_Op_Z5/Position').text, "21")

        self.assertEqual(tree.find('.//Src_Addr_X/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Src_Addr_X/Position').text, "1")
        self.assertEqual(tree.find('.//Src_Addr_Y/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Src_Addr_Y/Position').text, "1")
        self.assertEqual(tree.find('.//Src_Addr_Z/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Src_Addr_Z/Position').text, "1")
        self.assertEqual(tree.find('.//Src_Addr_Z4/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Src_Addr_Z4/Position').text, "1")
        self.assertEqual(tree.find('.//Src_Addr_Z5/Datatype').text, "UWORD")
        self.assertEqual(tree.find('.//Src_Addr_Z5/Position').text, "1")

        self.assertEqual(tree.find('.//Static_Record_Layout').text, "True")

        reserverd = tree.findall('.//Reserved')
        self.assertEqual(len(reserverd), 2)
        self.assertEqual(reserverd[0].find('.//DataSize').text, "BYTE")
        self.assertEqual(reserverd[0].find('.//Position').text, "4")
        self.assertEqual(reserverd[1].find('.//DataSize').text, "BYTE")
        self.assertEqual(reserverd[1].find('.//Position').text, "2")

    def test_record_layout_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_record_layout_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FRAME_BLOCK_EMPTY,
                      filelength=_TEST_FRAME_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

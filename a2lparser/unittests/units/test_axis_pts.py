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


_TEST_AXIS_PTS_BLOCK = """
/begin AXIS_PTS STV_N /* name */
    "axis points distribution speed" /* long identifier */
    0x9876 /* address */
    N /* input quantity */
    DAMOS_SST /* deposit */
    100.0 /* maxdiff */
    R_SPEED /* conversion */
    21 /* maximum number of axis points */
    0.0 /* lower limit */
    5800.0 /* upper limit */
    /begin ANNOTATION
        ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_1"
        ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_1"
        /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_1"
        /end ANNOTATION_TEXT
    /end ANNOTATION
    GUARD_RAILS /* uses guard rails*/
    REF_MEMORY_SEGMENT Data3
    /begin FUNCTION_LIST
        ID_ADJUSTM
        FL_ADJUSTM
        SPEED_LIM
    /end FUNCTION_LIST
    /begin IF_DATA
        ASAP1B_EXAMPLE /* Name of device */
        /* interface-specific parameters described in A2ML */
        /begin DP_BLOB
            0x12129977
            0xFF
        /end DP_BLOB
        /* interface-specific parameters described in A2ML */
        /begin PA_BLOB
            "Pumpenkennfeld"
            1
            2
            17
        /end PA_BLOB
    /end IF_DATA
    CALIBRATION_ACCESS CALIBRATION
    /begin ANNOTATION
        ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_2"
        ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_2"
        /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_2"
        /end ANNOTATION_TEXT
    /end ANNOTATION
    BYTE_ORDER MSB_LAST
    DISPLAY_IDENTIFIER load_engine
    STEP_SIZE 0.025
    FORMAT "%4.2"
    PHYS_UNIT "Nm"
    ECU_ADDRESS_EXTENSION 2
    READ_ONLY
    SYMBOL_LINK
        "_VehicleSpeed" /* Symbol name */
        0 /* Offset */
    MONOTONY MON_INCREASE
    DEPOSIT ABSOLUTE
    EXTENDED_LIMITS 0 6000.0
    /begin IF_DATA
        ASAP1B_EXAMPLE /* Name of device */
        "TEST_STRING"
        0x0123212 /* some address */
        TEST_IDENT
    /end IF_DATA
/end AXIS_PTS
"""

_TEST_AXIS_PTS_BLOCK_EMPTY = """
/begin AXIS_PTS
    /begin ANNOTATION
        /begin ANNOTATION_TEXT
        /end ANNOTATION_TEXT
    /end ANNOTATION
    /begin FUNCTION_LIST
    /end FUNCTION_LIST
/end AXIS_PTS
"""


class TestAxisPts(Testhandler):
    def test_axis_pts_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_axis_pts_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_AXIS_PTS_BLOCK,
                      filelength=_TEST_AXIS_PTS_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        axis_pts = tree.findall('Axis_Pts')

        self.assertEqual(len(axis_pts), 1)
        # mandatory parameter
        axis_pts = axis_pts[0]
        self.assertEqual(axis_pts.find('.//Name').text, "STV_N")
        self.assertEqual(axis_pts.find('.//LongIdentifier').text, "axis points distribution speed")
        self.assertEqual(axis_pts.find('.//InputQuantity').text, "N")
        self.assertEqual(axis_pts.find('.//Deposit_Ref').text, "DAMOS_SST")
        self.assertEqual(axis_pts.find('.//MaxDiff').text, "100.0")
        self.assertEqual(axis_pts.find('.//Conversion').text, "R_SPEED")
        self.assertEqual(axis_pts.find('.//MaxAxisPoints').text, "21")
        self.assertEqual(axis_pts.find('.//LowerLimit').text, "0.0")
        self.assertEqual(axis_pts.find('.//UpperLimit').text, "5800.0")

        # optional parameters
        self.assertEqual(axis_pts.find('.//Byte_Order').text, "MSB_LAST")
        self.assertEqual(axis_pts.find('.//Calibration_Access').text, "CALIBRATION")
        self.assertEqual(axis_pts.find('.//Display_Identifier').text, "load_engine")
        self.assertEqual(axis_pts.find('.//Deposit').text, "ABSOLUTE")
        self.assertEqual(axis_pts.find('.//Ecu_Address_Extension').text, "2")
        self.assertEqual(axis_pts.find('.//Format').text, "%4.2")
        self.assertEqual(axis_pts.find('.//Guard_Rails').text, "True")
        self.assertEqual(axis_pts.find('.//Monotony').text, "MON_INCREASE")
        self.assertEqual(axis_pts.find('.//Phys_Unit').text, "Nm")
        self.assertEqual(axis_pts.find('.//Read_Only').text, "True")
        self.assertEqual(axis_pts.find('.//Ref_Memory_Segment').text, "Data3")
        self.assertEqual(axis_pts.find('.//Step_Size').text, "0.025")
        self.assertEqual(axis_pts.find('.//Extended_Limits/UpperLimit').text, "6000.0")
        self.assertEqual(axis_pts.find('.//Extended_Limits/LowerLimit').text, "0")
        self.assertEqual(axis_pts.find('.//Function_List/Name').text, "ID_ADJUSTM, FL_ADJUSTM, SPEED_LIM")
        self.assertEqual(axis_pts.find('.//Symbol_Link/SymbolName').text, "_VehicleSpeed")
        self.assertEqual(axis_pts.find('.//Symbol_Link/Offset').text, "0")

        annotation = axis_pts.findall('Annotation')
        self.assertEqual(len(annotation), 2)
        self.assertEqual(annotation[0].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_BLOCK_1")
        self.assertEqual(annotation[0].find('.//Annotation_Label').text, "ANNOTATION_LABEL_BLOCK_1")
        self.assertEqual(annotation[0].find('.//Annotation_Text').text, "ANNOTATION_TEXT_BLOCK_1")
        self.assertEqual(annotation[1].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_BLOCK_2")
        self.assertEqual(annotation[1].find('.//Annotation_Label').text, "ANNOTATION_LABEL_BLOCK_2")
        self.assertEqual(annotation[1].find('.//Annotation_Text').text, "ANNOTATION_TEXT_BLOCK_2")

        # ToDo: IF_DATA_Test
        # if_data = axis_pts.findall('If_Data')
        # self.assertEqual(len(if_data), 2)
        # self.assertEqual(len(if_data[0][0]), 3)
        # x = if_data[0][0]


        function_list = axis_pts.findall('Function_List')
        self.assertEqual(len(function_list), 1)
        self.assertEqual(function_list[0].findall('.//Name')[0].text, "ID_ADJUSTM, FL_ADJUSTM, SPEED_LIM")

    def test_axis_pts_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_axis_pts_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_AXIS_PTS_BLOCK_EMPTY,
                      filelength=_TEST_AXIS_PTS_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validate_abstract_syntax_tree(ast), False)

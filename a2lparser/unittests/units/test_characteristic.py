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


import platform
from a2lparser.unittests.testhandler import Testhandler


_TEST_CHARACTERISTIC_BLOCK = """
/begin CHARACTERISTIC
	PUMKF /* name */
	"Pump characteristic map" /* long identifier */
	MAP /* type */
	0x7140 /* address */
	DAMOS_KF /* deposit */
	100.0 /* maxdiff */
	R_VOLTAGE /* conversion */
	0.0 /* lower limit */
	5000.0 /* upper limit */
	BIT_MASK 0x40
	BYTE_ORDER MSB_LAST
	CALIBRATION_ACCESS OFFLINE_CALIBRATION
	COMPARISON_QUANTITY COMPARISON_QUANTITY_NAME
	DISCRETE
	DISPLAY_IDENTIFIER load_engine
	FORMAT "%0.2"
	ECU_ADDRESS_EXTENSION 2
	EXTENDED_LIMITS 0 4000.0
	/begin DEPENDENT_CHARACTERISTIC
		"sin(X1)"
		BETA
	/end DEPENDENT_CHARACTERISTIC
	REF_MEMORY_SEGMENT Data1
	/begin FUNCTION_LIST
		ID_ADJUSTM
		FL_ADJUSTM
		SPEED_LIM
	/end FUNCTION_LIST
	GUARD_RAILS
	MATRIX_DIM 2 4 3
	/begin MAP_LIST
		one two three
	/end MAP_LIST
	NUMBER 123123123
	MAX_REFRESH 3 15
	PHYS_UNIT "Nm"
	READ_ONLY
	STEP_SIZE 3
	/begin IF_DATA
		DIM
		EXTERNAL
		INDIRECT
	/end IF_DATA
	SYMBOL_LINK
		"_VehicleSpeed" /* Symbol name */
		0 /* Offset */
	/begin ANNOTATION
		ANNOTATION_LABEL "ANNOTATION_LABEL_CHARACTERISTIC_1"
		ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_CHARACTERISTIC_1"
	/end ANNOTATION
	/begin ANNOTATION
		ANNOTATION_LABEL "ANNOTATION_LABEL_CHARACTERISTIC_2"
		ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_CHARACTERISTIC_2"
		/begin ANNOTATION_TEXT "ANNOTATION_TEXT_CHARACERISTIC"
		/end ANNOTATION_TEXT
	/end ANNOTATION
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
	/begin AXIS_DESCR
		/* description of Y-axis points */
		STD_AXIS /* standard axis points */
		AMOUNT /* reference to input quantity */
		CON_ME /* conversion */
		17 /* maximum number of axis points*/
		0.0 /* lower limit */
		43.0 /* upper limit */
	/end AXIS_DESCR
	/begin VIRTUAL_CHARACTERISTIC
		"sin(X1)"
		B
	/end VIRTUAL_CHARACTERISTIC
/end CHARACTERISTIC
"""

_TEST_CHARACTERISTIC_BLOCK_EMPTY = """
/begin CHARACTERISTIC
	/begin ANNOTATION
	/end ANNOTATION
	/begin AXIS_DESCR
	/end AXIS_DESCR
    /begin DEPENDENT_CHARACTERISTIC
	/end DEPENDENT_CHARACTERISTIC
    /begin FUNCTION_LIST
    /end FUNCTION_LIST
	/begin VIRTUAL_CHARACTERISTIC
	/end VIRTUAL_CHARACTERISTIC
    /begin IF_DATA
	/end IF_DATA
	/begin IF_DATA
	/end IF_DATA
	/begin MAP_LIST
	/end MAP_LIST
/end CHARACTERISTIC
"""


class TestCharacteristic(Testhandler):
    def test_characteristic_block(self):
        if platform.python_version_tuple()[0] == "2":
            from cStringIO import StringIO
        else:
            from io import StringIO

        p = self.param.parser
        ast = p.parse(filename="test_characteristic_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_CHARACTERISTIC_BLOCK,
                      filelength=_TEST_CHARACTERISTIC_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        characteristic = tree.findall('Characteristic')

        self.assertEqual(len(characteristic), 1)

        # mandatory parameter
        characteristic = characteristic[0]
        self.assertEqual(characteristic.find('.//Name').text, "PUMKF")
        self.assertEqual(characteristic.find('.//LongIdentifier').text, "Pump characteristic map")
        self.assertEqual(characteristic.find('.//Type').text, "MAP")
        self.assertEqual(characteristic.find('.//Address').text, "0x7140")
        self.assertEqual(characteristic.find('.//Deposit_Ref').text, "DAMOS_KF")
        self.assertEqual(characteristic.find('.//MaxDiff').text, "100.0")
        self.assertEqual(characteristic.find('.//Conversion').text, "R_VOLTAGE")
        self.assertEqual(characteristic.find('.//LowerLimit').text, "0.0")
        self.assertEqual(characteristic.find('.//UpperLimit').text, "5000.0")

        # optional parameters
        self.assertEqual(characteristic.find('.//Bit_Mask').text, "0x40")
        self.assertEqual(characteristic.find('.//Byte_Order').text, "MSB_LAST")
        self.assertEqual(characteristic.find('.//Calibration_Access').text, "OFFLINE_CALIBRATION")
        self.assertEqual(characteristic.find('.//Comparison_Quantity').text, "COMPARISON_QUANTITY_NAME")
        self.assertEqual(characteristic.find('.//Dependent_Characteristic/Formula').text, "sin(X1)")
        self.assertEqual(characteristic.find('.//Dependent_Characteristic/Characteristic').text, "BETA")
        self.assertEqual(characteristic.find('.//Discrete').text, "True")
        self.assertEqual(characteristic.find('.//Display_Identifier').text, "load_engine")
        self.assertEqual(characteristic.find('.//Ecu_Address_Extension').text, "2")
        self.assertEqual(characteristic.find('.//Extended_Limits/UpperLimit').text, "4000.0")
        self.assertEqual(characteristic.find('.//Extended_Limits/LowerLimit').text, "0")

        self.assertEqual(characteristic.find('.//Format').text, "%0.2")
        self.assertEqual(characteristic.find('.//Function_List/Name').text, "ID_ADJUSTM, FL_ADJUSTM, SPEED_LIM")
        self.assertEqual(characteristic.find('.//Guard_Rails').text, "True")

        self.assertEqual(characteristic.find('.//Map_List/Name').text, "one, two, three")
        self.assertEqual(characteristic.find('.//Matrix_Dim/xDim').text, "2")
        self.assertEqual(characteristic.find('.//Matrix_Dim/yDim').text, "4")
        self.assertEqual(characteristic.find('.//Matrix_Dim/zDim').text, "3")

        self.assertEqual(characteristic.find('.//Max_Refresh/ScalingUnit').text, "3")
        self.assertEqual(characteristic.find('.//Max_Refresh/Rate').text, "15")

        self.assertEqual(characteristic.find('.//Number').text, "123123123")
        self.assertEqual(characteristic.find('.//Phys_Unit').text, "Nm")
        self.assertEqual(characteristic.find('.//Read_Only').text, "True")
        self.assertEqual(characteristic.find('.//Ref_Memory_Segment').text, "Data1")

        self.assertEqual(characteristic.find('.//Step_Size').text, "3")
        self.assertEqual(characteristic.find('.//Symbol_Link/SymbolName').text, "_VehicleSpeed")
        self.assertEqual(characteristic.find('.//Symbol_Link/Offset').text, "0")

        self.assertEqual(characteristic.find('.//Virtual_Characteristic/Formula').text, "sin(X1)")
        self.assertEqual(characteristic.find('.//Virtual_Characteristic/Characteristic').text, "B")

        annotation = characteristic.findall('Annotation')  # annoation in characteristic
        self.assertEqual(len(annotation), 2)
        self.assertEqual(annotation[0].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_CHARACTERISTIC_1")
        self.assertEqual(annotation[0].find('.//Annotation_Label').text, "ANNOTATION_LABEL_CHARACTERISTIC_1")
        self.assertEqual(annotation[1].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_CHARACTERISTIC_2")
        self.assertEqual(annotation[1].find('.//Annotation_Label').text, "ANNOTATION_LABEL_CHARACTERISTIC_2")
        self.assertEqual(annotation[1].find('.//Annotation_Text').text, "ANNOTATION_TEXT_CHARACERISTIC")

        axis_descr = characteristic.findall('Axis_Descr')
        self.assertEqual(len(axis_descr), 2)

        self.assertEqual(axis_descr[0].find('.//Attribute').text, "STD_AXIS")
        self.assertEqual(axis_descr[0].find('.//InputQuantity').text, "N")
        self.assertEqual(axis_descr[0].find('.//Conversion').text, "CONV_N")
        self.assertEqual(axis_descr[0].find('.//MaxAxisPoints').text, "14")
        self.assertEqual(axis_descr[0].find('.//LowerLimit').text, "0.0")
        self.assertEqual(axis_descr[0].find('.//UpperLimit').text, "5800.0")
        self.assertEqual(axis_descr[0].find('.//Axis_Pts_Ref').text, "GRP_N")
        self.assertEqual(axis_descr[0].find('.//Byte_Order').text, "MSB_LAST")
        self.assertEqual(axis_descr[0].find('.//Curve_Axis_Ref').text, "SPD_NORM")
        self.assertEqual(axis_descr[0].find('.//Deposit').text, "ABSOLUTE")
        self.assertEqual(axis_descr[0].find('.//Format').text, "%4.2")
        self.assertEqual(axis_descr[0].find('.//Max_Grad').text, "20.0")
        self.assertEqual(axis_descr[0].find('.//Monotony').text, "MON_INCREASE")
        self.assertEqual(axis_descr[0].find('.//Phys_Unit').text, "Nm")
        self.assertEqual(axis_descr[0].find('.//Read_Only').text, "True")
        self.assertEqual(axis_descr[0].find('.//Step_Size').text, "0.025")
        self.assertEqual(axis_descr[0].find('.//Extended_Limits/UpperLimit').text, "6000.0")
        self.assertEqual(axis_descr[0].find('.//Extended_Limits/LowerLimit').text, "0")
        self.assertEqual(axis_descr[0].find('.//Fix_Axis_Par/Offset').text, "0")
        self.assertEqual(axis_descr[0].find('.//Fix_Axis_Par/Shift').text, "4")
        self.assertEqual(axis_descr[0].find('.//Fix_Axis_Par/Numberapo').text, "6")
        self.assertEqual(axis_descr[0].find('.//Fix_Axis_Par_Dist/Offset').text, "0")
        self.assertEqual(axis_descr[0].find('.//Fix_Axis_Par_Dist/Distance').text, "100")
        self.assertEqual(axis_descr[0].find('.//Fix_Axis_Par_Dist/Numberapo').text, "8")
        self.assertEqual(axis_descr[0].find('.//Fix_Axis_Par_List/AxisPts_Value').text, "2, 5, 9")

        self.assertEqual(axis_descr[1].find('.//Attribute').text, "STD_AXIS")
        self.assertEqual(axis_descr[1].find('.//InputQuantity').text, "AMOUNT")
        self.assertEqual(axis_descr[1].find('.//Conversion').text, "CON_ME")
        self.assertEqual(axis_descr[1].find('.//MaxAxisPoints').text, "17")
        self.assertEqual(axis_descr[1].find('.//LowerLimit').text, "0.0")
        self.assertEqual(axis_descr[1].find('.//UpperLimit').text, "43.0")


        # ToDo: IF_DATA_Test
        # if_data = axis_pts.findall('If_Data')
        # self.assertEqual(len(if_data), 2)
        # self.assertEqual(len(if_data[0][0]), 3)
        # x = if_data[0][0]

    def test_characteristic_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_characteristic_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_CHARACTERISTIC_BLOCK_EMPTY,
                      filelength=_TEST_CHARACTERISTIC_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validate_abstract_syntax_tree(ast), False)

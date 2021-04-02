import xml.etree.ElementTree as et
from tests.testhandler import Testhandler

_TEST_AXIS_DESCR_BLOCK_EMPTY = """
/begin AXIS_DESCR
    /begin ANNOTATION
        /begin ANNOTATION_TEXT
        /end ANNOTATION_TEXT
    /end ANNOTATION
    /begin FIX_AXIS_PAR_LIST
    /end FIX_AXIS_PAR_LIST
    /begin ANNOTATION
        /begin ANNOTATION_TEXT
        /end ANNOTATION_TEXT
    /end ANNOTATION
    /begin FIX_AXIS_PAR_LIST
    /end FIX_AXIS_PAR_LIST
/end AXIS_DESCR
"""

_TEST_AXIS_DESCR_BLOCK = """
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


class TestAxisDescr(Testhandler):
    def test_axis_descr_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_axis_descr_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_AXIS_DESCR_BLOCK,
                      filelength=_TEST_AXIS_DESCR_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        axis_descr = tree.findall('Axis_Descr')

        self.assertEqual(len(axis_descr), 1)

        # mandatory parameter
        axis_descr = axis_descr[0]
        self.assertEqual(axis_descr.find('.//Attribute').text, "STD_AXIS")
        self.assertEqual(axis_descr.find('.//InputQuantity').text, "N")
        self.assertEqual(axis_descr.find('.//Conversion').text, "CONV_N")
        self.assertEqual(axis_descr.find('.//MaxAxisPoints').text, "14")
        self.assertEqual(axis_descr.find('.//LowerLimit').text, "0.0")
        self.assertEqual(axis_descr.find('.//UpperLimit').text, "5800.0")

        # optional parameters
        self.assertEqual(axis_descr.find('.//Axis_Pts_Ref').text, "GRP_N")
        self.assertEqual(axis_descr.find('.//Byte_Order').text, "MSB_LAST")
        self.assertEqual(axis_descr.find('.//Curve_Axis_Ref').text, "SPD_NORM")
        self.assertEqual(axis_descr.find('.//Deposit').text, "ABSOLUTE")
        self.assertEqual(axis_descr.find('.//Format').text, "%4.2")
        self.assertEqual(axis_descr.find('.//Max_Grad').text, "20.0")
        self.assertEqual(axis_descr.find('.//Monotony').text, "MON_INCREASE")
        self.assertEqual(axis_descr.find('.//Phys_Unit').text, "Nm")
        self.assertEqual(axis_descr.find('.//Read_Only').text, "True")
        self.assertEqual(axis_descr.find('.//Step_Size').text, "0.025")
        self.assertEqual(axis_descr.find('.//Extended_Limits/UpperLimit').text, "6000.0")
        self.assertEqual(axis_descr.find('.//Extended_Limits/LowerLimit').text, "0")
        self.assertEqual(axis_descr.find('.//Fix_Axis_Par/Offset').text, "0")
        self.assertEqual(axis_descr.find('.//Fix_Axis_Par/Shift').text, "4")
        self.assertEqual(axis_descr.find('.//Fix_Axis_Par/Numberapo').text, "6")
        self.assertEqual(axis_descr.find('.//Fix_Axis_Par_Dist/Offset').text, "0")
        self.assertEqual(axis_descr.find('.//Fix_Axis_Par_Dist/Distance').text, "100")
        self.assertEqual(axis_descr.find('.//Fix_Axis_Par_Dist/Numberapo').text, "8")
        self.assertEqual(axis_descr.find('.//Fix_Axis_Par_List/AxisPts_Value').text, "2, 5, 9")

        annotation = axis_descr.findall('Annotation')
        self.assertEqual(len(annotation), 2)
        self.assertEqual(annotation[0].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_BLOCK_1")
        self.assertEqual(annotation[0].find('.//Annotation_Label').text, "ANNOTATION_LABEL_BLOCK_1")
        self.assertEqual(annotation[0].find('.//Annotation_Text').text, "ANNOTATION_TEXT_BLOCK_1")
        self.assertEqual(annotation[1].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_BLOCK_2")
        self.assertEqual(annotation[1].find('.//Annotation_Label').text, "ANNOTATION_LABEL_BLOCK_2")
        self.assertEqual(annotation[1].find('.//Annotation_Text').text, "ANNOTATION_TEXT_BLOCK_2")

    def test_axis_descr_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_axis_descr_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_AXIS_DESCR_BLOCK_EMPTY,
                      filelength=_TEST_AXIS_DESCR_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

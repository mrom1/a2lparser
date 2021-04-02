from tests.testhandler import Testhandler

_TEST_MEASUREMENT_BLOCK = """
/begin MEASUREMENT xxx4b4b52c21075c8.xc33258c9a5f26f4284.x87f0.x871bxxx "ex1"
      SWORD NO_FORMULA 0 0 -32768 32767
      BIT_MASK 0xFFFF
      BYTE_ORDER MSB_FIRST
      ECU_ADDRESS 0x2D474
      ECU_ADDRESS_EXTENSION 0x0
      FORMAT "%.3"
      DISCRETE
      /begin IF_DATA CANAPE_EXT
        100
        LINK_MAP "xxx79c13e523bc16dfbba3285.x794ec36d9751f96100fb3400ff.x79f0cb.x791bcbxxx" 0x2D474 0x0 0 0x0 1 0xCF 0x0
        DISPLAY 0 -36044.75 36043.75
      /end IF_DATA
      /begin IF_DATA CANAPE
        DISPLAY 0 -36044.75 36043.75
      /end IF_DATA
      ERROR_MASK 0x00000001
      LAYOUT ALTERNATE_WITH_Y
      MATRIX_DIM 2 4 3
      MAX_REFRESH 998 2
      PHYS_UNIT "Nm"
      READ_WRITE
      REF_MEMORY_SEGMENT Data1
      /begin ANNOTATION
        ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_1"
        ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_1"
        /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_1"
        /end ANNOTATION_TEXT
      /end ANNOTATION
	  /begin ANNOTATION
        ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_2"
        ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_2"
        /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_2"
        /end ANNOTATION_TEXT
      /end ANNOTATION
      /begin VIRTUAL
        PHI_BASIS
        PHI_CORR
      /end VIRTUAL
      SYMBOL_LINK
        "_VehicleSpeed" /* Symbol name */
        0 /* Offset */
/end MEASUREMENT
"""

_TEST_MEASUREMENT_BLOCK_EMPTY = """
/begin MEASUREMENT
/end MEASUREMENT
"""


class TestMeasurement(Testhandler):
    def test_measurement_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_measurement_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_MEASUREMENT_BLOCK,
                      filelength=_TEST_MEASUREMENT_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "xxx4b4b52c21075c8.xc33258c9a5f26f4284.x87f0.x871bxxx")
        self.assertEqual(tree.find('.//LongIdentifier').text, "ex1")
        self.assertEqual(tree.find('.//Datatype').text, "SWORD")
        self.assertEqual(tree.find('.//Conversion').text, "NO_FORMULA")
        self.assertEqual(tree.find('.//Resolution').text, "0")
        self.assertEqual(tree.find('.//Accuracy').text, "0")
        self.assertEqual(tree.find('.//LowerLimit').text, "-32768")
        self.assertEqual(tree.find('.//UpperLimit').text, "32767")
        self.assertEqual(tree.find('.//Bit_Mask').text, "0xFFFF")
        self.assertEqual(tree.find('.//Byte_Order').text, "MSB_FIRST")
        self.assertEqual(tree.find('.//Ecu_Address').text, "0x2D474")
        self.assertEqual(tree.find('.//Ecu_Address_Extension').text, "0x0")
        self.assertEqual(tree.find('.//Format').text, "%.3")
        self.assertEqual(tree.find('.//Discrete').text, "True")
        self.assertEqual(tree.find('.//Error_Mask').text, "0x00000001")
        self.assertEqual(tree.find('.//Layout').text, "ALTERNATE_WITH_Y")
        self.assertEqual(tree.find('.//Phys_Unit').text, "Nm")
        self.assertEqual(tree.find('.//Read_Write').text, "True")
        self.assertEqual(tree.find('.//Ref_Memory_Segment').text, "Data1")
        self.assertEqual(tree.find('.//Max_Refresh/ScalingUnit').text, "998")
        self.assertEqual(tree.find('.//Max_Refresh/Rate').text, "2")
        self.assertEqual(tree.find('.//Symbol_Link/SymbolName').text, "_VehicleSpeed")
        self.assertEqual(tree.find('.//Symbol_Link/Offset').text, "0")
        self.assertEqual(tree.find('.//Virtual/MeasuringChannel').text, "PHI_BASIS, PHI_CORR")

        if_data = tree.findall('.//If_Data')
        self.assertEqual(len(if_data), 2)
        self.assertEqual(if_data[0].find('.//Name').text, "CANAPE_EXT")
        self.assertEqual(if_data[0].find('.//DataParams').text,
                         "100, LINK_MAP, xxx79c13e523bc16dfbba3285.x794ec36d9751f96100fb3400ff.x79f0cb.x791bcbxxx, 0x2D474, 0x0, 0, 0x0, 1, 0xCF, 0x0, DISPLAY, 0, -36044.75, 36043.75")
        self.assertEqual(if_data[1].find('.//Name').text, "CANAPE")
        self.assertEqual(if_data[1].find('.//DataParams').text, "DISPLAY, 0, -36044.75, 36043.75")

        annotation = tree.findall('.//Annotation')  # annoation in characteristic
        self.assertEqual(len(annotation), 2)
        self.assertEqual(annotation[0].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_BLOCK_1")
        self.assertEqual(annotation[0].find('.//Annotation_Label').text, "ANNOTATION_LABEL_BLOCK_1")
        self.assertEqual(annotation[0].find('.//Annotation_Text').text, "ANNOTATION_TEXT_BLOCK_1")
        self.assertEqual(annotation[1].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_BLOCK_2")
        self.assertEqual(annotation[1].find('.//Annotation_Label').text, "ANNOTATION_LABEL_BLOCK_2")
        self.assertEqual(annotation[1].find('.//Annotation_Text').text, "ANNOTATION_TEXT_BLOCK_2")

    def test_measurement_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_measurement_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_MEASUREMENT_BLOCK_EMPTY,
                      filelength=_TEST_MEASUREMENT_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

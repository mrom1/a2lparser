from tests.testhandler import Testhandler

_TEST_FUNCTION_BLOCK = """
/begin FUNCTION
	Sssm140_CalcStopDynDecel
	"IDENT_LNG"
	FUNCTION_VERSION "BG5.0815"
	/begin SUB_FUNCTION
		CalcDynDecelState
		CalcStopDynDecel
		Sssm313_AEB_disabled
		Sssm314_AEB_enabled
		Sssm37_Subsystem
	/end SUB_FUNCTION
	/begin LOC_MEASUREMENT
		SsmInLastWinsThreshold
		SsmInThrottlePedalPosition
	/end LOC_MEASUREMENT
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
	/begin DEF_CHARACTERISTIC
		INJECTION_CURVE
		DELAY_FACTOR
	/end DEF_CHARACTERISTIC
	/begin IN_MEASUREMENT
		WHEEL_REVOLUTIONS
		ENGINE_SPEED
	/end IN_MEASUREMENT
	/begin OUT_MEASUREMENT
		OK_FLAG
		SENSOR_FLAG
	/end OUT_MEASUREMENT
	/begin REF_CHARACTERISTIC
		ENG_SPEED_CORR_CURVE
		ENG_SPEED_CORR_CURVE_STD
	/end REF_CHARACTERISTIC
	/begin SUB_FUNCTION
		SubFunctionParam1
		SubFunctionParam2
	/end SUB_FUNCTION
/end FUNCTION
"""

_TEST_FUNCTION_BLOCK_EMPTY = """
/begin FUNCTION
	/begin LOC_MEASUREMENT
	/end LOC_MEASUREMENT
    /begin SUB_FUNCTION
	/end SUB_FUNCTION
	/begin ANNOTATION
		/begin ANNOTATION_TEXT
		/end ANNOTATION_TEXT
	/end ANNOTATION
	/begin DEF_CHARACTERISTIC
	/end DEF_CHARACTERISTIC
	/begin IN_MEASUREMENT
	/end IN_MEASUREMENT
	/begin OUT_MEASUREMENT
	/end OUT_MEASUREMENT
	/begin REF_CHARACTERISTIC
	/end REF_CHARACTERISTIC
/end FUNCTION
"""


class TestFunction(Testhandler):
    def test_function_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_function_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FUNCTION_BLOCK,
                      filelength=_TEST_FUNCTION_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "Sssm140_CalcStopDynDecel")
        self.assertEqual(tree.find('.//LongIdentifier').text, "IDENT_LNG")

        self.assertEqual(tree.find('.//Def_Characteristic/Identifier').text, "INJECTION_CURVE, DELAY_FACTOR")
        self.assertEqual(tree.find('.//Function_Version').text, "BG5.0815")
        self.assertEqual(tree.find('.//In_Measurement/Identifier').text, "WHEEL_REVOLUTIONS, ENGINE_SPEED")
        self.assertEqual(tree.find('.//Loc_Measurement/Identifier').text,
                         "SsmInLastWinsThreshold, SsmInThrottlePedalPosition")
        self.assertEqual(tree.find('.//Out_Measurement/Identifier').text, "OK_FLAG, SENSOR_FLAG")

        ref_characteristic = tree.find('.//Ref_Characteristic')
        self.assertEqual(len(ref_characteristic), 2)
        self.assertEqual(ref_characteristic[0].get('characteristicId'), "ENG_SPEED_CORR_CURVE")
        self.assertEqual(ref_characteristic[1].get('characteristicId'), "ENG_SPEED_CORR_CURVE_STD")

        sub_function = tree.findall('.//Sub_Function')
        self.assertEqual(len(sub_function), 2)
        self.assertEqual(sub_function[0].find('.//Identifier').text,
                         "CalcDynDecelState, CalcStopDynDecel, Sssm313_AEB_disabled, Sssm314_AEB_enabled, Sssm37_Subsystem")
        self.assertEqual(sub_function[1].find('.//Identifier').text, "SubFunctionParam1, SubFunctionParam2")

        annotation = tree.findall('.//Annotation')  # annoation in characteristic
        self.assertEqual(len(annotation), 2)
        self.assertEqual(annotation[0].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_BLOCK_1")
        self.assertEqual(annotation[0].find('.//Annotation_Label').text, "ANNOTATION_LABEL_BLOCK_1")
        self.assertEqual(annotation[0].find('.//Annotation_Text').text, "ANNOTATION_TEXT_BLOCK_1")
        self.assertEqual(annotation[1].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_BLOCK_2")
        self.assertEqual(annotation[1].find('.//Annotation_Label').text, "ANNOTATION_LABEL_BLOCK_2")
        self.assertEqual(annotation[1].find('.//Annotation_Text').text, "ANNOTATION_TEXT_BLOCK_2")

    def test_function_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_frame_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FUNCTION_BLOCK_EMPTY,
                      filelength=_TEST_FUNCTION_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

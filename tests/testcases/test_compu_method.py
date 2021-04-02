from tests.testhandler import Testhandler

_TEST_COMPU_METHOD_BLOCK = """
/begin COMPU_METHOD CM_FIXED_SB_06 "LongIdentifier"
	TAB_INTP "%4.3" "UNIT_STRING"
	COMPU_TAB_REF CM_FIXED_SB_06
	COEFFS 0 4 8 3 2 5
	COEFFS_LINEAR 1.25 -2.0
	COMPU_TAB_REF TEMP_TAB
	/begin FORMULA
		"sqrt( 3 - 4*sin(X1) )"
		FORMULA_INV "asin( sqrt( (3 - X1)/4 ) )"
	/end FORMULA
	REF_UNIT kms_per_hour
	STATUS_STRING_REF CT_SensorStatus
/end COMPU_METHOD
"""

_TEST_COMPU_METHOD_BLOCK_EMPTY = """
/begin COMPU_METHOD
    /begin FORMULA
    /end FORMULA
/end COMPU_METHOD
"""


class TestCompuMethod(Testhandler):
    def test_compu_method_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_compu_method_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_COMPU_METHOD_BLOCK,
                      filelength=_TEST_COMPU_METHOD_BLOCK_EMPTY.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "CM_FIXED_SB_06")
        self.assertEqual(tree.find('.//LongIdentifier').text, "LongIdentifier")
        self.assertEqual(tree.find('.//ConversionType').text, "TAB_INTP")
        self.assertEqual(tree.find('.//Format').text, "%4.3")
        self.assertEqual(tree.find('.//Unit').text, "UNIT_STRING")

        self.assertEqual(tree.find('.//Coeffs/a').text, "0")
        self.assertEqual(tree.find('.//Coeffs/b').text, "4")
        self.assertEqual(tree.find('.//Coeffs/c').text, "8")
        self.assertEqual(tree.find('.//Coeffs/d').text, "3")
        self.assertEqual(tree.find('.//Coeffs/e').text, "2")
        self.assertEqual(tree.find('.//Coeffs/f').text, "5")
        self.assertEqual(tree.find('.//Coeffs_Linear/a').text, "1.25")
        self.assertEqual(tree.find('.//Coeffs_Linear/b').text, "-2.0")
        self.assertEqual(tree.find('.//Compu_Tab_Ref').text, "TEMP_TAB")
        self.assertEqual(tree.find('.//Formula/f_x').text, "sqrt( 3 - 4*sin(X1) )")
        self.assertEqual(tree.find('.//Formula/Formula_Inv/g_x').text, "asin( sqrt( (3 - X1)/4 ) )")
        self.assertEqual(tree.find('.//Ref_Unit').text, "kms_per_hour")
        self.assertEqual(tree.find('.//Status_String_Ref').text, "CT_SensorStatus")

    def test_compu_method_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_compu_method_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_COMPU_METHOD_BLOCK_EMPTY,
                      filelength=_TEST_COMPU_METHOD_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

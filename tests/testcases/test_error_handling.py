from tests.testhandler import Testhandler


_TEST_ERROR_RESOLVE_INVALID_PARAM = """
/begin VARIANT_CODING
	VAR_SEPARATOR "." /* PUMKF.1 */
	VAR_NAMING NUMERIC /* variant criterion "Car body" with three variants */
	/begin VAR_CRITERION
		Car
		"Car body"
		Limousine Kombi Cabrio
	/end VAR_CRITERION /* variant criterion "Type of gear box" with two variants */
	/begin VAR_CHARACTERISTIC
		PUMKF /*define PUMKF as variant coded*/
		Gear Car /* Gear box variants */
		/begin VAR_ADDRESS
		    0x8840
		    "error"
		    0x1231
		/end VAR_ADDRESS
	/end VAR_CHARACTERISTIC
	/begin VAR_CHARACTERISTIC
		NLLM /*define NLLM as variant coded */
		Gear Car /*car body and gear box variants*/
		/begin VAR_ADDRESS
			0x8858
			0x8870
		/end VAR_ADDRESS
	/end VAR_CHARACTERISTIC
/end VARIANT_CODING
"""


_TEST_BIT_OPERATION_BLOCK_EMPTY = """
/begin VARIANT_CODING
	/begin VAR_CHARACTERISTIC
		/begin VAR_ADDRESS
		/end VAR_ADDRESS
	/end VAR_CHARACTERISTIC
/end VARIANT_CODING
"""


class TestErrorHandling(Testhandler):

    def setUp(self):
        self.error_resolve_flag = self.param.parser.config.error_resolve_active
        self.param.parser.config.error_resolve_active = True

    def tearDown(self):
        self.param.parser.config.error_resolve_active = self.error_resolve_flag

    def test_error_resolve_invalid_param(self):
        p = self.param.parser
        ast = p.parse(filename="test_error_resolve_invalid_param",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_ERROR_RESOLVE_INVALID_PARAM,
                      filelength=_TEST_ERROR_RESOLVE_INVALID_PARAM.count('\n'))

        tree = self.getXmlFromAst(ast)



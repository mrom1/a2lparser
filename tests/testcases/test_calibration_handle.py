from tests.testhandler import Testhandler

_TEST_CALIBRATION_HANDLE_BLOCK = """
/begin CALIBRATION_HANDLE
        0x10000 /* start address of pointer table */
        0x200 /* length of pointer table */
        0x4 /* size of one pointer table entry */
        0x30000 /* start address of flash section */
        0x20000 /* length of flash section */
        CALIBRATION_HANDLE_TEXT "12345"
/end CALIBRATION_HANDLE
"""

_TEST_CALIBRATION_HANDLE_BLOCK_EMPTY = """
/begin CALIBRATION_HANDLE
/end CALIBRATION_HANDLE
"""


class TestCalibrationHandle(Testhandler):
    def test_calibration_handle_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_calibration_handle_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_CALIBRATION_HANDLE_BLOCK,
                      filelength=_TEST_CALIBRATION_HANDLE_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Calibration_Handle/Handle').text, "0x10000, 0x200, 0x4, 0x30000, 0x20000")
        self.assertEqual(tree.find('.//Calibration_Handle/Calibration_Handle_Text').text, "12345")

    def test_calibration_handle_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_calibration_handle_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_CALIBRATION_HANDLE_BLOCK_EMPTY,
                      filelength=_TEST_CALIBRATION_HANDLE_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

from tests.testhandler import Testhandler


_TEST_BIT_OPERATION_BLOCK = """
/begin BIT_OPERATION
    RIGHT_SHIFT 4 /*4 positions*/
    LEFT_SHIFT 0
    SIGN_EXTEND
/end BIT_OPERATION
"""

_TEST_BIT_OPERATION_BLOCK_EMPTY = """
/begin BIT_OPERATION
/end BIT_OPERATION
"""


class TestBitOperation(Testhandler):
    def test_bit_operation_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_bit_operation_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_BIT_OPERATION_BLOCK,
                      filelength=_TEST_BIT_OPERATION_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Bit_Operation/Right_Shift/Bitcount').text, "4")
        self.assertEqual(tree.find('.//Bit_Operation/Left_Shift/Bitcount').text, "0")
        self.assertEqual(tree.find('.//Bit_Operation/Sign_Extend/Boolean').text, "True")

    def test_bit_operation_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_bit_operation_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_BIT_OPERATION_BLOCK_EMPTY,
                      filelength=_TEST_BIT_OPERATION_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

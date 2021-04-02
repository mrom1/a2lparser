from tests.testhandler import Testhandler

_TEST_FRAME_BLOCK = """
/begin MOD_COMMON
	"COMMENT"
	ALIGNMENT_BYTE	1
	ALIGNMENT_FLOAT32_IEEE	4
	ALIGNMENT_FLOAT64_IEEE	4
	ALIGNMENT_INT64	8
	ALIGNMENT_LONG	4
	ALIGNMENT_WORD	2
	BYTE_ORDER	MSB_FIRST
	DEPOSIT	ABSOLUTE
	DATA_SIZE 16
/end MOD_COMMON
"""

_TEST_FRAME_BLOCK_EMPTY = """
/begin MOD_COMMON
/end MOD_COMMON
"""


class TestModCommon(Testhandler):
    def test_mod_common_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_mod_common_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FRAME_BLOCK,
                      filelength=_TEST_FRAME_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Comment').text, "COMMENT")

        self.assertEqual(tree.find('.//Alignment_Byte').text, "1")
        self.assertEqual(tree.find('.//Alignment_Float32_Ieee').text, "4")
        self.assertEqual(tree.find('.//Alignment_Float64_Ieee').text, "4")
        self.assertEqual(tree.find('.//Alignment_Int64').text, "8")
        self.assertEqual(tree.find('.//Alignment_Long').text, "4")
        self.assertEqual(tree.find('.//Alignment_Word').text, "2")
        self.assertEqual(tree.find('.//Byte_Order').text, "MSB_FIRST")
        self.assertEqual(tree.find('.//Data_Size').text, "16")
        self.assertEqual(tree.find('.//Deposit').text, "ABSOLUTE")

    def test_mod_common_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_mod_common_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FRAME_BLOCK_EMPTY,
                      filelength=_TEST_FRAME_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

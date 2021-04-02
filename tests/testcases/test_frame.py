from tests.testhandler import Testhandler

_TEST_FRAME_BLOCK = """
/begin FRAME ABS_ADJUSTM
	"function group ABS adjustment"
	3
	2 /* 2 msec. */
	FRAME_MEASUREMENT LOOP_COUNTER TEMPORARY_1
    /begin IF_DATA XCP
		LINK_MAP ref_name 0x003432
	/end IF_DATA
	/begin IF_DATA CANAPE
		STATIC ref_name 0xFF
	/end IF_DATA
/end FRAME
"""

_TEST_FRAME_BLOCK_EMPTY = """
/begin FRAME
/end FRAME
"""


class TestFrame(Testhandler):
    def test_frame_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_frame_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FRAME_BLOCK,
                      filelength=_TEST_FRAME_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "ABS_ADJUSTM")
        self.assertEqual(tree.find('.//LongIdentifier').text, "function group ABS adjustment")
        self.assertEqual(tree.find('.//ScalingUnit').text, "3")
        self.assertEqual(tree.find('.//Rate').text, "2")
        self.assertEqual(tree.find('.//Frame_Measurement').text, "LOOP_COUNTER, TEMPORARY_1")

        if_data = tree.findall('.//If_Data')
        self.assertEqual(len(if_data), 2)
        self.assertEqual(if_data[0].find('.//Name').text, "XCP")
        self.assertEqual(if_data[0].find('.//DataParams').text, "LINK_MAP, ref_name, 0x003432")
        self.assertEqual(if_data[1].find('.//Name').text, "CANAPE")
        self.assertEqual(if_data[1].find('.//DataParams').text, "STATIC, ref_name, 0xFF")

    def test_frame_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_frame_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FRAME_BLOCK_EMPTY,
                      filelength=_TEST_FRAME_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

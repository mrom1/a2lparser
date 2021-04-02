from tests.testhandler import Testhandler

_TEST_FRAME_BLOCK = """
/begin MEMORY_SEGMENT
		Data2
		"Data external Flash"
		DATA
		FLASH
		EXTERN
		0x7000
		0x2000
		-1 -1 -1 -1 -1
		/begin IF_DATA XCP
		    LINK_MAP ref_name 0x003432
		/end IF_DATA
		/begin IF_DATA CANAPE
		    STATIC ref_name 0xFF
		/end IF_DATA
/end MEMORY_SEGMENT
"""

_TEST_FRAME_BLOCK_EMPTY = """
/begin MEMORY_SEGMENT
/end MEMORY_SEGMENT
"""


class TestMemorySegment(Testhandler):
    def test_memory_segment_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_memory_segment_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FRAME_BLOCK,
                      filelength=_TEST_FRAME_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "Data2")
        self.assertEqual(tree.find('.//LongIdentifier').text, "Data external Flash")
        self.assertEqual(tree.find('.//PrgType').text, "DATA")
        self.assertEqual(tree.find('.//MemoryType').text, "FLASH")
        self.assertEqual(tree.find('.//Attribute').text, "EXTERN")
        self.assertEqual(tree.find('.//Address').text, "0x7000")
        self.assertEqual(tree.find('.//Size').text, "0x2000")
        self.assertEqual(tree.find('.//Offset').text, "-1, -1, -1, -1, -1")

        if_data = tree.findall('.//If_Data')
        self.assertEqual(len(if_data), 2)
        self.assertEqual(if_data[0].find('.//Name').text, "XCP")
        self.assertEqual(if_data[0].find('.//DataParams').text, "LINK_MAP, ref_name, 0x003432")
        self.assertEqual(if_data[1].find('.//Name').text, "CANAPE")
        self.assertEqual(if_data[1].find('.//DataParams').text, "STATIC, ref_name, 0xFF")

    def test_memory_segment_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_memory_segment_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FRAME_BLOCK_EMPTY,
                      filelength=_TEST_FRAME_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

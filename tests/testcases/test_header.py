from tests.testhandler import Testhandler

_TEST_HEADER_BLOCK = """
/begin HEADER "see also specification XYZ of 01.02.1994"
	VERSION "BG5.0815"
	PROJECT_NO M4711Z1
/end HEADER
"""

_TEST_HEADER_BLOCK_EMPTY = """
/begin HEADER
/end HEADER
"""


class TestHeader(Testhandler):
    def test_header_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_header_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_HEADER_BLOCK,
                      filelength=_TEST_HEADER_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Comment').text, "see also specification XYZ of 01.02.1994")
        self.assertEqual(tree.find('.//Project_No').text, "M4711Z1")
        self.assertEqual(tree.find('.//Version').text, "BG5.0815")

    def test_header_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_header_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_HEADER_BLOCK_EMPTY,
                      filelength=_TEST_HEADER_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

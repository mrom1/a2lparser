from tests.testhandler import Testhandler

_TEST_STRING_NEWLINE_BLOCK = """
/begin ANNOTATION
ANNOTATION_LABEL "ANNOTATION_LABEL"
ANNOTATION_ORIGIN "ANNOTATION_ORIGIN"
/begin ANNOTATION_TEXT
"XYZ
ABC"
/end ANNOTATION_TEXT
/end ANNOTATION
"""

_TEST_STRING_NEWLINE_BLOCK_EMPTY = """
/begin ANNOTATION
/end ANNOTATION
"""


class TestStringHandling(Testhandler):
    def test_string_newline_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_string_newline_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_STRING_NEWLINE_BLOCK,
                      filelength=_TEST_STRING_NEWLINE_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN")
        self.assertEqual(tree.find('.//Annotation_Label').text, "ANNOTATION_LABEL")
        self.assertEqual(tree.find('.//Annotation_Text').text, "XYZ\nABC")

    def test_string_newline_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_string_newline_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_STRING_NEWLINE_BLOCK_EMPTY,
                      filelength=_TEST_STRING_NEWLINE_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

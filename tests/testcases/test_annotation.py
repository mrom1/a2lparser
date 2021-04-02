from tests.testhandler import Testhandler


_TEST_ANNOTATION_BLOCK = """
/begin ANNOTATION
    ANNOTATION_LABEL "ANNOTATION_LABEL"
    ANNOTATION_ORIGIN "ANNOTATION_ORIGIN"
    /begin ANNOTATION_TEXT
        "STRING_LINE_1"
        "STRING_LINE_2"
    /end ANNOTATION_TEXT
/end ANNOTATION
"""

_TEST_ANNOTATION_BLOCK_EMPTY = """
/begin ANNOTATION
    /begin ANNOTATION_TEXT
    /end ANNOTATION_TEXT
    /begin ANNOTATION_TEXT
    /end ANNOTATION_TEXT
/end ANNOTATION
"""


class TestAnnotation(Testhandler):
    def test_annotation_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_annotation_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_ANNOTATION_BLOCK_EMPTY,
                      filelength=_TEST_ANNOTATION_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

    def test_annotation_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_annotation_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_ANNOTATION_BLOCK,
                      filelength=_TEST_ANNOTATION_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)

        self.assertEqual(tree.find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN")
        self.assertEqual(tree.find('.//Annotation_Label').text, "ANNOTATION_LABEL")
        self.assertEqual(tree.find('.//Annotation_Text').text, "STRING_LINE_1, STRING_LINE_2")


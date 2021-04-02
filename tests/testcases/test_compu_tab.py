from tests.testhandler import Testhandler

_TEST_COMPU_TAB_BLOCK = """
/begin COMPU_TAB
    TT /* name */
	"conversion table for oil temperatures"
	TAB_NOINTP /* convers_type */
	7 /* number_value_pairs */
	1 4.3 2 4.7 3 5.8 4 14.2 5 16.8 6 17.2 7 19.4 /* value pairs */
	DEFAULT_VALUE_NUMERIC 99.0
	DEFAULT_VALUE "DEFAULT_VALUE_STRING"
/end COMPU_TAB
"""

_TEST_COMPU_TAB_BLOCK_EMPTY = """
/begin COMPU_TAB
/end COMPU_TAB
"""


class TestCompuTab(Testhandler):
    def test_compu_tab_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_compu_tab_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_COMPU_TAB_BLOCK,
                      filelength=_TEST_COMPU_TAB_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "TT")
        self.assertEqual(tree.find('.//LongIdentifier').text, "conversion table for oil temperatures")
        self.assertEqual(tree.find('.//ConversionType').text, "TAB_NOINTP")
        self.assertEqual(tree.find('.//NumberValuePairs').text, "7")
        self.assertEqual(tree.find('.//Axis_Points').text,
                         "['1', '4.3'], ['2', '4.7'], ['3', '5.8'], ['4', '14.2'], ['5', '16.8'], ['6', '17.2'], ['7', '19.4']")
        self.assertEqual(tree.find('.//Default_Value_Numeric').text, "99.0")
        self.assertEqual(tree.find('.//Default_Value').text, "DEFAULT_VALUE_STRING")

    def test_compu_tab_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_compu_tab_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_COMPU_TAB_BLOCK_EMPTY,
                      filelength=_TEST_COMPU_TAB_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

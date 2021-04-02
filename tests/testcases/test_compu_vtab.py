from tests.testhandler import Testhandler

_TEST_COMPU_VTAB_BLOCK = """
/begin COMPU_VTAB CM_BuiltInDTypeId "LONG" TAB_VERB 9
      0 "SS_DOUBLE"
      1 "SS_SINGLE"
      2 "SS_INT8"
      3 "SS_UINT8"
      4 "SS_INT16"
      5 "SS_UINT16"
      6 "SS_INT32"
      7 "SS_UINT32"
      8 "SS_BOOLEAN"
      DEFAULT_VALUE "DEFAULT_VALUE"
/end COMPU_VTAB
"""

_TEST_COMPU_VTAB_BLOCK_EMPTY = """
/begin COMPU_VTAB
/end COMPU_VTAB
"""


class TestCompuVtab(Testhandler):
    def test_compu_vtab_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_compu_vtab_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_COMPU_VTAB_BLOCK,
                      filelength=_TEST_COMPU_VTAB_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "CM_BuiltInDTypeId")
        self.assertEqual(tree.find('.//LongIdentifier').text, "LONG")
        self.assertEqual(tree.find('.//ConversionType').text, "TAB_VERB")
        self.assertEqual(tree.find('.//NumberValuePairs').text, "9")
        self.assertEqual(tree.find('.//InVal_OutVal').text,
                         "['0', 'SS_DOUBLE'], ['1', 'SS_SINGLE'], ['2', 'SS_INT8'], ['3', 'SS_UINT8'], ['4', 'SS_INT16'], ['5', 'SS_UINT16'], ['6', 'SS_INT32'], ['7', 'SS_UINT32'], ['8', 'SS_BOOLEAN']")
        self.assertEqual(tree.find('.//Default_Value').text, "DEFAULT_VALUE")

    def test_compu_vtab_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_compu_vtab_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_COMPU_VTAB_BLOCK_EMPTY,
                      filelength=_TEST_COMPU_VTAB_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

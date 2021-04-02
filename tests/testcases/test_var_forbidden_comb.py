from tests.testhandler import Testhandler

_TEST_VAR_FORBIDDEN_COMB_BLOCK = """
/begin VAR_FORBIDDEN_COMB
		Car Limousine /* variant value 'Limousine' of criterion 'Car' */
		Gear Manual /* variant value 'Manual' of criterion 'Gear' */
/end VAR_FORBIDDEN_COMB
"""

_TEST_VAR_FORBIDDEN_COMB_BLOCK_EMPTY = """
/begin VAR_FORBIDDEN_COMB
/end VAR_FORBIDDEN_COMB
"""


class TestVarForbiddenComb(Testhandler):
    def test_var_forbidden_comb_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_var_forbidden_comb_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_VAR_FORBIDDEN_COMB_BLOCK,
                      filelength=_TEST_VAR_FORBIDDEN_COMB_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//CriterionList').text, "['Car', 'Limousine'], ['Gear', 'Manual']")

    def test_var_forbidden_comb_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_var_forbidden_comb_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_VAR_FORBIDDEN_COMB_BLOCK_EMPTY,
                      filelength=_TEST_VAR_FORBIDDEN_COMB_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

from tests.testhandler import Testhandler

_TEST_VAR_CRITERION_BLOCK = """
/begin VAR_CRITERION
		Car
		"Car body" /*Enumeration of criterion values*/
		Limousine Kombi Cabrio
		VAR_MEASUREMENT S_CAR
		VAR_SELECTION_CHARACTERISTIC V_CAR
/end VAR_CRITERION


"""

_TEST_VAR_CRITERION_BLOCK_EMPTY = """
/begin VAR_CRITERION
/end VAR_CRITERION
"""


class TestVarCriterion(Testhandler):
    def test_var_criterion_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_var_criterion_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_VAR_CRITERION_BLOCK,
                      filelength=_TEST_VAR_CRITERION_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Name').text, "Car")
        self.assertEqual(tree.find('.//LongIdentifier').text, "Car body")
        self.assertEqual(tree.find('.//Value').text, "Limousine, Kombi, Cabrio")
        self.assertEqual(tree.find('.//Var_Measurement').text, "S_CAR")
        self.assertEqual(tree.find('.//Var_Selection_Characteristic').text, "V_CAR")

    def test_var_criterion_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_var_criterion_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_VAR_CRITERION_BLOCK_EMPTY,
                      filelength=_TEST_VAR_CRITERION_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

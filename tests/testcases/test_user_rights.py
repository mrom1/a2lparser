from tests.testhandler import Testhandler

_TEST_USER_RIGHTS_block = """
/begin USER_RIGHTS
	measurement_engineers
	/begin REF_GROUP
		group_1
		group_2
		group_3
	/end REF_GROUP
	READ_ONLY
/end USER_RIGHTS
"""

_TEST_USER_RIGHTS_block_EMPTY = """
/begin USER_RIGHTS
		measurement_engineers
		/begin REF_GROUP
		/end REF_GROUP
/end USER_RIGHTS
"""


class TestUserRights(Testhandler):
    def test_user_rights_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_user_rights_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_USER_RIGHTS_block,
                      filelength=_TEST_USER_RIGHTS_block.count('\n'))

        tree = self.getXmlFromAst(ast)

        self.assertEqual(tree.find('.//UserLevelId').text, "measurement_engineers")
        self.assertEqual(tree.find('.//Read_Only').text, "True")
        self.assertEqual(tree.find('.//Ref_Group/Identifier').text, "group_1, group_2, group_3")

    def test_user_rights_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_user_rights_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_USER_RIGHTS_block_EMPTY,
                      filelength=_TEST_USER_RIGHTS_block_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

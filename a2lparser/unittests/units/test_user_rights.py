#######################################################################################
# a2lparser: https://github.com/mrom1/a2lparser                                       #
# author: https://github.com/mrom1                                                    #
#                                                                                     #
# This file is part of the a2lparser package.                                         #
#                                                                                     #
# a2lparser is free software: you can redistribute it and/or modify it                #
# under the terms of the GNU General Public License as published by the               #
# Free Software Foundation, either version 3 of the License, or (at your option)      #
# any later version.                                                                  #
#                                                                                     #
# a2lparser is distributed in the hope that it will be useful,                        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY      #
# or FITNESS FOR A PARTICULAR PURPOSE.                                                #
# See the GNU General Public License for more details.                                #
#                                                                                     #
# You should have received a copy of the GNU General Public License                   #
# along with a2lparser. If not, see <https://www.gnu.org/licenses/>.                  #
#######################################################################################


from a2lparser.unittests.testhandler import Testhandler


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

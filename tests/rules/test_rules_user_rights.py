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


from a2lparser.a2l.a2l_yacc import A2LYacc


def test_rules_user_rights():
    """
    Tests parsing a valid "USER_RIGHTS" block.
    """
    user_rights_block = """
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
    parser = A2LYacc()
    ast = parser.generate_ast(user_rights_block)
    assert ast

    user_rights = ast["USER_RIGHTS"]
    assert user_rights
    assert user_rights["UserLevelId"] == "measurement_engineers"
    assert user_rights["READ_ONLY"] is True

    assert user_rights["REF_GROUP"]["Identifier"][0] == "group_1"
    assert user_rights["REF_GROUP"]["Identifier"][1] == "group_2"
    assert user_rights["REF_GROUP"]["Identifier"][2] == "group_3"

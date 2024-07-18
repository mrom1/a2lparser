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


def test_rules_project_two_modules_minimal():
    """
    Tests a A2L "PROJECT" section.
    """
    project_content = """
    ASAP2_VERSION 1 71
    /begin PROJECT Example_Project "ProjectBackupModule"
        /begin HEADER
            "Tests a Project with two modules"
        /end HEADER

        /begin MODULE Module_x1
            "First Module Identifier"
        /end MODULE

        /begin MODULE Module_x2
            "Second Module Identifier"
        /end MODULE
    /end PROJECT
    """
    ast = A2LYacc().generate_ast(project_content)
    assert ast
    assert ast["ASAP2_VERSION"] == {"VersionNo": "1", "UpgradeNo": "71"}

    project = ast["PROJECT"]
    assert project["Name"] == "Example_Project"
    assert project["LongIdentifier"] == '"ProjectBackupModule"'
    assert project["HEADER"]["Comment"] == '"Tests a Project with two modules"'

    assert len(project["MODULE"]) == 2

    module_x1 = project["MODULE"][0]
    assert module_x1
    assert module_x1["Name"] == "Module_x1"
    assert module_x1["LongIdentifier"] == '"First Module Identifier"'

    module_x2 = project["MODULE"][1]
    assert module_x2
    assert module_x2["Name"] == "Module_x2"
    assert module_x2["LongIdentifier"] == '"Second Module Identifier"'

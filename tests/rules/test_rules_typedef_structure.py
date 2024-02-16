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


def test_rules_typedef_structure():
    """
    Test A2L TYPEDEF_STRUCTURE section.
    """
    typedef_structure_minimal = """
    /begin TYPEDEF_STRUCTURE
        MyStructure // structure name
        "..." // description
        64 // total size of structure
    /end TYPEDEF_STRUCTURE
    """
    ast = A2LYacc().generate_ast(typedef_structure_minimal)
    assert ast

    typedef_structure = ast["TYPEDEF_STRUCTURE"]
    assert typedef_structure["Name"] == "MyStructure"
    assert typedef_structure["LongIdentifier"] == '"..."'
    assert typedef_structure["Size"] == "64"

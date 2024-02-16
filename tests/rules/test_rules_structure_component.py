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


def test_rules_structure_component_minimal():
    """
    Test A2L STRUCTURE_COMPONENT section.
    """
    structure_component_minimal = """
    /begin STRUCTURE_COMPONENT
        XX MyUnsignedLongType
        0 // address offset
    /end STRUCTURE_COMPONENT
    """
    ast = A2LYacc().generate_ast(structure_component_minimal)
    assert ast

    structure_component = ast["STRUCTURE_COMPONENT"]
    assert structure_component["Name"] == "XX"
    assert structure_component["TypedefName"] == "MyUnsignedLongType"
    assert structure_component["AddressOffset"] == "0"


def test_rules_structure_component_full():
    """
    Test A2L STRUCTURE_COMPONENT section.
    """
    structure_component_full = """
    /begin STRUCTURE_COMPONENT
        BXB MyComplexComponent
        34                      // address offset

        MATRIX_DIM 10
        SYMBOL_TYPE_LINK "__MyComplexComponent.pdb"
        ADDRESS_TYPE PLONGLONG
        LAYOUT ALTERNATE_CURVES
    /end STRUCTURE_COMPONENT
    """
    ast = A2LYacc().generate_ast(structure_component_full)
    assert ast

    structure_component = ast["STRUCTURE_COMPONENT"]
    assert structure_component
    assert structure_component["Name"] == "BXB"
    assert structure_component["TypedefName"] == "MyComplexComponent"
    assert structure_component["AddressOffset"] == "34"
    assert structure_component["MATRIX_DIM"] == ["10"]
    assert structure_component["SYMBOL_TYPE_LINK"] == '"__MyComplexComponent.pdb"'
    assert structure_component["ADDRESS_TYPE"] == "PLONGLONG"
    assert structure_component["LAYOUT"] == "ALTERNATE_CURVES"

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


def test_rules_memory_layout():
    """
    Tests parsing a valid "MEMORY_LAYOUT" block.
    """
    memory_layout_block = """
    /begin MEMORY_LAYOUT
        PRG_RESERVED
        0x0000
        0x0400
        -1 -1 -1 -1 -1
        /begin IF_DATA XCP
            LINK_MAP ref_name 0x003432
        /end IF_DATA
        /begin IF_DATA CANAPE
            STATIC ref_name 0xFF
        /end IF_DATA
    /end MEMORY_LAYOUT
    """
    parser = A2LYacc()
    ast = parser.generate_ast(memory_layout_block)
    assert ast

    memory_layout = ast["MEMORY_LAYOUT"]
    assert memory_layout
    assert memory_layout["PrgType"] == "PRG_RESERVED"
    assert memory_layout["Address"] == "0x0000"
    assert memory_layout["Size"] == "0x0400"
    assert memory_layout["Offset"] == ["-1", "-1", "-1", "-1", "-1"]
    assert len(memory_layout["IF_DATA"]) == 2
    assert memory_layout["IF_DATA"][0]["Name"] == "XCP"
    assert memory_layout["IF_DATA"][0]["DataParams"] == ['LINK_MAP', 'ref_name', '0x003432']
    assert memory_layout["IF_DATA"][1]["Name"] == "CANAPE"
    assert memory_layout["IF_DATA"][1]["DataParams"] == ['STATIC', 'ref_name', '0xFF']

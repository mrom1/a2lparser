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


def test_rules_memory_segment():
    """
    Tests parsing a valid "MEMORY_SEGMENT" block.
    """
    memory_segment_block = """
    /begin MEMORY_SEGMENT
        Data2
        "Data external Flash"
        DATA
        FLASH
        EXTERN
        0x7000
        0x2000
        -1 -1 -1 -1 -1
        /begin IF_DATA XCP
            LINK_MAP ref_name 0x003432
        /end IF_DATA
        /begin IF_DATA CANAPE
            STATIC ref_name 0xFF
        /end IF_DATA
    /end MEMORY_SEGMENT
    """
    parser = A2LYacc()
    ast = parser.generate_ast(memory_segment_block)
    assert ast

    memory_segment = ast["MEMORY_SEGMENT"]
    assert memory_segment
    assert memory_segment["Name"] == "Data2"
    assert memory_segment["LongIdentifier"] == '"Data external Flash"'
    assert memory_segment["PrgType"] == "DATA"
    assert memory_segment["MemoryType"] == "FLASH"
    assert memory_segment["Attribute"] == "EXTERN"
    assert memory_segment["Address"] == "0x7000"
    assert memory_segment["Size"] == "0x2000"
    assert memory_segment["Offset"] == ["-1", "-1", "-1", "-1", "-1"]
    assert len(memory_segment["IF_DATA"]) == 2
    assert memory_segment["IF_DATA"][0]["Name"] == "XCP"
    assert memory_segment["IF_DATA"][0]["DataParams"] == ['LINK_MAP', 'ref_name', '0x003432']
    assert memory_segment["IF_DATA"][1]["Name"] == "CANAPE"
    assert memory_segment["IF_DATA"][1]["DataParams"] == ['STATIC', 'ref_name', '0xFF']

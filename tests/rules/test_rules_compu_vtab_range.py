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


def test_rules_compu_vtab_range():
    """
    Tests parsing a valid "COMPU_VTAB_RANGE" block.
    """
    compu_vtab_range_block = """
    /begin COMPU_VTAB_RANGE
        SAR_ASS_REQ_AX
        "Active assistant"
        33
        0 0 "IDLE"
        1 1 "NDEF1"
        2 2 "ACTV"
        3 3 "XT_ACTV"
        64 255 "not defined"
        DEFAULT_VALUE "SNA"
    /end COMPU_VTAB_RANGE
    """
    parser = A2LYacc()
    ast = parser.generate_ast(compu_vtab_range_block)
    assert ast

    compu_vtab_range = ast["COMPU_VTAB_RANGE"]
    assert compu_vtab_range
    assert compu_vtab_range["Name"] == "SAR_ASS_REQ_AX"
    assert compu_vtab_range["LongIdentifier"] == '"Active assistant"'
    assert compu_vtab_range["NumberValueTriples"] == "33"
    assert compu_vtab_range["InVal_MinMax_OutVal"] == [
        ["0", "0", '"IDLE"'],
        ["1", "1", '"NDEF1"'],
        ["2", "2", '"ACTV"'],
        ["3", "3", '"XT_ACTV"'],
        ["64", "255", '"not defined"'],
    ]
    assert compu_vtab_range["DEFAULT_VALUE"] == '"SNA"'

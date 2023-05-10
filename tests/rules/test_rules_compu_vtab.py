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


def test_rules_compu_vtab():
    """
    Tests parsing a valid "COMPU_VTAB" block.
    """
    compu_vtab_block = """
    /begin COMPU_VTAB CM_BuiltInDTypeId "LONG" TAB_VERB 9
          0 "SS_DOUBLE"
          1 "SS_SINGLE"
          2 "SS_INT8"
          3 "SS_UINT8"
          4 "SS_INT16"
          5 "SS_UINT16"
          6 "SS_INT32"
          7 "SS_UINT32"
          8 "SS_BOOLEAN"
          DEFAULT_VALUE "DEFAULT_VALUE"
    /end COMPU_VTAB
    """
    parser = A2LYacc()
    ast = parser.generate_ast(compu_vtab_block)
    assert ast

    compu_vtab = ast["COMPU_VTAB"]
    assert compu_vtab
    assert compu_vtab["Name"] == "CM_BuiltInDTypeId"
    assert compu_vtab["LongIdentifier"] == '"LONG"'
    assert compu_vtab["ConversionType"] == "TAB_VERB"
    assert compu_vtab["NumberValuePairs"] == "9"
    assert compu_vtab["InVal_OutVal"] == [
        ["0", '"SS_DOUBLE"'],
        ["1", '"SS_SINGLE"'],
        ["2", '"SS_INT8"'],
        ["3", '"SS_UINT8"'],
        ["4", '"SS_INT16"'],
        ["5", '"SS_UINT16"'],
        ["6", '"SS_INT32"'],
        ["7", '"SS_UINT32"'],
        ["8", '"SS_BOOLEAN"'],
    ]
    assert compu_vtab["DEFAULT_VALUE"] == '"DEFAULT_VALUE"'

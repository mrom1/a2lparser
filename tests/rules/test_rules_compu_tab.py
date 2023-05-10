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


def test_rules_compu_tab():
    """
    Tests parsing a valid "COMPU_TAB" block.
    """
    compu_tab_block = """
    /begin COMPU_TAB
        TT /* name */
        "conversion table for oil temperatures"
        TAB_NOINTP /* convers_type */
        7 /* number_value_pairs */
        1 4.3 2 4.7 3 5.8 4 14.2 5 16.8 6 17.2 7 19.4 /* value pairs */
        DEFAULT_VALUE_NUMERIC 99.0
        DEFAULT_VALUE "DEFAULT_VALUE_STRING"
    /end COMPU_TAB
    """
    parser = A2LYacc()
    ast = parser.generate_ast(compu_tab_block)
    assert ast

    compu_tab = ast["COMPU_TAB"]
    assert compu_tab
    assert compu_tab["Name"] == "TT"
    assert compu_tab["LongIdentifier"] == '"conversion table for oil temperatures"'
    assert compu_tab["ConversionType"] == "TAB_NOINTP"
    assert compu_tab["NumberValuePairs"] == "7"
    assert compu_tab["Axis_Points"] == [
        ["1", "4.3"],
        ["2", "4.7"],
        ["3", "5.8"],
        ["4", "14.2"],
        ["5", "16.8"],
        ["6", "17.2"],
        ["7", "19.4"],
    ]
    assert compu_tab["DEFAULT_VALUE"] == '"DEFAULT_VALUE_STRING"'
    assert compu_tab["DEFAULT_VALUE_NUMERIC"] == "99.0"

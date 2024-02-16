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


def test_rules_typedef_axis_minimal():
    """
    Test A2L TYPEDEF_AXIS section.
    """
    typedef_axis_minimal = """
    /begin TYPEDEF_AXIS
        T_AXIS_N // type name
        "axis points" // description
        N // input quantity
        REC_DMMAX // reference to record layout
        33.0 // maxdiff
        CONV_DMMAX // reference to conversion method
        100 // maximum number of axis points
        0.0 // lower limit
        2460.0 // upper limit
    /end TYPEDEF_AXIS
    """
    ast = A2LYacc().generate_ast(typedef_axis_minimal)
    assert ast

    typedef_axis = ast["TYPEDEF_AXIS"]
    assert typedef_axis
    assert typedef_axis["Name"] == "T_AXIS_N"
    assert typedef_axis["LongIdentifier"] == '"axis points"'
    assert typedef_axis["InputQuantity"] == "N"
    assert typedef_axis["RecordLayout"] == "REC_DMMAX"
    assert typedef_axis["MaxDiff"] == "33.0"
    assert typedef_axis["CONVERSION"] == "CONV_DMMAX"
    assert typedef_axis["MaxAxisPoints"] == "100"
    assert typedef_axis["LowerLimit"] == "0.0"
    assert typedef_axis["UpperLimit"] == "2460.0"

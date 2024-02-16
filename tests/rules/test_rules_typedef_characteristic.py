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


def test_rules_typedef_characteristic():
    """
    Test A2L TYPEDEF_CHARACTERISTIC section.
    """
    typedef_characteristic_minimal = """
    /begin TYPEDEF_CHARACTERISTIC
        T_TIME_MS // type name
        "time in ms" // description
        VALUE // object type
        RL_VALUE_ULONG // record layout
        100.0 // maxdiff
        NO_COMPU_METHOD // no conversion
        10 // lower limit
        65535 // upper limit
        PHYS_UNIT "ms" // physical unit
    /end TYPEDEF_CHARACTERISTIC
    """
    ast = A2LYacc().generate_ast(typedef_characteristic_minimal)
    assert ast

    typedef_characteristic = ast["TYPEDEF_CHARACTERISTIC"]
    assert typedef_characteristic
    assert typedef_characteristic["Name"] == "T_TIME_MS"
    assert typedef_characteristic["LongIdentifier"] == '"time in ms"'
    assert typedef_characteristic["Type"] == "VALUE"
    assert typedef_characteristic["RecordLayout"] == "RL_VALUE_ULONG"
    assert typedef_characteristic["MaxDiff"] == "100.0"
    assert typedef_characteristic["CONVERSION"] == "NO_COMPU_METHOD"
    assert typedef_characteristic["LowerLimit"] == "10"
    assert typedef_characteristic["UpperLimit"] == "65535"

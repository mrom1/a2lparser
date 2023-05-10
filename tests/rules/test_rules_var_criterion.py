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


def test_rules_var_criterion():
    """
    Tests parsing a valid "VAR_CRITERION" block.
    """
    var_criterion_block = """
    /begin VAR_CRITERION
        Car
        "Car body" /*Enumeration of criterion values*/
        Limousine Kombi Cabrio
        VAR_MEASUREMENT S_CAR
        VAR_SELECTION_CHARACTERISTIC V_CAR
    /end VAR_CRITERION
    """
    parser = A2LYacc()
    ast = parser.generate_ast(var_criterion_block)
    assert ast

    var_criterion = ast["VAR_CRITERION"]
    assert var_criterion
    assert var_criterion["Name"] == "Car"
    assert var_criterion["LongIdentifier"] == '"Car body"'
    assert var_criterion["VALUE"][0] == "Limousine"
    assert var_criterion["VALUE"][1] == "Kombi"
    assert var_criterion["VALUE"][2] == "Cabrio"
    assert var_criterion["VAR_MEASUREMENT"] == "S_CAR"
    assert var_criterion["VAR_SELECTION_CHARACTERISTIC"] == "V_CAR"

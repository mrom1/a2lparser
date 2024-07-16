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


def test_rules_var_characteristic():
    """
    Tests parsing a valid "VAR_CHARACTERISTIC" block.
    """
    var_characteristic_block = """
    /begin VAR_CHARACTERISTIC /* define NLLM as variant coded */
        NLLM
        Gear Car /* gear box including the 2 variants "Manual" and "Automatic" */
        /begin VAR_ADDRESS
            0x8840
            0x8858
            0x8870
            0x8888
        /end VAR_ADDRESS
    /end VAR_CHARACTERISTIC
    """
    parser = A2LYacc()
    ast = parser.generate_ast(var_characteristic_block)
    assert ast

    var_characteristic = ast["VAR_CHARACTERISTIC"]
    assert var_characteristic
    assert var_characteristic["Name"] == "NLLM"
    assert var_characteristic["CriterionName"][0] == "Gear"
    assert var_characteristic["CriterionName"][1] == "Car"

    assert var_characteristic["VAR_ADDRESS"]["Address"][0] == "0x8840"
    assert var_characteristic["VAR_ADDRESS"]["Address"][1] == "0x8858"
    assert var_characteristic["VAR_ADDRESS"]["Address"][2] == "0x8870"
    assert var_characteristic["VAR_ADDRESS"]["Address"][3] == "0x8888"

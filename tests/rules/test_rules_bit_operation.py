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


def test_rules_bit_operation():
    """
    Tests parsing a valid "BIT_OPERATION" block.
    """
    bit_operation_block = """
    /begin BIT_OPERATION
        RIGHT_SHIFT 4 /*4 positions*/
        LEFT_SHIFT 0
        SIGN_EXTEND
    /end BIT_OPERATION
    /begin BIT_OPERATION
        RIGHT_SHIFT 1 /*4 positions*/
        LEFT_SHIFT 2
    /end BIT_OPERATION
    """
    parser = A2LYacc()
    ast = parser.generate_ast(bit_operation_block)
    assert ast

    bit_operation = ast["BIT_OPERATION"]
    assert bit_operation
    assert len(bit_operation) == 2

    assert bit_operation[0]["LEFT_SHIFT"]["Bitcount"] == "0"
    assert bit_operation[0]["RIGHT_SHIFT"]["Bitcount"] == "4"
    assert bit_operation[0]["SIGN_EXTEND"]["Boolean"] is True
    assert bit_operation[1]["LEFT_SHIFT"]["Bitcount"] == "2"
    assert bit_operation[1]["RIGHT_SHIFT"]["Bitcount"] == "1"

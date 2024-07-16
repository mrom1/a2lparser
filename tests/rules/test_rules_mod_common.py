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


def test_rules_mod_common():
    """
    Tests parsing a valid "MOD_COMMON" block.
    """
    mod_common_block = """
    /begin MOD_COMMON
        "COMMENT"
        ALIGNMENT_BYTE	1
        ALIGNMENT_FLOAT16_IEEE  2
        ALIGNMENT_FLOAT32_IEEE  4
        ALIGNMENT_FLOAT64_IEEE  4
        ALIGNMENT_INT64	8
        ALIGNMENT_LONG	4
        ALIGNMENT_WORD	2
        BYTE_ORDER	MSB_FIRST
        DEPOSIT	ABSOLUTE
        DATA_SIZE 16
    /end MOD_COMMON
    """
    parser = A2LYacc()
    ast = parser.generate_ast(mod_common_block)
    assert ast

    mod_common = ast["MOD_COMMON"]
    assert mod_common
    assert mod_common['Comment'] == '"COMMENT"'
    assert mod_common['ALIGNMENT_BYTE'] == '1'
    assert mod_common['ALIGNMENT_FLOAT16_IEEE'] == '2'
    assert mod_common['ALIGNMENT_FLOAT32_IEEE'] == '4'
    assert mod_common['ALIGNMENT_FLOAT64_IEEE'] == '4'
    assert mod_common['ALIGNMENT_INT64'] == '8'
    assert mod_common['ALIGNMENT_LONG'] == '4'
    assert mod_common['ALIGNMENT_WORD'] == '2'
    assert mod_common['BYTE_ORDER'] == 'MSB_FIRST'
    assert mod_common['DATA_SIZE'] == '16'
    assert mod_common['DEPOSIT'] == 'ABSOLUTE'

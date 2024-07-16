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


def test_rules_def_characteristic():
    """
    Tests a A2L DEF_CHARACTERISTIC section.
    """
    characteristic_block = """
    /begin DEF_CHARACTERISTIC INJECTION_CURVE
        DELAY_FACTOR
        RANDOM_FACTOR
    /end DEF_CHARACTERISTIC
    """
    ast = A2LYacc().generate_ast(characteristic_block)
    assert ast
    assert ast["DEF_CHARACTERISTIC"] == {'Identifier':
                                         ['INJECTION_CURVE', 'DELAY_FACTOR', 'RANDOM_FACTOR']}

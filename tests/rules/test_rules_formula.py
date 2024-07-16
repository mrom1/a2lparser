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


def test_rules_formula():
    """
    Tests a A2L FORMULA section.
    """
    formula_block = """
    /begin FORMULA
        "sqrt( 3 - 4*sin(X1) )"
        FORMULA_INV "asin( sqrt( (3 - X1)/4 ) )"
    /end FORMULA
    """
    ast = A2LYacc().generate_ast(formula_block)
    assert ast

    formula = ast["FORMULA"]
    assert formula
    assert formula["f_x"] == '"sqrt( 3 - 4*sin(X1) )"'
    assert formula["FORMULA_INV"]["g_x"] == '"asin( sqrt( (3 - X1)/4 ) )"'

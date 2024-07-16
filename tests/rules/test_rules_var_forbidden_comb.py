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


def test_rules_var_forbidden_comb():
    """
    Tests parsing a valid "VAR_FORBIDDEN_COMB" block.
    """
    var_forbidden_comb_block = """
    /begin VAR_FORBIDDEN_COMB
        Car Limousine /* variant value 'Limousine' of criterion 'Car' */
        Gear Manual /* variant value 'Manual' of criterion 'Gear' */
    /end VAR_FORBIDDEN_COMB
    """
    parser = A2LYacc()
    ast = parser.generate_ast(var_forbidden_comb_block)
    assert ast

    var_forbidden_comb = ast["VAR_FORBIDDEN_COMB"]
    assert var_forbidden_comb
    assert var_forbidden_comb['CriterionList'][0][0] == 'Car'
    assert var_forbidden_comb['CriterionList'][0][1] == 'Limousine'
    assert var_forbidden_comb['CriterionList'][1][0] == 'Gear'
    assert var_forbidden_comb['CriterionList'][1][1] == 'Manual'

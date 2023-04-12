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


import tokenize
from a2lparser.a2l.a2l_yacc import A2LYacc


def test_rules_a2ml_version():
    """
    Test parsing the "a2ml_version" rule.

    Rule:
        "a2ml_version : A2ML_VERSION constant constant"
    """
    a2ml_version = "A2ML_VERSION 1 61"
    parser = A2LYacc()
    ast_version = parser.generate_ast(a2ml_version)["A2ML_VERSION"]
    assert ast_version
    assert ast_version["VERSIONNO"] == str(1)
    assert ast_version["UPGRADENO"] == str(61)


def test_rules_a2ml_version_error_resolve():
    """
    Test parsing content that hits the error conditions.

    Rule:
        "a2ml_version : a2ml_version_error"
        "a2ml_version_error : A2ML_VESION error_list"
    """
    error_error = "error1 error2 error3"
    a2ml_version_string_literal = '"A2ML_VERSION "1.61"'
    a2ml_version_too_few_args = "A2ML_VERSION 161 error12"
    a2ml_version_too_many_args = "A2ML_VERSION 1 6 1"
    a2ml_version_many_errors = "A2ML_VERSION 0x44ff '5462' \"string\" 61"

    parser = A2LYacc()
    # a2ml_version_string_literal
    # Should parse to this rule:
    # A2ML_VERSION string_literal -> A2ML_VERSION error_list
    ast_version_string_literal = parser.generate_ast(a2ml_version_too_few_args)
    assert ast_version_string_literal

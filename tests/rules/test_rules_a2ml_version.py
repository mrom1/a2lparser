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


def test_rules_a2ml_version():
    """
    Tests parsing a valid "A2ML_VERSION" type.
    """
    a2ml_version_input = """
    A2ML_VERSION
                    1
                    61 /* Version 1.6.1 */
    """
    parser = A2LYacc()
    ast = parser.generate_ast(a2ml_version_input)
    assert ast

    a2ml_version = ast["A2ML_VERSION"]
    assert a2ml_version
    assert a2ml_version["VersionNo"] == "1"
    assert a2ml_version["UpgradeNo"] == "61"

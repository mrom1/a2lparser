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


def test_rules_asap2_version():
    """
    Tests parsing a valid "ASAP2_VERSION" type.
    """
    asap2_version_input = """
    ASAP2_VERSION
                    4
                    91 /* Version 4.9.1 */
    """
    parser = A2LYacc()
    ast = parser.generate_ast(asap2_version_input)
    assert ast

    asap2_version = ast["ASAP2_VERSION"]
    assert asap2_version
    assert asap2_version["VersionNo"] == "4"
    assert asap2_version["UpgradeNo"] == "91"

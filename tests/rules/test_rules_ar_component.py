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


def test_rules_ar_component_minimal():
    """
    Testing A2L AR_COMPONENT section.
    """
    ar_component_minimal = """
    /begin AR_COMPONENT
        "ApplicationSwComponentType"
    /end AR_COMPONENT
    """
    ast = A2LYacc().generate_ast(ar_component_minimal)
    assert ast

    ar_component = ast["AR_COMPONENT"]
    assert ar_component
    assert ar_component["ComponentType"] == '"ApplicationSwComponentType"'


def test_rules_ar_component_full():
    """
    Testing A2L AR_COMPONENT section.
    """
    ar_component_full = """
    /begin AR_COMPONENT
        "ApplicationSwComponentType"
        AR_PROTOTYPE_OF "HANDLE"
    /end AR_COMPONENT
    """
    ast = A2LYacc().generate_ast(ar_component_full)
    assert ast

    ar_component = ast["AR_COMPONENT"]
    assert ar_component
    assert ar_component["ComponentType"] == '"ApplicationSwComponentType"'
    assert ar_component["AR_PROTOTYPE_OF"] == '"HANDLE"'

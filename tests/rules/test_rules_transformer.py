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


def test_rules_transformer_minimal():
    """
    Test A2L TRANSFORMER section.
    """
    transformer_minimal = """
    /begin TRANSFORMER TRANSFORMER_TOOL
        "1.4.3.33" /* Version info */
        "transformer_tool_x32.dll" /* DLL */
        "" /* no 64bit DLL */
        33000 /* timeout in [ms] */
        ON_USER_REQUEST
        TRANSFORMER_TOOL_REVERSE
    /end TRANSFORMER
    """
    ast = A2LYacc().generate_ast(transformer_minimal)
    assert ast

    transformer = ast["TRANSFORMER"]
    assert transformer
    assert transformer["Name"] == "TRANSFORMER_TOOL"
    assert transformer["VERSION"] == '"1.4.3.33"'
    assert transformer["Executable32"] == '"transformer_tool_x32.dll"'
    assert transformer["Executable64"] == '""'
    assert transformer["Timeout"] == "33000"
    assert transformer["Trigger"] == "ON_USER_REQUEST"
    assert transformer["InverseTransformer"] == "TRANSFORMER_TOOL_REVERSE"


def test_rules_transformer_full():
    """
    Test A2L TRANSFORMER section.
    """
    transformer = """
    /begin TRANSFORMER TEST_TRANSFORMER_TOOL
        "1.3.0.24" /* Version info */
        "transformer_x32.dll" /* 32bit DLL */
        "transformer_x64" /* 64bit DLL */
        5000 /* timeout in [ms] */
        ON_CHANGE
        TRANSFORMER_TOOL_REVERSE_1
        /begin TRANSFORMER_IN_OBJECTS
            IN_CHAR_1
            IN_BLOB_1
            IN_TYPEDEF_STRUCT_x1
        /end TRANSFORMER_IN_OBJECTS
        /begin TRANSFORMER_OUT_OBJECTS
            OUT_ID_14
            OUT_STRUCT_x2
            OUT_BLOB_1
            OUT_BLOB_2
        /end TRANSFORMER_OUT_OBJECTS
    /end TRANSFORMER
    """
    ast = A2LYacc().generate_ast(transformer)
    assert ast

    transformer = ast["TRANSFORMER"]
    assert transformer
    assert transformer["Name"] == "TEST_TRANSFORMER_TOOL"
    assert transformer["VERSION"] == '"1.3.0.24"'
    assert transformer["Executable32"] == '"transformer_x32.dll"'
    assert transformer["Executable64"] == '"transformer_x64"'
    assert transformer["Timeout"] == "5000"
    assert transformer["Trigger"] == "ON_CHANGE"
    assert transformer["InverseTransformer"] == "TRANSFORMER_TOOL_REVERSE_1"
    assert transformer["TRANSFORMER_IN_OBJECTS"] == ["IN_CHAR_1", "IN_BLOB_1", "IN_TYPEDEF_STRUCT_x1"]
    assert transformer["TRANSFORMER_OUT_OBJECTS"] == ["OUT_ID_14", "OUT_STRUCT_x2", "OUT_BLOB_1", "OUT_BLOB_2"]

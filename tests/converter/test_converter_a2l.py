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


from a2lparser.a2l.converter.a2l_converter import A2LConverter


def valid_ast_dict_multiple_files() -> dict:
    """
    Returns an AST dictionary with a multiple files structure.
    """
    return {
        "filename.a2l": {
            "key_1": "value_1",
        },
        "filename2.aml": {
            "key_2": "value_2",
        }
    }


def invalid_ast_dict_from_string() -> dict:
    """
    Returns an AST dictionary not parsed from a file.
    The AST has no filename in the top level.
    """
    return {
        "random_keyword": {
            "key": "value",
        },
        "IF_DATA": {
            "key": "value",
        },
        "MEASUREMENT": {
            "key": "value",
        }
    }


def test_converter_a2l_slice_multiple_files():
    """
    Tests slicing the AST with multiple files in the top level dictionary.
    """
    ast_dict = valid_ast_dict_multiple_files()
    converter = A2LConverter()
    result = converter.slice_ast(ast_dict, "json")
    assert len(result) == 2
    assert result[0][0] == "filename.json"
    assert result[1][0] == "filename2.json"
    assert result[0][1]["A2L-File"] == ast_dict["filename.a2l"]
    assert result[1][1]["A2L-File"] == ast_dict["filename2.aml"]


def test_converter_a2l_slice_ast_from_string():
    """
    Tests slicing the AST generated from a string.
    """
    ast_dict = invalid_ast_dict_from_string()
    converter = A2LConverter()
    result = converter.slice_ast(ast_dict, "xml", filename="MEASUREMENT")
    assert len(result) == 1
    filename, root = result[0]
    assert filename == "MEASUREMENT.xml"
    assert root["A2L-File"] == ast_dict


def test_converter_a2l_valid_structure():
    """
    The converter expects the top level keys to be the filenames of the parsed A2L files.
    """
    ast_dict = valid_ast_dict_multiple_files()
    converter = A2LConverter()
    assert converter.is_ast_valid_structure(ast_dict)
    dict_items = list(ast_dict.items())

    first_dict = converter.add_root_element(dict_items[0][1])
    first_filename = converter.remove_file_extension(dict_items[0][0])
    assert first_dict["A2L-File"] == ast_dict["filename.a2l"]
    assert first_filename == "filename"

    second_dict = converter.add_root_element(dict_items[1][1])
    second_filename = converter.remove_file_extension(dict_items[1][0])
    assert second_dict["A2L-File"] == ast_dict["filename2.aml"]
    assert second_filename == "filename2"


def test_converter_a2l_invalid_structure():
    """
    Tests the converter with an invalid structure.
    """
    ast_dict = invalid_ast_dict_from_string()
    converter = A2LConverter()
    assert not converter.is_ast_valid_structure(ast_dict)
    d = converter.add_root_element(ast_dict)
    assert d
    assert d["A2L-File"] == ast_dict

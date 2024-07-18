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
# pylint: disable=W0621  # redefined-outer-name (caused through pytest.fixture)


import pytest
import a2lparser.gen.a2l_ast as ASTNodes
from a2lparser.a2l.ast.abstract_syntax_tree import AbstractSyntaxTree


@pytest.fixture
def a2l_dict():
    """
    Returns a dictionary representing parsed A2L content.
    """
    return {
        "VERSION": {"Major_Version": 1, "Minor_Version": 0, "Patch_Version": 0},
        "MODULE": {"MODULE_NAME": "MyModule"},
        "ANNOTATION": {
            "ANNOTATION_NAME": "MyAnnotation",
            "ANNOTATION_TEXT": "This is my annotation",
        },
        "CHARACTERISTIC": {"CHARACTERISTIC_NAME": "MyCharacteristic"},
        "MEASUREMENT": {
            "MEASUREMENT_NAME": "MyMeasurement",
            "ANNOTATION": {
                "ANNOTATION_NAME": "MyMeasurementAnnotation",
                "ANNOTATION_TEXT": "This is my measurement annotation",
            },
        },
        "RECORD_LAYOUT": {"RECORD_LAYOUT_NAME": "MyRecordLayout"},
    }


@pytest.fixture
def a2l_dict_nested():
    """
    returns a nested dictionary
    """
    return {
        "VERSION": {"Major_Version": 1, "Minor_Version": 0, "Patch_Version": 51012},
        "MODULE": [
            {"MODULE_NAME": "MyModuleFirst"},
            {"MODULE_NAME": "MyModuleSecond"},
            {"MODULE_NAME": "MyModuleThird"},
        ],
        "ANNOTATION": {
            "ANNOTATION_NAME": "MyAnnotation",
            "ANNOTATION_TEXT": "This is my ANNOTATION",
        },
        "CHARACTERISTIC": {
            "CHARACTERISTIC_NAME": "MyCharacteristic",
            "ANNOTATION": {
                "ANNOTATION_TEXT": [
                    "Characteristic annotation",
                    "inside a LIST",
                    "a LIST with three items",
                ]
            },
        },
        "MEASUREMENT": {
            "MEASUREMENT_NAME": "MyMeasurement",
            "ECU_ADDRESS": "0x4488ee12",
            "ANNOTATION": {
                "ANNOTATION_NAME": "MyMeasurementAnnotation",
                "ANNOTATION_TEXT": "This is my MEASUREMENT annotation",
            },
            "CHARACTERISTIC": {
                "CHARACTERISTIC_NAME": "MyCharacteristicEcuAddress",
                "ECU_ADDRESS": "0x4488ee44",
                "ANNOTATION": [
                    {
                        "ANNOTATION_TEXT": [
                            "Characteristic annotation",
                            "inside a LIST",
                            "a LIST with three items",
                        ]
                    },
                    {"ANNOTATION_TEXT": ["ecu address: 0x88ff8800", "ecu_addr_match: 0x4488ef11"]},
                    {"ANNOTATION_TEXT": ["ecu_addr_no_match: 0xff88ef11"]},
                ],
            },
        },
        "RECORD_LAYOUT": {"RECORD_LAYOUT_NAME": "MyRecordLayout"},
        "ECU_ADDRESS": "0x4488ffff",
    }


@pytest.fixture
def a2l_node():
    """
    Returns an empty AST root node.
    """
    return ASTNodes.Abstract_Syntax_Tree([])


def test_abstract_syntax_tree_create_from_nodes():
    """
    Builds an AST object from nodes and compares the value.
    """
    label_string_literal = '"test_label"'
    annotation_opt = ASTNodes.Annotation_Opt()
    annotation_opt.Annotation_Label = label_string_literal
    annotation = ASTNodes.Annotation(OptionalParams=annotation_opt)
    ast_node = ASTNodes.Abstract_Syntax_Tree([annotation])
    ast = AbstractSyntaxTree(abstract_syntax_tree=ast_node.node)
    assert ast["ANNOTATION"]["ANNOTATION_LABEL"], label_string_literal


def test_abstract_syntax_tree_create_from_dictionary(a2l_dict):
    """
    Creates a AST object from a dictionary.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=None, dictionary=a2l_dict)
    assert ast


def test_abstract_syntax_tree_find_sections(a2l_dict, a2l_node):
    """
    Test the recursive find section utility function of the abstract syntax tree.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict)

    version = ast.find_sections("version")["VERSION"]
    assert version == a2l_dict["VERSION"]

    module = ast.find_sections("module")["MODULE"]
    assert module == a2l_dict["MODULE"]

    first_annotation, second_annotation = ast.find_sections("annotation")["ANNOTATION"]
    assert first_annotation == a2l_dict["ANNOTATION"]
    assert second_annotation == a2l_dict["MEASUREMENT"]["ANNOTATION"]

    characteristic = ast.find_sections("characteristic")["CHARACTERISTIC"]
    assert characteristic == a2l_dict["CHARACTERISTIC"]

    measurements = ast.find_sections("measurement")["MEASUREMENT"]
    measurements_ast = ast.find_sections("measurement")
    assert measurements == a2l_dict["MEASUREMENT"]

    measurement_annotations = measurements_ast.find_sections("annotation")["ANNOTATION"]
    assert measurement_annotations == a2l_dict["MEASUREMENT"]["ANNOTATION"]

    record_layouts = ast.find_sections("record_layout")["RECORD_LAYOUT"]
    assert record_layouts == a2l_dict["RECORD_LAYOUT"]


def test_abstract_syntax_tree_find_value(a2l_dict_nested, a2l_node):
    """
    Test the recursive find value utility function for the abstract syntax tree object.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict_nested)

    expected_modules_list = a2l_dict_nested["MODULE"]
    module_dict = ast.find_value("MyModule")
    modules_list = module_dict["MODULE"]
    assert len(module_dict) == 1
    assert len(modules_list) == 3
    assert modules_list == expected_modules_list

    expected_ecu_address_root = a2l_dict_nested["ECU_ADDRESS"]
    expected_ecu_address_measurement = a2l_dict_nested["MEASUREMENT"]["ECU_ADDRESS"]
    expected_ecu_address_measurement_characteristic = a2l_dict_nested["MEASUREMENT"][
        "CHARACTERISTIC"
    ]["ECU_ADDRESS"]
    expected_ecu_address_in_annotation_text = a2l_dict_nested["MEASUREMENT"]["CHARACTERISTIC"][
        "ANNOTATION"
    ][1]
    ecu_address = ast.find_value("0x4488")
    assert ecu_address
    assert ecu_address["ECU_ADDRESS"] == expected_ecu_address_root

    ecu_address_measurement = ecu_address["MEASUREMENT"]
    assert ecu_address_measurement
    assert ecu_address_measurement["ECU_ADDRESS"] == expected_ecu_address_measurement

    ecu_address_measurement_characteristic = ecu_address_measurement["CHARACTERISTIC"]
    assert (
        ecu_address_measurement_characteristic["ECU_ADDRESS"]
        == expected_ecu_address_measurement_characteristic
    )
    assert (
        ecu_address_measurement_characteristic["ANNOTATION"]["ANNOTATION_TEXT"]
        == expected_ecu_address_in_annotation_text["ANNOTATION_TEXT"]
    )


def test_abstract_syntax_tree_dict_init(a2l_dict, a2l_node):
    """
    Test dictionary functionality of the AbstractSyntaxTree class.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict)
    assert ast.get_dict() == a2l_dict


def test_abstract_syntax_tree_dict_getitem(a2l_dict, a2l_node):
    """
    Test dictionary functionality of the AbstractSyntaxTree class.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict)
    assert ast["VERSION"]["Major_Version"] == a2l_dict["VERSION"]["Major_Version"]


def test_abstract_syntax_tree_dict_setitem(a2l_dict, a2l_node):
    """
    Test dictionary functionality of the AbstractSyntaxTree class.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict)
    ast["VERSION"]["Major_Version"] = 2
    assert ast["VERSION"]["Major_Version"] == 2


def test_abstract_syntax_tree_dict_delitem(a2l_dict, a2l_node):
    """
    Test dictionary functionality of the AbstractSyntaxTree class.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict)
    del ast["VERSION"]
    assert "VERSION" not in ast


def test_abstract_syntax_tree_dict_len(a2l_dict, a2l_node):
    """
    Test dictionary functionality of the AbstractSyntaxTree class.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict)
    assert len(ast) == len(a2l_dict)


def test_abstract_syntax_tree_dict_keys(a2l_dict, a2l_node):
    """
    Test dictionary functionality of the AbstractSyntaxTree class.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict)
    assert list(ast.keys()) == list(a2l_dict.keys())


def test_abstract_syntax_tree_dict_values(a2l_dict, a2l_node):
    """
    Test dictionary functionality of the AbstractSyntaxTree class.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict)
    assert list(ast.values()) == list(a2l_dict.values())


def test_abstract_syntax_tree_dict_items(a2l_dict, a2l_node):
    """
    Test dictionary functionality of the AbstractSyntaxTree class.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict)
    assert list(ast.items()) == list(a2l_dict.items())


def test_abstract_syntax_tree_dict_update(a2l_dict, a2l_node):
    """
    Test dictionary functionality of the AbstractSyntaxTree class.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict)
    tmp = a2l_dict
    ast.update({"VERSION": "version1", "RECORD_LAYOUT": "new_record_layout"})
    tmp.update({"VERSION": "version1", "RECORD_LAYOUT": "new_record_layout"})
    assert ast == tmp


def test_abstract_syntax_tree_dict_clear(a2l_dict, a2l_node):
    """
    Test dictionary functionality of the AbstractSyntaxTree class.
    """
    ast = AbstractSyntaxTree(abstract_syntax_tree=a2l_node.node, dictionary=a2l_dict)
    ast.clear()
    assert len(ast) == 0

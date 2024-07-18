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
# pylint: disable=W0212, W0621


import pytest
from a2lparser.a2l.ast.abstract_syntax_tree import AbstractSyntaxTree


@pytest.fixture
def nested_dict():
    """
    returns a nested dictionary
    """
    return {
        "VERSION": {"Major_Version": 1, "Minor_Version": 0, "Patch_Version": 51012},
        "MODULE": {"MODULE_NAME": "MyModule"},
        "ANNOTATION": {
            "ANNOTATION_NAME": "MyAnnotation",
            "ANNOTATION_TEXT": "This is my ANNOTATION",
        },
        "CHARACTERISTIC": {
            "CHARACTERISTIC_NAME": "MyCharacteristic",
            "ANNOTATION": {"ANNOTATION_TEXT": ["Characteristic annotation", "inside a LIST"]},
        },
        "MEASUREMENT": {
            "MEASUREMENT_NAME": "MyMeasurement",
            "ECU_ADDRESS": "0x4488ee12",
            "ANNOTATION": {
                "ANNOTATION_NAME": "MyMeasurementAnnotation",
                "ANNOTATION_TEXT": "This is my MEASUREMENT annotation",
            },
        },
        "RECORD_LAYOUT": {"RECORD_LAYOUT_NAME": "MyRecordLayout"},
    }


def test_ast_is_value_match_non_recursive(nested_dict):
    """
    Tests matching values on the first level of the passed dictionary.
    """
    ast = AbstractSyntaxTree(None, nested_dict)
    matched = ast._is_value_match(
        value=nested_dict["VERSION"],
        search_expression=str(nested_dict["VERSION"]["Patch_Version"]),
        case_sensitive=False,
        exact_match=True,
        recursive_search=False,
    )
    assert matched is True

    non_matched = ast._is_value_match(
        value=nested_dict,
        search_expression=str(nested_dict["VERSION"]["Patch_Version"]),
        case_sensitive=False,
        exact_match=True,
        recursive_search=False,
    )
    assert non_matched is False


def test_ast_is_value_match_nested_list(nested_dict):
    """
    Tests if a value nested in a list can be matched.
    """
    ast = AbstractSyntaxTree(None, nested_dict)
    matched = ast._is_value_match(
        value=nested_dict,
        search_expression="a LIST",
        case_sensitive=False,
        exact_match=False,
        recursive_search=True,
    )
    assert matched is True

    matched_non_recursive = ast._is_value_match(
        value=nested_dict["CHARACTERISTIC"]["ANNOTATION"]["ANNOTATION_TEXT"],
        search_expression="a list",
        case_sensitive=False,
        exact_match=False,
        recursive_search=False,
    )
    assert matched_non_recursive is True

    non_matched_non_recursive = ast._is_value_match(
        value=nested_dict["CHARACTERISTIC"]["ANNOTATION"],
        search_expression="a list",
        case_sensitive=False,
        exact_match=False,
        recursive_search=False,
    )
    assert non_matched_non_recursive is False


@pytest.mark.parametrize(
    "search_expression, case_sensitive, expected_result",
    [
        ("This is my", True, True),
        ("measurement annotation", False, True),
        ("this is my measurement annotation", True, False),
        ("MEASUREMENT annotation", True, True),
    ],
)
def test_ast_is_value_match_partial(
    nested_dict, search_expression, case_sensitive, expected_result
):
    """
    Test matching a part of a value in a nested dictionary.
    """
    # create an AST object
    ast = AbstractSyntaxTree(None, nested_dict)

    # match the search value with the nested dictionary value
    is_value_matched = ast._is_value_match(
        value=nested_dict,
        search_expression=search_expression,
        case_sensitive=case_sensitive,
        exact_match=False,
        recursive_search=True,
    )
    assert is_value_matched == expected_result


@pytest.mark.parametrize(
    "search_expression, case_sensitive, expected_result",
    [
        ("This is my MEASUREMENT annotation", True, True),
        ("this is my measurement annotation", True, False),
        ("this is my measurement annotation", False, True),
    ],
)
def test_ast_is_value_match_case_sensitivity(
    nested_dict, search_expression, case_sensitive, expected_result
):
    """
    Test for matching a value in a nested dictionary with and without case sensitivity.
    """
    # create an AST object
    ast = AbstractSyntaxTree(None, nested_dict)

    # match the search value with the nested dictionary value
    is_value_matched = ast._is_value_match(
        value=nested_dict,
        search_expression=search_expression,
        case_sensitive=case_sensitive,
        exact_match=False,
        recursive_search=True,
    )
    assert is_value_matched == expected_result


@pytest.mark.parametrize(
    "search_expression, case_sensitive, exact_match, expected_result",
    [
        ("This is my MEASUREMENT annotation", True, True, True),
    ],
)
def test_ast_is_value_match_exact_case(
    nested_dict, search_expression, case_sensitive, exact_match, expected_result
):
    """
    Test for matching the exact case of a value in a nested dictionary.
    """
    # create an AST object
    ast = AbstractSyntaxTree(None, nested_dict)

    # match the search value with the nested dictionary value
    is_value_matched = ast._is_value_match(
        value=nested_dict,
        search_expression=search_expression,
        case_sensitive=case_sensitive,
        exact_match=exact_match,
        recursive_search=True,
    )
    assert is_value_matched == expected_result

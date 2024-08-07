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

import re
from typing import Union, Any
from a2lparser.a2l.lex.lexer_keywords import LexerKeywords
import a2lparser.gen.a2l_ast as ASTNodes


class AbstractSyntaxTree:
    """
    Utility class for wrapping the Abstract Syntax Tree created from YACC into a dictionary.
    Can be used like a dictionary with extra utility methods.

    Usage:
        >>> ast: AbstractSyntaxTree = parser.generate_ast(content=a2l_content)
        >>> measurements_dict = ast["MEASUREMENT"]
        >>> print(ast.find_sections("annotation"))
        >>> print(ast.find_value("0x4408ff12", "measurement"))
    """

    class ASTException(Exception):
        """
        Raised when a fatal error is encountered while trying to generate an AST dictionary.
        """

    def __init__(self, abstract_syntax_tree, dictionary: dict = None) -> None:
        """
        AbstractSyntaxTree Constructor.

        Args:
            abstract_syntax_tree: A generated abstract syntax tree from YACC.
            dictionary: If a dictionary is passed the AST will be populated from the dictionary.
        """
        if dictionary is None:
            dictionary = {}

        if not bool(dictionary) and not AbstractSyntaxTree.validate_ast(abstract_syntax_tree):
            raise AbstractSyntaxTree.ASTException(
                f"Unable to create an AbstractSyntaxTree container from values "
                f"'abstract_syntax_tree={abstract_syntax_tree}', 'dictionary={dictionary}'"
            )

        self._ast = abstract_syntax_tree
        self._dict = dictionary

        if not bool(dictionary) and abstract_syntax_tree:
            self._create_dict_from_ast(abstract_syntax_tree)

    @staticmethod
    def validate_ast(ast) -> bool:
        """
        Validates the abstract syntax tree.
        """
        if isinstance(ast, ASTNodes.Abstract_Syntax_Tree):
            if getattr(ast, "node") is not None:
                return True
        elif isinstance(ast, (dict, list, tuple)) and len(ast) > 0:
            return True
        elif hasattr(ast, "children") and callable(getattr(ast, "children")):
            return True
        return False

    def find_value(
        self, search_value: str, case_sensitive: bool = False, exact_match: bool = False
    ) -> "AbstractSyntaxTree":
        """
        Returns the dictionaries containing the passed value like this:
        { "<search_value>": {found_dictionaries} }

        Args:
            search_value: The search value to search for.
            case_sensitive: Whether or not the value should be matched case-sensitive.
            exact_match: Whether or not the value should be exactly matched.

        Returns:
            dict: A dictionary containing the found values.
        """
        return AbstractSyntaxTree(
            self._ast, self._find_value(search_value, self._dict, case_sensitive, exact_match)
        )

    def find_sections(self, section_name: str) -> "AbstractSyntaxTree":
        """
        Returns an AbstractSyntaxTree object containing the sections of the given section_name.

        Args:
            section_name (str): The name of the section to search for.

        Returns:
            AbstractSyntaxTree: An AbstractSyntaxTree object containing the found sections.
                Dictionary access is wrapped through section name as key.
                If only one section is found, it is wrapped in a dictionary.
                If multiple sections are found, they are wrapped in a list.
        """
        sections = []
        section_name = section_name.upper()
        for key, value in self._dict.items():
            if key.upper() == section_name:
                sections.append(value)
            elif isinstance(value, dict):
                if section := AbstractSyntaxTree(self._ast, value).find_sections(section_name):
                    if isinstance(section[section_name], list):
                        sections.extend(section[section_name])
                    else:
                        sections.append(section[section_name])
        if len(sections) == 1:
            return AbstractSyntaxTree(
                abstract_syntax_tree=self._ast, dictionary={section_name: sections[0]}
            )
        return AbstractSyntaxTree(
            abstract_syntax_tree=self._ast, dictionary={section_name: sections}
        )

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __delitem__(self, key):
        del self._dict[key]

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        return iter(self._dict)

    def __contains__(self, key):
        return key in self._dict

    def __str__(self):
        return self._print_dict(self._dict)

    def __eq__(self, other):
        if isinstance(other, dict):
            return self._dict == other
        if isinstance(other, AbstractSyntaxTree):
            return self._dict == other._dict
        return False

    def keys(self):
        """
        Returns a view object that contains the keys of the object.
        """
        return self._dict.keys()

    def values(self):
        """
        This method returns a view object that contains the values of the object.
        """
        return self._dict.values()

    def items(self):
        """
        This method returns a view object that contains the key-value pairs of the object.
        """
        return self._dict.items()

    def update(self, other):
        """
        Updates the dictionary
        """
        self._dict.update(other)

    def clear(self):
        """
        Clears the dictionary.
        """
        self._dict.clear()

    def get_dict(self):
        """
        Returns a reference to the dictionary object.
        """
        return self._dict

    def _print_dict(self, dictionary, indent=""):
        """
        Recursively prints a dictionary in a tree-like structure, similar to the Unix tree command.

        Args:
            dictionary (dict): The dictionary to be printed.
            indent (str, optional): The indentation string to be used for each level of the tree.
                Defaults to an empty string.

        Returns:
            str: The string representation of the dictionary in the tree-like structure.

        Examples:
            >>> dictionary = {'a': {'b': 1, 'c': 2}, 'd': [{'e': 3}, {'f': 4}]}
            >>> print(_print_dict(dictionary))
            .
            ├── a:
            │   ├── b: 1
            │   ├── c: 2
            │   └── d:
            │       ├── e: 3
            │       └── f: 4
            └── d:
                ├── e: 3
                └── f: 4
        """
        if not isinstance(dictionary, dict):
            return f"{indent}└── {dictionary}"
        result = ""
        for i, (key, value) in enumerate(dictionary.items()):
            if isinstance(value, dict):
                if i == len(dictionary) - 1:
                    result += f"\n{indent}└── {key}:"
                    result += self._print_dict(value, f"{indent}    ")
                else:
                    result += f"\n{indent}├── {key}:"
                    result += self._print_dict(value, f"{indent}│   ")
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        if i == len(dictionary) - 1:
                            result += f"\n{indent}└── {key}:"
                            result += self._print_dict(item, f"{indent}    ")
                        else:
                            result += f"\n{indent}├── {key}:"
                            result += self._print_dict(item, f"{indent}│   ")
                    else:
                        result += (
                            f"\n{indent}└── {key}: {item}"
                            if i == len(dictionary) - 1
                            else f"\n{indent}├── {key}: {item}"
                        )
            elif i == len(dictionary) - 1:
                result += f"\n{indent}└── {key}: {value}"
            else:
                result += f"\n{indent}├── {key}: {value}"
        return result

    def _find_value(
        self,
        search_expression: Union[str, re.Pattern],
        dictionary: dict,
        case_sensitive: bool,
        exact_match: bool,
    ) -> dict:
        """
        Searches recursively for a search expression under the values of the given dictionary.

        Args:
            search_value: The search value to search for.
            dictionary: Expects a dctionary to be passed.
            case_sensitive: Whether or not the value should be matched case-sensitive.
            exact_match: Whether or not the value should be exactly matched.

        Returns:
            dict: A dictionary containing the found values.
        """
        result = {}
        if isinstance(dictionary, dict):
            for key, value in dictionary.items():
                if self._is_value_match(
                    value, search_expression, case_sensitive, exact_match, True
                ):
                    if key in result:
                        if not isinstance(result[key], list):
                            result[key] = [result[key]]
                    else:
                        result[key] = {}
                    if isinstance(value, list):
                        for obj in value:
                            if isinstance(obj, dict):
                                if section := self._find_value(
                                    search_expression, obj, case_sensitive, exact_match
                                ):
                                    if key in result:
                                        if isinstance(result[key], list):
                                            result[key].append(section)
                                        elif not bool(result[key]):
                                            result[key] = section
                                        else:
                                            result[key] = [result[key], section]
                    if self._is_value_match(
                        value, search_expression, case_sensitive, exact_match, False
                    ):
                        if isinstance(value, dict):
                            if section := self._find_value(
                                search_expression, value, case_sensitive, exact_match
                            ):
                                result[key] = section
                        else:
                            result[key] = value
                    elif isinstance(value, dict):
                        if section := self._find_value(
                            search_expression, value, case_sensitive, exact_match
                        ):
                            result[key] = section
                elif isinstance(value, dict):
                    self._find_value(search_expression, value, case_sensitive, exact_match)
        return result

    def _is_value_match(
        self,
        value: Any,
        search_expression: Union[str, re.Pattern],
        case_sensitive: bool,
        exact_match: bool,
        recursive_search: bool,
    ) -> bool:
        """Checks if the given value matches the search expression.

        Args:
            value: The value to be checked.
            search_expression: The expression to search for.
            case_sensitive: Whether the search should be case-sensitive.
            exact_match: Whether the search should be an exact match.
            recursive_search: Whether to perform a recursive search.

        Returns:
            bool: True if the value matches the search expression, False otherwise.
        """

        if isinstance(value, dict):
            values = list(value.values())
        elif isinstance(value, (list, tuple)):
            values = value
        else:
            values = str(value)

        if isinstance(values, str):
            if self._is_value_match_expression(
                values, search_expression, case_sensitive, exact_match
            ):
                return True
        elif not recursive_search and isinstance(values, list):
            for obj in values:
                if not isinstance(
                    obj, (dict, list, tuple, AbstractSyntaxTree)
                ) and self._is_value_match_expression(
                    str(obj), search_expression, case_sensitive, exact_match
                ):
                    return True
        elif recursive_search and isinstance(values, list):
            for obj in values:
                if self._is_value_match(
                    obj, search_expression, case_sensitive, exact_match, recursive_search
                ):
                    return True
        return False

    def _is_value_match_expression(
        self,
        value_string: str,
        search_expression: Union[str, re.Pattern],
        case_sensitive: bool,
        exact_match: bool,
    ):
        """
        Checks if the given value string matches the search expression.

        Args:
            value_string (str): The value string to be checked.
            search_expression (Union[str, re.Pattern]): The expression to search for.
            case_sensitive (bool): Whether the search should be case-sensitive.
            exact_match (bool): Whether the search should be an exact match.

        Returns:
            bool: True if the value string matches the search expression, False otherwise.
        """
        if isinstance(search_expression, str):
            if not case_sensitive:
                search_expression = search_expression.lower()
                value_string = value_string.lower()
            if (
                exact_match
                and value_string == search_expression
                or not exact_match
                and search_expression in value_string
            ):
                return True
        elif isinstance(search_expression, re.Pattern):
            return search_expression.search(value_string) is not None
        return False

    def _is_node_name_keyword(
        self,
        node_name: str,
        keywords: list = LexerKeywords.keywords_type
        + LexerKeywords.keywords_enum
        + LexerKeywords.keywords_section
        + LexerKeywords.keywords_datatypes,
    ) -> bool:
        """
        Check if the given node name is a keyword.

        Args:
            node_name (str): The name of the node.
            keywords (list, optional): The list of keywords. Defaults to the combination of
                keywords_type, keywords_enum, keywords_section, and keywords_datatypes.

        Returns:
            bool: True if the node name is a keyword, False otherwise.
        """
        return any(node_name.upper() == keyword for keyword in keywords)

    def _create_dict_from_ast(self, abstract_syntax_tree) -> None:
        """
        Create a dictionary from parsed AST nodes.
        """
        for node in abstract_syntax_tree:
            node_name = type(node).__name__.upper()

            if node_name in self._dict:
                if isinstance(self._dict[node_name], dict):
                    self._dict[node_name] = [self._dict[node_name]]
                self._dict[node_name].append({})
                node_dict = self._dict[node_name][-1]
            else:
                node_dict = {}
                self._dict[node_name] = node_dict

            attr_names = getattr(node, "attr_names", ())
            for attr_name in attr_names:
                attr_value = getattr(node, attr_name)
                if self._is_node_name_keyword(attr_name):
                    attr_name = attr_name.upper()
                node_dict[attr_name] = attr_value
            self._add_children(node, node_dict)

    def _add_children(self, node, parent_dict):
        """
        Recursively adds children nodes to the parent dictionary based on the given node.

        Args:
            self: The object instance.
            node: The current node to process.
            parent_dict: The dictionary representing the parent node.
        """
        if not hasattr(node, "children"):
            return
        for child in node.children():
            if (
                not isinstance(child, tuple)
                or len(child) != 2
                or not isinstance(child[0], str)
                # or not hasattr(child[1], "children")
            ):
                raise ValueError("Invalid nodelist structure")
            child_name = child[0]
            child_obj = child[1]

            if re.match(r".+\[\d+\]$", child_name):
                child_name = re.sub(r"\[\d+\]$", "", child_name)

            if self._is_node_name_keyword(child_name):
                child_name = child_name.upper()
            elif child_name == ASTNodes.If_Data_Block.__name__:
                child_name = child_obj.Name

            if child_name == "OptionalParams":
                child_dict = parent_dict
            elif child_name in parent_dict:
                if isinstance(parent_dict[child_name], dict):
                    parent_dict[child_name] = [parent_dict[child_name]]
                parent_dict[child_name].append({})
                child_dict = parent_dict[child_name][-1]
            else:
                child_dict = {}
                parent_dict[child_name] = child_dict

            if isinstance(child_obj, (str, int, float, bool)):
                parent_dict[child_name] = child_obj
                child_dict = parent_dict[child_name]
            else:
                attr_names = getattr(child_obj, "attr_names", ())
                for attr_name in attr_names:
                    attr_value = getattr(child_obj, attr_name)
                    if attr_value is not None:
                        if self._is_node_name_keyword(attr_name):
                            attr_name = attr_name.upper()
                        child_dict[attr_name] = attr_value

            self._add_children(child_obj, child_dict)

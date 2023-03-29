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


import a2lparser.gen.a2l_ast as ASTNodes


class AbstractSyntaxTree:
    """
    Utility class for the Abstract Syntax Tree created from YACC.
    """

    def __init__(self, abstract_syntax_tree) -> None:
        """
        AbstractSyntaxTree Constructor.

        Args:
            - abstract_syntax_tree: A genereated abstract syntax tree from YACC.
        """
        self.ast = abstract_syntax_tree
        self.data = {}
        self._create_dict_from_ast(abstract_syntax_tree)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, key):
        return key in self.data

    def __str__(self):
        return self._print_dict(self.data)

    def keys(self):
        """
        Returns a view object that contains the keys of the object.
        """
        return self.data.keys()

    def values(self):
        """
        this method returns a view object that contains the values of the object.
        """
        return self.data.values()

    def items(self):
        """
        this method returns a view object that contains the key-value pairs of the object.
        """
        return self.data.items()

    def _add_children(self, node, parent_dict):
        children = node.children()
        for child in children:
            if (
                not isinstance(child, tuple)
                or len(child) != 2
                or not isinstance(child[0], str)
                or not hasattr(child[1], "children")
            ):
                raise ValueError("Invalid nodelist structure")
            child_name = child[0]
            child_obj = child[1]

            if child_name == "OptionalParams":
                child_dict = parent_dict
            elif child_name in parent_dict:
                if isinstance(parent_dict[child_name], dict):
                    parent_dict[child_name] = [parent_dict[child_name]]
                    parent_dict[child_name].append({})
                else:
                    parent_dict[child_name].append({})
                child_dict = parent_dict[child_name][-1]
            else:
                child_dict = {}
                parent_dict[child_name] = child_dict

            attr_names = getattr(child_obj, "attr_names", ())
            for attr_name in attr_names:
                attr_value = getattr(child_obj, attr_name)
                child_dict[attr_name] = attr_value
            self._add_children(child_obj, child_dict)

    def _create_dict_from_ast(self, abstract_syntax_tree) -> None:
        for node in abstract_syntax_tree:
            node_name = type(node).__name__

            if node_name in self.data:
                if isinstance(self.data[node_name], dict):
                    self.data[node_name] = [self.data[node_name]]
                    self.data[node_name].append({})
                else:
                    self.data[node_name].append({})
                node_dict = self.data[node_name][-1]
            else:
                node_dict = {}
                self.data[node_name] = node_dict

            attr_names = getattr(node, "attr_names", ())
            for attr_name in attr_names:
                attr_value = getattr(node, attr_name)
                node_dict[attr_name] = attr_value
            self._add_children(node, node_dict)

    def _print_dict(self, dictionary, indent=""):
        """
        Prints the AST dictionary in the style of the unix tree command.
        """
        if isinstance(dictionary, dict):
            result = ""
            for i, (key, value) in enumerate(dictionary.items()):
                if isinstance(value, dict):
                    if i == len(dictionary) - 1:
                        result += f"\n{indent}└── {key}:"
                        result += self._print_dict(value, indent + "    ")
                    else:
                        result += f"\n{indent}├── {key}:"
                        result += self._print_dict(value, indent + "│   ")
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            if i == len(dictionary) - 1:
                                result += f"\n{indent}└── {key}:"
                                result += self._print_dict(item, indent + "    ")
                            else:
                                result += f"\n{indent}├── {key}:"
                                result += self._print_dict(item, indent + "│   ")
                        else:
                            if i == len(dictionary) - 1:
                                result += f"\n{indent}└── {key}: {item}"
                            else:
                                result += f"\n{indent}├── {key}: {item}"
                else:
                    if i == len(dictionary) - 1:
                        result += f"\n{indent}└── {key}: {value}"
                    else:
                        result += f"\n{indent}├── {key}: {value}"
            return result
        else:
            return f"{indent}└── {dictionary}"

    def validate_ast(self) -> bool:
        """
        Validates the abstract syntax tree.
        """
        if not isinstance(self.ast, ASTNodes.Abstract_Syntax_Tree):
            return False

        ast_node = getattr(self.ast, "node")
        if ast_node is None:
            return False

        return True

    def validate_node(self) -> bool:
        """
        Validates an abstract syntax tree node.
        """
        return True

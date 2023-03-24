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


from typing import Any
import a2lparser.a2l.ast.a2l_ast as nodes


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
        self.ast_dict = {}
        self.index = 0
        self._create_ast_dictionary()

    def __iter__(self):
        self.index = 0
        return self.index

    def __next__(self):
        return "value"

    def find_entry(self, entry_name: str, entry_value: Any = None) -> dict:
        """
        Finds a parsed section of the A2L file.
        """
        entry = {}
        if self.validate_ast() is False:
            return entry

        return entry

    def validate_ast(self) -> bool:
        """
        Validates the abstract syntax tree.
        """
        if not isinstance(self.ast, nodes.Abstract_Syntax_Tree):
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

    def _create_ast_dictionary(self) -> None:
        """
        Creates a dictionary from the AST.
        """
        for node in self.ast.node:
            key = node.__class__.__name__
            for attribute in node.attr_names:
                self.ast_dict[key] = attribute

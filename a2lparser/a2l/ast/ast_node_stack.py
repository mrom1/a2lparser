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


class ASTNodeStack:
    """
    AST Node Stack.

    Keeps track of current nodes parsed in the grammar rules.
    """

    def __init__(self):
        self._stack = []

    def create_node(self, node):
        """
        Creates a new node and adds it to the stack.
        """
        self._stack.append(node)
        return self._stack[-1]

    def get_node(self, node, reverse=True):
        """
        Returns the first node of the given type in the stack.
        """
        if reverse:
            return next(
                (_node for _node in reversed(self._stack) if isinstance(_node, node)),
                None,
            )
        return next(
            (_node for _node in self._stack if isinstance(_node, node)),
            None,
        )

    def get_or_create_node(self, node, reverse=True):
        """
        Creates or returns the given node in the stack.
        """
        _node = self.get_node(node=node, reverse=reverse)
        if _node is None:
            _node = self.create_node(node=node())
        return _node

    def remove_node(self, node, reverse=True, single_remove=False) -> None:
        """
        Removes the given node from the stack.
        """
        if reverse:
            for _node in reversed(self._stack):
                if isinstance(_node, node):
                    self._stack.remove(_node)
                    if single_remove:
                        break
        else:
            for _node in self._stack:
                if isinstance(_node, node):
                    self._stack.remove(_node)

    def add_node_param(self, node_class, ast_node_names, param):
        """
        Adds the parameter to the given node.
        """
        for _node in ast_node_names:
            if isinstance(param, _node):
                setattr(node_class, param.__class__.__name__, getattr(param, param.__slots__[0]))

    def add_node_object(self, node_class, ast_node_names, param):
        """
        Adds another node object as a parameter to the given node class object.
        """
        for _node in ast_node_names:
            if isinstance(param, _node):
                setattr(node_class, param.__class__.__name__, param)

    def add_node_object_list(self, node_class, ast_node_names, param):
        """
        Adds a list of node objects as a parameter to the given node class object.
        """
        for _node in ast_node_names:
            if isinstance(param, _node):
                if getattr(node_class, param.__class__.__name__) is None:
                    setattr(node_class, param.__class__.__name__, [param])
                else:
                    getattr(node_class, param.__class__.__name__).append(param)

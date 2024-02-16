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


from string import Template


_FILE_COMMENT = r"""
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
# pylint: disable-all
# flake8: noqa
# ---------------------------------------------------------------------- #
# *** IMPORTENT ***                                                      #
# This code was generated from the config file:                          #
#   $cfg_filename  #
#                                                                        #
# If you wish to edit this code use the generator in the subfolder gen   #
# and adjust the config file, not the code itself!                       #
# Don't edit this file manually!                                         #
# *** IMPORTENT ***                                                      #
#                                                                        #
#                                                                        #
# Abstract Syntax Tree (AST) Node Classes.                               #
#                                                                        #
# ---------------------------------------------------------------------- #

"""


_FILE_CODE = """

class Node(object):
    __slots__ = ()

    def children(self):
        pass


class NodeVisitor(object):
    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for ast_class_name, ast_class in node.children():
            self.visit(ast_class)


class NodeCorrupted(Node):
    __slots__ = ('Corrupted', 'node_name', 'node_obj', '__weakref__')
    def __init__(self, node_name, node_obj):
        self.Corrupted = True
        self.node_name = node_name
        self.node_obj = node_obj

    def children(self):
        nodelist = []
        if (node_name := self.node_name) and (node_obj := self.node_obj):
            nodelist.append((node_name, node_obj))
        return tuple(nodelist)

    attr_names = ('Corrupted', )


"""


class ASTGenerator:
    """
    ASTGenerator generates the python file containing the AST node classes.

    Usage:
        >>> ast_generator = ASTGenerator("A2L_config.cfg", "a2l_ast.py")
        >>> ast_generator.generate(use_clean_names=True)
    """

    def __init__(self, cfg_filename: str, out_filename: str) -> None:
        """
        Initialize Abstract Syntax Tree Code Generator from config file.

        Args:
            cfg_filename: The A2L ASAM configuration file.
            out_filename: The output file to generate the code to.
        """
        self.cfg_filename = cfg_filename
        self.out_filename = out_filename
        self.node_config = [NodeConfiguration(name, content) for (name, content) in self.parse_config()]

    def generate(self, use_clean_names: bool = True) -> None:
        """
        Generate AST Code and writes it to file.

        Args:
            - use_clean_names: Will use some encoding to generate clean names for
                               classes, values etc. like adding underscores.
                               It is highly recommended to use this.
        """
        with open(self.out_filename, "w", encoding="utf-8") as file:
            file.write(Template(_FILE_COMMENT).substitute(cfg_filename=self.cfg_filename))
            file.write(_FILE_CODE)
            for node_config in self.node_config:
                file.write(node_config.generate_node_source(use_clean_names) + "\n\n\n")

    def parse_config(self):
        """
        Parse the configuration file.
        """
        with open(self.cfg_filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue  # comment
                colon_i = line.find(":")
                left_parenthesis_i = line.find("(")
                right_parenthesis_i = line.find(")")
                if colon_i < 1 or left_parenthesis_i <= colon_i or right_parenthesis_i <= left_parenthesis_i:
                    raise RuntimeError(f"Invalid line in {self.cfg_filename}:\n{line}\n" % (self.cfg_filename, line))

                name = line[:colon_i]
                val = line[left_parenthesis_i + 1: right_parenthesis_i]
                vallist = [v.strip() for v in val.split(",")] if val else []
                yield name, vallist


class NodeConfiguration:
    """
    NodeConfiguration class.
    """

    def __init__(self, node_name, content) -> None:
        """
        NodeConfiguration Constructor.

        Args:
            - node_name: Name
            - content: list of entries of a specific A2L Node
                       e.g. UpperLimit, ECU_Address etc.
        """

        self.node_name = node_name
        self.attributes = []
        self.children = []
        self.seq_children = []
        self.entries = []

        for entry in content:
            clean_entry = entry.strip("*")
            self.entries.append(clean_entry)

            if entry.endswith("**"):
                self.seq_children.append(clean_entry)
            elif entry.endswith("*"):
                self.children.append(clean_entry)
            else:
                self.attributes.append(entry)

    def generate_node_source(self, use_clean_names: bool = True) -> str:
        """
        Generates the source code for one node in the abstract syntax tree.

        Args:
            - use_clean_names: Will use some encoding to generate clean names for
                               classes, values etc. like adding underscores.
                               It is highly recommended to use this.

        Returns:
            The source code of one node in the abstract syntax tree.

        Generated source example:
        class Axis_Pts_Ref(Node):
            __slots__ = ('AxisPoints', '__weakref__')
            def __init__(self, AxisPoints):
                self.AxisPoints = AxisPoints

            def children(self):
                nodelist = []
                return tuple(nodelist)

            attr_names = ('AxisPoints', )
        """
        src = self._gen_base(use_clean_names)
        src += "\n" + self._gen_children()
        src += "\n" + self._gen_attr_names()
        return src

    def _gen_base(self, use_clean_names):
        """
        Generates the class name, slots, constructor code of the node.

        Generated source example:
        class Axis_Pts_Ref(Node):
            __slots__ = ('AxisPoints', '__weakref__')
            def __init__(self, AxisPoints):
                self.AxisPoints = AxisPoints
        """
        if use_clean_names:
            clean_name = self.node_name.lower()
            clean_name = clean_name[0].upper() + clean_name[1:]
            if "_" in clean_name:
                index = [i for i, ltr in enumerate(clean_name) if ltr == "_"]
                indices = [i + 1 for i in index]
                clean_name = "".join(c.upper() if i in indices else c for i, c in enumerate(clean_name))

            self.node_name = clean_name

        src = f"class {self.node_name}(Node):\n"

        clean_entries = []
        if self.entries:
            arguments_list = "(self"
            for entry in self.entries:
                arguments_list += ", "
                if entry.startswith("?"):
                    clean_entry = entry.strip("?") + " = None"
                    arguments_list += clean_entry
                else:
                    arguments_list += entry

            arguments_list += ")"

            for entry in self.entries:
                clean_entries.append(entry.strip("?"))

            slots = ", ".join(f"'{e}'" for e in clean_entries)
            slots += ", '__weakref__'"

        else:
            slots = "'__weakref__'"
            arguments_list = "(self)"

        src += f"    __slots__ = ({slots})\n"
        src += f"    def __init__{arguments_list}:\n"

        for name in clean_entries:
            src += f"        self.{name} = {name}\n"

        return src

    def _gen_children(self):
        """
        Generates the children method code of the node class.

        Generated source example:
            def children(self):
                nodelist = []
                return tuple(nodelist)
        """
        clean_children = []
        clean_seq_children = []
        for child in self.children:
            clean_children.append(child.strip("?"))

        for seq_child in self.seq_children:
            clean_seq_children.append(seq_child.strip("?"))

        src = "    def children(self):\n"

        if self.entries:
            src += "        nodelist = []\n"

            for child in clean_children:
                src += ("        if self.%(child)s is not None:" + ' nodelist.append(("%(child)s", self.%(child)s))\n') % (
                    dict(child=child)
                )

            for seq_child in clean_seq_children:
                src += (
                    "        for i, child in enumerate(self.%(child)s or []):\n"
                    '            nodelist.append(("%(child)s[%%d]" %% i, child))\n'
                ) % (dict(child=seq_child))

            src += "        return tuple(nodelist)\n"
        else:
            src += "        return ()\n"

        return src

    def _gen_attr_names(self):
        """
        Generate the attributes code for the node class.

        Generated source example:
            attr_names = ('AxisPoints', )
        """
        clean_attributes = []
        for attribute in self.attributes:
            clean_attributes.append(attribute.strip("?"))
        src = "    attr_names = (" + ''.join(f"{nm!r}, " for nm in clean_attributes) + ')'
        return src

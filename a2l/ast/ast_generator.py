from string import Template
from sys import argv

import re

_FILE_COMMENT = \
r'''#-----------------------------------------------------------------
# *** IMPORTENT ***
# This code was generated from the config file:
# $cfg_filename
#
# If you wish to edit this code use the generator in the subfolder gen
# and adjust the config file, not the code itself!
# Don't edit this file manually!
# *** IMPORTENT ***
#
#
# Abstract Syntax Tree (AST) Node Classes.
#
#-----------------------------------------------------------------

'''


_FILE_CODE = \
r'''
import sys


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


'''

class ASTGenerator(object):
    def __init__(self,
                 cfg_filename,
                 out_filename):
        """
        Initialize Abstract Syntax Tree Code Generator from config file.
        """
        self.cfg_filename = cfg_filename
        self.out_filename = out_filename
        self.node_config = [NodeConfiguration(name, content)
            for (name, content) in self.parse_config()]


    def generate(self, cleanNames=False):
        """
        Generate AST Code.
        """
        file_buffer = open(self.out_filename, 'w')
        ast_code = Template(_FILE_COMMENT).substitute(cfg_filename=self.cfg_filename)

        ast_code += _FILE_CODE

        for node_config in self.node_config:
            ast_code = ast_code + node_config.generate_node_source(cleanNames) + '\n\n'

        file_buffer.write(ast_code)

    def parse_config(self):
        """
        Parse the configuration file.
        """
        with open(self.cfg_filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue    # comment
                colon_i = line.find(':')
                lParenthesis_i = line.find('(')
                rParenthesis_i = line.find(')')
                if colon_i < 1 or lParenthesis_i <= colon_i or rParenthesis_i <= lParenthesis_i:
                    raise RuntimeError("Invalid line in %s:\n%s\n" % (self.cfg_filename, line))

                name = line[:colon_i]
                val = line[lParenthesis_i + 1:rParenthesis_i]
                vallist = [v.strip() for v in val.split(',')] if val else []
                yield name, vallist



class NodeConfiguration(object):
    def __init__(self,
                 node_name,
                 content):
        """
        node_name: Name
        content: list of entries of a specific A2L Node
                 e.g. UpperLimit, ECU_Address etc.
        """

        self.node_name = node_name
        self.attributes = []
        self.children = []
        self.seq_children = []
        self.entries = []

        for entry in content:
            clean_entry = entry.strip('*')
            self.entries.append(clean_entry)

            if entry.endswith('**'):
                self.seq_children.append(clean_entry)
            elif entry.endswith('*'):
                self.children.append(clean_entry)
            else:
                self.attributes.append(entry)


    def generate_node_source(self, cleanNames):
        src = self._gen_base(cleanNames)
        src += '\n' + self._gen_children()
        src += '\n' + self._gen_attr_names()
        return src

    def _gen_base(self, cleanNames):
        if cleanNames:
            clean_name = self.node_name.lower()
            clean_name = clean_name[0].upper() + clean_name[1:]
            if '_' in clean_name:
                index = [i for i, ltr in enumerate(clean_name) if ltr == '_']
                indices = [i+1 for i in index] 
                clean_name = "".join(c.upper() if i in indices else c for i, c in enumerate(clean_name))

            self.node_name = clean_name

        src = "class %s(Node):\n" % self.node_name

        clean_entries = []
        if self.entries:
            arguments_list = '(self '
            for entry in self.entries:
                arguments_list += ', '
                if entry.startswith('?'):
                    clean_entry = entry.strip('?') + ' = None'
                    arguments_list += clean_entry
                else:
                    #clean_entry = entry
                    arguments_list += entry

            arguments_list += ' )'

            for entry in self.entries:
                clean_entries.append(entry.strip('?'))
                
            slots = ', '.join("'{0}'".format(e) for e in clean_entries)
            slots += ", '__weakref__'"

        else:
            slots = "'__weakref__'"
            arguments_list = '(self)'

        src += "    __slots__ = (%s)\n" % slots
        src += "    def __init__%s:\n" % arguments_list

        for name in clean_entries:
            src += "        self.%s = %s\n" % (name, name)

        return src

    def _gen_children(self):
        
        clean_children = []
        clean_seq_children = []
        for child in self.children:
            clean_children.append(child.strip('?'))
        
        for seq_child in self.seq_children:
            clean_seq_children.append(seq_child.strip('?'))
        
        src = '    def children(self):\n'

        if self.entries:
            src += '        nodelist = []\n'

            for child in clean_children:
                src += (
                    '        if self.%(child)s is not None:' +
                    ' nodelist.append(("%(child)s", self.%(child)s))\n') % (
                        dict(child=child))

            for seq_child in clean_seq_children:
                src += (
                    '        for i, child in enumerate(self.%(child)s or []):\n'
                    '            nodelist.append(("%(child)s[%%d]" %% i, child))\n') % (
                        dict(child=seq_child))

            src += '        return tuple(nodelist)\n'
        else:
            src += '        return ()\n'

        return src

    def _gen_attr_names(self):
        clean_attributes = []
        for attribute in self.attributes:
            clean_attributes.append(attribute.strip('?'))
        src = "    attr_names = (" + ''.join("%r, " % nm for nm in clean_attributes) + ')'
        return src
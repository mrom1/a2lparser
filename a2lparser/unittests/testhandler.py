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


import unittest
import xml.etree.ElementTree as et
from io import StringIO
from typing import Any
from xml.etree.ElementTree import Element
from a2lparser.a2l.converter.xml_converter import XMLConverter
from a2lparser.a2l.ast.abstract_syntax_tree import AbstractSyntaxTree


class Testhandler(unittest.TestCase):
    """
    TestCase classes that want to be parametrized should inherit from this class.
    """

    def __init__(self, methodName="runTest", param: Any = None):
        """
        Testhandler Constructor.

        Args:
            - methodName: Name of the method to be called.
            - param: Parameter to be passed.
        """
        super(Testhandler, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """
        Create a suite containing all tests taken from the given
        subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite

    def get_xml_tree_from_ast(self, abstract_syntax_tree: AbstractSyntaxTree) -> Element:
        """
        Retruns an XML tree from the abstract syntax tree.
        """
        if not hasattr(self.param, "parser"):
            return Element("")
        if not hasattr(self.param.parser, "config"):
            return Element("")

        buffer = StringIO()
        xml = XMLConverter(self.param.parser.config)
        xml.generate_xml(abstract_syntax_tree, buffer=buffer)
        content = buffer.getvalue()
        buffer.close()
        try:
            tree = et.fromstring(content)
            return tree
        except Exception as ex:
            raise RuntimeError() from ex

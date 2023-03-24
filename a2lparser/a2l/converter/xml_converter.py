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


import sys
from typing import TextIO
from lxml import etree as et
from lxml.etree import Element
from a2lparser.logger.logger import Logger
from a2lparser.a2l.abstract_syntax_tree import AbstractSyntaxTree


class XMLConverter:
    """
    Converter class for converting an A2L abstract syntax tree to an XML file.

    Usage:
        >>> with open(xmlFileName, 'w') as f:
        >>>     xml = XMLConverter(config=Config())
        >>>     xml.generate_xml(abstract_syntax_tree=AST, buffer=f)
    """

    def __init__(self, config, encoding="utf-8"):
        """
        XMLConverter Constructor.

        Args:
            - config: Config object.
            - encoding: The encoding to use for the XML file.
        """
        self.logger_manager = Logger()
        self.logger = self.logger_manager.new_module("XML")
        self.config = config
        self.encoding = encoding

    def generate_xml_file(self, abstract_syntax_tree: AbstractSyntaxTree, buffer: TextIO = sys.stdout) -> None:
        """
        Generates the XML file.

        Args:
            - abstract_syntax_tree: The parsed AbstractSyntaxTree object.
            - buffer: A TextIO buffer to write to.
        """

    def generate_xml(self, abstract_syntax_tree: AbstractSyntaxTree) -> Element:  # type: ignore
        """
        Generates an XML element containing the given abstract syntax tree.
        """
        # create the XML header
        xml_declaration = et.Element("xml", version="1.0", encoding="UTF-8")

        # create the root element
        root = et.Element("File") # type: ignore

        # create the XML document and add the header and root element to it
        xml_doc = et.ElementTree(root)
        xml_doc._setroot(root)
        xml_doc.addprevious(xml_declaration)

        return root

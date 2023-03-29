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
from a2lparser.a2l.ast.abstract_syntax_tree import AbstractSyntaxTree
import a2lparser.gen.a2l_ast as ASTNodes


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
        self.config = config
        self.encoding = encoding

        fn_dict = ASTNodes.__dict__
        self.ast_a2l_nodes = {
            i: v
            for i, v in fn_dict.items()
            if (i != "sys" and not i.startswith("_"))
            and not (i.endswith("_Opt") or i.endswith("_Opt_List") or i == "Abstract_Syntax_Tree" or i == "If_Data_Block_List")
        }
        self.ast_a2l_nodes_opt_only = {
            i: v
            for i, v in fn_dict.items()
            if (i != "sys" and not i.startswith("_"))
            and (i.endswith("_Opt") or i.endswith("_Opt_List"))
            or (i in ["Abstract_Syntax_Tree", "If_Data_Block_List"])
        }

        self.xml_types = ["Measurement", "Characteristic", "Compu_Method", "Compu_Tab"]
        self.xml_types_ref = ["Ref_Measurement", "Ref_Characteristic"]
        self.xml_ref_names = {
            "Measurement": "signalMeasurementId",
            "Characteristic": "characteristicId",
            "Compu_Method": "compuMethodId",
            "Compu_Tab": "compuTabId",
            "Ref_Measurement": "signalMeasurementId",
            "Ref_Characteristic": "characteristicId",
        }

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
        root = et.Element("File")  # type: ignore

        # create the XML document and add the header and root element to it
        xml_doc = et.ElementTree(root)
        xml_doc._setroot(root)
        xml_doc.addprevious(xml_declaration)

        return root

    def validate_abstract_syntax_tree(self, abstract_syntax_tree) -> bool:
        """
        Validates the given abstract syntax tree.
        """
        if hasattr(abstract_syntax_tree, "children"):
            children = abstract_syntax_tree.children()
            for _, child in children:
                if child.__class__.__name__ in self.ast_a2l_nodes:
                    return True
        return False

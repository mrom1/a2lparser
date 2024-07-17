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


import xmltodict
from loguru import logger
from a2lparser.converter.a2l_converter import A2LConverter


class XMLConverter(A2LConverter):
    """
    Converter class for converting an A2L abstract syntax tree to an XML file.

    Usage Example:
        >>> XMLConverter().convert(ast_dict, output_dir="./xml_files/")
    """

    class XMLConverterException(Exception):
        """
        Exception raised when an error occurs while converting an AST to a XML file.
        """

    def convert(
        self, ast: dict, output_dir: str = ".", output_filename: str = None, encoding: str = "utf-8", pretty: bool = True
    ) -> None:
        """
        Convert the given AST dictionary to XML and write it to a file.

        Args:
            ast (dict): The AST dictionary to be converted to XML.
            output_dir (str, optional): The directory to write the XML file.
            output_filename (str, optional): The filename of the XML file.
            encoding (str, optional): The encoding to be used for the XML file.
            pretty (bool, optional): Whether to format the XML file with indentation and newlines.
        """
        try:
            logger.info("Converting AST to XML and writing to file...")
            converted_tuples = self.convert_to_string(ast, output_filename, encoding, pretty)
            for tup in converted_tuples:
                filename, xml_string = tup
                self.write_to_file(content=xml_string, filename=filename, output_dir=output_dir)
                logger.success(f"Created XML file: {filename}")

        except Exception as e:
            raise self.XMLConverterException(e) from e

    def convert_to_string(self, ast: dict,
                          output_filename: str = None,
                          encoding: str = "utf-8",
                          pretty: bool = True) -> list:
        """
        Convert the given AST dictionary to a XML string.

        Args:
            ast (dict): The AST dictionary to be converted to XML.
            output_filename (str, optional): The filename to be used for the XML string.
            encoding (str, optional): The encoding to be used for the XML string (default is "utf-8").
            pretty (bool, optional): Whether to format the XML string with indentation and newlines (default is True).

        Returns:
            str: List of tuples (filename, xml_string).
        """
        try:
            result = []
            sliced_ast = self.slice_ast(ast, file_extension="xml", filename=output_filename)
            for tup in sliced_ast:
                filename, root = tup
                xml_string = xmltodict.unparse(root, encoding=encoding, pretty=pretty)
                result.append((filename, xml_string))
            return result
        except Exception as e:
            raise self.XMLConverterException(e) from e

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


import json
from loguru import logger
from a2lparser.converter.a2l_converter import A2LConverter


class JSONConverter(A2LConverter):
    """
    Converter class for converting an A2L abstract syntax tree to an JSON file.

    Usage Example:
        >>> JSONConverter().convert(ast_dict, output_dir="./json_files/")
    """

    class JSONConverterException(Exception):
        """
        Exception raised when an error occurs while converting an AST to a JSON file.
        """

    def convert(
        self, ast: dict, output_dir: str = ".", output_filename: str = None, pretty: bool = True
    ) -> None:
        """
        Convert the given AST dictionary to JSON and write it to a file.

        Args:
            ast (dict): The AST dictionary to be converted to JSON.
            output_dir (str, optional): The directory to write the JSON file.
            output_filename (str, optional): The filename of the JSON file.
            pretty (bool, optional): Whether to format the JSON file with indentation and newlines.
        """
        try:
            logger.info("Converting AST to JSON and writing to file...")
            converted_tuples = self.convert_to_string(ast, output_filename, pretty)
            for tup in converted_tuples:
                filename, json_string = tup
                self.write_to_file(content=json_string, filename=filename, output_dir=output_dir)
                logger.success(f"Created JSON file: {filename}")

        except Exception as e:
            raise self.JSONConverterException(e) from e

    def convert_to_string(
        self, ast: dict, output_filename: str = None, pretty: bool = True
    ) -> list:
        """
        Convert the given AST dictionary to a JSON string.

        Args:
            ast (dict): The AST dictionary to be converted to JSON.
            output_filename (str, optional): The filename to be used.
            pretty (bool, optional): Format the JSON string with indentation and newlines.

        Returns:
            list: List of tuples (filename, json_string).
        """
        try:
            result = []
            sliced_ast = self.slice_ast(ast, file_extension="json", filename=output_filename)
            for tup in sliced_ast:
                filename, root = tup
                json_string = json.dumps(root, indent=2) if pretty else json.dumps(root)
                result.append((filename, json_string))
            return result
        except Exception as e:
            raise self.JSONConverterException(e) from e

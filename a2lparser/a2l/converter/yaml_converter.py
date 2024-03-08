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


import yaml
from a2lparser.a2l.converter.a2l_converter import A2LConverter


class YAMLConverter(A2LConverter):
    """
    Converter class for converting an A2L abstract syntax tree to an YAML file.

    Usage Example:
        >>> YAMLConverter().convert(ast_dict, output_dir="./yaml_files/")
    """

    class YAMLConverterException(Exception):
        """
        Exception raised when an error occurs while converting an AST to a YAML file.
        """

    def convert(self, ast: dict,
                output_dir: str = ".",
                output_filename: str = None) -> None:
        """
        Convert the given AST dictionary to YAML and write it to a file.

        Args:
            ast (dict): The AST dictionary to be converted to YAML.
            output_dir (str, optional): The directory to write the YAML file.
            output_filename (str, optional): The filename of the YAML file.
        """
        try:
            converted_tuples = self.convert_to_string(ast, output_filename)
            for tup in converted_tuples:
                filename, yaml_string = tup
                self.write_to_file(content=yaml_string, filename=filename, output_dir=output_dir)
        except Exception as e:
            raise self.YAMLConverterException(e) from e

    def convert_to_string(self, ast: dict, output_filename: str = None) -> list:
        """
        Convert the given AST dictionary to a YAML string.

        Args:
            ast (dict): The AST dictionary to be converted to YAML.
            output_filename (str, optional): The filename to be used.

        Returns:
            str: List of tuples (filename, yaml_string).
        """
        try:
            result = []
            sliced_ast = self.slice_ast(ast, file_extension="yml", filename=output_filename)
            for tup in sliced_ast:
                filename, root = tup
                yaml_string = yaml.dump(root)
                result.append((filename, yaml_string))
            return result
        except Exception as e:
            raise self.YAMLConverterException(e) from e

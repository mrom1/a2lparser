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


import os
from a2lparser.a2l.lex.lexer_keywords import LexerKeywords
from a2lparser.a2l.ast.abstract_syntax_tree import AbstractSyntaxTree


class A2LConverter():
    """
    Base class for converting an A2L dictionary.
    """

    class A2LConverterException(Exception):
        """
        Raises if there is an error in the general conversion process.
        """

    def slice_ast(self, ast: dict, file_extension: str, filename: str = None) -> list:
        """
        Slices the given AST into a list of (filename, ast) tuples.
        Will add a root element to the AST dictionary.

        Args:
            ast (dict): The AST dictionary to be sliced.
            file_extension (str): The file extension to be used for the output files.
            filename (str, optional): The filename to be used for the output files. Defaults to None.

        Returns:
            list: A list of (filename, ast) tuples.
        """
        result = []
        try:
            if not self.is_ast_valid_structure(ast):
                # In this case the structure is not parsed from a file
                # If no filename is given, we raise an exception.
                if filename is None:
                    raise self.A2LConverterException(
                        "Could not find filename in AST. Pass filename argument to resolve this error.")
                root = self.add_root_element(ast)
                out_filename = f"{filename}.{file_extension}"
                result.append((out_filename, root))
            else:
                # In this case the structure is parsed from a file
                # The AST either contains a single file or multiple files.
                for index, (input_filename, a2l_ast) in enumerate(ast.items(), start=1):
                    root = self.add_root_element(a2l_ast)
                    if filename is not None:
                        out_filename = f"filename_{index}.{file_extension}"
                    else:
                        out_filename = f"{self.remove_file_extension(input_filename)}.{file_extension}"
                    result.append((out_filename, root))
        except Exception as e:
            raise self.A2LConverterException(
                f"Conversion Error while slicing AST: {e}"
            ) from e
        return result

    def write_to_file(self, content: str, filename: str, output_dir: str = ".") -> None:
        """
        Writes the converted content to a file.

        Args:
            filename (str): The filename to be written.
            content (str): The content to be written.
            output_dir (str, optional): The output directory. Defaults to ".".
        """
        if output_dir is None:
            output_dir = "."
        else:
            output_dir = output_dir.replace("\"", "").replace("'", "")
        full_output_dir = os.path.abspath(output_dir)

        if not os.path.isdir(full_output_dir):
            raise self.A2LConverterException(
                f"Unable to write to output directory: '{full_output_dir}'. The directory does not exist."
            )

        full_path = os.path.join(full_output_dir, filename)

        try:
            with open(full_path, 'w', encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            raise self.A2LConverterException(
                f"Error writing to file '{filename}': {e}"
            ) from e

    def is_ast_valid_structure(self, ast: dict) -> bool:
        """
        Validates the structure of the AST.
        Expected valid structure is a filename key, with an AST dict value.

        Example:
            ast = {
                "filename.a2l": {
                    ...
                },
                "filename_2.aml": {
                    ...
                }
            }
        """
        if not isinstance(ast, dict):
            raise self.A2LConverterException("The given AST is not a dictionary.")

        # We accept all key values which are not exact A2L keyword matches
        # and have a dictionary object as their value
        return all(
            key.upper() not in LexerKeywords.keywords_section + LexerKeywords.keywords_type
            for key in ast
        )

    def add_root_element(self, ast: dict, element_name: str = "A2L-File") -> dict:
        """
        Adding a root element to the AST dictionary.

        Args:
            ast (dict): The AST dictionary to be converted to XML.
            element_name (str, optional): The name of the root element. Defaults to "A2L-File".

        Returns:
            dict: The AST dictionary with the root element added.
        """
        if isinstance(ast, AbstractSyntaxTree):
            ast = ast.get_dict()
        return {element_name: ast}

    def remove_file_extension(self, filename: str) -> str:
        """
        Removes the file extension from the filename, and returns the filename.

        Args:
            filename (str): The filename to be processed.

        Returns:
            str: The filename without the file extension.
        """
        base, _ = os.path.splitext(filename)
        return base

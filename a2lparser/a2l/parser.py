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


import glob
from typing import List, Union
from a2lparser.a2l.a2l_yacc import A2LYacc
from a2lparser.a2l.parsing_exception import ParsingException
from a2lparser.a2l.ast.abstract_syntax_tree import AbstractSyntaxTree


class Parser:
    """
    Parser class for parsing A2L content.

    Usage:
        >>> try:
        >>>     parser = Parser()
        >>>     ast = parser.parse_content(content=a2l_content)
        >>>     ast = parser.parse_files(files="./data/*.a2l")
        >>> except ParsingException as ex:
        >>>     print(ex)
    """

    def __init__(self, debug: bool = False, optimize: bool = True):
        """
        Parser Constructor.

        Args:
            - debug: Will print detailed parsing debug information.
            - optimize: Will optimize the lex and yacc parsing process.
        """
        self.parser = A2LYacc(debug=debug, optimize=optimize)

    def parse_content(self, content: str) -> AbstractSyntaxTree:
        """
        Parses the given content string and returns an AbstractSyntaxTree object.
        """
        return self.parser.generate_ast(content)

    def parse_files(self, files: str) -> dict:
        """
        Parses the given files.
        Returns a dictionary of the AbstractSyntaxTree with the file name as a key.
        """
        ast_objects = {}
        for a2l_file in glob.glob(files):
            with open(a2l_file, "r", encoding="utf-8") as file:
                ast_objects[a2l_file] = self.parse_content(content=file.read())

        if len(ast_objects) == 0:
            raise ParsingException(f"None of the given files could be parsed: files = '{files}'")

        return ast_objects

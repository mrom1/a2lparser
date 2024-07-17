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
import re
import sys
import glob
from pathlib import Path
from loguru import logger
from a2lparser.a2l.a2l_yacc import A2LYacc
from a2lparser.a2l.a2l_validator import A2LValidator
from a2lparser.a2lparser_exception import A2LParserException
from a2lparser.a2l.ast.abstract_syntax_tree import AbstractSyntaxTree


class A2LParser:
    """
    Parser class for parsing A2L content.

    Usage:
        >>> try:
        >>>     parser = Parser()
        >>>     ast = parser.parse_file(files="./data/*.a2l")
        >>> except ParsingException as ex:
        >>>     print(ex)
    """

    def __init__(self, validation: bool = True, optimize: bool = True, log_level: str = "INFO", quiet: bool = False) -> None:
        """
        Parser Constructor.

        Args:
            validation: Will validate the A2L content before parsing.
            optimize: Will optimize the lex and yacc parsing process.
            log_level: The log level of the console output.
            quiet: Will not log anything to the console.
        """
        self.validation = validation
        self.quiet_mode = quiet
        self.show_progressbar = log_level in {"DEBUG", "INFO"} and not quiet
        self.parser = A2LYacc(optimize=optimize)
        self._include_pattern = re.compile(
            r"""
            /include    # matches literal string "/include"
            \s+         # matches one or more whitespaces
            (           # start of the capturing group for the filename
            [^\s"']+    # matches any character that is not whitespace or a quotation mark
            |           # OR
            "[^"]*"     # matches a quoted string (double quotes) capturing the content inside the quotes
            |           # OR
            '[^']*'     # matches a quoted string (single quotes) capturing the content inside the quotes
            )           # end of the capturing group
        """,
            re.IGNORECASE | re.VERBOSE,
        )
        # Set loguru logger format and level
        logger.remove()
        if not quiet:
            logger.add(
                sink=sys.stdout,
                format="[{time:HH:mm:ss}] <lvl>[{level}]</lvl> <lvl>{message}</lvl>",
                level=log_level,
            )

    def parse_file(self, files: str) -> dict:
        """
        Parses the given files.
        Returns a dictionary of AbstractSyntaxTree objects with the file name as a key pair.
        """
        ast_objects = {}

        # Glob A2L input files
        a2l_files = glob.glob(files)
        if not a2l_files:
            raise A2LParserException(f'Unable to find any A2L files matching: "{files}"')

        for a2l_file in a2l_files:
            try:
                # Load content from file into memory
                logger.info("Parsing file: {}", a2l_file)
                a2l_content = self._load_file(filename=a2l_file)

                # Validate the content read
                if self.validation:
                    try:
                        A2LValidator().validate(a2l_content)
                    except A2LValidator.A2LValidationError as e:
                        logger.warning(f'Validation of file "{a2l_file}" failed!\n{e}')

                # Parse the content
                filename = os.path.basename(a2l_file)
                ast_objects[filename] = self._parse_content(content=a2l_content, show_progressbar=self.show_progressbar)
                logger.success("Created Abstract Syntax Tree from file: {}", filename)

            except A2LParserException as e:
                logger.error(f'Unable to parse file "{a2l_file}": {e}')

        return ast_objects

    def _parse_content(self, content: str, show_progressbar: bool = True) -> AbstractSyntaxTree:
        """
        Parses the given content string and returns an AbstractSyntaxTree object.
        """
        logger.debug("Starting AST generation...")
        return self.parser.generate_ast(content, show_progressbar)

    def _load_file(self, filename: str, current_dir: str = None) -> str:
        """
        Reads the content of the given filename and returns it with includes replaced recursively.

        Args:
            filename (str): The filename of the A2L file to be read.

        Returns:
            str: The complete A2L file with the included content.
        """
        a2l_file = Path(filename)
        if current_dir is None:
            current_dir = a2l_file.parent
            file_path = current_dir / a2l_file.name
        else:
            file_path = current_dir / a2l_file
        file_path = file_path.resolve()
        current_dir = file_path.parent

        encodings = ["utf-8", "utf-16", "utf-32"]
        for encoding in encodings:
            try:
                with open(file_path, "r", encoding=encoding) as file:
                    content = file.read()
                    break
            except UnicodeError:
                content = None

        if content is None:
            with open(file_path, "r", encoding="latin-1") as file:
                content = file.read()

        if includes := self._find_includes(content):
            if isinstance(includes, list):
                for include in includes:
                    included_content = self._load_file(include, current_dir)
                    content = self._include_pattern.sub(included_content, content, count=1)
            else:
                included_content = self._load_file(includes, current_dir)
                content = self._include_pattern.sub(included_content, content)
        return content

    def _find_includes(self, content: str) -> str | list | None:
        """
        Looks for /include {file.a2l} tags inside given content and returns the full filename.

        Args:
            content (str): The content of the A2L file.

        Returns:
            str | list | None: The filenames to be included if found.
        """
        try:
            matches = self._include_pattern.findall(content)
            if len(matches) == 1:
                return matches[0].strip("\"'")
            if len(matches) > 1:
                return [match.strip("\"'") for match in matches]
        except Exception as e:
            raise A2LParserException(e) from e

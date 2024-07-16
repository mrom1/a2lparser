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


import re


class A2LValidator:
    """
    A2LValidator class inspects the A2L input for syntax errors.
    Will raise an A2LValidationError exception if the input is invalid.

    Usage:
        >>> try:
        >>>     A2LValidator().validate("/begin MEASUREMENT /end")
        >>> expect A2LValidator.A2LValidationError as ex:
        >>>     print(e)
    """

    class A2LValidationError(Exception):
        """
        This exception occurs if a syntax error is encountered in validating a A2L string.
        """

        def __init__(self, errors):
            self.errors = errors

        def __str__(self):
            error_messages = "\n".join([f"{i+1}: {error}" for i, error in enumerate(self.errors)])
            return f"A2L validation failed with the following errors:\n{error_messages}"

    def __init__(self):
        self.section_pattern = re.compile(
            r"""
            /(?:begin|end)\s+(\w+)  # Match /begin or /end followed by a keyword
        """,
            re.VERBOSE | re.IGNORECASE,
        )

    def validate(self, a2l_content: str) -> None:
        """
        Validates the syntax of the A2L content.

        Args:
            a2l_content: A string containing the A2L content.

        Raises:
            A2LValidationError: Raises if the content fails the syntax validation.
        """
        errors = []
        sections_stack = []
        for i, line in enumerate(a2l_content.splitlines(), start=1):
            line = self._remove_comments(line)
            for match in self.section_pattern.finditer(line):
                section = match.group(1)
                if match.group().lower().startswith("/begin"):
                    sections_stack.append((i, section))
                elif match.group().lower().startswith("/end"):
                    _, last_section = sections_stack[-1]
                    if last_section != section:
                        errors.append(f"Detected unexpected end of section on '{line.lstrip()}' at line {i}.")
                    else:
                        sections_stack.pop()

        for open_section in reversed(sections_stack):
            i, section = open_section
            errors.append(f"Detected unclosed section '{section}' starting at line {i}.")
        if errors:
            raise self.A2LValidationError(errors)

    def _remove_comments(self, line: str) -> str:
        result = []
        i = 0
        length = len(line)
        skip_tokens = False
        string_literal_started = False

        while i < length:
            # If inside a comment block, skip characters until the end of the block
            if skip_tokens:
                if line[i:i+2] == '*/':
                    skip_tokens = False
                    i += 2
                    continue
                i += 1
            # Detect the start of a multiline comment
            elif line[i:i+2] == '/*' and not string_literal_started:
                skip_tokens = True
                i += 2
            # Detect the start of a single line comment
            elif line[i:i+2] == '//' and not string_literal_started:
                break
            # Handle string literals properly
            elif line[i] in {'"', "'"}:
                quote_char = line[i]
                result.append(line[i])
                i += 1
                string_literal_started = not string_literal_started
                while i < length and (line[i] != quote_char or (line[i] == quote_char and line[i-1] == '\\')):
                    result.append(line[i])
                    i += 1
                if i < length:
                    result.append(line[i])
                string_literal_started = not string_literal_started
                i += 1
            # Append non-comment characters to result
            else:
                result.append(line[i])
                i += 1

        return ''.join(result)

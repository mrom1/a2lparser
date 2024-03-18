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
        self.skip_tokens = False
        self.accept_tokens = False
        self.string_literal_started = False
        self.section_pattern = re.compile(r"""
            /(?:begin|end)\s+(\w+)  # Match /begin or /end followed by a keyword
        """, re.VERBOSE | re.IGNORECASE)

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
                if match.group().lower().startswith('/begin'):
                    sections_stack.append((i, section))
                elif match.group().lower().startswith('/end'):
                    last_line, last_section = sections_stack[-1]
                    if last_section != section:
                        errors.append(
                            f"Invalid \"/end {section}\" found at line {i}. "
                            f"Last found section {last_section} at line {last_line}."
                        )
                    else:
                        sections_stack.pop()

        for open_section in sections_stack:
            i, section = open_section
            errors.append(f"Found \"/begin {section}\" tag without matching /end tag at line {i}.")
        if errors:
            raise self.A2LValidationError(errors)

    def _remove_comments(self, line: str) -> str:
        # Initialize list to store processed words
        words = []

        # Iterate through each word in the line
        for word in line.split():
            # Check if the word starts a string literal and is not part of a comment.
            if (word.startswith('"') or word.startswith("'")) and not self.skip_tokens:
                # Mark beginning or end of the string literal
                self.string_literal_started = not self.string_literal_started

                # Inside a string literal we accept all incoming tokens
                # So if it's the start of a string literal we accept even comment tags like "//" or "/*", "*/".
                self.accept_tokens = self.string_literal_started

                # Add last word to the list
                if not self.accept_tokens:
                    words.append(word)
                    continue

            if self.accept_tokens:
                words.append(word)
                continue

            # Check if the word is a comment
            if "/*" in word:
                if (comment := word.split("/*", 1)) and comment[0]:
                    words.append(comment[0])
                self.skip_tokens = True
            elif "*/" in word:
                if (comment := word.split("*/", 1)) and comment[1]:
                    words.append(comment[1])
                self.skip_tokens = False
            elif "//" in word:
                if (comment := word.split("//", 1)) and comment[0]:
                    words.append(comment[0])
                break
            else:
                if not self.skip_tokens:
                    words.append(word)

        return " ".join(words)

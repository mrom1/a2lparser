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
# @TODO Ignore lines that start with a comment


import re


class A2LValidator:
    """
    A2LValidator class inspects the A2L input for syntax errors.
    Will raise an A2LValidationError exception if the input is invalid.

    Usage:
        >>> try:
        >>>     A2LValidator.validate("/begin MEASUREMENT /end")
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

    @staticmethod
    def validate(a2l_content: str) -> None:
        """
        Validates the syntax of the A2L content.

        Args:
            - a2l_content: A string containing the A2L content.

        Raises:
            - A2LValidationError: Raises if the content fails the syntax validation.
        """
        errors = []
        lines = a2l_content.splitlines()
        re_pattern = r"/\s*(begin|BEGIN)|/\s*(end|END)"
        open_stack = []
        open_keyword_stack = []

        # Check for missing opening/closing statements
        for i, line in enumerate(lines, 1):
            for match in re.finditer(re_pattern, line):
                tag = match.group().lower().strip()
                if tag == "/begin":
                    if keyword_match := re.search(
                        r"^\s*/begin\s+(\S+)", line, re.IGNORECASE
                    ):
                        keyword = keyword_match[1].lower()
                        open_stack.append((i, match.start()))
                        open_keyword_stack.append(keyword)
                    else:
                        errors.append(f"Invalid /begin tag at line {i}, column {match.start()+1}.")
                elif tag == "/end":
                    if not open_stack:
                        errors.append(f"Found /end tag without matching /begin tag at line {i}, column {match.start()+1}.")
                    else:
                        _, start = open_stack.pop()
                        open_keyword = open_keyword_stack.pop()
                        if end_keyword_match := re.search(
                            r"^\s*/end\s+(\S+)", line, re.IGNORECASE
                        ):
                            end_keyword = end_keyword_match[1].lower()
                            if end_keyword != open_keyword:
                                errors.append(
                                    f"Found /end {end_keyword} tag without matching /begin {open_keyword} "
                                    f"tag at line {i}, column {match.start()+1}."
                                )
                        else:
                            errors.append(f"Invalid /end tag at line {i}, column {match.start()+1}.")
        if open_stack:
            i, start = open_stack.pop()
            open_keyword = open_keyword_stack.pop()
            errors.append(f"Found /begin {open_keyword} tag without matching /end tag at line {i}, column {start+1}.")

        # Check for invalid characters
        for i, line in enumerate(lines, 1):
            if match := re.search(r"[^\x20-\x7E]", line):
                errors.append(f"Invalid character '{match.group()}' found at line {i}, column {match.start()+1}.")

        if errors:
            raise A2LValidator.A2LValidationError(errors)

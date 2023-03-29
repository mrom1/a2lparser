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


import readline
from a2lparser import A2L_PARSER_HEADLINE


class CommandPrompt:
    """
    CommandPrompt class which lets the user evaluate any input.
    Used to access the generated AST dictionary.

    Usage:
        >>> parser = Parser()
        >>> ast = parser.parse_content(a2l_content)
        >>> CommandPrompt.prompt(ast)
    """

    @staticmethod
    def prompt(ast):
        """
        Prompts the user for input..
        """
        print(A2L_PARSER_HEADLINE)
        print("You can access the 'ast' attribute which holds the abstract syntax tree as a reference.\n")
        while True:
            user_input = input(">>> ")
            if user_input == "exit":
                break
            else:
                try:
                    result = eval(user_input, {}, {"ast": ast})
                    if result:
                        print(result)
                except Exception as ex:
                    print(str(ex))
            readline.add_history(user_input)

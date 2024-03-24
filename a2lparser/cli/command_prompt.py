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


import code
from pathlib import Path
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from a2lparser import A2L_PACKAGE_DIR
from a2lparser import A2L_PARSER_HEADLINE


class CommandPrompt:
    """
    CommandPrompt class which lets the user evaluate any input.
    Used to access the generated AST dictionary.

    Usage:
        >>> parser = Parser()
        >>> ast = parser.parse_files("ECU_Example.a2l")
        >>> CommandPrompt.prompt(ast)
    """
    _session = None

    @staticmethod
    def get_session():
        """
        Returns the prompt session.
        """
        if CommandPrompt._session is None:
            history_file: Path = A2L_PACKAGE_DIR / "logs" / "a2lparser_history"
            CommandPrompt._session = PromptSession(history=FileHistory(history_file), auto_suggest=AutoSuggestFromHistory())
        return CommandPrompt._session

    @staticmethod
    def cli_readfunc(prompt):
        """
        Read function returning the session from prompt-toolkit.
        """
        return CommandPrompt.get_session().prompt(prompt)

    @staticmethod
    def prompt(ast):
        """
        Prompts the user for input..
        """
        local_vars = {"ast": ast}

        print(A2L_PARSER_HEADLINE)
        print("You can access the 'ast' attribute which holds the abstract syntax tree as a reference.\n")

        while True:
            try:
                code.interact(banner="", local=local_vars, readfunc=CommandPrompt.cli_readfunc)
                break
            except KeyboardInterrupt:
                continue

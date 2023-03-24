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


from pathlib import Path
from a2lparser.a2l.ast.ast_generator import ASTGenerator
from a2lparser.a2l.config.config_exception import ConfigException


class ConfigBuilder:
    """
    ConfiguBuilder utility to intialize a configuration used py the A2LParser.
    """

    GENERATED_AST_PYTHON_FILE = Path(__file__).parent / ".." / "ast" / "a2l_ast.py"

    @staticmethod
    def build_config(
        config_file: str, output_file: str = GENERATED_AST_PYTHON_FILE.as_posix(), use_clean_names: bool = True
    ) -> None:
        """
        Builds the AST node classes.

        Args:
            - config_file: The A2L configuration file containing the ASAM A2L specification.
            - output_file: The python file that will contain the generated AST nodes.
        """
        try:
            generator = ASTGenerator(config_file, output_file)
            generator.generate(use_clean_names)
        except Exception as ex:
            raise ConfigException(ex) from ex

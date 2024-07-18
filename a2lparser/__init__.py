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


#################################
# A2LParser package information #
#################################
from pathlib import Path

__package_name__ = "a2lparser"
__version__ = "0.1.1"
__author__ = "mrom1"
__author_email__ = "mrom@linuxmail.org"
__description__ = "ASAP2 A2L file parsing tool."
__license__ = "GNU General Public License v3 (GPLv3)"
__url__ = "https://github.com/mrom1/a2lparser"

A2L_PARSER_HEADLINE = """
 ████╗ ██████╗██╗      ██████╗ ████╗ █████╗ ██████╗██████╗█████╗
██╔═██╗╚═══██║██║      ██╔═██║██╔═██╗██╔═██╗██╔═══╝██╔═══╝██╔═██╗
██████║██████║██║      ██████║██████║█████╔╝██████╗█████╗ █████╔╝
██╔═██║██╔═══╝██║      ██╔═══╝██╔═██║██╔═██╗╚═══██║██╔══╝ ██╔═██╗
██║ ██║██████╗██████╗  ██║    ██║ ██║██║ ██║██████║██████╗██║ ██║
╚═╝ ╚═╝╚═════╝╚═════╝  ╚═╝    ╚═╝ ╚═╝╚═╝ ╚═╝╚═════╝╚═════╝╚═╝ ╚═╝
"""
A2L_PACKAGE_DIR = Path(__file__).parent
A2L_GENERATED_FILES_DIR = A2L_PACKAGE_DIR / "gen"
A2L_CONFIGS_DIR = A2L_PACKAGE_DIR / "configs"
A2L_CLI_HISTORY_FILE = A2L_PACKAGE_DIR / "logs" / "a2lparser_history"
A2L_DEFAULT_CONFIG_NAME = "ASAP2_MCD_v171.cfg"


#############################
# First time initialization #
#############################
try:
    # We try to import the AST node classes
    # If they can't be found it indicates a first time usage
    from a2lparser.gen.a2l_ast import Node

    Node()

except ImportError:
    print("No AST node classes found.  Generating AST nodes...")
    from a2lparser.a2l.ast.ast_generator import ASTGenerator

    # Generate the AST nodes from the standard config in configs/A2L_ASAM.cfg
    asam_config = A2L_CONFIGS_DIR / A2L_DEFAULT_CONFIG_NAME
    ast_nodes_file = A2L_GENERATED_FILES_DIR / "a2l_ast.py"

    # Generate the AST node containers
    generator = ASTGenerator(asam_config.as_posix(), ast_nodes_file.as_posix())
    generator.generate()
    print(f"Generated AST nodes file at:  {ast_nodes_file.as_posix()}")

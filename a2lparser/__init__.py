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


#############################
# First time initialization #
#############################
try:
    # We try to import the AST node classes
    # If they can't be found it indicates a first time usage
    from a2lparser.a2l.ast.a2l_ast import Node

    Node()
except ImportError:
    try:
        print("First time initialization...")
        from pathlib import Path
        from a2lparser.a2l.config.config_builder import ConfigBuilder

        # Generate the AST nodes from the standard config in configs/A2L_ASAM.cfg
        asam_config = Path(__file__).parent / "configs" / "A2L_ASAM.cfg"
        # Generate the AST node containers
        print("Generating python file containing the AST nodes...")
        ConfigBuilder.build_config(config_file=asam_config.as_posix())
    except Exception as ex:
        print(f"Unable to generate AST node containers: {ex}")


#################################
# A2LParser package information #
#################################
__package_name__ = "a2lparser"
__version__ = "0.0.1"
__author__ = "mrom1"
__author_email__ = "mrom@linuxmail.org"
__description__ = "A2L file parsing tool and XML converter."
__license__ = "GPLv3"
__url__ = "https://github.com/mrom1/a2lparser"

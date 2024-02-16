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
import sys
import argparse
from loguru import logger
from a2lparser import __version__
from a2lparser import A2L_PARSER_HEADLINE
from a2lparser import A2L_CONFIGS_DIR
from a2lparser import A2L_DEFAULT_CONFIG_NAME
from a2lparser import A2L_GENERATED_FILES_DIR
from a2lparser.a2l.parser import Parser
from a2lparser.cli.command_prompt import CommandPrompt
from a2lparser.a2l.ast.ast_generator import ASTGenerator
from a2lparser.a2l.parsing_exception import ParsingException


@logger.catch
def main() -> None:
    """
    Main function of the a2lparser.

    Usage through installation with pip:
    $ a2lparser --help

    Usage from root project dir:
    $ python -m a2lparser.a2lparser --help

    Documentation at: https://github.com/mrom1/a2lparser
    """
    try:
        args = parse_arguments(sys.argv[1:])

        # Set the logger
        logger.remove()
        if args.debug:
            logger.add(
                sink=sys.stderr,
                format="[{time:HH:mm:ss}] <lvl>{message}</lvl>",
                level="DEBUG",
            )
        else:
            logger.add(
                sink=sys.stderr,
                format="[{time:HH:mm:ss}] <lvl>{message}</lvl>",
                level="INFO",
            )

        # Generates the AST node classes for the A2L objects using the ASTGenerator
        if args.gen_ast:
            print("Generating python file containing the AST nodes...")
            if args.gen_ast == A2L_DEFAULT_CONFIG_NAME:
                config_file = A2L_CONFIGS_DIR / A2L_DEFAULT_CONFIG_NAME
            elif os.path.isfile(args.gen_ast):
                config_file = args.gen_ast
            else:
                print(f"Given config file {args.gen_ast} not found.  Aborting AST generation.")
                sys.exit(1)
            print("Generating AST nodes from config at: ", config_file.as_posix())
            generated_file = A2L_GENERATED_FILES_DIR / "a2l_ast.py"
            generator = ASTGenerator(config_file.as_posix(), generated_file.as_posix())
            generator.generate()
            print(f"Generated {generated_file.as_posix()}")
            sys.exit(0)

        # Provide a file or a collection of A2L-files to parse.
        if args.filename is None:
            print()
            print(A2L_PARSER_HEADLINE)
            print("\nPlease specify a A2L file.")
            print("For more information use the -h or --help flag.")
            sys.exit(1)

        # Initializing the A2L Parser
        parser = Parser(debug=args.debug, optimize=args.optimize)
        ast = parser.parse_files(args.filename)

        if args.xml:
            raise NotImplementedError("A2L to XML converter not implemented yet.")

        CommandPrompt.prompt(ast)

    except ParsingException as ex:
        logger.error(ex)


def parse_arguments(args: list) -> argparse.Namespace:
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(prog="a2lparser")
    parser.add_argument("filename", nargs="?", help="relative path to the full filename")
    parser.add_argument("-d", "--debug", action="store_true", default=False, help="enable debug output on stderr")
    parser.add_argument("-o", "--optimize", action="store_true", default=False, help="enables optimize mode")
    parser.add_argument("-x", "--xml", action="store_true", help="XML output file")
    parser.add_argument("--gen-ast", nargs="?", const=A2L_DEFAULT_CONFIG_NAME,
                        help="generates python file containing AST node classes")
    parser.add_argument("--version", action="version", version=f"a2lparser version: {__version__}")
    return parser.parse_args(args)


if __name__ == "__main__":
    main()

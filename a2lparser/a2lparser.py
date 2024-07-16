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
from a2lparser import A2L_CONFIGS_DIR
from a2lparser import A2L_PARSER_HEADLINE
from a2lparser import A2L_DEFAULT_CONFIG_NAME
from a2lparser import A2L_GENERATED_FILES_DIR
from a2lparser.a2l.parser import Parser
from a2lparser.cli.command_prompt import CommandPrompt
from a2lparser.a2l.ast.ast_generator import ASTGenerator
from a2lparser.converter.xml_converter import XMLConverter
from a2lparser.converter.json_converter import JSONConverter
from a2lparser.converter.yaml_converter import YAMLConverter


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
        logger.add(
            sink=sys.stdout,
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
        if args.file is None:
            print()
            print(A2L_PARSER_HEADLINE)
            print("\nPlease specify a A2L file.")
            print("For more information use the -h or --help flag.")
            sys.exit(1)

        # Initializing the A2L Parser
        parser = Parser(optimize=not args.no_optimize, validation=not args.no_validation)

        # Parse input files into abstract syntax tree
        ast = parser.parse_files(args.file)
        if not ast:
            logger.error("Unable to parse any of the given files! Aborting now...")
            sys.exit(1)

        if args.xml:
            try:
                XMLConverter().convert(ast, output_dir=args.output_dir)
            except XMLConverter.XMLConverterException as ex:
                logger.error(f"XML Conversion error: {ex}")
        if args.json:
            try:
                JSONConverter().convert(ast, output_dir=args.output_dir)
            except JSONConverter.JSONConverterException as ex:
                logger.error(f"JSON Conversion error: {ex}")
        if args.yaml:
            try:
                YAMLConverter().convert(ast, output_dir=args.output_dir)
            except YAMLConverter.YAMLConverterException as ex:
                logger.error(f"YAML Conversion error: {ex}")

        if not args.no_prompt:
            CommandPrompt.prompt(ast)

    except Exception as ex:
        logger.error(ex)


def parse_arguments(args: list) -> argparse.Namespace:
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(prog="a2lparser")
    parser.add_argument("file", nargs="?", help="A2L files to parse")
    parser.add_argument("-x", "--xml", action="store_true", help="Converts an A2L file to a XML output file")
    parser.add_argument("-j", "--json", action="store_true", help="Converts an A2L file to a JSON output file")
    parser.add_argument("-y", "--yaml", action="store_true", help="Converts an A2L file to a YAML output file")
    parser.add_argument("--no-prompt", action="store_true", default=False, help="Disables CLI prompt after parsing")
    parser.add_argument("--no-optimize", action="store_true", default=False, help="Disables optimization mode")
    parser.add_argument("--no-validation", action="store_true", default=False, help="Disables possible A2L validation warnings")
    parser.add_argument("--output-dir", nargs="?", default=None, metavar="PATH", help="Output directory for converted files")
    parser.add_argument("--gen-ast", nargs="?", metavar="CONFIG", const=A2L_DEFAULT_CONFIG_NAME,
                        help="Generates python file containing AST node classes")
    parser.add_argument("--version", action="version", version=f"a2lparser version: {__version__}")
    return parser.parse_args(args)


if __name__ == "__main__":
    main()

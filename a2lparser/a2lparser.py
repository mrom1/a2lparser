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


import sys
import argparse
from pathlib import Path
from a2lparser import __version__  # Make sure to trigger __init__.py imports
from a2lparser.a2l.parser import Parser
from a2lparser.a2l.config.config import Config
from a2lparser.a2l.config.config_builder import ConfigBuilder
from a2lparser.a2l.config.config_exception import ConfigException
from a2lparser.unittests.testsuite import Testsuite


_A2LPARSER_DESCRIPTION = """\n
* * * * * * * * * * * * *\n
*    A2L File Parser    *\n
* * * * * * * * * * * * *\n
"""


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

        # Generates the AST node classes for the A2L objects using the ASTGenerator
        if args.gen_ast:
            print("Generating python file containing the AST nodes...")
            generated_file = Path(__file__).parent / "a2l" / "ast" / "a2l_ast.py"
            ConfigBuilder.build_config(config_file=args.gen_ast, output_file=generated_file.as_posix())
            print(f"Generated {generated_file.as_posix()}")
            sys.exit(0)

        # Either trigger a run through A2L unit tests or provide a file to work with
        if args.filename is None and args.unittests is False:
            print(_A2LPARSER_DESCRIPTION)
            print("\nPlease specifiy a A2L file.")
            print("For more information use the -h or --help flag.")
            sys.exit(2)

        # Set config values
        if args.o2 is True:
            _optimize = 1
            _gen_tables = False
        elif args.o1 is True:
            _optimize = 1
            _gen_tables = True
        else:
            _optimize = 0
            _gen_tables = True

        if args.unittests:
            _verbosity = 0
            _optimize = 0
            _gen_tables = True
        else:
            _verbosity = 2

        # Initialize the config
        cfg = Config(debug=args.debug, optimize=_optimize, write_tables=_gen_tables, verbosity=_verbosity)
        parser = Parser(config=cfg)

        if args.unittests:
            Testsuite(parser)
        else:
            parser.parseFile(fileName=args.filename)
    except ConfigException as ex:
        print(ex)


def parse_arguments(args: list) -> argparse.Namespace:
    """
    Parse the command line arguments.
    """
    parser = argparse.ArgumentParser(prog="a2lparser", description=_A2LPARSER_DESCRIPTION)
    parser.add_argument("filename", nargs="?", help="relativ path to the full filename")
    parser.add_argument("-d", "--debug", action="store_true", help="enable debug output on stderr")
    parser.add_argument("-x", "--xml", action="store_true", help="XML output file")
    parser.add_argument("-o1", action="store_true", help="initial generated table")
    parser.add_argument("-o2", action="store_true", help="will not generate a table")
    parser.add_argument("--unittests", action="store_true", help="start all testcases")
    parser.add_argument("--gen-ast", nargs="?", help="input ASAM config to generate AST nodes")
    parser.add_argument("--version", action="version", version=f"a2lparser version: {__version__}")

    return parser.parse_args(args)


if __name__ == "__main__":
    main()

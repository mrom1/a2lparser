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
from argparse import RawTextHelpFormatter
from a2lparser import __version__
from a2lparser.a2l.parser import Parser
from a2lparser.a2l.config.config import Config
from a2lparser.a2l.config.config_builder import ConfigBuilder
from a2lparser.unittests.testsuite import Testsuite


_A2LPARSER_DESCRIPTION = """\n
* * * * * * * * * * * * *\n
*    A2L File Parser    *\n
* * * * * * * * * * * * *\n
"""


def main():
    argparser = argparse.ArgumentParser(description=_A2LPARSER_DESCRIPTION, formatter_class=RawTextHelpFormatter)
    argparser.add_argument("filename", nargs="?", help="relativ path to the full filename")
    argparser.add_argument("-d", "--debug", action="store_true", help="enable debug output on stderr")
    argparser.add_argument("-t", "--test", action="store_true", help="test the given file")
    argparser.add_argument("-x", "--xml", action="store_true", help="XML output file")
    argparser.add_argument("-o1", action="store_true", help="initial generated table")
    argparser.add_argument("-o2", action="store_true", help="don't generate a table")
    argparser.add_argument("--testcases", action="store_true", help="start all testcases")
    argparser.add_argument("--error-resolve", action="store_true", help="use error resolve function")
    argparser.add_argument("--gen-ast", nargs="?", help="generate ast file")
    argparser.add_argument("--gen-rules", action="store_true", help="generate a2l yacc rules file")
    argparser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"a2lparser version: {__version__}",
        help="show version of the a2lparser package.",
    )
    args = argparser.parse_args()

    if args.gen_ast:
        ConfigBuilder(config=args.gen_ast, output_filename="a2l/ast/a2l_ast.py")
        sys.exit(0)

    if args.filename is None and args.testcases is False:
        print(_A2LPARSER_DESCRIPTION)
        print("\nPlease specifiy a A2L file.")
        print("For more information use the -h or --help flag.")
        sys.exit(2)

    if args.o2 is True:
        _optimize = 1
        _gen_tables = 0
    elif args.o1 is True:
        _optimize = 1
        _gen_tables = 1
    else:
        _optimize = 0
        _gen_tables = 1

    if args.testcases:
        _verbosity = 0
        _optimize = 0
        _gen_tables = 1
    else:
        _verbosity = 2

    cfg = Config(debug=args.debug, optimize=_optimize, error_resolve=True, write_tables=_gen_tables, verbosity=_verbosity)

    p = Parser(config=cfg)

    if args.testcases:
        Testsuite(p)
    else:
        p.parseFile(fileName=args.filename)


if __name__ == "__main__":
    main()

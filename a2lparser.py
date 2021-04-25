import sys
import argparse

from argparse import RawTextHelpFormatter

from a2l.parser import Parser
from a2l.config.config import Config
from a2l.config.config_builder import ConfigBuilder


_A2LPARSER_DESCRIPTION = \
"""\n
* * * * * * * * * * * * *\n
* A2L to XML Parser * * *\n
* * * * * * * * * * * * *\n
"""

def main():
    argparser = argparse.ArgumentParser(description=_A2LPARSER_DESCRIPTION, formatter_class=RawTextHelpFormatter)
    argparser.add_argument('filename', nargs='?', help='relativ path to the full filename')
    argparser.add_argument('-d', '--debug', action='store_true', help="enable debug output on stderr" )
    argparser.add_argument('-t', '--test', action='store_true', help="test the given file" )
    argparser.add_argument('-x', '--xml', action='store_true', help="XML output file" )
    argparser.add_argument('-o1', action='store_true', help="initial generated table" )
    argparser.add_argument('-o2', action='store_true', help="don't generate a table" )
    argparser.add_argument('--testcases', action='store_true', help="start all testcases" )
    argparser.add_argument('--error-resolve', action='store_true', help="use error resolve function" )
    argparser.add_argument('--gen-ast', nargs='?', help="generate ast file" )
    argparser.add_argument('--gen-rules', action='store_true', help="generate a2l yacc rules file" )
    args = argparser.parse_args()


    if args.gen_ast:
        ConfigBuilder(config=args.gen_ast, output_filename="a2l/ast/a2l_ast.py")
        sys.exit(0)

    if args.filename is None and args.testcases is False:
        print(_A2LPARSER_DESCRIPTION)
        print("\nPlease specifiy a A2L file.")
        print("For more information use the -h or --help flag.")
        sys.exit(2)

    if args.debug is True:
        _debug = 1
    else:
        _debug = 0

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

    cfg = Config(debug=_debug,
                 optimize=_optimize,
                 error_resolve=True,
                 write_tables=_gen_tables,
                 verbosity=_verbosity)

    p = Parser(config=cfg)

    if args.testcases:
        from tests.testsuite import Testsuite
        Testsuite(p)
    else:
        p.parseFile(fileName=args.filename)


if __name__ == "__main__":
    main()
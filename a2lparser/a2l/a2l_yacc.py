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


from ply.yacc import yacc
from alive_progress import alive_bar
from a2lparser.a2l.a2l_lex import A2LLex
from a2lparser import A2L_GENERATED_FILES_DIR
from a2lparser.a2l.rules.rules_meta import RulesMeta
from a2lparser.a2l.rules.rules_enum import RulesEnum
from a2lparser.a2l.rules.rules_sections import RulesSections
from a2lparser.a2l.rules.rules_datatypes import RulesDatatypes
from a2lparser.a2l.parsing_exception import ParsingException
from a2lparser.a2l.ast.abstract_syntax_tree import AbstractSyntaxTree
import a2lparser.gen.a2l_ast as ASTNodes


class A2LYacc(RulesEnum, RulesDatatypes, RulesMeta, RulesSections):
    """
    A2LYacc class which represents the an instance of the YACC module from ply.yacc.

    Usage:
        >>> yacc = A2LYacc()
        >>> ast: AbstractSyntaxTree = yacc.generate_ast(input=content)
    """

    def __init__(
        self,
        debug: bool = False,
        optimize: bool = True,
        write_tables: bool = True,
        yacc_table_file: str = "_a2l_yacc_tables",
        lex_table_file: str = "_a2l_lex_tables",
        generated_files_dir: str = str(A2L_GENERATED_FILES_DIR),
    ) -> None:
        """
        A2LYacc Constructor.

        Args:
            - debug: will output debug information from ply
            - optimize: optimize flag for the ply parser
            - write_tables: whether to generate table files or not
            - yacc_table_file: the name of the yacc table file
            - lex_table_file: the name of the lex table file
            - generated_files_dir: the directory to write the generated files to
        """
        super().__init__()
        self.a2l_lex = A2LLex(
            debug=debug, optimize=optimize, generated_files_dir=generated_files_dir, lex_table_file=lex_table_file
        )
        self.tokens = self.a2l_lex.tokens
        self.experimental_error_resolve = False

        self.a2l_yacc = yacc(
            module=self,
            start="abstract_syntax_tree_final",
            debug=debug,
            optimize=optimize,
            tabmodule=yacc_table_file,
            outputdir=generated_files_dir,
            write_tables=write_tables,
        )
        self.debug = debug
        self.a2l_sections_list = []

    def generate_ast(self, content: str) -> AbstractSyntaxTree:
        """
        Generates an AbstractSyntaxTree from an input string.
        """
        content_lines = content.count("\n")
        with alive_bar(content_lines) as progressbar:
            self.a2l_lex.progressbar = progressbar
            ast = self.a2l_yacc.parse(input=content, lexer=self.a2l_lex, debug=self.debug)

        if hasattr(ast, "node") and ast.node is not None:
            return AbstractSyntaxTree(ast.node)

        raise ParsingException("Unable to parse given input. Generated AST is empty!")

    ##################################################
    # General Parsing rules and starting point.      #
    #                                                #
    # These rules define the structure of the parser #
    # and the basic grammer. For more specific rules #
    # look into a2lparser.a2l.rules                  #
    ##################################################
    # pylint: disable=C0103
    # def p_error(self, p):  # pylint: disable=W0613
    #     """
    #     Error handler function.
    #     """
    #     # We just do nothing for now and wait for the next valid section
    #     if self.experimental_error_resolve:
    #         raise NotImplementedError("Experimental error resolving is not implemented yet.")
    #     # while True:
    #     #     if p.type == "END":
    #     #         break
    #     #     tok = self.a2l_lex.token()  # Get the next token
    #     #     if not tok or tok.type == "END":
    #     #         break  # Stop skipping when we reach the end of the section
    #     # # Return an empty list to continue parsing the remaining sections
    #     # return []

    def p_error(self, p):
        """
        Error handler function.
        """
        if p:
            token = self.a2l_yacc.token()
            self.a2l_yacc.errok()
            return token

    def p_empty(self, p):
        """
        empty :
        """
        p[0] = None

    def p_abstract_syntax_tree_final(self, p):
        """
        abstract_syntax_tree_final : a2l_final
                                   | empty
        """
        if p[1] is None:
            p[0] = ASTNodes.Abstract_Syntax_Tree(None)
        else:
            p[0] = ASTNodes.Abstract_Syntax_Tree(p[1])

    def p_a2l_final(self, p):
        """
        a2l_final : a2l_sections
        """
        p[0] = p[1]

    def p_a2l_sections(self, p):
        """
        a2l_sections : a2l_section_list
        """
        p[0] = p[1]

    def p_a2l_section_list(self, p):
        """
        a2l_section_list : a2l_section
                         | a2l_section_list a2l_section
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            if p[2]:
                p[1].append(p[2])
            p[0] = p[1]

    def p_a2l_section(self, p):
        """
        a2l_section : meta_block
                    | meta_block_empty
        """
        if p[1]:
            p[0] = p[1]

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


from a2lparser.a2l.a2l_yacc import A2lYacc as A2LYacc
from a2lparser.a2l.config.config import Config
from a2lparser.a2l.abstract_syntax_tree import AbstractSyntaxTree


def test_unit_ast_empty():
    """
    Creates an AST from an empty A2L file
    """
    A2L_FILE_EMPTY = ""
    a2l_yacc = A2LYacc(Config())
    ast = a2l_yacc.generate_ast(A2L_FILE_EMPTY, A2L_FILE_EMPTY.count("\n"))
    assert ast
    assert isinstance(ast, AbstractSyntaxTree)


def test_unit_ast_calibration_handle_node():
    """
    Creates an AST from a A2L calibration block.
    """
    A2L_CALIBRATION_HANDLE = """
    /begin CALIBRATION_HANDLE
        0x10000 /* start address of pointer table */
        0x200 /* length of pointer table */
        0x4 /* size of one pointer table entry */
        0x30000 /* start address of flash section */
        0x20000 /* length of flash section */
        CALIBRATION_HANDLE_TEXT "12345"
    /end CALIBRATION_HANDLE
    """
    A2L_CALIBRATION_HANDLE_EMPTY = """
    /begin CALIBRATION_HANDLE
    /end CALIBRATION_HANDLE
    """
    a2l_yacc = A2LYacc(Config())
    ast = a2l_yacc.generate_ast(A2L_CALIBRATION_HANDLE_EMPTY, A2L_CALIBRATION_HANDLE_EMPTY.count("\n"))
    assert isinstance(ast, AbstractSyntaxTree)
    assert ast.ast

    ast = a2l_yacc.generate_ast(A2L_CALIBRATION_HANDLE, A2L_CALIBRATION_HANDLE.count("\n"))
    assert isinstance(ast, AbstractSyntaxTree)
    assert ast.ast


def test_unit_ast_simple_project():
    """
    Create an AST from a simple A2L project.
    """
    A2L_FILE = """
    ASAM VERSION "1.7.0"
    /BEGIN PROJECT
    PROJECT "My Project"
      VERSION "1.0"
    /END PROJECT

    /BEGIN HEADER
    HEADER
      AUTHOR ""
      PROJECT "My Project"
      VERSION "1.0"
      DATE "2023-03-24"
    /END HEADER
    """
    a2l_yacc = A2LYacc(Config())
    ast = a2l_yacc.generate_ast(A2L_FILE, A2L_FILE.count("\n"))
    assert ast

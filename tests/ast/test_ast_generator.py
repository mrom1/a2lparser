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
import tempfile
import importlib.util
from a2lparser import A2L_PACKAGE_DIR
from a2lparser import A2L_CONFIGS_DIR
from a2lparser import A2L_DEFAULT_CONFIG_NAME
from a2lparser.a2l.ast.ast_generator import ASTGenerator


def test_ast_generator():
    """
    Attempts to create the python file containing the AST node classes.
    """
    temp_test_output_path = A2L_PACKAGE_DIR / "../tests"
    temp_test_dir_prefix = "temp_dir_output_"

    with tempfile.TemporaryDirectory(dir=temp_test_output_path, prefix=temp_test_dir_prefix) as tempdir:
        config_file = A2L_CONFIGS_DIR / A2L_DEFAULT_CONFIG_NAME
        ast_python_file = os.path.join(tempdir, "test_a2l_ast.py")
        ast_generator = ASTGenerator(cfg_filename=str(config_file), out_filename=ast_python_file)
        ast_generator.generate(use_clean_names=True)

        # Load the module from the generated file
        spec = importlib.util.spec_from_file_location("test_a2l_ast", ast_python_file)
        assert spec is not None
        assert spec.loader is not None
        a2l_ast = importlib.util.module_from_spec(spec)  # type: ignore
        spec.loader.exec_module(a2l_ast)

        # Instantiate the A2ml_Version class
        a2ml_version = a2l_ast.A2ml_Version("1", "2")
        assert a2ml_version.VersionNo == "1"
        assert a2ml_version.UpgradeNo == "2"

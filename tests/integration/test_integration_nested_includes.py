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


import tempfile
from pathlib import Path
from a2lparser import A2L_PACKAGE_DIR
from a2lparser.a2lparser import main
from tests.fixture_utils import compare_files, check_files_exist


def test_integration_nested_includes(monkeypatch, compare_files, check_files_exist):
    """
    Tests parsing and converting the NESTED_INCLUDES.a2l file.
    """
    a2l_filename = "TEST_Nested_Includes.a2l"
    temp_test_output_path = A2L_PACKAGE_DIR / "../testfiles"
    temp_test_dir_prefix = "temp_dir_output_"

    with tempfile.TemporaryDirectory(dir=temp_test_output_path, prefix=temp_test_dir_prefix) as tempdir:
        monkeypatch.setattr("sys.argv", [
            "a2lparser",  f"testfiles/A2L/{a2l_filename}",
            "--json", "--xml", "--yaml", "--no-prompt",
            "--output-dir",  f"\"{Path(tempdir).resolve().as_posix()}\"",
        ])
        main()

        # Check if files were generated
        check_files_exist(
            f"{Path(tempdir).as_posix()}/TEST_Nested_Includes.xml",
            f"{Path(tempdir).as_posix()}/TEST_Nested_Includes.json",
            f"{Path(tempdir).as_posix()}/TEST_Nested_Includes.yml",
        )

        # Compare files
        compare_files(
            f"{Path(tempdir).as_posix()}/TEST_Nested_Includes.xml",
            f"{temp_test_output_path.as_posix()}/XML/TEST_Nested_Includes.xml",
        )
        compare_files(
            f"{Path(tempdir).as_posix()}/TEST_Nested_Includes.json",
            f"{temp_test_output_path.as_posix()}/JSON/TEST_Nested_Includes.json",
        )
        compare_files(
            f"{Path(tempdir)}/TEST_Nested_Includes.yml",
            f"{temp_test_output_path.as_posix()}/YAML/TEST_Nested_Includes.yml",
        )

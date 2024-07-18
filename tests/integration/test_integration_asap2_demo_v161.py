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
from a2lparser.main import main
# from tests.fixture_utils import compare_files, check_files_exist


def test_integration_asap2_demo_v161(monkeypatch, compare_files, check_files_exist):
    """
    Tests parsing and converting the ASAP2_Demo_V161.a2l file.
    """
    a2l_filename = "ASAP2_Demo_V161.a2l"
    temp_test_output_path = A2L_PACKAGE_DIR / "../testfiles"
    temp_test_dir_prefix = "temp_dir_output_"

    with tempfile.TemporaryDirectory(
        dir=temp_test_output_path, prefix=temp_test_dir_prefix
    ) as tempdir:
        monkeypatch.setattr(
            "sys.argv",
            [
                "a2lparser",
                f"testfiles/A2L/{a2l_filename}",
                "--json",
                "--xml",
                "--yaml",
                "--output-dir",
                f'"{Path(tempdir).resolve().as_posix()}"',
            ],
        )
        main()

        # Check if files were generated
        check_files_exist(
            f"{Path(tempdir).as_posix()}/ASAP2_Demo_V161.xml",
            f"{Path(tempdir).as_posix()}/ASAP2_Demo_V161.json",
            f"{Path(tempdir).as_posix()}/ASAP2_Demo_V161.yml",
        )

        # Compare files
        compare_files(
            f"{Path(tempdir).as_posix()}/ASAP2_Demo_V161.xml",
            f"{temp_test_output_path.as_posix()}/XML/ASAP2_Demo_V161.xml",
        )
        compare_files(
            f"{Path(tempdir).as_posix()}/ASAP2_Demo_V161.json",
            f"{temp_test_output_path.as_posix()}/JSON/ASAP2_Demo_V161.json",
        )
        compare_files(
            f"{Path(tempdir)}/ASAP2_Demo_V161.yml",
            f"{temp_test_output_path.as_posix()}/YAML/ASAP2_Demo_V161.yml",
        )

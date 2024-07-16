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
import pytest


@pytest.fixture
def check_files_exist():
    """
    Fixture for checking if files exist.
    """

    def _check_files_exist(*file_paths):
        missing_files = [file_path for file_path in file_paths if not os.path.exists(file_path)]
        assert not missing_files, f"The following files are missing: {missing_files}"

    return _check_files_exist


@pytest.fixture
def compare_files():
    """
    Fixture for comparing two files for equality.
    """

    def _normalize_lines(lines):
        return [line.strip() for line in lines]

    def _compare_files(file1, file2):
        with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
            lines1 = _normalize_lines(f1.readlines())
            lines2 = _normalize_lines(f2.readlines())
            assert lines1 == lines2, f"Files {file1} and {file2} do not match."

    return _compare_files

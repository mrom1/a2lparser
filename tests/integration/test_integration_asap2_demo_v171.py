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
# @TODO


import tempfile
from a2lparser import A2L_PACKAGE_DIR
from a2lparser.a2lparser import main


def test_integration_asap2_demo_v171(monkeypatch):
    """
    Tests parsing and converting the ASAP2_Demo_V161.a2l file.
    """
    a2l_filename = "ASAP2_Demo_V171.a2l"
    temp_test_output_path = A2L_PACKAGE_DIR / "../tests"
    temp_test_dir_prefix = "temp_dir_output_"

    with tempfile.TemporaryDirectory(dir=temp_test_output_path, prefix=temp_test_dir_prefix) as tempdir:
        monkeypatch.setattr("sys.argv", ["a2lparser", f"testfiles/A2L/{a2l_filename}",
                            f"--output-dir {tempdir}", "--json", "--xml", "--yaml", "--quiet", "--no-prompt"])
        main()

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


import pytest
from a2lparser import __version__
from a2lparser.main import main


def test_integration_version_argument(monkeypatch, capsys):
    """
    Tests the "version" parameter of the a2lparser.

    Calls "a2lparser --version" and checks if the output contains the expected version information.
    """
    # Modify sys.argv to include the version argument
    monkeypatch.setattr('sys.argv', ['a2lparser', '--version'])

    # Call main function
    with pytest.raises(SystemExit):
        main()

    # Capture the output
    captured = capsys.readouterr()

    # Check if the output contains the expected version information
    assert f"a2lparser version: {__version__}\n" == captured.out

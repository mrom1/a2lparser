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


import six
import subprocess


def test_a2lpaser_trigger_unittests():
    """
    Test case that runs a2lparser with version as an argument.

    $ a2lparser --unittests
    """
    args = ["python", "-m", "a2lparser.a2lparser", "--unittests"]
    if six.PY3:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
    else:
        result = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, errors = result.communicate()
        if result.returncode != 0:
            raise Exception("Command failed with return code %d: %s" % (result.returncode, errors.decode()))
    assert result.returncode == 0  # Assert that the program ran successfully

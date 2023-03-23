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


import sys
from a2lparser.logger.logger import Logger
from a2lparser.unittests.testhandler import Testhandler


if sys.version_info[0] == 2:
    from io import BytesIO as StringIO
else:
    from io import StringIO


class TestLogger(Testhandler):
    def setUp(self):
        self.output = StringIO()
        self.manager = Logger()
        self.manager.set_output(self.output)
        self.logger = self.manager.new_module("TEST")

    def test_level(self):
        self.logger.debug("test")
        self.assertEqual(self.output.tell(), 0)
        self.manager.set_level("DEBUG")
        self.logger.debug("test")
        self.assertNotEqual(self.output.tell(), 0)

    def test_output(self):
        self.manager.set_level("DEBUG")
        self.logger.debug("test")
        self.assertEqual(self.output.getvalue(), "[TEST][DEBUG] test\n")

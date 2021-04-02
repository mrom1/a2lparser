import sys

from logger.logger import Logger
from tests.testhandler import Testhandler

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

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


from a2lparser.unittests.testhandler import Testhandler


_TEST_CALIBRATION_METHOD_BLOCK = """
/begin CALIBRATION_METHOD
    "FixedSizeMoveableEmuRAM"  /* Method name */
    1                           /* Method version */
    /begin CALIBRATION_HANDLE
        0                    /* EmuRAM page identifier */
        0xBF000000           /* Original RAM Address */
        0x10000               /* Page size */
    /end CALIBRATION_HANDLE
    /begin CALIBRATION_HANDLE
		1                    /* EmuRAM page identifier */
		0xBF010000           /* Original RAM Address */
		0x20000               /* Page size */
    /end CALIBRATION_HANDLE
    /begin CALIBRATION_HANDLE
        0x10000 /* start address of pointer table */
        0x200 /* length of pointer table */
        0x4 /* size of one pointer table entry */
        0x10000 /* start address of flash section */
        0x10000 /* length of flash section */
        CALIBRATION_HANDLE_TEXT "Nmot"
    /end CALIBRATION_HANDLE
/end CALIBRATION_METHOD
"""

_TEST_CALIBRATION_METHOD_BLOCK_EMPTY = """
/begin CALIBRATION_METHOD
    /begin CALIBRATION_HANDLE
    /end CALIBRATION_HANDLE
    /begin CALIBRATION_HANDLE
    /end CALIBRATION_HANDLE
/end CALIBRATION_METHOD
"""


class TestCalibrationMethod(Testhandler):
    def test_calibration_method_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_calibration_method_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_CALIBRATION_METHOD_BLOCK,
                      filelength=_TEST_CALIBRATION_METHOD_BLOCK_EMPTY.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Calibration_Method/Method').text, "FixedSizeMoveableEmuRAM")
        self.assertEqual(tree.find('.//Calibration_Method/Version').text, "1")

        calibration_handles = tree.findall('.//Calibration_Method/Calibration_Handle')
        self.assertEqual(len(calibration_handles), 3)
        self.assertEqual(calibration_handles[0].find('.//Handle').text, "0, 0xBF000000, 0x10000")
        self.assertEqual(calibration_handles[1].find('.//Handle').text, "1, 0xBF010000, 0x20000")
        self.assertEqual(calibration_handles[2].find('.//Handle').text, "0x10000, 0x200, 0x4, 0x10000, 0x10000")
        self.assertEqual(calibration_handles[2].find('.//Calibration_Handle_Text').text, "Nmot")

    def test_calibration_method_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_calibration_method_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_CALIBRATION_METHOD_BLOCK_EMPTY,
                      filelength=_TEST_CALIBRATION_METHOD_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

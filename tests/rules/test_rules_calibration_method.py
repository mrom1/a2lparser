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


from a2lparser.a2l.a2l_yacc import A2LYacc


def test_rules_calibration_method():
    """
    Tests parsing a valid "CALIBRATION_METHOD" block.
    """
    calibration_method_block = """
    /begin CALIBRATION_METHOD
        "FixedSizeMoveableEmuRAM"  /* Method name */
        1                          /* Method version */
        /begin CALIBRATION_HANDLE
            0                    /* EmuRAM page identifier */
            0xBF000000           /* Original RAM Address */
            0x10000              /* Page size */
        /end CALIBRATION_HANDLE
        /begin CALIBRATION_HANDLE
            1                    /* EmuRAM page identifier */
            0xBF010000           /* Original RAM Address */
            0x20000              /* Page size */
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
    parser = A2LYacc()
    ast = parser.generate_ast(calibration_method_block)
    assert ast

    calibration_method = ast["CALIBRATION_METHOD"]
    assert calibration_method
    assert calibration_method["Method"] == '"FixedSizeMoveableEmuRAM"'
    assert calibration_method["VERSION"] == "1"

    calibration_method_handle = calibration_method["CALIBRATION_HANDLE"]
    assert len(calibration_method_handle) == 3
    assert calibration_method_handle[0]["Handle"] == ["0", "0xBF000000", "0x10000"]
    assert calibration_method_handle[1]["Handle"] == ["1", "0xBF010000", "0x20000"]
    assert calibration_method_handle[2]["Handle"] == ["0x10000", "0x200", "0x4", "0x10000", "0x10000"]

    calibration_handle_text = calibration_method_handle[2]["CALIBRATION_HANDLE_TEXT"].Text
    assert calibration_handle_text == '"Nmot"'

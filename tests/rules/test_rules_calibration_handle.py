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


def test_rules_calibration_handle():
    """
    Tests parsing a valid "CALIBRATION_HANDLE" block.
    """
    calibration_handle_block = """
    /begin CALIBRATION_HANDLE
            0x10000 /* start address of pointer table */
            0x200 /* length of pointer table */
            0x4 /* size of one pointer table entry */
            0x30000 /* start address of flash section */
            0x20000 /* length of flash section */
            CALIBRATION_HANDLE_TEXT "12345"
    /end CALIBRATION_HANDLE
    /begin CALIBRATION_HANDLE
            0x40000 /* start address of pointer table */
            0x800 /* length of pointer table */
            0x2 /* size of one pointer table entry */
            0xFF000 /* start address of flash section */
            0xCC000 /* length of flash section */
            CALIBRATION_HANDLE_TEXT "description"
    /end CALIBRATION_HANDLE
    """
    parser = A2LYacc()
    ast = parser.generate_ast(calibration_handle_block)
    assert ast

    calibration_handle = ast["CALIBRATION_HANDLE"]
    assert len(calibration_handle) == 2
    assert calibration_handle[0]["Handle"] == ["0x10000", "0x200", "0x4", "0x30000", "0x20000"]
    assert calibration_handle[0]["CALIBRATION_HANDLE_TEXT"]["CALIBRATION_HANDLE_TEXT"] == '"12345"'
    assert calibration_handle[1]["Handle"] == ["0x40000", "0x800", "0x2", "0xFF000", "0xCC000"]
    assert calibration_handle[1]["CALIBRATION_HANDLE_TEXT"]["CALIBRATION_HANDLE_TEXT"] == '"description"'

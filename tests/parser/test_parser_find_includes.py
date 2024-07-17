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
from a2lparser.a2lparser import A2LParser


@pytest.mark.parametrize('matching_includes, expected_filename', [
    (r'/include "C:\DATA\ECU.A2L"', r'C:\DATA\ECU.A2L'),
    (r'/INCLUDE "..\includes\CANAPE_OET.A2L"', r'..\includes\CANAPE_OET.A2L'),
    (r'/INCLUDE "\\server1\documents\templates\template.aml"', r'\\server1\documents\templates\template.aml'),
    (r'/Include ECU_DATA.a2l', r'ECU_DATA.a2l'),
    (r'/include "AML Template.aml"', r'AML Template.aml'),
    (r'/include "/home/user/A2L\ Files/ECU_1221.A2L"', r'/home/user/A2L\ Files/ECU_1221.A2L'),
    (r'/include "../../../blobs/TP_BLOB.a2l"', r'../../../blobs/TP_BLOB.a2l'),
    (r'/begin A2ML /include "/home/user/IF_DATA/XCP.txt" STV_N /* name */ /end A2ML', r'/home/user/IF_DATA/XCP.txt'),
    (r'/begin MODULE /Include My_Module.A2L UNIT 2 "" "" DERIVED /end MODULE', r'My_Module.A2L'),
    (r'/begin PROJECT /include "\\Z:\tmp\ecu project.a2l" /* EOF */ /end PROJECT', r'\\Z:\tmp\ecu project.a2l'),
    (r'/begin PROJECT /include "/home/ecu/header/my_header.a2l" /include my_module.a2l /end PROJECT',
     [r'/home/ecu/header/my_header.a2l', r'my_module.a2l']),
    (r'/begin MODULE /begin MEASUREMENT /end MEASUREMENT /end MODULE', None)
])
def test_parser_load_file_include_mechanism(matching_includes, expected_filename):
    """
    Tests the include mechanism of the A2L parser.
    """
    parser = A2LParser()
    filename = parser._find_includes(matching_includes)
    assert filename == expected_filename

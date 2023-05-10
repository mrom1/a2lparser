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


def test_rules_mod_par_valid():
    """
    Tests parsing a valid "MOD_PAR" block.
    """
    mod_par_block = """
    /begin MOD_PAR
        "comment"
        /begin CALIBRATION_METHOD
            "InCircuit"
            2
            /begin CALIBRATION_HANDLE
                0                    /* EmuRAM page identifier */
                0xBF000000           /* Original RAM Address */
                0x10000              /* Page size */
            /end CALIBRATION_HANDLE
        /end CALIBRATION_METHOD
        /begin CALIBRATION_METHOD
            "Example"
            4
            /begin CALIBRATION_HANDLE
                1                    /* EmuRAM page identifier */
                0xBF100000           /* Original RAM Address */
                0x90000              /* Page size */
            /end CALIBRATION_HANDLE
        /end CALIBRATION_METHOD
        ADDR_EPK 0x14567
        ADDR_EPK 0x76541
        CPU_TYPE "INTEL 4711"
        CUSTOMER "Company - Name"
        CUSTOMER_NO "191188"
        ECU "Steering control"
        ECU_CALIBRATION_OFFSET 0x1000
        EPK "EPROM identifier test"
        /begin MEMORY_LAYOUT
            PRG_RESERVED
            0x0000
            0x0400
            -1 -1 -1 -1 -1
        /end MEMORY_LAYOUT
        /begin MEMORY_LAYOUT
            PRG_RESERVED
            0x8000
            0x0300
            -3 -2 -5 1 99
        /end MEMORY_LAYOUT
        /begin MEMORY_SEGMENT
            Data1
            "comment"
            DATA
            FLASH
            EXTERN
            0x4000
            0x3000
            -1 -1 -1 -1 -1
        /end MEMORY_SEGMENT
        /begin MEMORY_SEGMENT
            Data2
            "Data external Flash"
            DATA
            FLASH
            EXTERN
            0x7000
            0x2000
            -1 -1 -1 -1 -1
        /end MEMORY_SEGMENT
        NO_OF_INTERFACES 3
        PHONE_NO "09498 594562"
        SUPPLIER "Smooth and Easy"
        USER "Username"
        SYSTEM_CONSTANT "Fd" "1.10"
        SYSTEM_CONSTANT "Ts" "0.010"
        SYSTEM_CONSTANT "Zd" "0.3"
        SYSTEM_CONSTANT "Zn" "0.07"
        VERSION "BG5.0815"
    /end MOD_PAR
    """
    parser = A2LYacc()
    ast = parser.generate_ast(mod_par_block)
    assert ast

    mod_par = ast["MOD_PAR"]
    assert mod_par
    assert mod_par["Comment"] == '"comment"'
    assert mod_par["CPU_TYPE"] == '"INTEL 4711"'
    assert mod_par["CUSTOMER"] == '"Company - Name"'
    assert mod_par["CUSTOMER_NO"] == '"191188"'
    assert mod_par["ECU"] == '"Steering control"'
    assert mod_par["ECU_CALIBRATION_OFFSET"] == "0x1000"
    assert mod_par["EPK"] == '"EPROM identifier test"'
    assert mod_par["NO_OF_INTERFACES"] == "3"
    assert mod_par["PHONE_NO"] == '"09498 594562"'
    assert mod_par["SUPPLIER"] == '"Smooth and Easy"'
    assert mod_par["USER"] == '"Username"'
    assert mod_par["VERSION"] == '"BG5.0815"'

    assert len(mod_par["ADDR_EPK"]) == 2
    assert mod_par["ADDR_EPK"][0]["Address"] == "0x14567"
    assert mod_par["ADDR_EPK"][1]["Address"] == "0x76541"

    assert len(mod_par["CALIBRATION_METHOD"]) == 2
    assert mod_par["CALIBRATION_METHOD"][0]["Method"] == '"InCircuit"'
    assert mod_par["CALIBRATION_METHOD"][0]["VERSION"] == "2"
    assert mod_par["CALIBRATION_METHOD"][0]["CALIBRATION_HANDLE"]["Handle"][0] == "0"
    assert mod_par["CALIBRATION_METHOD"][0]["CALIBRATION_HANDLE"]["Handle"][1] == "0xBF000000"
    assert mod_par["CALIBRATION_METHOD"][0]["CALIBRATION_HANDLE"]["Handle"][2] == "0x10000"
    assert mod_par["CALIBRATION_METHOD"][1]["Method"] == '"Example"'
    assert mod_par["CALIBRATION_METHOD"][1]["VERSION"] == "4"
    assert mod_par["CALIBRATION_METHOD"][1]["CALIBRATION_HANDLE"]["Handle"][0] == "1"
    assert mod_par["CALIBRATION_METHOD"][1]["CALIBRATION_HANDLE"]["Handle"][1] == "0xBF100000"
    assert mod_par["CALIBRATION_METHOD"][1]["CALIBRATION_HANDLE"]["Handle"][2] == "0x90000"

    assert len(mod_par["MEMORY_LAYOUT"]) == 2
    assert mod_par["MEMORY_LAYOUT"][0]["PrgType"] == "PRG_RESERVED"
    assert mod_par["MEMORY_LAYOUT"][0]["Address"] == "0x0000"
    assert mod_par["MEMORY_LAYOUT"][0]["Size"] == "0x0400"
    assert mod_par["MEMORY_LAYOUT"][0]["Offset"][0] == "-1"
    assert mod_par["MEMORY_LAYOUT"][0]["Offset"][1] == "-1"
    assert mod_par["MEMORY_LAYOUT"][0]["Offset"][2] == "-1"
    assert mod_par["MEMORY_LAYOUT"][0]["Offset"][3] == "-1"
    assert mod_par["MEMORY_LAYOUT"][0]["Offset"][4] == "-1"
    assert mod_par["MEMORY_LAYOUT"][1]["PrgType"] == "PRG_RESERVED"
    assert mod_par["MEMORY_LAYOUT"][1]["Address"] == "0x8000"
    assert mod_par["MEMORY_LAYOUT"][1]["Size"] == "0x0300"
    assert mod_par["MEMORY_LAYOUT"][1]["Offset"][0] == "-3"
    assert mod_par["MEMORY_LAYOUT"][1]["Offset"][1] == "-2"
    assert mod_par["MEMORY_LAYOUT"][1]["Offset"][2] == "-5"
    assert mod_par["MEMORY_LAYOUT"][1]["Offset"][3] == "1"
    assert mod_par["MEMORY_LAYOUT"][1]["Offset"][4] == "99"

    assert len(mod_par["MEMORY_SEGMENT"]) == 2
    assert mod_par["MEMORY_SEGMENT"][0]["Name"] == "Data1"
    assert mod_par["MEMORY_SEGMENT"][0]["LongIdentifier"] == '"comment"'
    assert mod_par["MEMORY_SEGMENT"][0]["PrgType"] == "DATA"
    assert mod_par["MEMORY_SEGMENT"][0]["MemoryType"] == "FLASH"
    assert mod_par["MEMORY_SEGMENT"][0]["Attribute"] == "EXTERN"
    assert mod_par["MEMORY_SEGMENT"][0]["Address"] == "0x4000"
    assert mod_par["MEMORY_SEGMENT"][0]["Size"] == "0x3000"
    assert mod_par["MEMORY_SEGMENT"][0]["Offset"][0] == "-1"
    assert mod_par["MEMORY_SEGMENT"][0]["Offset"][1] == "-1"
    assert mod_par["MEMORY_SEGMENT"][0]["Offset"][2] == "-1"
    assert mod_par["MEMORY_SEGMENT"][0]["Offset"][3] == "-1"
    assert mod_par["MEMORY_SEGMENT"][0]["Offset"][4] == "-1"
    assert mod_par["MEMORY_SEGMENT"][1]["Name"] == "Data2"
    assert mod_par["MEMORY_SEGMENT"][1]["LongIdentifier"] == '"Data external Flash"'
    assert mod_par["MEMORY_SEGMENT"][1]["PrgType"] == "DATA"
    assert mod_par["MEMORY_SEGMENT"][1]["MemoryType"] == "FLASH"
    assert mod_par["MEMORY_SEGMENT"][1]["Attribute"] == "EXTERN"
    assert mod_par["MEMORY_SEGMENT"][1]["Address"] == "0x7000"
    assert mod_par["MEMORY_SEGMENT"][1]["Size"] == "0x2000"
    assert mod_par["MEMORY_SEGMENT"][1]["Offset"][0] == "-1"
    assert mod_par["MEMORY_SEGMENT"][1]["Offset"][1] == "-1"
    assert mod_par["MEMORY_SEGMENT"][1]["Offset"][2] == "-1"
    assert mod_par["MEMORY_SEGMENT"][1]["Offset"][3] == "-1"
    assert mod_par["MEMORY_SEGMENT"][1]["Offset"][4] == "-1"

    assert len(mod_par["SYSTEM_CONSTANT"]) == 4
    assert mod_par["SYSTEM_CONSTANT"][0]["Name"] == '"Fd"'
    assert mod_par["SYSTEM_CONSTANT"][0]["VALUE"] == '"1.10"'
    assert mod_par["SYSTEM_CONSTANT"][1]["Name"] == '"Ts"'
    assert mod_par["SYSTEM_CONSTANT"][1]["VALUE"] == '"0.010"'
    assert mod_par["SYSTEM_CONSTANT"][2]["Name"] == '"Zd"'
    assert mod_par["SYSTEM_CONSTANT"][2]["VALUE"] == '"0.3"'
    assert mod_par["SYSTEM_CONSTANT"][3]["Name"] == '"Zn"'
    assert mod_par["SYSTEM_CONSTANT"][3]["VALUE"] == '"0.07"'


    
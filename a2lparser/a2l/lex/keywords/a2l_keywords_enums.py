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


class A2LKeywordsEnums:
    """
    Keywords for parsing A2L enums.
    """

    keywords: list = [
        # axis description enum
        "CURVE_AXIS",
        "COM_AXIS",
        "FIX_AXIS",
        "RES_AXIS",
        "STD_AXIS",
        # calibration access enum
        "CALIBRATION",
        "NO_CALIBRATION",
        "NOT_IN_MCD_SYSTEM",
        "OFFLINE_CALIBRATION",
        # characteristic enum
        "ASCII",
        "CURVE",
        "MAP",
        "CUBOID",
        "CUBE_4",
        "CUBE_5",
        "VAL_BLK",
        "VALUE",
        # conversation type enum
        "IDENTICAL",
        "FORM",
        "LINEAR",
        "RAT_FUNC",
        "TAB_INTP",
        "TAB_NOINTP",
        "TAB_VERB",
        # mode enum
        "ABSOLUTE",
        "DIFFERENCE",
        # index mode enum
        "ALTERNATE_CURVES",
        "ALTERNATE_WITH_X",
        "ALTERNATE_WITH_Y",
        "COLUMN_DIR",
        "ROW_DIR",
        # memory type enum
        "EEPROM",
        "EPROM",
        "FLASH",
        "RAM",
        "ROM",
        "REGISTER",
        # monotony enum
        "MON_DECREASE",
        "MON_INCREASE",
        "STRICT_DECREASE",
        "STRICT_INCREASE",
        "MONOTONOUS",
        "STRICT_MON",
        "NOT_MON",
        # prgtype enum
        "PRG_CODE",
        "PRG_DATA",
        "PRG_RESERVED",
        "CALIBRATION_VARIABLES",
        "CODE",
        "DATA",
        "EXCLUDE_FROM_FLASH",
        "OFFLINE_DATA",
        "SERAM",
        "VARIABLES",
        # unit type enum
        "DERIVED",
        "EXTENDED_SI",
        # tag enum
        "NUMERIC",
        "ALPHA",
    ]

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
# pylint: disable=C0103


# @TODO: change rule for "datatype" and "datasize" to "datatype_enum" and "datasize_enum"
class RulesEnum:
    """
    Rules for parsing enum datatypes.
    """

    def p_addrtype_enum(self, p):
        """
        addrtype_enum : PBYTE
                      | PWORD
                      | PLONG
                      | DIRECT
        """
        p[0] = p[1]

    def p_attribute_enum(self, p):
        """
        attribute_enum : INTERN
                       | EXTERN
        """
        p[0] = p[1]

    def p_axis_descr_enum(self, p):
        """
        axis_descr_enum : CURVE_AXIS
                        | COM_AXIS
                        | FIX_AXIS
                        | RES_AXIS
                        | STD_AXIS
        """
        p[0] = p[1]

    def p_byte_order_enum(self, p):
        """
        byte_order_enum : MSB_FIRST
                        | MSB_LAST
                        | LITTLE_ENDIAN
                        | BIG_ENDIAN
        """
        p[0] = p[1]

    def p_calibration_access_enum(self, p):
        """
        calibration_access_enum : CALIBRATION
                                | NO_CALIBRATION
                                | NOT_IN_MCD_SYSTEM
                                | OFFLINE_CALIBRATION
        """
        p[0] = p[1]

    def p_characteristic_enum(self, p):
        """
        characteristic_enum : ASCII
                            | CURVE
                            | MAP
                            | CUBOID
                            | CUBE_4
                            | CUBE_5
                            | VAL_BLK
                            | VALUE
        """
        p[0] = p[1]

    def p_conversion_type_enum(self, p):
        """
        conversion_type_enum : IDENTICAL
                             | FORM
                             | LINEAR
                             | RAT_FUNC
                             | TAB_INTP
                             | TAB_NOINTP
                             | TAB_VERB
        """
        p[0] = p[1]

    def p_datasize_enum(self, p):
        """
        datasize_enum : BYTE
                      | WORD
                      | LONG
        """
        p[0] = p[1]

    def p_datatype_enum(self, p):
        """
        datatype_enum : SBYTE
                      | UBYTE
                      | UWORD
                      | SWORD
                      | ULONG
                      | SLONG
                      | A_UINT64
                      | A_INT64
                      | FLOAT32_IEEE
                      | FLOAT64_IEEE
        """
        p[0] = p[1]

    def p_mode_enum(self, p):
        """
        mode_enum : ABSOLUTE
                  | DIFFERENCE
        """
        p[0] = p[1]

    def p_indexmode_enum(self, p):
        """
        indexmode_enum : ALTERNATE_CURVES
                       | ALTERNATE_WITH_X
                       | ALTERNATE_WITH_Y
                       | COLUMN_DIR
                       | ROW_DIR
        """
        p[0] = p[1]

    def p_indexorder_enum(self, p):
        """
        indexorder_enum : INDEX_INCR
                        | INDEX_DECR
        """
        p[0] = p[1]

    def p_memorytype_enum(self, p):
        """
        memorytype_enum : EEPROM
                        | EPROM
                        | FLASH
                        | RAM
                        | ROM
                        | REGISTER
        """
        p[0] = p[1]

    def p_monotony_enum(self, p):
        """
        monotony_enum : MON_DECREASE
                      | MON_INCREASE
                      | STRICT_DECREASE
                      | STRICT_INCREASE
                      | MONOTONOUS
                      | STRICT_MON
                      | NOT_MON
        """
        p[0] = p[1]

    def p_prgtype_enum_1(self, p):
        """
        prgtype_enum : PRG_CODE
                     | PRG_DATA
                     | PRG_RESERVED
        """
        p[0] = p[1]

    def p_prgtype_enum_2(self, p):
        """
        prgtype_enum : CALIBRATION_VARIABLES
                     | CODE
                     | DATA
                     | EXCLUDE_FROM_FLASH
                     | OFFLINE_DATA
                     | RESERVED
                     | SERAM
                     | VARIABLES
        """
        p[0] = p[1]

    def p_unit_type_enum(self, p):
        """
        unit_type_enum : DERIVED
                       | EXTENDED_SI
        """
        p[0] = p[1]

    def p_tag_enum(self, p):
        """
        tag_enum : NUMERIC
                 | ALPHA
        """
        p[0] = p[1]

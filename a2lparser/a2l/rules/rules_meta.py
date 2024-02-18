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


class RulesMeta:
    """
    General grammar rules to parse A2L sections.
    """

    def p_meta_block_empty(self, p):
        """
        meta_block_empty : BEGIN meta_block_keyword END meta_block_keyword
        """

    def p_meta_block_post_error(self, p):
        """
        meta_block_error : meta_block error
        """
        if p[1]:
            p[0] = p[1]

    def p_meta_block(self, p):
        """
        meta_block : project
                   | a2ml_block
                   | a2ml_version
                   | annotation
                   | ar_component
                   | asap2_version
                   | axis_descr
                   | axis_pts
                   | bit_operation
                   | blob
                   | calibration_handle
                   | calibration_method
                   | characteristic
                   | compu_method
                   | compu_tab
                   | compu_vtab
                   | compu_vtab_range
                   | def_characteristic
                   | dependent_characteristic
                   | fix_axis_par_list
                   | formula
                   | frame
                   | function
                   | function_list
                   | group
                   | header
                   | if_data
                   | in_measurement
                   | instance
                   | loc_measurement
                   | map_list
                   | measurement
                   | memory_layout
                   | memory_segment
                   | mod_common
                   | mod_par
                   | module
                   | out_measurement
                   | overwrite
                   | record_layout
                   | ref_characteristic
                   | ref_group
                   | ref_measurement
                   | sub_function
                   | sub_group
                   | structure_component
                   | transformer
                   | typedef_axis
                   | typedef_blob
                   | typedef_characteristic
                   | typedef_measurement
                   | typedef_structure
                   | unit
                   | user_rights
                   | var_address
                   | var_characteristic
                   | var_criterion
                   | var_forbidden_comb
                   | variant_coding
                   | virtual
                   | virtual_characteristic
        """
        p[0] = p[1]

    def p_meta_block_keywords(self, p):
        """
        meta_block_keyword : A2ML
                           | ANNOTATION
                           | ANNOTATION_TEXT
                           | AR_COMPONENT
                           | AXIS_DESCR
                           | AXIS_PTS
                           | BIT_OPERATION
                           | BLOB
                           | CALIBRATION_HANDLE
                           | CALIBRATION_METHOD
                           | CHARACTERISTIC
                           | COMPU_METHOD
                           | COMPU_TAB
                           | COMPU_TAB_REF
                           | COMPU_VTAB
                           | COMPU_VTAB_RANGE
                           | DEF_CHARACTERISTIC
                           | DEPENDENT_CHARACTERISTIC
                           | FIX_AXIS_PAR_LIST
                           | FORMULA
                           | FRAME
                           | FUNCTION
                           | FUNCTION_LIST
                           | FUNCTION_VERSION
                           | GROUP
                           | HEADER
                           | IN_MEASUREMENT
                           | INSTANCE
                           | LOC_MEASUREMENT
                           | MAP_LIST
                           | MEASUREMENT
                           | MEMORY_LAYOUT
                           | MEMORY_SEGMENT
                           | MOD_COMMON
                           | MOD_PAR
                           | MODULE
                           | OUT_MEASUREMENT
                           | OVERWRITE
                           | PROJECT
                           | RECORD_LAYOUT
                           | REF_CHARACTERISTIC
                           | REF_GROUP
                           | REF_MEASUREMENT
                           | SUB_FUNCTION
                           | SUB_GROUP
                           | STRUCTURE_COMPONENT
                           | TRANSFORMER
                           | TYPEDEF_AXIS
                           | TYPEDEF_BLOB
                           | TYPEDEF_CHARACTERISTIC
                           | TYPEDEF_MEASUREMENT
                           | TYPEDEF_STRUCTURE
                           | UNIT
                           | UNIT_CONVERSION
                           | USER
                           | USER_RIGHTS
                           | VAR_ADDRESS
                           | VAR_CHARACTERISTIC
                           | VAR_CRITERION
                           | VAR_FORBIDDEN_COMB
                           | VARIANT_CODING
                           | VIRTUAL
                           | VIRTUAL_CHARACTERISTIC
        """
        p[0] = p[1]

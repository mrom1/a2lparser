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


class RulesSectionsErrorhandlers:
    """
    Grammar for parsing encountered A2L Section error tokens.

    Current error handling strategy is to throw out all sections
    which encounter errors, and resynchronize the parser at the next section.

    @TODO: add error resolve for optional parameters.
    """

    def p_a2ml_version_error(self, p):
        """
        a2ml_version : A2ML_VERSION error
        """

    def p_addr_epk_error(self, p):
        """
        addr_epk : ADDR_EPK error
        """

    def p_address_type_error(self, p):
        """
        address_type : ADDRESS_TYPE error
        """

    def p_alignment_byte_error(self, p):
        """
        alignment_byte : ALIGNMENT_BYTE error
        """

    def p_alignment_float16_ieee_error(self, p):
        """
        alignment_float16_ieee : ALIGNMENT_FLOAT16_IEEE error
        """

    def p_alignment_float32_ieee_error(self, p):
        """
        alignment_float32_ieee : ALIGNMENT_FLOAT32_IEEE error
        """

    def p_alignment_float64_ieee_error(self, p):
        """
        alignment_float64_ieee : ALIGNMENT_FLOAT64_IEEE error
        """

    def p_alignment_int64_error(self, p):
        """
        alignment_int64 : ALIGNMENT_INT64 error
        """

    def p_alignment_long_error(self, p):
        """
        alignment_long : ALIGNMENT_LONG error
        """

    def p_alignment_word_error(self, p):
        """
        alignment_word : ALIGNMENT_WORD error
        """

    def p_annotation_error(self, p):
        """
        annotation : BEGIN ANNOTATION error END ANNOTATION
                   | BEGIN ANNOTATION END ANNOTATION
        """

    def p_annotation_label_error(self, p):
        """
        annotation_label : ANNOTATION_LABEL error
        """

    def p_annotation_origin_error(self, p):
        """
        annotation_origin : ANNOTATION_ORIGIN error
        """

    def p_annotation_text_error(self, p):
        """
        annotation_text : BEGIN ANNOTATION_TEXT error END ANNOTATION_TEXT
                        | BEGIN ANNOTATION_TEXT END ANNOTATION_TEXT
        """

    def p_array_size_error(self, p):
        """
        array_size : ARRAY_SIZE error
        """

    def p_ar_component_error(self, p):
        """
        ar_component : BEGIN AR_COMPONENT error END AR_COMPONENT
                     | BEGIN AR_COMPONENT END AR_COMPONENT
        """

    def p_ar_prototype_of_error(self, p):
        """
        ar_prototype_of : AR_PROTOTYPE_OF error
        """

    def p_asap2_version_error(self, p):
        """
        asap2_version : ASAP2_VERSION error
        """

    def p_axis_descr_error(self, p):
        """
        axis_descr : BEGIN AXIS_DESCR error END AXIS_DESCR
                   | BEGIN AXIS_DESCR END AXIS_DESCR
        """

    def p_axis_pts_error(self, p):
        """
        axis_pts : BEGIN AXIS_PTS error END AXIS_PTS
                 | BEGIN AXIS_PTS END AXIS_PTS
        """

    def p_axis_pts_ref_error(self, p):
        """
        axis_pts_ref : AXIS_PTS_REF error
        """

    def p_axis_pts_x_error(self, p):
        """
        axis_pts_x : AXIS_PTS_X error
        """

    def p_axis_pts_y_error(self, p):
        """
        axis_pts_y : AXIS_PTS_Y error
        """

    def p_axis_pts_z_error(self, p):
        """
        axis_pts_z : AXIS_PTS_Z error
        """

    def p_axis_pts_4_error(self, p):
        """
        axis_pts_4 : AXIS_PTS_4 error
        """

    def p_axis_pts_5_error(self, p):
        """
        axis_pts_5 : AXIS_PTS_5 error
        """

    def p_axis_rescale_x_error(self, p):
        """
        axis_rescale_x : AXIS_RESCALE_X error
        """

    def p_bit_mask_error(self, p):
        """
        bit_mask : BIT_MASK error
        """

    def p_bit_operation_error(self, p):
        """
        bit_operation : BEGIN BIT_OPERATION error END BIT_OPERATION
                      | BEGIN BIT_OPERATION END BIT_OPERATION
        """

    def p_blob_error(self, p):
        """
        blob : BEGIN BLOB error END BLOB
             | BEGIN BLOB END BLOB
        """

    def p_byte_order_error(self, p):
        """
        byte_order : BYTE_ORDER error
        """

    def p_calibration_access_error(self, p):
        """
        calibration_access : CALIBRATION_ACCESS error
        """

    def p_calibration_handle_error(self, p):
        """
        calibration_handle : BEGIN CALIBRATION_HANDLE error END CALIBRATION_HANDLE
                           | BEGIN CALIBRATION_HANDLE END CALIBRATION_HANDLE
        """

    def p_calibration_handle_text_error(self, p):
        """
        calibration_handle_text : CALIBRATION_HANDLE_TEXT error
        """

    def p_calibration_method_error(self, p):
        """
        calibration_method : BEGIN CALIBRATION_METHOD error END CALIBRATION_METHOD
                           | BEGIN CALIBRATION_METHOD END CALIBRATION_METHOD
        """

    def p_characteristic_error(self, p):
        """
        characteristic : BEGIN CHARACTERISTIC error END CHARACTERISTIC
                       | BEGIN CHARACTERISTIC END CHARACTERISTIC
        """

    def p_coeffs_error(self, p):
        """
        coeffs : COEFFS error
        """

    def p_coeffs_linear_error(self, p):
        """
        coeffs_linear : COEFFS_LINEAR error
        """

    def p_comparison_quantity_error(self, p):
        """
        comparison_quantity : COMPARISON_QUANTITY error
        """

    def p_compu_method_error(self, p):
        """
        compu_method : BEGIN COMPU_METHOD error END COMPU_METHOD
                     | BEGIN COMPU_METHOD END COMPU_METHOD
        """

    def p_compu_tab_error(self, p):
        """
        compu_tab : BEGIN COMPU_TAB error END COMPU_TAB
                  | BEGIN COMPU_TAB END COMPU_TAB
        """

    def p_compu_tab_ref_error(self, p):
        """
        compu_tab_ref : COMPU_TAB_REF error
        """

    def p_compu_vtab_error(self, p):
        """
        compu_vtab : BEGIN COMPU_VTAB error END COMPU_VTAB
                   | BEGIN COMPU_VTAB END COMPU_VTAB
        """

    def p_compu_vtab_range_error(self, p):
        """
        compu_vtab_range : BEGIN COMPU_VTAB_RANGE error END COMPU_VTAB_RANGE
                         | BEGIN COMPU_VTAB_RANGE END COMPU_VTAB_RANGE
        """

    def p_conversion_error(self, p):
        """
        conversion : CONVERSION error
        """

    def p_cpu_type_error(self, p):
        """
        cpu_type : CPU_TYPE error
        """

    def p_curve_axis_ref_error(self, p):
        """
        curve_axis_ref : CURVE_AXIS_REF error
        """

    def p_customer_error(self, p):
        """
        customer : CUSTOMER error
        """

    def p_customer_no_error(self, p):
        """
        customer_no : CUSTOMER_NO error
        """

    def p_data_size_error(self, p):
        """
        data_size : DATA_SIZE error
        """

    def p_def_characteristic_error(self, p):
        """
        def_characteristic : BEGIN DEF_CHARACTERISTIC error END DEF_CHARACTERISTIC
                           | BEGIN DEF_CHARACTERISTIC END DEF_CHARACTERISTIC
        """

    def p_default_value_error(self, p):
        """
        default_value : DEFAULT_VALUE error
        """

    def p_default_value_numeric_error(self, p):
        """
        default_value_numeric : DEFAULT_VALUE_NUMERIC error
        """

    def p_dependent_characteristic_error(self, p):
        """
        dependent_characteristic : BEGIN DEPENDENT_CHARACTERISTIC error END DEPENDENT_CHARACTERISTIC
                                 | BEGIN DEPENDENT_CHARACTERISTIC END DEPENDENT_CHARACTERISTIC
        """

    def p_deposit_error(self, p):
        """
        deposit : DEPOSIT error
        """

    def p_display_identifier_error(self, p):
        """
        display_identifier : DISPLAY_IDENTIFIER error
        """

    def p_dist_op_x_error(self, p):
        """
        dist_op_x : DIST_OP_X error
        """

    def p_dist_op_y_error(self, p):
        """
        dist_op_y : DIST_OP_Y error
        """

    def p_dist_op_z_error(self, p):
        """
        dist_op_z : DIST_OP_Z error
        """

    def p_dist_op_4_error(self, p):
        """
        dist_op_4 : DIST_OP_4 error
        """

    def p_dist_op_5_error(self, p):
        """
        dist_op_5 : DIST_OP_5 error
        """

    def p_ecu_error(self, p):
        """
        ecu : ECU error
        """

    def p_ecu_address_error(self, p):
        """
        ecu_address : ECU_ADDRESS error
        """

    def p_ecu_address_extension_error(self, p):
        """
        ecu_address_extension : ECU_ADDRESS_EXTENSION error
        """

    def p_ecu_calibration_offset_error(self, p):
        """
        ecu_calibration_offset : ECU_CALIBRATION_OFFSET error
        """

    def p_encoding_error(self, p):
        """
        encoding : ENCODING error
        """

    def p_epk_error(self, p):
        """
        epk : EPK error
        """

    def p_error_mask_error(self, p):
        """
        error_mask : ERROR_MASK error
        """

    def p_extended_limits_error(self, p):
        """
        extended_limits : EXTENDED_LIMITS error
        """

    def p_fix_axis_par_error(self, p):
        """
        fix_axis_par : FIX_AXIS_PAR error
        """

    def p_fix_axis_par_dist_error(self, p):
        """
        fix_axis_par_dist : FIX_AXIS_PAR_DIST error
        """

    def p_fix_axis_par_list_error(self, p):
        """
        fix_axis_par_list : BEGIN FIX_AXIS_PAR_LIST error END FIX_AXIS_PAR_LIST
                          | BEGIN FIX_AXIS_PAR_LIST END FIX_AXIS_PAR_LIST
        """

    def p_fix_no_axis_pts_x_error(self, p):
        """
        fix_no_axis_pts_x : FIX_NO_AXIS_PTS_X error
        """

    def p_fix_no_axis_pts_y_error(self, p):
        """
        fix_no_axis_pts_y : FIX_NO_AXIS_PTS_Y error
        """

    def p_fix_no_axis_pts_z_error(self, p):
        """
        fix_no_axis_pts_z : FIX_NO_AXIS_PTS_Z error
        """

    def p_fix_no_axis_pts_4_error(self, p):
        """
        fix_no_axis_pts_4 : FIX_NO_AXIS_PTS_4 error
        """

    def p_fix_no_axis_pts_5_error(self, p):
        """
        fix_no_axis_pts_5 : FIX_NO_AXIS_PTS_5 error
        """

    def p_fnc_values_error(self, p):
        """
        fnc_values : FNC_VALUES error
        """

    def p_format_error(self, p):
        """
        format : FORMAT error
        """

    def p_formula_error(self, p):
        """
        formula : BEGIN FORMULA error END FORMULA
                | BEGIN FORMULA END FORMULA
        """

    def p_formula_inv_error(self, p):
        """
        formula_inv : FORMULA_INV error
        """

    def p_frame_error(self, p):
        """
        frame : BEGIN FRAME error END FRAME
              | BEGIN FRAME END FRAME
        """

    def p_frame_measurement_error(self, p):
        """
        frame_measurement : FRAME_MEASUREMENT error
        """

    def p_function_error(self, p):
        """
        function : BEGIN FUNCTION error END FUNCTION
                 | BEGIN FUNCTION END FUNCTION
        """

    def p_function_list_error(self, p):
        """
        function_list : BEGIN FUNCTION_LIST error END FUNCTION_LIST
                      | BEGIN FUNCTION_LIST END FUNCTION_LIST
        """

    def p_function_version_error(self, p):
        """
        function_version : FUNCTION_VERSION error
        """

    def p_group_error(self, p):
        """
        group : BEGIN GROUP error END GROUP
              | BEGIN GROUP END GROUP
        """

    def p_header_error(self, p):
        """
        header : BEGIN HEADER error END HEADER
               | BEGIN HEADER END HEADER
        """

    def p_identification_error(self, p):
        """
        identification : IDENTIFICATION error
        """

    def p_if_data_error(self, p):
        """
        if_data : BEGIN IF_DATA error END IF_DATA
                | BEGIN IF_DATA END IF_DATA
        """

    def p_if_data_opt_error(self, p):
        """
        if_data_opt : error
        """
        # We allow all parsed tokens inside an IF_DATA block
        p[0] = p[1].value if p[1] else p[1]

    def p_in_measurement_error(self, p):
        """
        in_measurement : BEGIN IN_MEASUREMENT error END IN_MEASUREMENT
                       | BEGIN IN_MEASUREMENT END IN_MEASUREMENT
        """

    def p_input_quantity_error(self, p):
        """
        input_quantity : INPUT_QUANTITY error
        """

    def p_instance_error(self, p):
        """
        instance : BEGIN INSTANCE error END INSTANCE
                 | BEGIN INSTANCE END INSTANCE
        """

    def p_layout_error(self, p):
        """
        layout : LAYOUT error
        """

    def p_left_shift_error(self, p):
        """
        left_shift : LEFT_SHIFT error
        """

    def p_limits_error(self, p):
        """
        limits : LIMITS error
        """

    def p_loc_measurement_error(self, p):
        """
        loc_measurement : BEGIN LOC_MEASUREMENT error END LOC_MEASUREMENT
                        | BEGIN LOC_MEASUREMENT END LOC_MEASUREMENT
        """

    def p_map_list_error(self, p):
        """
        map_list : BEGIN MAP_LIST error END MAP_LIST
                 | BEGIN MAP_LIST END MAP_LIST
        """

    def p_matrix_dim_error(self, p):
        """
        matrix_dim : MATRIX_DIM error
        """

    def p_max_grad_error(self, p):
        """
        max_grad : MAX_GRAD error
        """

    def p_max_refresh_error(self, p):
        """
        max_refresh : MAX_REFRESH error
        """

    def p_measurement_error(self, p):
        """
        measurement : BEGIN MEASUREMENT error END MEASUREMENT
                    | BEGIN MEASUREMENT END MEASUREMENT
        """

    def p_memory_layout_error(self, p):
        """
        memory_layout : BEGIN MEMORY_LAYOUT error END MEMORY_LAYOUT
                      | BEGIN MEMORY_LAYOUT END MEMORY_LAYOUT
        """

    def p_memory_segment_error(self, p):
        """
        memory_segment : BEGIN MEMORY_SEGMENT error END MEMORY_SEGMENT
                       | BEGIN MEMORY_SEGMENT END MEMORY_SEGMENT
        """

    def p_mod_common_error(self, p):
        """
        mod_common : BEGIN MOD_COMMON error END MOD_COMMON
                   | BEGIN MOD_COMMON END MOD_COMMON
        """

    def p_mod_par_error(self, p):
        """
        mod_par : BEGIN MOD_PAR error END MOD_PAR
                | BEGIN MOD_PAR END MOD_PAR
        """

    def p_model_link_error(self, p):
        """
        model_link : MODEL_LINK error
        """

    def p_module_error(self, p):
        """
        module : BEGIN MODULE error END MODULE
               | BEGIN MODULE END MODULE
        """

    def p_monotony_error(self, p):
        """
        monotony : MONOTONY error
        """

    def p_no_axis_pts_x_error(self, p):
        """
        no_axis_pts_x : NO_AXIS_PTS_X error
        """

    def p_no_axis_pts_y_error(self, p):
        """
        no_axis_pts_y : NO_AXIS_PTS_Y error
        """

    def p_no_axis_pts_z_error(self, p):
        """
        no_axis_pts_z : NO_AXIS_PTS_Z error
        """

    def p_no_axis_pts_4_error(self, p):
        """
        no_axis_pts_4 : NO_AXIS_PTS_4 error
        """

    def p_no_axis_pts_5_error(self, p):
        """
        no_axis_pts_5 : NO_AXIS_PTS_5 error
        """

    def p_no_of_interfaces_error(self, p):
        """
        no_of_interfaces : NO_OF_INTERFACES error
        """

    def p_no_rescale_x_error(self, p):
        """
        no_rescale_x : NO_RESCALE_X error
        """

    def p_number_error(self, p):
        """
        number : NUMBER error
        """

    def p_offset_x_error(self, p):
        """
        offset_x : OFFSET_X error
        """

    def p_offset_y_error(self, p):
        """
        offset_y : OFFSET_Y error
        """

    def p_offset_z_error(self, p):
        """
        offset_z : OFFSET_Z error
        """

    def p_offset_4_error(self, p):
        """
        offset_4 : OFFSET_4 error
        """

    def p_offset_5_error(self, p):
        """
        offset_5 : OFFSET_5 error
        """

    def p_out_measurement_error(self, p):
        """
        out_measurement : BEGIN OUT_MEASUREMENT error END OUT_MEASUREMENT
                        | BEGIN OUT_MEASUREMENT END OUT_MEASUREMENT
        """

    def p_overwrite_error(self, p):
        """
        overwrite : BEGIN OVERWRITE error END OVERWRITE
                  | BEGIN OVERWRITE END OVERWRITE
        """

    def p_phone_no_error(self, p):
        """
        phone_no : PHONE_NO error
        """

    def p_phys_unit_error(self, p):
        """
        phys_unit : PHYS_UNIT error
        """

    def p_project_error(self, p):
        """
        project : BEGIN PROJECT error END PROJECT
                | BEGIN PROJECT END PROJECT
        """

    def p_project_no_error(self, p):
        """
        project_no : PROJECT_NO error
        """

    def p_record_layout_error(self, p):
        """
        record_layout : BEGIN RECORD_LAYOUT error END RECORD_LAYOUT
                      | BEGIN RECORD_LAYOUT END RECORD_LAYOUT
        """

    def p_ref_characteristic_error(self, p):
        """
        ref_characteristic : BEGIN REF_CHARACTERISTIC error END REF_CHARACTERISTIC
                           | BEGIN REF_CHARACTERISTIC END REF_CHARACTERISTIC
        """

    def p_ref_group_error(self, p):
        """
        ref_group : BEGIN REF_GROUP error END REF_GROUP
                  | BEGIN REF_GROUP END REF_GROUP
        """

    def p_ref_measurement_error(self, p):
        """
        ref_measurement : BEGIN REF_MEASUREMENT error END REF_MEASUREMENT
                        | BEGIN REF_MEASUREMENT END REF_MEASUREMENT
        """

    def p_ref_memory_segment_error(self, p):
        """
        ref_memory_segment : REF_MEMORY_SEGMENT error
        """

    def p_ref_unit_error(self, p):
        """
        ref_unit : REF_UNIT error
        """

    def p_reserved_error(self, p):
        """
        reserved : RESERVED error
        """

    def p_right_shift_error(self, p):
        """
        right_shift : RIGHT_SHIFT error
        """

    def p_rip_addr_w_error(self, p):
        """
        rip_addr_w : RIP_ADDR_W error
        """

    def p_rip_addr_x_error(self, p):
        """
        rip_addr_x : RIP_ADDR_X error
        """

    def p_rip_addr_y_error(self, p):
        """
        rip_addr_y : RIP_ADDR_Y error
        """

    def p_rip_addr_z_error(self, p):
        """
        rip_addr_z : RIP_ADDR_Z error
        """

    def p_rip_addr_4_error(self, p):
        """
        rip_addr_4 : RIP_ADDR_4 error
        """

    def p_rip_addr_5_error(self, p):
        """
        rip_addr_5 : RIP_ADDR_5 error
        """

    def p_shift_op_x_error(self, p):
        """
        shift_op_x : SHIFT_OP_X error
        """

    def p_shift_op_y_error(self, p):
        """
        shift_op_y : SHIFT_OP_Y error
        """

    def p_shift_op_z_error(self, p):
        """
        shift_op_z : SHIFT_OP_Z error
        """

    def p_shift_op_4_error(self, p):
        """
        shift_op_4 : SHIFT_OP_4 error
        """

    def p_shift_op_5_error(self, p):
        """
        shift_op_5 : SHIFT_OP_5 error
        """

    def p_si_exponents_error(self, p):
        """
        si_exponents : SI_EXPONENTS error
        """

    def p_src_addr_x_error(self, p):
        """
        src_addr_x : SRC_ADDR_X error
        """

    def p_src_addr_y_error(self, p):
        """
        src_addr_y : SRC_ADDR_Y error
        """

    def p_src_addr_z_error(self, p):
        """
        src_addr_z : SRC_ADDR_Z error
        """

    def p_src_addr_4_error(self, p):
        """
        src_addr_4 : SRC_ADDR_4 error
        """

    def p_src_addr_5_error(self, p):
        """
        src_addr_5 : SRC_ADDR_5 error
        """

    def p_status_string_ref_error(self, p):
        """
        status_string_ref : STATUS_STRING_REF error
        """

    def p_step_size_error(self, p):
        """
        step_size : STEP_SIZE error
        """

    def p_structure_component_error(self, p):
        """
        structure_component : BEGIN STRUCTURE_COMPONENT error END STRUCTURE_COMPONENT
                            | BEGIN STRUCTURE_COMPONENT END STRUCTURE_COMPONENT
        """

    def p_sub_function_error(self, p):
        """
        sub_function : BEGIN SUB_FUNCTION error END SUB_FUNCTION
                     | BEGIN SUB_FUNCTION END SUB_FUNCTION
        """

    def p_sub_group_error(self, p):
        """
        sub_group : BEGIN SUB_GROUP error END SUB_GROUP
                  | BEGIN SUB_GROUP END SUB_GROUP
        """

    def p_supplier_error(self, p):
        """
        supplier : SUPPLIER error
        """

    def p_symbol_link_error(self, p):
        """
        symbol_link : SYMBOL_LINK error
        """

    def p_symbol_type_link_error(self, p):
        """
        symbol_type_link : SYMBOL_TYPE_LINK error
        """

    def p_system_constant_error(self, p):
        """
        system_constant : SYSTEM_CONSTANT error
        """

    def p_transformer_error(self, p):
        """
        transformer : BEGIN TRANSFORMER error END TRANSFORMER
                    | BEGIN TRANSFORMER END TRANSFORMER
        """

    def p_transformer_in_objects_error(self, p):
        """
        transformer_in_objects : BEGIN TRANSFORMER_IN_OBJECTS error END TRANSFORMER_IN_OBJECTS
                               | BEGIN TRANSFORMER_IN_OBJECTS END TRANSFORMER_IN_OBJECTS
        """

    def p_transformer_out_objects_error(self, p):
        """
        transformer_out_objects : BEGIN TRANSFORMER_OUT_OBJECTS error END TRANSFORMER_OUT_OBJECTS
                                | BEGIN TRANSFORMER_OUT_OBJECTS END TRANSFORMER_OUT_OBJECTS
        """

    def p_typedef_axis_error(self, p):
        """
        typedef_axis : BEGIN TYPEDEF_AXIS error END TYPEDEF_AXIS
                     | BEGIN TYPEDEF_AXIS END TYPEDEF_AXIS
        """

    def p_typedef_blob_error(self, p):
        """
        typedef_blob : BEGIN TYPEDEF_BLOB error END TYPEDEF_BLOB
                     | BEGIN TYPEDEF_BLOB END TYPEDEF_BLOB
        """

    def p_typedef_characteristic_error(self, p):
        """
        typedef_characteristic : BEGIN TYPEDEF_CHARACTERISTIC error END TYPEDEF_CHARACTERISTIC
                               | BEGIN TYPEDEF_CHARACTERISTIC END TYPEDEF_CHARACTERISTIC
        """

    def p_typedef_measurement_error(self, p):
        """
        typedef_measurement : BEGIN TYPEDEF_MEASUREMENT error END TYPEDEF_MEASUREMENT
                            | BEGIN TYPEDEF_MEASUREMENT END TYPEDEF_MEASUREMENT
        """

    def p_typedef_structure(self, p):
        """
        typedef_structure : BEGIN TYPEDEF_STRUCTURE error END TYPEDEF_STRUCTURE
                          | BEGIN TYPEDEF_STRUCTURE END TYPEDEF_STRUCTURE
        """

    def p_unit_error(self, p):
        """
        unit : BEGIN UNIT error END UNIT
             | BEGIN UNIT END UNIT
        """

    def p_unit_conversion_error(self, p):
        """
        unit_conversion : UNIT_CONVERSION error
        """

    def p_user_error(self, p):
        """
        user : USER error
        """

    def p_user_rights_error(self, p):
        """
        user_rights : BEGIN USER_RIGHTS error END USER_RIGHTS
                    | BEGIN USER_RIGHTS END USER_RIGHTS
        """

    def p_var_address_error(self, p):
        """
        var_address : BEGIN VAR_ADDRESS error END VAR_ADDRESS
                    | BEGIN VAR_ADDRESS END VAR_ADDRESS
        """

    def p_var_characteristic_error(self, p):
        """
        var_characteristic : BEGIN VAR_CHARACTERISTIC error END VAR_CHARACTERISTIC
                           | BEGIN VAR_CHARACTERISTIC END VAR_CHARACTERISTIC
        """

    def p_var_criterion_error(self, p):
        """
        var_criterion : BEGIN VAR_CRITERION error END VAR_CRITERION
                      | BEGIN VAR_CRITERION END VAR_CRITERION
        """

    def p_var_forbidden_comb_error(self, p):
        """
        var_forbidden_comb : BEGIN VAR_FORBIDDEN_COMB error END VAR_FORBIDDEN_COMB
                           | BEGIN VAR_FORBIDDEN_COMB END VAR_FORBIDDEN_COMB
        """

    def p_var_measurement_error(self, p):
        """
        var_measurement : VAR_MEASUREMENT error
        """

    def p_var_naming_error(self, p):
        """
        var_naming : VAR_NAMING error
        """

    def p_var_selection_characteristic_error(self, p):
        """
        var_selection_characteristic : VAR_SELECTION_CHARACTERISTIC error
        """

    def p_var_separator_error(self, p):
        """
        var_seperator : VAR_SEPARATOR error
        """

    def p_variant_coding_error(self, p):
        """
        variant_coding : BEGIN VARIANT_CODING error END VARIANT_CODING
                       | BEGIN VARIANT_CODING END VARIANT_CODING
        """

    def p_version_error(self, p):
        """
        version : VERSION error
        """

    def p_virtual_error(self, p):
        """
        virtual : BEGIN VIRTUAL error END VIRTUAL
                | BEGIN VIRTUAL END VIRTUAL
        """

    def p_virtual_characteristic_error(self, p):
        """
        virtual_characteristic : BEGIN VIRTUAL_CHARACTERISTIC error END VIRTUAL_CHARACTERISTIC
                               | BEGIN VIRTUAL_CHARACTERISTIC END VIRTUAL_CHARACTERISTIC
        """

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


import a2lparser.gen.a2l_ast as ASTNodes
from a2lparser.a2l.ast.ast_node_stack import ASTNodeStack


# Some of this code is generated and does not follow snake_case naming
# pylint: disable=C0103
class RulesSections:
    """
    Grammar for parsing A2L sections.
    """

    def __init__(self):
        self.stack = ASTNodeStack()

    def p_a2ml_content_string(self, p):
        """
        a2ml_format_specification : A2ML_CONTENT
        """
        p[0] = p[1]

    def p_a2ml_block(self, p):
        """
        a2ml_block : a2ml_format_specification
        """
        p[0] = ASTNodes.A2ml(FormatSpecification=p[1])

    def p_a2ml_version(self, p):
        """
        a2ml_version : A2ML_VERSION constant constant
        """
        p[0] = ASTNodes.A2ml_Version(VersionNo=p[2], UpgradeNo=p[3])

    def p_addr_epk(self, p):
        """
        addr_epk : ADDR_EPK constant
        """
        p[0] = ASTNodes.Addr_Epk(Address=p[2])

    def p_address_type(self, p):
        """
        address_type : ADDRESS_TYPE addrtype_enum
        """
        p[0] = ASTNodes.Address_Type(AddressType=p[2])

    def p_asap2_version(self, p):
        """
        asap2_version : ASAP2_VERSION constant constant
        """
        p[0] = ASTNodes.Asap2_Version(VersionNo=p[2], UpgradeNo=p[3])

    def p_alignment_byte(self, p):
        """
        alignment_byte : ALIGNMENT_BYTE constant
        """
        p[0] = ASTNodes.Alignment_Byte(AlignmentBorder=p[2])

    def p_alignment_float16_ieee(self, p):
        """
        alignment_float16_ieee : ALIGNMENT_FLOAT16_IEEE constant
        """
        p[0] = ASTNodes.Alignment_Float16_Ieee(AlignmentBorder=p[2])

    def p_alignment_float32_ieee(self, p):
        """
        alignment_float32_ieee : ALIGNMENT_FLOAT32_IEEE constant
        """
        p[0] = ASTNodes.Alignment_Float32_Ieee(AlignmentBorder=p[2])

    def p_alignment_float64_ieee(self, p):
        """
        alignment_float64_ieee : ALIGNMENT_FLOAT64_IEEE constant
        """
        p[0] = ASTNodes.Alignment_Float64_Ieee(AlignmentBorder=p[2])

    def p_alignment_int64(self, p):
        """
        alignment_int64 : ALIGNMENT_INT64 constant
        """
        p[0] = ASTNodes.Alignment_Int64(AlignmentBorder=p[2])

    def p_alignment_long(self, p):
        """
        alignment_long : ALIGNMENT_LONG constant
        """
        p[0] = ASTNodes.Alignment_Long(AlignmentBorder=p[2])

    def p_alignment_word(self, p):
        """
        alignment_word : ALIGNMENT_WORD constant
        """
        p[0] = ASTNodes.Alignment_Word(AlignmentBorder=p[2])

    def p_annotation(self, p):
        """
        annotation : BEGIN ANNOTATION annotation_opt_list END ANNOTATION
        """
        p[0] = ASTNodes.Annotation(OptionalParams=p[3])
        self.stack.remove_node(ASTNodes.Annotation_Opt)

    def p_annotation_opt(self, p):
        """
        annotation_opt : annotation_label
                       | annotation_origin
                       | annotation_text
        """
        node = self.stack.get_or_create_node(ASTNodes.Annotation_Opt)
        self.stack.add_node_param(
            node, [ASTNodes.Annotation_Label, ASTNodes.Annotation_Origin, ASTNodes.Annotation_Text], p[1]
        )
        p[0] = node

    def p_annotation_opt_list(self, p):
        """
        annotation_opt_list : annotation_opt
                            | annotation_opt_list annotation_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_annotation_label(self, p):
        """
        annotation_label : ANNOTATION_LABEL string_literal
        """
        p[0] = ASTNodes.Annotation_Label(label=p[2])

    def p_annotation_origin(self, p):
        """
        annotation_origin : ANNOTATION_ORIGIN string_literal
        """
        p[0] = ASTNodes.Annotation_Origin(origin=p[2])

    def p_annotation_text(self, p):
        """
        annotation_text : BEGIN ANNOTATION_TEXT string_literal_list END ANNOTATION_TEXT
        """
        if len(p) > 2:
            p[0] = ASTNodes.Annotation_Text(annotation_text=p[3])

    def p_array_size(self, p):
        """
        array_size : ARRAY_SIZE constant
        """
        p[0] = ASTNodes.Array_Size(p[2])

    def p_ar_component(self, p):
        """
        ar_component : BEGIN AR_COMPONENT string_literal END AR_COMPONENT
                     | BEGIN AR_COMPONENT string_literal ar_prototype_of END AR_COMPONENT
        """
        p[0] = ASTNodes.Ar_Component(ComponentType=p[3])
        if len(p) == 7:
            ar_prototype_of = p[4].Name
            p[0].AR_Prototype_Of = ar_prototype_of

    def p_ar_prototype_of(self, p):
        """
        ar_prototype_of : AR_PROTOTYPE_OF string_literal
        """
        p[0] = ASTNodes.Ar_Prototype_Of(Name=p[2])

    def p_axis_descr(self, p):
        """
        axis_descr : BEGIN AXIS_DESCR \
                        axis_descr_enum ident ident constant constant constant \
                     END AXIS_DESCR

                   | BEGIN AXIS_DESCR \
                        axis_descr_enum ident ident constant constant constant axis_descr_opt_list \
                     END AXIS_DESCR
        """
        p[0] = ASTNodes.Axis_Descr(
            Attribute=p[3], InputQuantity=p[4], Conversion=p[5], MaxAxisPoints=p[6], LowerLimit=p[7], UpperLimit=p[8]
        )
        if len(p) == 12:
            p[0].OptionalParams = p[9]
            self.stack.remove_node(ASTNodes.Axis_Descr_Opt)

    def p_axis_descr_opt_params(self, p):
        """
        axis_descr_opt : axis_pts_ref
                       | byte_order
                       | curve_axis_ref
                       | deposit
                       | format
                       | max_grad
                       | monotony
                       | phys_unit
                       | read_only
                       | step_size

        """
        node = self.stack.get_or_create_node(ASTNodes.Axis_Descr_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Axis_Pts_Ref,
                ASTNodes.Byte_Order,
                ASTNodes.Curve_Axis_Ref,
                ASTNodes.Deposit,
                ASTNodes.Format,
                ASTNodes.Max_Grad,
                ASTNodes.Monotony,
                ASTNodes.Phys_Unit,
                ASTNodes.Read_Only,
                ASTNodes.Step_Size,
            ],
            param=p[1],
        )
        p[0] = node

    def p_axis_descr_opt_objects(self, p):
        """
        axis_descr_opt : extended_limits
                       | fix_axis_par
                       | fix_axis_par_dist
                       | fix_axis_par_list
        """
        node = self.stack.get_or_create_node(ASTNodes.Axis_Descr_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Extended_Limits,
                ASTNodes.Fix_Axis_Par,
                ASTNodes.Fix_Axis_Par_Dist,
                ASTNodes.Fix_Axis_Par_List,
            ],
            param=p[1],
        )
        p[0] = node

    def p_axis_descr_opt_objects_list(self, p):
        """
        axis_descr_opt : annotation
        """
        node = self.stack.get_or_create_node(ASTNodes.Axis_Descr_Opt)
        self.stack.add_node_object_list(node_class=node, ast_node_names=[ASTNodes.Annotation], param=p[1])
        p[0] = node

    def p_axis_descr_opt_list(self, p):
        """
        axis_descr_opt_list : axis_descr_opt
                            | axis_descr_opt_list axis_descr_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_axis_pts(self, p):
        """
        axis_pts : BEGIN AXIS_PTS \
                      ident string_literal constant ident ident constant ident constant constant constant \
                   END AXIS_PTS

                 | BEGIN AXIS_PTS \
                      ident string_literal constant ident ident constant ident constant constant constant axis_pts_opt_list \
                   END AXIS_PTS
        """
        p[0] = self.stack.create_node(
            ASTNodes.Axis_Pts(
                Name=p[3],
                LongIdentifier=p[4],
                Address=p[5],
                InputQuantity=p[6],
                Deposit_Ref=p[7],
                MaxDiff=p[8],
                Conversion=p[9],
                MaxAxisPoints=p[10],
                LowerLimit=p[11],
                UpperLimit=p[12],
            )
        )
        if len(p) == 16:
            p[0].OptionalParams = p[13]
            self.stack.remove_node(ASTNodes.Axis_Pts_Opt)

    def p_axis_pts_opt_params(self, p):
        """
        axis_pts_opt : byte_order
                     | calibration_access
                     | deposit
                     | display_identifier
                     | ecu_address_extension
                     | format
                     | guard_rails
                     | model_link
                     | monotony
                     | phys_unit
                     | read_only
                     | ref_memory_segment
                     | step_size
        """
        node = self.stack.get_or_create_node(ASTNodes.Axis_Pts_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Byte_Order,
                ASTNodes.Calibration_Access,
                ASTNodes.Deposit,
                ASTNodes.Display_Identifier,
                ASTNodes.Ecu_Address_Extension,
                ASTNodes.Format,
                ASTNodes.Guard_Rails,
                ASTNodes.Model_Link,
                ASTNodes.Monotony,
                ASTNodes.Phys_Unit,
                ASTNodes.Read_Only,
                ASTNodes.Ref_Memory_Segment,
                ASTNodes.Step_Size,
            ],
            param=p[1],
        )
        p[0] = node

    def p_axis_pts_opt_objects(self, p):
        """
        axis_pts_opt : extended_limits
                     | max_refresh
                     | symbol_link
                     | function_list
        """
        node = self.stack.get_or_create_node(ASTNodes.Axis_Pts_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Max_Refresh,
                ASTNodes.Extended_Limits,
                ASTNodes.Symbol_Link,
                ASTNodes.Function_List],
            param=p[1]
        )
        p[0] = node

    def p_axis_pts_opt_objects_list(self, p):
        """
        axis_pts_opt : annotation
                     | if_data
        """
        node = self.stack.get_or_create_node(ASTNodes.Axis_Pts_Opt)
        self.stack.add_node_object_list(node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.If_Data], param=p[1])
        p[0] = node

    def p_axis_pts_opt_list(self, p):
        """
        axis_pts_opt_list : axis_pts_opt
                          | axis_pts_opt_list axis_pts_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_axis_pts_ref(self, p):
        """
        axis_pts_ref : AXIS_PTS_REF ident
        """
        p[0] = ASTNodes.Axis_Pts_Ref(p[2])

    def p_axis_pts_x(self, p):
        """
        axis_pts_x : AXIS_PTS_X constant datatype_enum indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Pts_X(Position=p[2], Datatype=p[3], IndexIncr=p[4], Addressing=p[5])

    def p_axis_pts_y(self, p):
        """
        axis_pts_y : AXIS_PTS_Y constant datatype_enum indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Pts_Y(Position=p[2], Datatype=p[3], IndexIncr=p[4], Addressing=p[5])

    def p_axis_pts_z(self, p):
        """
        axis_pts_z : AXIS_PTS_Z constant datatype_enum indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Pts_Z(Position=p[2], Datatype=p[3], IndexIncr=p[4], Addressing=p[5])

    def p_axis_pts_4(self, p):
        """
        axis_pts_4 : AXIS_PTS_4 constant datatype_enum indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Pts_4(Position=p[2], Datatype=p[3], IndexIncr=p[4], Addressing=p[5])

    def p_axis_pts_5(self, p):
        """
        axis_pts_5 : AXIS_PTS_5 constant datatype_enum indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Pts_5(Position=p[2], Datatype=p[3], IndexIncr=p[4], Addressing=p[5])

    def p_axis_rescale_x(self, p):
        """
        axis_rescale_x : AXIS_RESCALE_X constant datatype_enum constant indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Rescale_X(
            Position=p[2], Datatype=p[3], MaxNumberOfRescalePairs=p[4], IndexIncr=p[5], Addressing=p[6]
        )

    def p_bit_mask(self, p):
        """
        bit_mask : BIT_MASK constant
        """
        p[0] = ASTNodes.Bit_Mask(p[2])

    def p_bit_operation(self, p):
        """
        bit_operation : BEGIN BIT_OPERATION bit_operation_opt_list END BIT_OPERATION
        """
        p[0] = ASTNodes.Bit_Operation(OptionalParams=p[3])
        self.stack.remove_node(ASTNodes.Bit_Operation_Opt)

    def p_bit_operation_opt(self, p):
        """
        bit_operation_opt : left_shift
                          | right_shift
                          | sign_extend

        """
        node = self.stack.get_or_create_node(ASTNodes.Bit_Operation_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Left_Shift,
                ASTNodes.Right_Shift,
                ASTNodes.Sign_Extend,
            ],
            param=p[1],
        )
        p[0] = node

    def p_bit_operation_opt_list(self, p):
        """
        bit_operation_opt_list : bit_operation_opt
                               | bit_operation_opt_list bit_operation_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_blob(self, p):
        """
        blob : BEGIN BLOB ident string_literal constant constant END BLOB
             | BEGIN BLOB ident string_literal constant constant blob_opt_list END BLOB
        """
        p[0] = ASTNodes.Blob(Name=p[3], LongIdentifier=p[4], Address=p[5], Size=p[6])

        if len(p) == 10:
            p[0].OptionalParams = p[7]
            self.stack.remove_node(ASTNodes.Blob_Opt)

    def p_blob_opt_list(self, p):
        """
        blob_opt_list : blob_opt
                      | blob_opt_list blob_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_blob_opt_params(self, p):
        """
        blob_opt : address_type
                 | calibration_access
                 | display_identifier
                 | ecu_address_extension
                 | model_link
        """
        node = self.stack.get_or_create_node(ASTNodes.Blob_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Address_Type,
                ASTNodes.Calibration_Access,
                ASTNodes.Display_Identifier,
                ASTNodes.Ecu_Address_Extension,
                ASTNodes.Model_Link,
            ],
            param=p[1],
        )
        p[0] = node

    def p_blob_opt_objects(self, p):
        """
        blob_opt : max_refresh
                 | symbol_link
        """
        node = self.stack.get_or_create_node(ASTNodes.Blob_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Max_Refresh,
                ASTNodes.Symbol_Link,
            ],
            param=p[1],
        )
        p[0] = node

    def p_blob_opt_objects_list(self, p):
        """
        blob_opt : annotation
                 | if_data
        """
        node = self.stack.get_or_create_node(ASTNodes.Blob_Opt)
        self.stack.add_node_object_list(
            node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.If_Data], param=p[1]
        )
        p[0] = node

    def p_byte_order(self, p):
        """
        byte_order : BYTE_ORDER byte_order_enum
        """
        p[0] = ASTNodes.Byte_Order(p[2])

    def p_calibration_access(self, p):
        """
        calibration_access : CALIBRATION_ACCESS calibration_access_enum
        """
        p[0] = ASTNodes.Calibration_Access(p[2])

    def p_calibration_handle(self, p):
        """
        calibration_handle : BEGIN CALIBRATION_HANDLE constant_list END CALIBRATION_HANDLE
                           | BEGIN CALIBRATION_HANDLE constant_list calibration_handle_text END CALIBRATION_HANDLE
        """
        p[0] = ASTNodes.Calibration_Handle(Handle=p[3])
        if len(p) == 7:
            p[0].Calibration_Handle_Text = p[4]

    def p_calibration_handle_text(self, p):
        """
        calibration_handle_text : CALIBRATION_HANDLE_TEXT string_literal
        """
        p[0] = ASTNodes.Calibration_Handle_Text(p[2])

    def p_calibration_method(self, p):
        """
        calibration_method : BEGIN CALIBRATION_METHOD string_literal constant END CALIBRATION_METHOD

                           | BEGIN CALIBRATION_METHOD \
                                string_literal constant calibration_method_opt_list \
                             END CALIBRATION_METHOD
        """
        if len(p) == 7:
            p[0] = ASTNodes.Calibration_Method(Method=p[3], Version=p[4])
        else:
            p[0] = ASTNodes.Calibration_Method(Method=p[3], Version=p[4], Calibration_Handle=p[5])

    def p_calibration_method_opt(self, p):
        """
        calibration_method_opt : calibration_handle
        """
        p[0] = p[1]

    def p_calibration_method_opt_list(self, p):
        """
        calibration_method_opt_list : calibration_method_opt
                                    | calibration_method_opt_list calibration_method_opt
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            if p[2] is not None:
                p[1].append(p[2])
            p[0] = p[1]

    def p_characteristic(self, p):
        """
        characteristic : BEGIN CHARACTERISTIC \
                            ident string_literal characteristic_enum constant ident constant ident constant constant \
                         END CHARACTERISTIC

                       | BEGIN CHARACTERISTIC \
                            ident string_literal characteristic_enum constant ident \
                            constant ident constant constant characteristic_opt_list \
                         END CHARACTERISTIC
        """
        p[0] = ASTNodes.Characteristic(
            Name=p[3],
            LongIdentifier=p[4],
            Type=p[5],
            Address=p[6],
            Deposit_Ref=p[7],
            MaxDiff=p[8],
            Conversion=p[9],
            LowerLimit=p[10],
            UpperLimit=p[11],
        )
        if len(p) == 15:
            p[0].OptionalParams = p[12]
            self.stack.remove_node(ASTNodes.Characteristic_Opt)

    def p_characteristic_opt_params(self, p):
        """
        characteristic_opt : bit_mask
                           | byte_order
                           | calibration_access
                           | comparison_quantity
                           | discrete
                           | display_identifier
                           | ecu_address_extension
                           | encoding
                           | format
                           | guard_rails
                           | number
                           | matrix_dim
                           | model_link
                           | phys_unit
                           | read_only
                           | ref_memory_segment
                           | step_size

        """
        node = self.stack.get_or_create_node(ASTNodes.Characteristic_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Bit_Mask,
                ASTNodes.Byte_Order,
                ASTNodes.Calibration_Access,
                ASTNodes.Comparison_Quantity,
                ASTNodes.Discrete,
                ASTNodes.Display_Identifier,
                ASTNodes.Ecu_Address_Extension,
                ASTNodes.Encoding,
                ASTNodes.Format,
                ASTNodes.Guard_Rails,
                ASTNodes.Number,
                ASTNodes.Matrix_Dim,
                ASTNodes.Model_Link,
                ASTNodes.Phys_Unit,
                ASTNodes.Read_Only,
                ASTNodes.Ref_Memory_Segment,
                ASTNodes.Step_Size,
            ],
            param=p[1],
        )
        p[0] = node

    def p_characteristic_opt_objects(self, p):
        """
        characteristic_opt : dependent_characteristic
                           | extended_limits
                           | function_list
                           | map_list
                           | max_refresh
                           | symbol_link
                           | virtual_characteristic
        """
        node = self.stack.get_or_create_node(ASTNodes.Characteristic_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Dependent_Characteristic,
                ASTNodes.Extended_Limits,
                ASTNodes.Function_List,
                ASTNodes.Map_List,
                ASTNodes.Max_Refresh,
                ASTNodes.Symbol_Link,
                ASTNodes.Virtual_Characteristic,
            ],
            param=p[1],
        )
        p[0] = node

    def p_characteristic_opt_objects_list(self, p):
        """
        characteristic_opt : annotation
                           | axis_descr
                           | if_data
        """
        node = self.stack.get_or_create_node(ASTNodes.Characteristic_Opt)
        self.stack.add_node_object_list(
            node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.Axis_Descr, ASTNodes.If_Data], param=p[1]
        )
        p[0] = node

    def p_characteristic_opt_list(self, p):
        """
        characteristic_opt_list : characteristic_opt
                                | characteristic_opt_list characteristic_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_coeffs(self, p):
        """
        coeffs : COEFFS constant constant constant constant constant constant
        """
        # float a b c d e f
        # f(x) = (axx + bx + c) / (dxx + ex + f)
        # INT = f(PHYS)
        p[0] = ASTNodes.Coeffs(a=p[2], b=p[3], c=p[4], d=p[5], e=p[6], f=p[7])

    def p_coeffs_linear(self, p):
        """
        coeffs_linear : COEFFS_LINEAR constant constant
        """
        # float a b
        # f(x) = ax + b
        # PHYS = f(INT)
        p[0] = ASTNodes.Coeffs_Linear(a=p[2], b=p[3])

    def p_comparison_quantity(self, p):
        """
        comparison_quantity : COMPARISON_QUANTITY ident
        """
        p[0] = ASTNodes.Comparison_Quantity(p[2])

    def p_compu_method(self, p):
        """
        compu_method : BEGIN COMPU_METHOD \
                           ident string_literal conversion_type_enum string_literal string_literal \
                       END COMPU_METHOD

                     | BEGIN COMPU_METHOD \
                           ident string_literal conversion_type_enum string_literal string_literal compu_method_opt_list \
                       END COMPU_METHOD
        """
        p[0] = ASTNodes.Compu_Method(Name=p[3], LongIdentifier=p[4], ConversionType=p[5], Format=p[6], Unit=p[7])
        if len(p) == 11:
            p[0].OptionalParams = p[8]
            self.stack.remove_node(ASTNodes.Compu_Method_Opt)

    def p_compu_method_opt_params(self, p):
        """
        compu_method_opt : compu_tab_ref
                         | ref_unit
                         | status_string_ref
        """
        node = self.stack.get_or_create_node(ASTNodes.Compu_Method_Opt)
        self.stack.add_node_param(
            node_class=node, ast_node_names=[ASTNodes.Compu_Tab_Ref, ASTNodes.Ref_Unit, ASTNodes.Status_String_Ref], param=p[1]
        )
        p[0] = node

    def p_compu_method_opt_objects(self, p):
        """
        compu_method_opt : coeffs
                         | coeffs_linear
                         | formula

        """
        node = self.stack.get_or_create_node(ASTNodes.Compu_Method_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Coeffs,
                ASTNodes.Coeffs_Linear,
                ASTNodes.Formula,
            ],
            param=p[1],
        )
        p[0] = node

    def p_compu_method_opt_list(self, p):
        """
        compu_method_opt_list : compu_method_opt
                              | compu_method_opt_list compu_method_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_compu_tab(self, p):
        """
        compu_tab : BEGIN COMPU_TAB \
                        ident string_literal conversion_type_enum constant axis_points_list \
                    END COMPU_TAB

                  | BEGIN COMPU_TAB \
                        ident string_literal conversion_type_enum constant axis_points_list compu_tab_opt_list \
                    END COMPU_TAB
        """
        p[0] = ASTNodes.Compu_Tab(Name=p[3], LongIdentifier=p[4], ConversionType=p[5], NumberValuePairs=p[6], Axis_Points=p[7])
        if len(p) == 11:
            p[0].OptionalParams = p[8]
            self.stack.remove_node(ASTNodes.Compu_Tab_Opt)

    def p_compu_tab_opt_params(self, p):
        """
        compu_tab_opt : default_value
                      | default_value_numeric

        """
        node = self.stack.get_or_create_node(ASTNodes.Compu_Tab_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Default_Value,
                ASTNodes.Default_Value_Numeric,
            ],
            param=p[1],
        )
        p[0] = node

    def p_compu_tab_opt_list(self, p):
        """
        compu_tab_opt_list : compu_tab_opt
                           | compu_tab_opt_list compu_tab_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_compu_tab_ref(self, p):
        """
        compu_tab_ref : COMPU_TAB_REF ident
        """
        p[0] = ASTNodes.Compu_Tab_Ref(p[2])

    def p_compu_vtab(self, p):
        """
        compu_vtab : BEGIN COMPU_VTAB \
                        ident string_literal conversion_type_enum constant inVal_outVal_list \
                     END COMPU_VTAB

                   | BEGIN COMPU_VTAB \
                        ident string_literal conversion_type_enum constant inVal_outVal_list default_value \
                     END COMPU_VTAB
        """
        p[0] = ASTNodes.Compu_Vtab(
            Name=p[3], LongIdentifier=p[4], ConversionType=p[5], NumberValuePairs=p[6], InVal_OutVal=p[7]
        )
        if len(p) == 11:
            p[0].Default_Value = getattr(p[8], p[8].__slots__[0])

    def p_compu_vtab_range(self, p):
        """
        compu_vtab_range     : BEGIN COMPU_VTAB_RANGE \
                                  ident string_literal constant inVal_MinMax_outVal_list \
                               END COMPU_VTAB_RANGE

                             | BEGIN COMPU_VTAB_RANGE \
                                   ident string_literal constant inVal_MinMax_outVal_list default_value \
                               END COMPU_VTAB_RANGE
        """
        p[0] = ASTNodes.Compu_Vtab_Range(Name=p[3], LongIdentifier=p[4], NumberValueTriples=p[5], InVal_MinMax_OutVal=p[6])
        if len(p) == 10:
            p[0].Default_Value = getattr(p[7], p[7].__slots__[0])

    def p_consistent_exchange(self, p):
        """
        consistent_exchange : CONSISTENT_EXCHANGE
        """
        p[0] = ASTNodes.Consistent_Exchange(True)

    def p_conversion(self, p):
        """
        conversion : CONVERSION ident
        """
        p[0] = ASTNodes.Conversion(ConversionMethod=p[2])

    def p_cpu_type(self, p):
        """
        cpu_type : CPU_TYPE string_literal
        """
        p[0] = ASTNodes.Cpu_Type(p[2])

    def p_curve_axis_ref(self, p):
        """
        curve_axis_ref : CURVE_AXIS_REF ident
        """
        p[0] = ASTNodes.Curve_Axis_Ref(p[2])

    def p_customer(self, p):
        """
        customer : CUSTOMER string_literal
        """
        p[0] = ASTNodes.Customer(p[2])

    def p_customer_no(self, p):
        """
        customer_no : CUSTOMER_NO string_literal
        """
        p[0] = ASTNodes.Customer_No(p[2])

    def p_data_size(self, p):
        """
        data_size : DATA_SIZE constant
        """
        p[0] = ASTNodes.Data_Size(p[2])

    def p_def_characteristic(self, p):
        """
        def_characteristic : BEGIN DEF_CHARACTERISTIC ident_list END DEF_CHARACTERISTIC
        """
        p[0] = ASTNodes.Def_Characteristic(p[3])

    def p_default_value(self, p):
        """
        default_value : DEFAULT_VALUE string_literal
        """
        p[0] = ASTNodes.Default_Value(p[2])

    def p_default_value_numeric(self, p):
        """
        default_value_numeric : DEFAULT_VALUE_NUMERIC constant
        """
        p[0] = ASTNodes.Default_Value_Numeric(p[2])

    def p_dependent_characteristic(self, p):
        """
        dependent_characteristic : BEGIN DEPENDENT_CHARACTERISTIC \
                                       string_literal ident_list \
                                   END DEPENDENT_CHARACTERISTIC
        """
        p[0] = ASTNodes.Dependent_Characteristic(Formula=p[3], Characteristic=p[4])

    def p_deposit(self, p):
        """
        deposit : DEPOSIT mode_enum
        """
        p[0] = ASTNodes.Deposit(p[2])

    def p_discrete(self, p):
        """
        discrete : DISCRETE
        """
        p[0] = ASTNodes.Discrete(Boolean=True)

    def p_display_identifier(self, p):
        """
        display_identifier : DISPLAY_IDENTIFIER ident
        """
        p[0] = ASTNodes.Display_Identifier(p[2])

    def p_dist_op_x(self, p):
        """
        dist_op_x : DIST_OP_X constant datatype_enum
        """
        p[0] = ASTNodes.Dist_Op_X(Position=p[2], Datatype=p[3])

    def p_dist_op_y(self, p):
        """
        dist_op_y : DIST_OP_Y constant datatype_enum
        """
        p[0] = ASTNodes.Dist_Op_Y(Position=p[2], Datatype=p[3])

    def p_dist_op_z(self, p):
        """
        dist_op_z : DIST_OP_Z constant datatype_enum
        """
        p[0] = ASTNodes.Dist_Op_Z(Position=p[2], Datatype=p[3])

    def p_dist_op_4(self, p):
        """
        dist_op_4 : DIST_OP_4 constant datatype_enum
        """
        p[0] = ASTNodes.Dist_Op_4(Position=p[2], Datatype=p[3])

    def p_dist_op_5(self, p):
        """
        dist_op_5 : DIST_OP_5 constant datatype_enum
        """
        p[0] = ASTNodes.Dist_Op_5(Position=p[2], Datatype=p[3])

    def p_ecu(self, p):
        """
        ecu : ECU string_literal
        """
        p[0] = ASTNodes.Ecu(p[2])

    def p_ecu_address(self, p):
        """
        ecu_address : ECU_ADDRESS constant
        """
        p[0] = ASTNodes.Ecu_Address(p[2])

    def p_ecu_address_extension(self, p):
        """
        ecu_address_extension : ECU_ADDRESS_EXTENSION constant
        """
        p[0] = ASTNodes.Ecu_Address_Extension(p[2])

    def p_ecu_calibration_offset(self, p):
        """
        ecu_calibration_offset : ECU_CALIBRATION_OFFSET constant
        """
        p[0] = ASTNodes.Ecu_Calibration_Offset(p[2])

    def p_encoding(self, p):
        """
        encoding : ENCODING encoding_enum
        """
        p[0] = ASTNodes.Encoding(Encoding=p[2])

    def p_epk(self, p):
        """
        epk : EPK string_literal
        """
        p[0] = ASTNodes.Epk(p[2])

    def p_error_mask(self, p):
        """
        error_mask : ERROR_MASK constant
        """
        p[0] = ASTNodes.Error_Mask(p[2])

    def p_extended_limits(self, p):
        """
        extended_limits : EXTENDED_LIMITS constant constant
        """
        p[0] = ASTNodes.Extended_Limits(LowerLimit=p[2], UpperLimit=p[3])

    def p_fix_axis_par(self, p):
        """
        fix_axis_par : FIX_AXIS_PAR constant constant constant
        """
        p[0] = ASTNodes.Fix_Axis_Par(Offset=p[2], Shift=p[3], Numberapo=p[4])

    def p_fix_axis_par_dist(self, p):
        """
        fix_axis_par_dist : FIX_AXIS_PAR_DIST constant constant constant
        """
        p[0] = ASTNodes.Fix_Axis_Par_Dist(Offset=p[2], Distance=p[3], Numberapo=p[4])

    def p_fix_axis_par_list(self, p):
        """
        fix_axis_par_list : BEGIN FIX_AXIS_PAR_LIST constant_list END FIX_AXIS_PAR_LIST
        """
        p[0] = ASTNodes.Fix_Axis_Par_List(p[3])

    def p_fix_no_axis_pts_x(self, p):
        """
        fix_no_axis_pts_x : FIX_NO_AXIS_PTS_X constant
        """
        p[0] = ASTNodes.Fix_No_Axis_Pts_X(p[2])

    def p_fix_no_axis_pts_y(self, p):
        """
        fix_no_axis_pts_y : FIX_NO_AXIS_PTS_Y constant
        """
        p[0] = ASTNodes.Fix_No_Axis_Pts_Y(p[2])

    def p_fix_no_axis_pts_z(self, p):
        """
        fix_no_axis_pts_z : FIX_NO_AXIS_PTS_Z constant
        """
        p[0] = ASTNodes.Fix_No_Axis_Pts_Z(p[2])

    def p_fix_no_axis_pts_4(self, p):
        """
        fix_no_axis_pts_4 : FIX_NO_AXIS_PTS_4 constant
        """
        p[0] = ASTNodes.Fix_No_Axis_Pts_4(p[2])

    def p_fix_no_axis_pts_5(self, p):
        """
        fix_no_axis_pts_5 : FIX_NO_AXIS_PTS_5 constant
        """
        p[0] = ASTNodes.Fix_No_Axis_Pts_5(p[2])

    def p_fnc_values(self, p):
        """
        fnc_values : FNC_VALUES constant datatype_enum indexmode_enum addrtype_enum
        """
        p[0] = ASTNodes.Fnc_Values(Position=p[2], Datatype=p[3], IndexMode=p[4], Addresstype=p[5])

    def p_format(self, p):
        """
        format : FORMAT string_literal
        """
        p[0] = ASTNodes.Format(p[2])

    def p_formula(self, p):
        """
        formula : BEGIN FORMULA string_literal END FORMULA
                | BEGIN FORMULA string_literal formula_inv END FORMULA
        """
        if len(p) == 6:
            p[0] = ASTNodes.Formula(f_x=p[3])
        else:
            p[0] = ASTNodes.Formula(f_x=p[3], Formula_Inv=p[4])

    def p_formula_inv(self, p):
        """
        formula_inv : FORMULA_INV string_literal
        """
        p[0] = ASTNodes.Formula_Inv(g_x=p[2])

    def p_frame(self, p):
        """
        frame     : BEGIN FRAME ident string_literal constant constant END FRAME
                  | BEGIN FRAME ident string_literal constant constant frame_opt_list END FRAME
        """
        p[0] = ASTNodes.Frame(Name=p[3], LongIdentifier=p[4], ScalingUnit=p[5], Rate=p[6])
        if len(p) == 10:
            p[0].OptionalParams = p[7]
            self.stack.remove_node(ASTNodes.Frame_Opt)

    def p_frame_opt_params(self, p):
        """
        frame_opt : frame_measurement
        """
        node = self.stack.get_or_create_node(ASTNodes.Frame_Opt)
        self.stack.add_node_param(node_class=node, ast_node_names=[ASTNodes.Frame_Measurement], param=p[1])
        p[0] = node

    def p_frame_opt_objects_list(self, p):
        """
        frame_opt : if_data
        """
        node = self.stack.get_or_create_node(ASTNodes.Frame_Opt)
        self.stack.add_node_object_list(node_class=node, ast_node_names=[ASTNodes.If_Data], param=p[1])
        p[0] = node

    def p_frame_opt_list(self, p):
        """
        frame_opt_list : frame_opt
                       | frame_opt_list frame_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_frame_measurement(self, p):
        """
        frame_measurement : FRAME_MEASUREMENT ident_list
        """
        p[0] = ASTNodes.Frame_Measurement(p[2])

    def p_function(self, p):
        """
        function : BEGIN FUNCTION ident string_literal END FUNCTION
                 | BEGIN FUNCTION ident string_literal function_opt_list END FUNCTION
        """
        p[0] = ASTNodes.Function(Name=p[3], LongIdentifier=p[4])
        if len(p) == 8:
            p[0].OptionalParams = p[5]
            self.stack.remove_node(ASTNodes.Function_Opt)

    def p_function_opt_params(self, p):
        """
        function_opt : function_version
        """
        node = self.stack.get_or_create_node(ASTNodes.Function_Opt)
        self.stack.add_node_param(node_class=node, ast_node_names=[ASTNodes.Function_Version], param=p[1])
        p[0] = node

    def p_function_opt_objects(self, p):
        """
        function_opt : ar_component
                     | def_characteristic
                     | in_measurement
                     | loc_measurement
                     | out_measurement
                     | ref_characteristic
                     | sub_function
        """
        node = self.stack.get_or_create_node(ASTNodes.Function_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Ar_Component,
                ASTNodes.Def_Characteristic,
                ASTNodes.In_Measurement,
                ASTNodes.Loc_Measurement,
                ASTNodes.Out_Measurement,
                ASTNodes.Ref_Characteristic,
                ASTNodes.Sub_Function,
            ],
            param=p[1],
        )
        p[0] = node

    def p_function_opt_objects_list(self, p):
        """
        function_opt : annotation
                     | if_data
        """
        node = self.stack.get_or_create_node(ASTNodes.Function_Opt)
        self.stack.add_node_object_list(
            node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.If_Data], param=p[1]
        )
        p[0] = node

    def p_function_opt_list(self, p):
        """
        function_opt_list : function_opt
                          | function_opt_list function_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_function_list(self, p):
        """
        function_list : BEGIN FUNCTION_LIST ident_list END FUNCTION_LIST
        """
        p[0] = ASTNodes.Function_List(Name=p[3])

    def p_function_version(self, p):
        """
        function_version : FUNCTION_VERSION string_literal
        """
        p[0] = ASTNodes.Function_Version(p[2])

    def p_group(self, p):
        """
        group : BEGIN GROUP ident string_literal END GROUP
              | BEGIN GROUP ident string_literal group_opt_list END GROUP
        """
        p[0] = ASTNodes.Group(GroupName=p[3], GroupLongIdentifier=p[4])
        if len(p) == 8:
            p[0].OptionalParams = p[5]
            self.stack.remove_node(ASTNodes.Group_Opt)

    def p_group_opt_params(self, p):
        """
        group_opt : root
        """
        node = self.stack.get_or_create_node(ASTNodes.Group_Opt)
        self.stack.add_node_param(node_class=node, ast_node_names=[ASTNodes.Root], param=p[1])
        p[0] = node

    def p_group_opt_objects(self, p):
        """
        group_opt : function_list
                  | ref_characteristic
                  | ref_measurement
                  | sub_group
        """
        node = self.stack.get_or_create_node(ASTNodes.Group_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[ASTNodes.Function_List, ASTNodes.Ref_Characteristic, ASTNodes.Ref_Measurement, ASTNodes.Sub_Group],
            param=p[1],
        )
        p[0] = node

    def p_group_opt_objects_list(self, p):
        """
        group_opt : annotation
                  | if_data
        """
        node = self.stack.get_or_create_node(ASTNodes.Group_Opt)
        self.stack.add_node_object_list(node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.If_Data], param=p[1])
        p[0] = node

    def p_group_opt_list(self, p):
        """
        group_opt_list : group_opt
                       | group_opt_list group_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_guard_rails(self, p):
        """
        guard_rails : GUARD_RAILS
        """
        p[0] = ASTNodes.Guard_Rails(Boolean=True)

    def p_header(self, p):
        """
        header : BEGIN HEADER string_literal END HEADER
               | BEGIN HEADER string_literal header_opt_list END HEADER
        """
        p[0] = ASTNodes.Header(Comment=p[3])
        if len(p) == 7:
            p[0].OptionalParams = p[4]
            self.stack.remove_node(ASTNodes.Header_Opt)

    def p_header_opt(self, p):
        """
        header_opt : project_no
                   | version
        """
        node = self.stack.get_or_create_node(ASTNodes.Header_Opt)
        self.stack.add_node_param(node_class=node, ast_node_names=[ASTNodes.Project_No, ASTNodes.Version], param=p[1])
        p[0] = node

    def p_header_opt_list(self, p):
        """
        header_opt_list : header_opt
                        | header_opt_list header_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_identification(self, p):
        """
        identification : IDENTIFICATION constant datatype_enum
        """
        p[0] = ASTNodes.Identification(Position=p[2], Datatype=p[3])

    def p_if_data(self, p):
        """
        if_data : if_data_begin if_data_opt_list if_data_end
        """
        data_params = [x for x in p[2] if not isinstance(x, ASTNodes.If_Data_Block)]
        if_data_block = [x for x in p[2] if isinstance(x, ASTNodes.If_Data_Block)]
        p[0] = ASTNodes.If_Data(
            Name=p[1], OptionalParams=ASTNodes.If_Data_Opt(DataParams=data_params, If_Data_Block=if_data_block)
        )

    def p_if_data_mandatory_only(self, p):
        """
        if_data : if_data_begin if_data_end
        """
        p[0] = ASTNodes.If_Data(Name=p[1])

    def p_if_data_begin(self, p):
        """
        if_data_begin : BEGIN IF_DATA ident
        """
        p[0] = p[3]

    def p_if_data_end(self, p):
        """
        if_data_end : END IF_DATA
                    | END
        """

    def p_if_data_opt_param(self, p):
        """
        if_data_opt : constant
                    | string_literal
                    | ident
                    | meta_block_keyword
                    | addrtype_enum
                    | attribute_enum
                    | axis_descr_enum
                    | byte_order_enum
                    | calibration_access_enum
                    | characteristic_enum
                    | conversion_type_enum
                    | datasize_enum
                    | datatype_enum
                    | encoding_enum
                    | mode_enum
                    | indexmode_enum
                    | indexorder_enum
                    | memorytype_enum
                    | monotony_enum
                    | transformer_trigger_enum
                    | prgtype_enum
                    | unit_type_enum
                    | tag_enum
        """
        p[0] = p[1]

    def p_if_data_opt_block(self, p):
        """
        if_data_opt : if_data_block
        """
        if p[1]:
            p[0] = p[1]

    def p_if_data_opt_list(self, p):
        """
        if_data_opt_list : if_data_opt
                         | if_data_opt_list if_data_opt
        """
        if len(p) > 2:
            p[1].append(p[2])
            p[0] = p[1]
        else:
            p[0] = [p[1]]

    def p_if_data_block(self, p):
        """
        if_data_block : if_data_block_begin if_data_opt_list if_data_block_end
        """
        if_data_block = [x for x in p[2] if isinstance(x, ASTNodes.If_Data_Block)]
        data_params = [x for x in p[2] if not isinstance(x, ASTNodes.If_Data_Block)]
        p[0] = ASTNodes.If_Data_Block(Name=p[1], DataParams=data_params, If_Data_Block=if_data_block)

    def p_if_data_block_empty(self, p):
        """
        if_data_block : if_data_block_begin if_data_block_end
        """
        p[0] = ASTNodes.If_Data_Block(Name=p[1])

    def p_if_data_block_begin(self, p):
        """
        if_data_block_begin : BEGIN ident
        """
        p[0] = p[2]

    def p_if_data_block_end(self, p):
        """
        if_data_block_end : END ident
        """
        p[0] = p[2]

    def p_in_measurement(self, p):
        """
        in_measurement : BEGIN IN_MEASUREMENT ident_list END IN_MEASUREMENT
        """
        p[0] = ASTNodes.In_Measurement(p[3])

    def p_input_quantity(self, p):
        """
        input_quantity : INPUT_QUANTITY ident
        """
        p[0] = ASTNodes.Input_Quantity(p[2])

    def p_instance(self, p):
        """
        instance : BEGIN INSTANCE ident string_literal ident constant END INSTANCE
                 | BEGIN INSTANCE ident string_literal ident constant instance_opt_list END INSTANCE
        """
        p[0] = ASTNodes.Instance(Name=p[3], LongIdentifier=p[4], TypedefName=p[5], Address=p[6])
        if len(p) == 10:
            p[0].OptionalParams = p[7]
            self.stack.remove_node(ASTNodes.Instance_Opt)

    def p_instance_opt_list(self, p):
        """
        instance_opt_list : instance_opt
                          | instance_opt_list instance_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_instance_opt_params(self, p):
        """
        instance_opt : address_type
                     | calibration_access
                     | display_identifier
                     | ecu_address_extension
                     | layout
                     | read_write
                     | matrix_dim
                     | model_link
        """
        node = self.stack.get_or_create_node(ASTNodes.Instance_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Address_Type,
                ASTNodes.Calibration_Access,
                ASTNodes.Display_Identifier,
                ASTNodes.Ecu_Address_Extension,
                ASTNodes.Layout,
                ASTNodes.Read_Write,
                ASTNodes.Matrix_Dim,
                ASTNodes.Model_Link,
            ],
            param=p[1],
        )
        p[0] = node

    def p_instance_opt_objects(self, p):
        """
        instance_opt : max_refresh
                     | symbol_link
        """
        node = self.stack.get_or_create_node(ASTNodes.Instance_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Max_Refresh,
                ASTNodes.Symbol_Link,
            ],
            param=p[1],
        )
        p[0] = node

    def p_instance_opt_objects_list(self, p):
        """
        instance_opt : annotation
                     | if_data
                     | overwrite
        """
        node = self.stack.get_or_create_node(ASTNodes.Instance_Opt)
        self.stack.add_node_object_list(
            node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.If_Data, ASTNodes.Overwrite], param=p[1]
        )
        p[0] = node

    def p_layout(self, p):
        """
        layout : LAYOUT indexmode_enum
        """
        # Description: This keyword describes the layout of a
        # multi-dimensional measurement array.
        # It can be used at MEASUREMENT.
        p[0] = ASTNodes.Layout(p[2])

    def p_left_shift(self, p):
        """
        left_shift : LEFT_SHIFT constant
        """
        # Description: The LEFT_SHIFT keyword is only used within the
        # BIT_OPERATION keyword. See description of BIT_OPERATION.
        p[0] = ASTNodes.Left_Shift(p[2])

    def p_limits(self, p):
        """
        limits : LIMITS constant constant
        """
        p[0] = ASTNodes.Limits(LowerLimit=p[2], UpperLimit=p[3])

    def p_loc_measurement(self, p):
        """
        loc_measurement : BEGIN LOC_MEASUREMENT ident_list END LOC_MEASUREMENT
        """
        p[0] = ASTNodes.Loc_Measurement(p[3])

    def p_map_list(self, p):
        """
        map_list : BEGIN MAP_LIST ident_list END MAP_LIST
        """
        p[0] = ASTNodes.Map_List(p[3])

    def p_matrix_dim(self, p):
        """
        matrix_dim : MATRIX_DIM constant constant constant
                   | MATRIX_DIM constant constant
                   | MATRIX_DIM constant
        """
        p[0] = ASTNodes.Matrix_Dim(Dim=p[2:])

    def p_max_grad(self, p):
        """
        max_grad : MAX_GRAD constant
        """
        p[0] = ASTNodes.Max_Grad(p[2])

    def p_max_refresh(self, p):
        """
        max_refresh : MAX_REFRESH constant constant
        """
        p[0] = ASTNodes.Max_Refresh(ScalingUnit=p[2], Rate=p[3])

    def p_measurement(self, p):
        """
        measurement : BEGIN MEASUREMENT \
                          ident string_literal datatype_enum ident \
                          constant constant constant constant \
                      END MEASUREMENT

                    | BEGIN MEASUREMENT \
                          ident string_literal datatype_enum ident \
                            constant constant constant constant \
                            measurement_opt_list \
                      END MEASUREMENT
        """
        p[0] = ASTNodes.Measurement(
            Name=p[3],
            LongIdentifier=p[4],
            Datatype=p[5],
            Conversion=p[6],
            Resolution=p[7],
            Accuracy=p[8],
            LowerLimit=p[9],
            UpperLimit=p[10],
        )
        if len(p) == 14:
            p[0].OptionalParams = p[11]
            self.stack.remove_node(ASTNodes.Measurement_Opt)

    def p_measurement_opt_params(self, p):
        """
        measurement_opt : array_size
                        | address_type
                        | bit_mask
                        | byte_order
                        | discrete
                        | display_identifier
                        | ecu_address
                        | ecu_address_extension
                        | error_mask
                        | format
                        | layout
                        | matrix_dim
                        | model_link
                        | phys_unit
                        | read_write
                        | ref_memory_segment

        """
        node = self.stack.get_or_create_node(ASTNodes.Measurement_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Array_Size,
                ASTNodes.Address_Type,
                ASTNodes.Bit_Mask,
                ASTNodes.Byte_Order,
                ASTNodes.Discrete,
                ASTNodes.Display_Identifier,
                ASTNodes.Ecu_Address,
                ASTNodes.Ecu_Address_Extension,
                ASTNodes.Error_Mask,
                ASTNodes.Format,
                ASTNodes.Layout,
                ASTNodes.Matrix_Dim,
                ASTNodes.Model_Link,
                ASTNodes.Phys_Unit,
                ASTNodes.Read_Write,
                ASTNodes.Ref_Memory_Segment,
            ],
            param=p[1],
        )
        p[0] = node

    def p_measurement_opt_objects(self, p):
        """
        measurement_opt : bit_operation
                        | function_list
                        | max_refresh
                        | symbol_link
                        | virtual
        """
        node = self.stack.get_or_create_node(ASTNodes.Measurement_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Bit_Operation,
                ASTNodes.Function_List,
                ASTNodes.Max_Refresh,
                ASTNodes.Symbol_Link,
                ASTNodes.Virtual,
            ],
            param=p[1],
        )
        p[0] = node

    def p_measurement_opt_objects_list(self, p):
        """
        measurement_opt : annotation
                        | if_data
        """
        node = self.stack.get_or_create_node(ASTNodes.Measurement_Opt)
        self.stack.add_node_object_list(node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.If_Data], param=p[1])
        p[0] = node

    def p_measurement_opt_list(self, p):
        """
        measurement_opt_list : measurement_opt
                             | measurement_opt_list measurement_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_memory_layout(self, p):
        """
        memory_layout : BEGIN MEMORY_LAYOUT \
                            prgtype_enum constant constant constant_list \
                        END MEMORY_LAYOUT

                      | BEGIN MEMORY_LAYOUT \
                            prgtype_enum constant constant constant_list memory_layout_opt_list \
                        END MEMORY_LAYOUT
        """
        p[0] = ASTNodes.Memory_Layout(PrgType=p[3], Address=p[4], Size=p[5], Offset=p[6])
        if len(p) == 10:
            p[0].If_Data = p[7]

    def p_memory_layout_opt(self, p):
        """
        memory_layout_opt : if_data
        """
        p[0] = p[1]

    def p_memory_layout_opt_list(self, p):
        """
        memory_layout_opt_list : memory_layout_opt
                               | memory_layout_opt_list memory_layout_opt
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_memory_segment(self, p):
        """
        memory_segment     : BEGIN MEMORY_SEGMENT \
                                 ident string_literal prgtype_enum memorytype_enum attribute_enum \
                                 constant constant constant_list \
                             END MEMORY_SEGMENT

                           | BEGIN MEMORY_SEGMENT \
                                 ident string_literal prgtype_enum memorytype_enum attribute_enum \
                                    constant constant constant_list memory_segment_opt_list \
                             END MEMORY_SEGMENT
        """
        p[0] = ASTNodes.Memory_Segment(
            Name=p[3], LongIdentifier=p[4], PrgType=p[5], MemoryType=p[6], Attribute=p[7], Address=p[8], Size=p[9], Offset=p[10]
        )

        if len(p) == 14:
            p[0].If_Data = p[11]

    def p_memory_segment_opt(self, p):
        """
        memory_segment_opt : if_data
        """
        p[0] = p[1]

    def p_memory_segment_opt_list(self, p):
        """
        memory_segment_opt_list : memory_segment_opt
                                | memory_segment_opt_list memory_segment_opt
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_mod_common(self, p):
        """
        mod_common : BEGIN MOD_COMMON string_literal END MOD_COMMON
                   | BEGIN MOD_COMMON string_literal mod_common_opt_list END MOD_COMMON
        """
        p[0] = ASTNodes.Mod_Common(Comment=p[3])
        if len(p) == 7:
            p[0].OptionalParams = p[4]
            self.stack.remove_node(ASTNodes.Mod_Common_Opt)

    def p_mod_common_opt(self, p):
        """
        mod_common_opt : alignment_byte
                       | alignment_float16_ieee
                       | alignment_float32_ieee
                       | alignment_float64_ieee
                       | alignment_int64
                       | alignment_long
                       | alignment_word
                       | byte_order
                       | data_size
                       | deposit
        """
        node = self.stack.get_or_create_node(ASTNodes.Mod_Common_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Alignment_Byte,
                ASTNodes.Alignment_Float16_Ieee,
                ASTNodes.Alignment_Float32_Ieee,
                ASTNodes.Alignment_Float64_Ieee,
                ASTNodes.Alignment_Int64,
                ASTNodes.Alignment_Long,
                ASTNodes.Alignment_Word,
                ASTNodes.Byte_Order,
                ASTNodes.Data_Size,
                ASTNodes.Deposit,
            ],
            param=p[1],
        )
        p[0] = node

    def p_mod_common_opt_list(self, p):
        """
        mod_common_opt_list : mod_common_opt
                            | mod_common_opt_list mod_common_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_mod_par(self, p):
        """
        mod_par : BEGIN MOD_PAR string_literal END MOD_PAR
                | BEGIN MOD_PAR string_literal mod_par_opt_list END MOD_PAR
        """
        p[0] = ASTNodes.Mod_Par(Comment=p[3])
        if len(p) == 7:
            p[0].OptionalParams = p[4]
            self.stack.remove_node(ASTNodes.Mod_Par_Opt)

    def p_mod_par_opt_params(self, p):
        """
        mod_par_opt : cpu_type
                    | customer
                    | customer_no
                    | ecu
                    | ecu_calibration_offset
                    | epk
                    | no_of_interfaces
                    | phone_no
                    | supplier
                    | user
                    | version

        """
        node = self.stack.get_or_create_node(ASTNodes.Mod_Par_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Cpu_Type,
                ASTNodes.Customer,
                ASTNodes.Customer_No,
                ASTNodes.Ecu,
                ASTNodes.Ecu_Calibration_Offset,
                ASTNodes.Epk,
                ASTNodes.No_Of_Interfaces,
                ASTNodes.Phone_No,
                ASTNodes.Supplier,
                ASTNodes.User,
                ASTNodes.Version,
            ],
            param=p[1],
        )
        p[0] = node

    def p_mod_par_opt_objects_list(self, p):
        """
        mod_par_opt : addr_epk
                    | calibration_method
                    | memory_layout
                    | memory_segment
                    | system_constant
        """
        node = self.stack.get_or_create_node(ASTNodes.Mod_Par_Opt)
        self.stack.add_node_object_list(
            node_class=node,
            ast_node_names=[
                ASTNodes.Addr_Epk,
                ASTNodes.Calibration_Method,
                ASTNodes.Memory_Layout,
                ASTNodes.Memory_Segment,
                ASTNodes.System_Constant,
            ],
            param=p[1],
        )
        p[0] = node

    def p_mod_par_opt_list(self, p):
        """
        mod_par_opt_list : mod_par_opt
                         | mod_par_opt_list mod_par_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_model_link(self, p):
        """
        model_link : MODEL_LINK string_literal
        """
        p[0] = ASTNodes.Model_Link(p[2])

    def p_module(self, p):
        """
        module : BEGIN MODULE ident string_literal END MODULE
               | BEGIN MODULE ident string_literal module_opt_list END MODULE
        """
        p[0] = ASTNodes.Module(Name=p[3], LongIdentifier=p[4])
        if len(p) == 8:
            p[0].OptionalParams = p[5]
            self.stack.remove_node(ASTNodes.Module_Opt)

    def p_module_opt_params(self, p):
        """
        module_opt : a2ml_block
        """
        node = self.stack.get_or_create_node(ASTNodes.Module_Opt)
        self.stack.add_node_param(node_class=node, ast_node_names=[ASTNodes.A2ml], param=p[1])
        p[0] = node

    def p_module_opt_objects(self, p):
        """
        module_opt : mod_common
                   | mod_par
                   | variant_coding
        """
        node = self.stack.get_or_create_node(ASTNodes.Module_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Mod_Common,
                ASTNodes.Mod_Par,
                ASTNodes.Variant_Coding,
            ],
            param=p[1],
        )
        p[0] = node

    def p_module_opt_objects_list(self, p):
        """
        module_opt : axis_pts
                   | blob
                   | characteristic
                   | compu_method
                   | compu_tab
                   | compu_vtab
                   | compu_vtab_range
                   | frame
                   | function
                   | group
                   | if_data
                   | instance
                   | measurement
                   | record_layout
                   | transformer
                   | typedef_axis
                   | typedef_blob
                   | typedef_characteristic
                   | typedef_measurement
                   | typedef_structure
                   | unit
                   | user_rights
        """
        node = self.stack.get_or_create_node(ASTNodes.Module_Opt)
        self.stack.add_node_object_list(
            node_class=node,
            ast_node_names=[
                ASTNodes.Axis_Pts,
                ASTNodes.Blob,
                ASTNodes.Characteristic,
                ASTNodes.Compu_Method,
                ASTNodes.Compu_Tab,
                ASTNodes.Compu_Vtab,
                ASTNodes.Compu_Vtab_Range,
                ASTNodes.Frame,
                ASTNodes.Function,
                ASTNodes.Group,
                ASTNodes.If_Data,
                ASTNodes.Instance,
                ASTNodes.Measurement,
                ASTNodes.Record_Layout,
                ASTNodes.Transformer,
                ASTNodes.Typedef_Axis,
                ASTNodes.Typedef_Blob,
                ASTNodes.Typedef_Characteristic,
                ASTNodes.Typedef_Measurement,
                ASTNodes.Typedef_Structure,
                ASTNodes.Unit,
                ASTNodes.User_Rights,
            ],
            param=p[1],
        )
        p[0] = node

    def p_module_opt_list(self, p):
        """
        module_opt_list : module_opt
                        | module_opt_list module_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_monotony(self, p):
        """
        monotony : MONOTONY monotony_enum
        """
        p[0] = ASTNodes.Monotony(p[2])

    def p_no_axis_pts_x(self, p):
        """
        no_axis_pts_x : NO_AXIS_PTS_X constant datatype_enum
        """
        p[0] = ASTNodes.No_Axis_Pts_X(Position=p[2], Datatype=p[3])

    def p_no_axis_pts_y(self, p):
        """
        no_axis_pts_y : NO_AXIS_PTS_Y constant datatype_enum
        """
        p[0] = ASTNodes.No_Axis_Pts_Y(Position=p[2], Datatype=p[3])

    def p_no_axis_pts_z(self, p):
        """
        no_axis_pts_z : NO_AXIS_PTS_Z constant datatype_enum
        """
        p[0] = ASTNodes.No_Axis_Pts_Z(Position=p[2], Datatype=p[3])

    def p_no_axis_pts_4(self, p):
        """
        no_axis_pts_4 : NO_AXIS_PTS_4 constant datatype_enum
        """
        p[0] = ASTNodes.No_Axis_Pts_4(Position=p[2], Datatype=p[3])

    def p_no_axis_pts_5(self, p):
        """
        no_axis_pts_5 : NO_AXIS_PTS_5 constant datatype_enum
        """
        p[0] = ASTNodes.No_Axis_Pts_5(Position=p[2], Datatype=p[3])

    def p_no_of_interfaces(self, p):
        """
        no_of_interfaces : NO_OF_INTERFACES constant
        """
        p[0] = ASTNodes.No_Of_Interfaces(p[2])

    def p_no_rescale_x(self, p):
        """
        no_rescale_x : NO_RESCALE_X constant datatype_enum
        """
        p[0] = ASTNodes.No_Rescale_X(Position=p[2], Datatype=p[3])

    def p_number(self, p):
        """
        number : NUMBER constant
        """
        p[0] = ASTNodes.Number(p[2])

    def p_offset_x(self, p):
        """
        offset_x : OFFSET_X constant datatype_enum
        """
        p[0] = ASTNodes.Offset_X(Position=p[2], Datatype=p[3])

    def p_offset_y(self, p):
        """
        offset_y : OFFSET_Y constant datatype_enum
        """
        p[0] = ASTNodes.Offset_Y(Position=p[2], Datatype=p[3])

    def p_offset_z(self, p):
        """
        offset_z : OFFSET_Z constant datatype_enum
        """
        p[0] = ASTNodes.Offset_Z(Position=p[2], Datatype=p[3])

    def p_offset_4(self, p):
        """
        offset_4 : OFFSET_4 constant datatype_enum
        """
        p[0] = ASTNodes.Offset_4(Position=p[2], Datatype=p[3])

    def p_offset_5(self, p):
        """
        offset_5 : OFFSET_5 constant datatype_enum
        """
        p[0] = ASTNodes.Offset_5(Position=p[2], Datatype=p[3])

    def p_out_measurement(self, p):
        """
        out_measurement : BEGIN OUT_MEASUREMENT ident_list END OUT_MEASUREMENT
        """
        p[0] = ASTNodes.Out_Measurement(p[3])

    def p_overwrite(self, p):
        """
        overwrite : BEGIN OVERWRITE ident constant END OVERWRITE
                  | BEGIN OVERWRITE ident constant overwrite_opt_list END OVERWRITE
        """
        p[0] = ASTNodes.Overwrite(Name=p[3], AxisNumber=p[4])
        if len(p) == 8:
            p[0].OptionalParams = p[5]
            self.stack.remove_node(ASTNodes.Overwrite_Opt)

    def p_overwrite_opt_list(self, p):
        """
        overwrite_opt_list : overwrite_opt
                           | overwrite_opt_list overwrite_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_overwirte_opt_params(self, p):
        """
        overwrite_opt : conversion
                      | format
                      | input_quantity
                      | monotony
                      | phys_unit
        """
        node = self.stack.get_or_create_node(ASTNodes.Overwrite_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Conversion,
                ASTNodes.Format,
                ASTNodes.Input_Quantity,
                ASTNodes.Monotony,
                ASTNodes.Phys_Unit,
            ],
            param=p[1],
        )
        p[0] = node

    def p_overwrite_opt_objects(self, p):
        """
        overwrite_opt : extended_limits
                      | limits
        """
        node = self.stack.get_or_create_node(ASTNodes.Overwrite_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Extended_Limits,
                ASTNodes.Limits,
            ],
            param=p[1],
        )
        p[0] = node

    def p_phone_no(self, p):
        """
        phone_no : PHONE_NO string_literal
        """
        p[0] = ASTNodes.Phone_No(p[2])

    def p_phys_unit(self, p):
        """
        phys_unit : PHYS_UNIT string_literal
        """
        p[0] = ASTNodes.Phys_Unit(p[2])

    def p_project(self, p):
        """
        project : BEGIN PROJECT ident string_literal END PROJECT
                | BEGIN PROJECT ident string_literal project_opt_list END PROJECT
        """
        p[0] = ASTNodes.Project(Name=p[3], LongIdentifier=p[4])
        if len(p) == 8:
            p[0].OptionalParams = p[5]
            self.stack.remove_node(ASTNodes.Project_Opt)

    def p_project_opt_objects(self, p):
        """
        project_opt : header
        """
        node = self.stack.get_or_create_node(ASTNodes.Project_Opt)
        self.stack.add_node_object(node_class=node, ast_node_names=[ASTNodes.Header], param=p[1])
        p[0] = node

    def p_project_opt_objects_list(self, p):
        """
        project_opt : module
        """
        node = self.stack.get_or_create_node(ASTNodes.Project_Opt)
        self.stack.add_node_object_list(node_class=node, ast_node_names=[ASTNodes.Module], param=p[1])
        p[0] = node

    def p_project_opt_list(self, p):
        """
        project_opt_list : project_opt
                         | project_opt_list project_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_project_no(self, p):
        """
        project_no : PROJECT_NO ident
        """
        p[0] = ASTNodes.Project_No(p[2])

    def p_read_only(self, p):
        """
        read_only : READ_ONLY
        """
        # This keyword is used to indicate that an adjustable
        # object cannot be changed (but can only be read).
        p[0] = ASTNodes.Read_Only(Boolean=True)

    def p_read_write(self, p):
        """
        read_write : READ_WRITE
        """
        # Description: This keyword is used to mark a measurement
        # object to be writeable.
        p[0] = ASTNodes.Read_Write(Boolean=True)

    def p_record_layout(self, p):
        """
        record_layout : BEGIN RECORD_LAYOUT ident END RECORD_LAYOUT
                      | BEGIN RECORD_LAYOUT ident record_layout_opt_list END RECORD_LAYOUT
        """
        p[0] = ASTNodes.Record_Layout(Name=p[3])
        if len(p) == 7:
            p[0].OptionalParams = p[4]
            self.stack.remove_node(ASTNodes.Record_Layout_Opt)

    def p_record_layout_opt_params(self, p):
        """
        record_layout_opt : alignment_byte
                          | alignment_float16_ieee
                          | alignment_float32_ieee
                          | alignment_float64_ieee
                          | alignment_int64
                          | alignment_long
                          | alignment_word
                          | fix_no_axis_pts_x
                          | fix_no_axis_pts_y
                          | fix_no_axis_pts_z
                          | fix_no_axis_pts_4
                          | fix_no_axis_pts_5
                          | static_address_offsets
                          | static_record_layout
        """
        node = self.stack.get_or_create_node(ASTNodes.Record_Layout_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Alignment_Byte,
                ASTNodes.Alignment_Float16_Ieee,
                ASTNodes.Alignment_Float32_Ieee,
                ASTNodes.Alignment_Float64_Ieee,
                ASTNodes.Alignment_Int64,
                ASTNodes.Alignment_Long,
                ASTNodes.Alignment_Word,
                ASTNodes.Fix_No_Axis_Pts_X,
                ASTNodes.Fix_No_Axis_Pts_Y,
                ASTNodes.Fix_No_Axis_Pts_Z,
                ASTNodes.Fix_No_Axis_Pts_4,
                ASTNodes.Fix_No_Axis_Pts_5,
                ASTNodes.Static_Address_Offsets,
                ASTNodes.Static_Record_Layout,
            ],
            param=p[1],
        )
        p[0] = node

    def p_record_layout_opt_objects(self, p):
        """
        record_layout_opt : axis_pts_x
                          | axis_pts_y
                          | axis_pts_z
                          | axis_pts_4
                          | axis_pts_5
                          | axis_rescale_x
                          | dist_op_x
                          | dist_op_y
                          | dist_op_z
                          | dist_op_4
                          | dist_op_5
                          | fnc_values
                          | identification
                          | no_axis_pts_x
                          | no_axis_pts_y
                          | no_axis_pts_z
                          | no_axis_pts_4
                          | no_axis_pts_5
                          | no_rescale_x
                          | offset_x
                          | offset_y
                          | offset_z
                          | offset_4
                          | offset_5
                          | rip_addr_x
                          | rip_addr_w
                          | rip_addr_y
                          | rip_addr_z
                          | rip_addr_4
                          | rip_addr_5
                          | src_addr_x
                          | src_addr_y
                          | src_addr_z
                          | src_addr_4
                          | src_addr_5
                          | shift_op_x
                          | shift_op_y
                          | shift_op_z
                          | shift_op_4
                          | shift_op_5
        """
        node = self.stack.get_or_create_node(ASTNodes.Record_Layout_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Axis_Pts_X,
                ASTNodes.Axis_Pts_Y,
                ASTNodes.Axis_Pts_Z,
                ASTNodes.Axis_Pts_4,
                ASTNodes.Axis_Pts_5,
                ASTNodes.Axis_Rescale_X,
                ASTNodes.Dist_Op_X,
                ASTNodes.Dist_Op_Y,
                ASTNodes.Dist_Op_Z,
                ASTNodes.Dist_Op_4,
                ASTNodes.Dist_Op_5,
                ASTNodes.Fnc_Values,
                ASTNodes.Identification,
                ASTNodes.No_Axis_Pts_X,
                ASTNodes.No_Axis_Pts_Y,
                ASTNodes.No_Axis_Pts_Z,
                ASTNodes.No_Axis_Pts_4,
                ASTNodes.No_Axis_Pts_5,
                ASTNodes.No_Rescale_X,
                ASTNodes.Offset_X,
                ASTNodes.Offset_Y,
                ASTNodes.Offset_Z,
                ASTNodes.Offset_4,
                ASTNodes.Offset_5,
                ASTNodes.Rip_Addr_W,
                ASTNodes.Rip_Addr_X,
                ASTNodes.Rip_Addr_Y,
                ASTNodes.Rip_Addr_Z,
                ASTNodes.Rip_Addr_4,
                ASTNodes.Rip_Addr_5,
                ASTNodes.Src_Addr_X,
                ASTNodes.Src_Addr_Y,
                ASTNodes.Src_Addr_Z,
                ASTNodes.Src_Addr_4,
                ASTNodes.Src_Addr_5,
                ASTNodes.Shift_Op_X,
                ASTNodes.Shift_Op_Y,
                ASTNodes.Shift_Op_Z,
                ASTNodes.Shift_Op_4,
                ASTNodes.Shift_Op_5,
            ],
            param=p[1],
        )
        p[0] = node

    def p_record_layout_opt_objects_list(self, p):
        """
        record_layout_opt : reserved
        """
        node = self.stack.get_or_create_node(ASTNodes.Record_Layout_Opt)
        self.stack.add_node_object_list(node_class=node, ast_node_names=[ASTNodes.Reserved], param=p[1])
        p[0] = node

    def p_record_layout_opt_list(self, p):
        """
        record_layout_opt_list : record_layout_opt
                               | record_layout_opt_list record_layout_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_ref_characteristic(self, p):
        """
        ref_characteristic : BEGIN REF_CHARACTERISTIC ident_list END REF_CHARACTERISTIC
        """
        p[0] = ASTNodes.Ref_Characteristic(Identifier=p[3])

    def p_ref_group(self, p):
        """
        ref_group : BEGIN REF_GROUP ident_list END REF_GROUP
        """
        p[0] = ASTNodes.Ref_Group(Identifier=p[3])

    def p_ref_measurement(self, p):
        """
        ref_measurement : BEGIN REF_MEASUREMENT ident_list END REF_MEASUREMENT
        """
        p[0] = ASTNodes.Ref_Measurement(Identifier=p[3])

    def p_ref_memory_segment(self, p):
        """
        ref_memory_segment : REF_MEMORY_SEGMENT ident
        """
        p[0] = ASTNodes.Ref_Memory_Segment(p[2])

    def p_ref_unit(self, p):
        """
        ref_unit : REF_UNIT ident
        """
        p[0] = ASTNodes.Ref_Unit(p[2])

    def p_reserved(self, p):
        """
        reserved : RESERVED constant datasize_enum
        """
        p[0] = ASTNodes.Reserved(Position=p[2], DataSize=p[3])

    def p_right_shift(self, p):
        """
        right_shift : RIGHT_SHIFT constant
        """
        p[0] = ASTNodes.Right_Shift(p[2])

    def p_rip_addr_w(self, p):
        """
        rip_addr_w : RIP_ADDR_W constant datatype_enum
        """
        p[0] = ASTNodes.Rip_Addr_W(Position=p[2], Datatype=p[3])

    def p_rip_addr_x(self, p):
        """
        rip_addr_x : RIP_ADDR_X constant datatype_enum
        """
        p[0] = ASTNodes.Rip_Addr_X(Position=p[2], Datatype=p[3])

    def p_rip_addr_y(self, p):
        """
        rip_addr_y : RIP_ADDR_Y constant datatype_enum
        """
        p[0] = ASTNodes.Rip_Addr_Y(Position=p[2], Datatype=p[3])

    def p_rip_addr_z(self, p):
        """
        rip_addr_z : RIP_ADDR_Z constant datatype_enum
        """
        p[0] = ASTNodes.Rip_Addr_Z(Position=p[2], Datatype=p[3])

    def p_rip_addr_4(self, p):
        """
        rip_addr_4 : RIP_ADDR_4 constant datatype_enum
        """
        p[0] = ASTNodes.Rip_Addr_4(Position=p[2], Datatype=p[3])

    def p_rip_addr_5(self, p):
        """
        rip_addr_5 : RIP_ADDR_5 constant datatype_enum
        """
        p[0] = ASTNodes.Rip_Addr_5(Position=p[2], Datatype=p[3])

    def p_root(self, p):
        """
        root : ROOT
        """
        p[0] = ASTNodes.Root(Boolean=True)

    def p_shift_op_x(self, p):
        """
        shift_op_x : SHIFT_OP_X constant datatype_enum
        """
        p[0] = ASTNodes.Shift_Op_X(Position=p[2], Datatype=p[3])

    def p_shift_op_y(self, p):
        """
        shift_op_y : SHIFT_OP_Y constant datatype_enum
        """
        p[0] = ASTNodes.Shift_Op_Y(Position=p[2], Datatype=p[3])

    def p_shift_op_z(self, p):
        """
        shift_op_z : SHIFT_OP_Z constant datatype_enum
        """
        p[0] = ASTNodes.Shift_Op_Z(Position=p[2], Datatype=p[3])

    def p_shift_op_4(self, p):
        """
        shift_op_4 : SHIFT_OP_4 constant datatype_enum
        """
        p[0] = ASTNodes.Shift_Op_4(Position=p[2], Datatype=p[3])

    def p_shift_op_5(self, p):
        """
        shift_op_5 : SHIFT_OP_5 constant datatype_enum
        """
        p[0] = ASTNodes.Shift_Op_5(Position=p[2], Datatype=p[3])

    def p_sign_extend(self, p):
        """
        sign_extend : SIGN_EXTEND
        """
        p[0] = ASTNodes.Sign_Extend(Boolean=True)

    def p_si_exponents(self, p):
        """
        si_exponents : SI_EXPONENTS constant constant constant constant constant constant constant
        """
        p[0] = ASTNodes.Si_Exponents(
            Length=p[2],
            Mass=p[3],
            Time=p[4],
            ElectricCurrent=p[5],
            Temperature=p[6],
            AmountOfSubstance=p[7],
            LuminousIntensity=p[8],
        )

    def p_src_addr_x(self, p):
        """
        src_addr_x : SRC_ADDR_X constant datatype_enum
        """
        p[0] = ASTNodes.Src_Addr_X(Position=p[2], Datatype=p[3])

    def p_src_addr_y(self, p):
        """
        src_addr_y : SRC_ADDR_Y constant datatype_enum
        """
        p[0] = ASTNodes.Src_Addr_Y(Position=p[2], Datatype=p[3])

    def p_src_addr_z(self, p):
        """
        src_addr_z : SRC_ADDR_Z constant datatype_enum
        """
        p[0] = ASTNodes.Src_Addr_Z(Position=p[2], Datatype=p[3])

    def p_src_addr_4(self, p):
        """
        src_addr_4 : SRC_ADDR_4 constant datatype_enum
        """
        p[0] = ASTNodes.Src_Addr_4(Position=p[2], Datatype=p[3])

    def p_src_addr_5(self, p):
        """
        src_addr_5 : SRC_ADDR_5 constant datatype_enum
        """
        p[0] = ASTNodes.Src_Addr_5(Position=p[2], Datatype=p[3])

    def p_static_address_offsets(self, p):
        """
        static_address_offsets : STATIC_ADDRESS_OFFSETS
        """
        p[0] = ASTNodes.Static_Address_Offsets(Boolean=True)

    def p_static_record_layout(self, p):
        """
        static_record_layout : STATIC_RECORD_LAYOUT
        """
        p[0] = ASTNodes.Static_Record_Layout(Boolean=True)

    def p_status_string_ref(self, p):
        """
        status_string_ref : STATUS_STRING_REF ident
        """
        # ConversionTable
        p[0] = ASTNodes.Status_String_Ref(p[2])

    def p_step_size(self, p):
        """
        step_size : STEP_SIZE constant
        """
        p[0] = ASTNodes.Step_Size(p[2])

    def p_structure_component(self, p):
        """
        structure_component : BEGIN STRUCTURE_COMPONENT ident ident constant END STRUCTURE_COMPONENT
                            | BEGIN STRUCTURE_COMPONENT \
                                ident ident constant structure_component_opt_list \
                              END STRUCTURE_COMPONENT
        """
        p[0] = ASTNodes.Structure_Component(Name=p[3], TypedefName=p[4], AddressOffset=p[5])
        if len(p) == 9:
            p[0].OptionalParams = p[6]
            self.stack.remove_node(ASTNodes.Structure_Component_Opt)

    def p_structure_component_opt_list(self, p):
        """
        structure_component_opt_list : structure_component_opt
                                     | structure_component_opt_list structure_component_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_structure_component_opt_params(self, p):
        """
        structure_component_opt : address_type
                                | layout
                                | matrix_dim
                                | symbol_type_link
        """
        node = self.stack.get_or_create_node(ASTNodes.Structure_Component_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Address_Type,
                ASTNodes.Layout,
                ASTNodes.Matrix_Dim,
                ASTNodes.Symbol_Type_Link,
            ],
            param=p[1],
        )
        p[0] = node

    def p_sub_function(self, p):
        """
        sub_function : BEGIN SUB_FUNCTION ident_list END SUB_FUNCTION
        """
        p[0] = ASTNodes.Sub_Function(Identifier=p[3])

    def p_sub_group(self, p):
        """
        sub_group : BEGIN SUB_GROUP ident_list END SUB_GROUP
        """
        p[0] = ASTNodes.Sub_Group(p[3])

    def p_supplier(self, p):
        """
        supplier : SUPPLIER string_literal
        """
        p[0] = ASTNodes.Supplier(p[2])

    def p_symbol_link(self, p):
        """
        symbol_link : SYMBOL_LINK string_literal constant
        """
        p[0] = ASTNodes.Symbol_Link(SymbolName=p[2], Offset=p[3])

    def p_symbol_type_link(self, p):
        """
        symbol_type_link : SYMBOL_TYPE_LINK string_literal
        """
        p[0] = ASTNodes.Symbol_Type_Link(SymbolName=p[2])

    def p_system_constant(self, p):
        """
        system_constant : SYSTEM_CONSTANT string_literal string_literal
        """
        p[0] = ASTNodes.System_Constant(Name=p[2], Value=p[3])

    def p_transformer(self, p):
        """
        transformer : BEGIN TRANSFORMER \
                        ident string_literal string_literal string_literal \
                        constant transformer_trigger_enum ident \
                      END TRANSFORMER
                    | BEGIN TRANSFORMER \
                        ident string_literal string_literal string_literal \
                        constant transformer_trigger_enum ident transformer_opt_list \
                      END TRANSFORMER

        """
        p[0] = ASTNodes.Transformer(Name=p[3], Version=p[4], Executable32=p[5], Executable64=p[6],
                                    Timeout=p[7], Trigger=p[8], InverseTransformer=p[9])
        if len(p) == 13:
            p[0].OptionalParams = p[10]
            self.stack.remove_node(ASTNodes.Transformer_Opt)

    def p_transformer_opt_list(self, p):
        """
        transformer_opt_list : transformer_opt
                             | transformer_opt_list transformer_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_transformer_opt_params(self, p):
        """
        transformer_opt : transformer_in_objects
                        | transformer_out_objects
        """
        node = self.stack.get_or_create_node(ASTNodes.Transformer_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Transformer_In_Objects,
                ASTNodes.Transformer_Out_Objects,
            ],
            param=p[1],
        )
        p[0] = node

    def p_transformer_in_objects(self, p):
        """
        transformer_in_objects : BEGIN TRANSFORMER_IN_OBJECTS ident_list END TRANSFORMER_IN_OBJECTS
        """
        p[0] = ASTNodes.Transformer_In_Objects(p[3])

    def p_transformer_out_objects(self, p):
        """
        transformer_out_objects : BEGIN TRANSFORMER_OUT_OBJECTS ident_list END TRANSFORMER_OUT_OBJECTS
        """
        p[0] = ASTNodes.Transformer_Out_Objects(p[3])

    def p_typedef_axis(self, p):
        """
        typedef_axis : BEGIN TYPEDEF_AXIS \
                        ident string_literal ident ident constant \
                        ident constant constant constant \
                       END TYPEDEF_AXIS
                     | BEGIN TYPEDEF_AXIS \
                        ident string_literal ident ident constant \
                        ident constant constant constant typedef_axis_opt_list \
                       END TYPEDEF_AXIS
        """
        p[0] = ASTNodes.Typedef_Axis(Name=p[3],
                                     LongIdentifier=p[4],
                                     InputQuantity=p[5],
                                     RecordLayout=p[6],
                                     MaxDiff=p[7],
                                     Conversion=p[8],
                                     MaxAxisPoints=p[9],
                                     LowerLimit=p[10],
                                     UpperLimit=p[11])
        if len(p) == 15:
            p[0].OptionalParams = p[12]
            self.stack.remove_node(ASTNodes.Typedef_Axis_Opt)

    def p_typedef_axis_opt_list(self, p):
        """
        typedef_axis_opt_list : typedef_axis_opt
                              | typedef_axis_opt_list typedef_axis_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_typedef_axis_opt_params(self, p):
        """
        typedef_axis_opt : byte_order
                         | deposit
                         | format
                         | monotony
                         | phys_unit
                         | step_size
        """
        node = self.stack.get_or_create_node(ASTNodes.Typedef_Axis_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Byte_Order,
                ASTNodes.Deposit,
                ASTNodes.Format,
                ASTNodes.Monotony,
                ASTNodes.Phys_Unit,
                ASTNodes.Step_Size
            ],
            param=p[1],
        )
        p[0] = node

    def p_typedef_axis_opt_objects(self, p):
        """
        typedef_axis_opt : extended_limits
        """
        node = self.stack.get_or_create_node(ASTNodes.Typedef_Axis_Opt)
        self.stack.add_node_object(node_class=node, ast_node_names=[ASTNodes.Extended_Limits], param=p[1])
        p[0] = node

    def p_typedef_blob(self, p):
        """
        typedef_blob : BEGIN TYPEDEF_BLOB ident string_literal constant END TYPEDEF_BLOB
                     | BEGIN TYPEDEF_BLOB ident string_literal constant address_type END TYPEDEF_BLOB
        """
        if len(p) == 8:
            p[0] = ASTNodes.Typedef_Blob(Name=p[3], LongIdentifier=p[4], Size=p[5])
        elif len(p) == 9:
            address_type = p[6].AddressType
            p[0] = ASTNodes.Typedef_Blob(Name=p[3], LongIdentifier=p[4], Size=p[5], Address_Type=address_type)

    def p_typedef_characteristic(self, p):
        """
        typedef_characteristic : BEGIN TYPEDEF_CHARACTERISTIC \
                                    ident string_literal characteristic_enum ident constant \
                                    ident constant constant  \
                                 END TYPEDEF_CHARACTERISTIC
                               | BEGIN TYPEDEF_CHARACTERISTIC \
                                    ident string_literal characteristic_enum ident constant \
                                    ident constant constant typedef_characteristic_opt_list \
                                 END TYPEDEF_CHARACTERISTIC
        """
        p[0] = ASTNodes.Typedef_Characteristic(Name=p[3],
                                               LongIdentifier=p[4],
                                               Type=p[5],
                                               RecordLayout=p[6],
                                               MaxDiff=p[7],
                                               Conversion=p[8],
                                               LowerLimit=p[9],
                                               UpperLimit=p[10])
        if len(p) == 14:
            p[0].OptionalParams = p[11]
            self.stack.remove_node(ASTNodes.Typedef_Characteristic_Opt)

    def p_typedef_characteristic_opt_list(self, p):
        """
        typedef_characteristic_opt_list : typedef_characteristic_opt
                                        | typedef_characteristic_opt_list typedef_characteristic_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_typedef_characteristic_opt_params(self, p):
        """
        typedef_characteristic_opt : bit_mask
                                   | byte_order
                                   | discrete
                                   | encoding
                                   | format
                                   | matrix_dim
                                   | number
                                   | phys_unit
                                   | step_size
        """
        node = self.stack.get_or_create_node(ASTNodes.Typedef_Characteristic_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Bit_Mask,
                ASTNodes.Byte_Order,
                ASTNodes.Discrete,
                ASTNodes.Encoding,
                ASTNodes.Format,
                ASTNodes.Matrix_Dim,
                ASTNodes.Number,
                ASTNodes.Phys_Unit,
                ASTNodes.Step_Size,
            ],
            param=p[1],
        )
        p[0] = node

    def p_typedef_characteristic_opt_objects(self, p):
        """
        typedef_characteristic_opt : extended_limits
        """
        node = self.stack.get_or_create_node(ASTNodes.Typedef_Characteristic_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Extended_Limits,
            ],
            param=p[1],
        )
        p[0] = node

    def p_typedef_characteristic_opt_objects_list(self, p):
        """
        typedef_characteristic_opt : axis_descr
        """
        node = self.stack.get_or_create_node(ASTNodes.Typedef_Characteristic_Opt)
        self.stack.add_node_object_list(node_class=node, ast_node_names=[ASTNodes.Axis_Descr], param=p[1])
        p[0] = node

    def p_typedef_measurement(self, p):
        """
        typedef_measurement : BEGIN TYPEDEF_MEASUREMENT \
                                ident string_literal datatype_enum ident constant \
                                constant constant constant  \
                              END TYPEDEF_MEASUREMENT
                            | BEGIN TYPEDEF_MEASUREMENT \
                                ident string_literal datatype_enum ident constant \
                                constant constant constant typedef_measurement_opt_list \
                              END TYPEDEF_MEASUREMENT
        """
        p[0] = ASTNodes.Typedef_Measurement(Name=p[3],
                                            LongIdentifier=p[4],
                                            Datatype=p[5],
                                            Conversion=p[6],
                                            Resolution=p[7],
                                            Accuracy=p[8],
                                            LowerLimit=p[9],
                                            UpperLimit=p[10])
        if len(p) == 14:
            p[0].OptionalParams = p[11]
            self.stack.remove_node(ASTNodes.Typedef_Measurement_Opt)

    def p_typedef_measurement_opt_list(self, p):
        """
        typedef_measurement_opt_list : typedef_measurement_opt
                                     | typedef_measurement_opt_list typedef_measurement_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_typedef_measurement_opt_params(self, p):
        """
        typedef_measurement_opt : address_type
                                | bit_mask
                                | byte_order
                                | discrete
                                | error_mask
                                | format
                                | layout
                                | matrix_dim
                                | phys_unit
        """
        node = self.stack.get_or_create_node(ASTNodes.Typedef_Measurement_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Address_Type,
                ASTNodes.Bit_Mask,
                ASTNodes.Byte_Order,
                ASTNodes.Discrete,
                ASTNodes.Error_Mask,
                ASTNodes.Format,
                ASTNodes.Layout,
                ASTNodes.Matrix_Dim,
                ASTNodes.Phys_Unit,
            ],
            param=p[1],
        )
        p[0] = node

    def p_typedef_measurement_opt_objects(self, p):
        """
        typedef_measurement_opt : bit_operation
        """
        node = self.stack.get_or_create_node(ASTNodes.Typedef_Measurement_Opt)
        self.stack.add_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Bit_Operation,
            ],
            param=p[1],
        )
        p[0] = node

    def p_typedef_structure(self, p):
        """
        typedef_structure : BEGIN TYPEDEF_STRUCTURE ident string_literal constant END TYPEDEF_STRUCTURE
                          | BEGIN TYPEDEF_STRUCTURE \
                                ident string_literal constant \
                                typedef_structure_opt_list \
                            END TYPEDEF_STRUCTURE
        """
        p[0] = ASTNodes.Typedef_Structure(Name=p[3], LongIdentifier=p[4], Size=p[5])
        if len(p) == 9:
            p[0].OptionalParams = p[6]
            self.stack.remove_node(ASTNodes.Typedef_Structure_Opt)

    def p_typedef_structure_opt_list(self, p):
        """
        typedef_structure_opt_list : typedef_structure_opt
                                   | typedef_structure_opt_list typedef_structure_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_typedef_structure_opt_params(self, p):
        """
        typedef_structure_opt : address_type
                              | consistent_exchange
                              | symbol_type_link
        """
        node = self.stack.get_or_create_node(ASTNodes.Typedef_Structure_Opt)
        self.stack.add_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Address_Type,
                ASTNodes.Consistent_Exchange,
                ASTNodes.Symbol_Type_Link,
            ],
            param=p[1],
        )
        p[0] = node

    def p_typedef_structure_opt_objects_list(self, p):
        """
        typedef_structure_opt : structure_component
        """
        node = self.stack.get_or_create_node(ASTNodes.Typedef_Structure_Opt)
        self.stack.add_node_object_list(node_class=node, ast_node_names=[ASTNodes.Structure_Component], param=p[1])
        p[0] = node

    def p_unit(self, p):
        """
        unit : BEGIN UNIT ident string_literal string_literal unit_type_enum END UNIT
             | BEGIN UNIT ident string_literal string_literal unit_type_enum unit_opt_list END UNIT
        """
        p[0] = ASTNodes.Unit(Name=p[3], LongIdentifier=p[4], Display=p[5], Type=p[6])
        if len(p) == 10:
            p[0].OptionalParams = p[7]
            self.stack.remove_node(ASTNodes.Unit_Opt)

    def p_unit_opt_params(self, p):
        """
        unit_opt : ref_unit
        """
        node = self.stack.get_or_create_node(ASTNodes.Unit_Opt)
        self.stack.add_node_param(node_class=node, ast_node_names=[ASTNodes.Ref_Unit], param=p[1])
        p[0] = node

    def p_unit_opt_objects(self, p):
        """
        unit_opt : si_exponents
                 | unit_conversion
        """
        node = self.stack.get_or_create_node(ASTNodes.Unit_Opt)
        self.stack.add_node_object(node_class=node, ast_node_names=[
                                   ASTNodes.Si_Exponents, ASTNodes.Unit_Conversion], param=p[1])
        p[0] = node

    def p_unit_opt_list(self, p):
        """
        unit_opt_list : unit_opt
                      | unit_opt_list unit_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_unit_conversion(self, p):
        """
        unit_conversion : UNIT_CONVERSION constant constant
        """
        p[0] = ASTNodes.Unit_Conversion(Gradient=p[2], Offset=p[3])

    def p_user(self, p):
        """
        user : USER string_literal
        """
        p[0] = ASTNodes.User(p[2])

    def p_user_rights(self, p):
        """
        user_rights : BEGIN USER_RIGHTS ident END USER_RIGHTS
                    | BEGIN USER_RIGHTS ident user_rights_opt_list END USER_RIGHTS
        """
        p[0] = ASTNodes.User_Rights(UserLevelId=p[3])
        if len(p) == 7:
            p[0].OptionalParams = p[4]
            self.stack.remove_node(ASTNodes.User_Rights_Opt)

    def p_user_rights_opt_params(self, p):
        """
        user_rights_opt : read_only
        """
        node = self.stack.get_or_create_node(ASTNodes.User_Rights_Opt)
        self.stack.add_node_param(node_class=node, ast_node_names=[ASTNodes.Read_Only], param=p[1])
        p[0] = node

    def p_user_rights_opt_objects_list(self, p):
        """
        user_rights_opt : ref_group
        """
        node = self.stack.get_or_create_node(ASTNodes.User_Rights_Opt)
        self.stack.add_node_object_list(node_class=node, ast_node_names=[ASTNodes.Ref_Group], param=p[1])
        p[0] = node

    def p_user_rights_opt_list(self, p):
        """
        user_rights_opt_list : user_rights_opt
                             | user_rights_opt_list user_rights_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_var_address(self, p):
        """
        var_address : BEGIN VAR_ADDRESS constant_list END VAR_ADDRESS
        """
        if len(p) > 2:
            p[0] = ASTNodes.Var_Address(p[3])

    def p_var_characteristic(self, p):
        """
        var_characteristic : BEGIN VAR_CHARACTERISTIC ident END VAR_CHARACTERISTIC
                           | BEGIN VAR_CHARACTERISTIC ident ident_list END VAR_CHARACTERISTIC
                           | BEGIN VAR_CHARACTERISTIC ident ident_list var_address END VAR_CHARACTERISTIC
        """
        if len(p) == 8:
            p[0] = ASTNodes.Var_Characteristic(Name=p[3], CriterionName=p[4], Var_Address=p[5])
        elif len(p) == 7:
            p[0] = ASTNodes.Var_Characteristic(Name=p[3], CriterionName=p[4])
        else:
            p[0] = ASTNodes.Var_Characteristic(Name=p[3])

    def p_var_criterion(self, p):
        """
        var_criterion : BEGIN VAR_CRITERION ident string_literal END VAR_CRITERION
                      | BEGIN VAR_CRITERION ident string_literal ident_list END VAR_CRITERION
                      | BEGIN VAR_CRITERION ident string_literal ident_list var_criterion_opt_list END VAR_CRITERION
        """
        if len(p) == 9:
            p[0] = ASTNodes.Var_Criterion(Name=p[3], LongIdentifier=p[4], Value=p[5], OptionalParams=p[6])
            self.stack.remove_node(ASTNodes.Var_Criterion_Opt)
        elif len(p) == 8:
            p[0] = ASTNodes.Var_Criterion(Name=p[3], LongIdentifier=p[4], Value=p[5])
        else:
            p[0] = ASTNodes.Var_Criterion(Name=p[3], LongIdentifier=p[4])

    def p_var_criterion_opt(self, p):
        """
        var_criterion_opt : var_measurement
                          | var_selection_characteristic

        """
        node = self.stack.get_or_create_node(ASTNodes.Var_Criterion_Opt)
        self.stack.add_node_param(
            node_class=node, ast_node_names=[ASTNodes.Var_Measurement, ASTNodes.Var_Selection_Characteristic], param=p[1]
        )
        p[0] = node

    def p_var_criterion_opt_list(self, p):
        """
        var_criterion_opt_list : var_criterion_opt
                               | var_criterion_opt_list var_criterion_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_var_forbidden_comb(self, p):
        """
        var_forbidden_comb : BEGIN VAR_FORBIDDEN_COMB ident_ident_list END VAR_FORBIDDEN_COMB
        """
        p[0] = ASTNodes.Var_Forbidden_Comb(p[3])

    def p_var_measurement(self, p):
        """
        var_measurement : VAR_MEASUREMENT ident
        """
        p[0] = ASTNodes.Var_Measurement(p[2])

    def p_var_naming(self, p):
        """
        var_naming : VAR_NAMING tag_enum
        """
        p[0] = ASTNodes.Var_Naming(p[2])

    def p_var_selection_characteristic(self, p):
        """
        var_selection_characteristic : VAR_SELECTION_CHARACTERISTIC ident
        """
        p[0] = ASTNodes.Var_Selection_Characteristic(p[2])

    def p_var_separator(self, p):
        """
        var_seperator : VAR_SEPARATOR string_literal
        """
        p[0] = ASTNodes.Var_Separator(p[2])

    def p_variant_coding(self, p):
        """
        variant_coding : BEGIN VARIANT_CODING variant_coding_opt_list END VARIANT_CODING
        """
        p[0] = ASTNodes.Variant_Coding(OptionalParams=p[3])
        self.stack.remove_node(ASTNodes.Variant_Coding_Opt)

    def p_variant_coding_opt_params(self, p):
        """
        variant_coding_opt : var_naming
                           | var_seperator

        """
        node = self.stack.get_or_create_node(ASTNodes.Variant_Coding_Opt)
        self.stack.add_node_param(node_class=node, ast_node_names=[ASTNodes.Var_Naming, ASTNodes.Var_Separator], param=p[1])
        p[0] = node

    def p_variant_coding_opt_objects_list(self, p):
        """
        variant_coding_opt : var_characteristic
                           | var_criterion
                           | var_forbidden_comb
        """
        node = self.stack.get_or_create_node(ASTNodes.Variant_Coding_Opt)
        self.stack.add_node_object_list(
            node_class=node,
            ast_node_names=[ASTNodes.Var_Characteristic, ASTNodes.Var_Criterion, ASTNodes.Var_Forbidden_Comb],
            param=p[1],
        )
        p[0] = node

    def p_variant_coding_opt_list(self, p):
        """
        variant_coding_opt_list : variant_coding_opt
                                | variant_coding_opt_list variant_coding_opt
        """
        p[0] = p[1] if len(p) == 2 else p[2]

    def p_version(self, p):
        """
        version : VERSION string_literal
        """
        p[0] = ASTNodes.Version(p[2])

    def p_virtual(self, p):
        """
        virtual : BEGIN VIRTUAL ident_list END VIRTUAL
        """
        p[0] = ASTNodes.Virtual(MeasuringChannel=p[3])

    def p_virtual_characteristic(self, p):
        """
        virtual_characteristic : BEGIN VIRTUAL_CHARACTERISTIC string_literal END VIRTUAL_CHARACTERISTIC
                               | BEGIN VIRTUAL_CHARACTERISTIC string_literal ident_list END VIRTUAL_CHARACTERISTIC
        """
        if len(p) == 7:
            p[0] = ASTNodes.Virtual_Characteristic(Formula=p[3], Characteristic=p[4])
        else:
            p[0] = ASTNodes.Virtual_Characteristic(Formula=p[3])

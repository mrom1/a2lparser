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


# Some of this code is generated and does not follow snake_case naming
# Some docstrings are long
# pylint: disable=C0103, C0301, R0904
# flake8: noqa
class RulesSections:
    """
    Grammar for parsing A2L sections.
    """

    def __init__(self):
        self.ast_scope_stack = []

    def _create_ast_node(self, node):
        self.ast_scope_stack.append(node)
        return self.ast_scope_stack[-1]

    def _get_ast_node(self, node, reverse=True):
        if reverse:
            for _node in reversed(self.ast_scope_stack):
                if isinstance(_node, node):
                    return _node
            return None
        for _node in self.ast_scope_stack:
            if isinstance(_node, node):
                return _node
        return None

    def _get_or_create_ast_node(self, node, reverse=True):
        _node = self._get_ast_node(node=node, reverse=reverse)
        if _node is None:
            _node = self._create_ast_node(node=node())
        return _node

    def _remove_ast_node(self, node, reverse=True, single_remove=False) -> None:
        if reverse:
            for _node in reversed(self.ast_scope_stack):
                if isinstance(_node, node):  # type: ignore
                    self.ast_scope_stack.remove(_node)
                    if single_remove:
                        break
        else:
            for _node in self.ast_scope_stack:
                if isinstance(_node, node):  # type: ignore
                    self.ast_scope_stack.remove(_node)

    def _add_ast_node_object(self, node_class, ast_node_names, param):
        for _node in ast_node_names:
            if isinstance(param, _node):
                setattr(node_class, param.__class__.__name__, param)

    def _add_ast_node_object_list(self, node_class, ast_node_names, param):
        for _node in ast_node_names:
            if isinstance(param, _node):
                if getattr(node_class, param.__class__.__name__) is None:
                    setattr(node_class, param.__class__.__name__, [param])
                else:
                    getattr(node_class, param.__class__.__name__).append(param)

    def _add_ast_node_param(self, node_class, ast_node_names, param):
        for _node in ast_node_names:
            if isinstance(param, _node):
                setattr(node_class, param.__class__.__name__, getattr(param, param.__slots__[0]))

    def p_A2L_section_error(self, p):
        """
        a2l_section_error : BEGIN meta_block_keyword error END meta_block_keyword
                          | BEGIN meta_block_keyword error END
        """
        if len(self.ast_scope_stack) > 0:
            p[0] = ASTNodes.NodeCorrupted(p[2], self.ast_scope_stack[-1])

    def p_A2ML_VERSION(self, p):
        """
        a2ml_version     : A2ML_VERSION constant constant
        """
        p[0] = ASTNodes.A2ml_Version(VersionNo=p[2], UpgradeNo=p[3])

    def p_ADDR_EPK(self, p):
        """
        addr_epk     : ADDR_EPK constant
        """
        p[0] = ASTNodes.Addr_Epk(Address=p[2])

    def p_ASAP2_VERSION(self, p):
        """
        asap2_version     : ASAP2_VERSION constant constant
        """
        p[0] = ASTNodes.Asap2_Version(VersionNo=p[2], UpgradeNo=p[3])

    def p_ALIGNMENT_BYTE(self, p):
        """
        alignment_byte     : ALIGNMENT_BYTE constant
        """
        p[0] = ASTNodes.Alignment_Byte(AlignmentBorder=p[2])

    def p_ALIGNMENT_FLOAT32_IEEE(self, p):
        """
        alignment_float32_ieee     : ALIGNMENT_FLOAT32_IEEE constant
        """
        p[0] = ASTNodes.Alignment_Float32_Ieee(AlignmentBorder=p[2])

    def p_ALIGNMENT_FLOAT64_IEEE(self, p):
        """
        alignment_float64_ieee     : ALIGNMENT_FLOAT64_IEEE constant
        """
        p[0] = ASTNodes.Alignment_Float64_Ieee(AlignmentBorder=p[2])

    def p_ALIGNMENT_INT64(self, p):
        """
        alignment_int64     : ALIGNMENT_INT64 constant
        """
        p[0] = ASTNodes.Alignment_Int64(AlignmentBorder=p[2])

    def p_ALIGNMENT_LONG(self, p):
        """
        alignment_long     : ALIGNMENT_LONG constant
        """
        p[0] = ASTNodes.Alignment_Long(AlignmentBorder=p[2])

    def p_ALIGNMENT_WORD(self, p):
        """
        alignment_word     : ALIGNMENT_WORD constant
        """
        p[0] = ASTNodes.Alignment_Word(AlignmentBorder=p[2])

    def p_ANNOTATION(self, p):
        """
        annotation     : BEGIN ANNOTATION annotation_opt_list END ANNOTATION

        """
        if len(p) > 2 and p[3]:
            p[0] = ASTNodes.Annotation(OptionalParams=p[3])
        self._remove_ast_node(ASTNodes.Annotation_Opt)

    def p_ANNOTATION_opt(self, p):
        """
        annotation_opt    : annotation_label
                          | annotation_origin
                          | annotation_text
        """
        if p[1]:
            node = self._get_or_create_ast_node(ASTNodes.Annotation_Opt)
            self._add_ast_node_param(
                node, [ASTNodes.Annotation_Label, ASTNodes.Annotation_Origin, ASTNodes.Annotation_Text], p[1]
            )
            p[0] = node

    def p_ANNOTATION_opt_list(self, p):
        """
        annotation_opt_list    : annotation_opt
                               | annotation_opt_list annotation_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_ANNOTATION_LABEL(self, p):
        """
        annotation_label     : ANNOTATION_LABEL string_literal
        """
        p[0] = ASTNodes.Annotation_Label(label=p[2])

    def p_ANNOTATION_ORIGIN(self, p):
        """
        annotation_origin     : ANNOTATION_ORIGIN string_literal
        """
        p[0] = ASTNodes.Annotation_Origin(origin=p[2])

    def p_ANNOTATION_TEXT(self, p):
        """
        annotation_text     : BEGIN ANNOTATION_TEXT string_literal_list END ANNOTATION_TEXT
        """
        if len(p) > 2:
            p[0] = ASTNodes.Annotation_Text(annotation_text=p[3])

    def p_ARRAY_SIZE(self, p):
        """
        array_size     : ARRAY_SIZE constant
        """
        p[0] = ASTNodes.Array_Size(p[2])

    def p_AXIS_DESCR(self, p):
        """
        axis_descr     : BEGIN AXIS_DESCR axis_descr_enum ident ident constant constant constant END AXIS_DESCR
                       | BEGIN AXIS_DESCR axis_descr_enum ident ident constant constant constant axis_descr_opt_list END AXIS_DESCR
        """
        if len(p) > 2:
            p[0] = ASTNodes.Axis_Descr(
                Attribute=p[3], InputQuantity=p[4], Conversion=p[5], MaxAxisPoints=p[6], LowerLimit=p[7], UpperLimit=p[8]
            )

            if len(p) == 12:
                p[0].OptionalParams = p[9]

            self._remove_ast_node(ASTNodes.Axis_Descr_Opt)

    def p_AXIS_DESCR_opt_params(self, p):
        """
        axis_descr_opt    : axis_pts_ref
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
        node = self._get_or_create_ast_node(ASTNodes.Axis_Descr_Opt)
        self._add_ast_node_param(
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

    def p_AXIS_DESCR_opt_objects(self, p):
        """
        axis_descr_opt    : extended_limits
                          | fix_axis_par
                          | fix_axis_par_dist
                          | fix_axis_par_list
        """
        node = self._get_or_create_ast_node(ASTNodes.Axis_Descr_Opt)
        self._add_ast_node_object(
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

    def p_AXIS_DESCR_opt_objects_list(self, p):
        """
        axis_descr_opt    : annotation
        """
        node = self._get_or_create_ast_node(ASTNodes.Axis_Descr_Opt)
        self._add_ast_node_object_list(node_class=node, ast_node_names=[ASTNodes.Annotation], param=p[1])
        p[0] = node

    def p_AXIS_DESCR_opt_list(self, p):
        """
        axis_descr_opt_list    : axis_descr_opt
                               | axis_descr_opt_list axis_descr_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_AXIS_PTS(self, p):
        """
        axis_pts     : BEGIN AXIS_PTS ident string_literal constant ident ident constant ident constant constant constant END AXIS_PTS
                     | BEGIN AXIS_PTS ident string_literal constant ident ident constant ident constant constant constant axis_pts_opt_list END AXIS_PTS
        """
        if len(p) > 2:
            p[0] = self._create_ast_node(
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

            self._remove_ast_node(ASTNodes.Axis_Pts_Opt)

    def p_AXIS_PTS_opt_params(self, p):
        """
        axis_pts_opt    : byte_order
                        | calibration_access
                        | deposit
                        | display_identifier
                        | ecu_address_extension
                        | format
                        | guard_rails
                        | monotony
                        | phys_unit
                        | read_only
                        | ref_memory_segment
                        | step_size

        """
        node = self._get_or_create_ast_node(ASTNodes.Axis_Pts_Opt)
        self._add_ast_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Byte_Order,
                ASTNodes.Calibration_Access,
                ASTNodes.Deposit,
                ASTNodes.Display_Identifier,
                ASTNodes.Ecu_Address_Extension,
                ASTNodes.Format,
                ASTNodes.Guard_Rails,
                ASTNodes.Monotony,
                ASTNodes.Phys_Unit,
                ASTNodes.Read_Only,
                ASTNodes.Ref_Memory_Segment,
                ASTNodes.Step_Size,
            ],
            param=p[1],
        )

        p[0] = node

    def p_AXIS_PTS_opt_objects(self, p):
        """
        axis_pts_opt    : extended_limits
                        | symbol_link
                        | function_list
        """
        node = self._get_or_create_ast_node(ASTNodes.Axis_Pts_Opt)
        self._add_ast_node_object(
            node_class=node, ast_node_names=[ASTNodes.Extended_Limits, ASTNodes.Symbol_Link, ASTNodes.Function_List], param=p[1]
        )
        p[0] = node

    def p_AXIS_PTS_opt_objects_list(self, p):
        """
        axis_pts_opt    : annotation
                        | if_data
        """
        node = self._get_or_create_ast_node(ASTNodes.Axis_Pts_Opt)
        self._add_ast_node_object_list(node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.If_Data], param=p[1])
        p[0] = node

    def p_AXIS_PTS_opt_list(self, p):
        """
        axis_pts_opt_list    : axis_pts_opt
                             | axis_pts_opt_list axis_pts_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_AXIS_PTS_REF(self, p):
        """
        axis_pts_ref     : AXIS_PTS_REF ident
        """
        p[0] = ASTNodes.Axis_Pts_Ref(p[2])

    def p_AXIS_PTS_X(self, p):
        """
        axis_pts_x     : AXIS_PTS_X constant datatype indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Pts_X(Position=p[2], Datatype=p[3], IndexIncr=p[4], Addressing=p[5])

    def p_AXIS_PTS_Y(self, p):
        """
        axis_pts_y     : AXIS_PTS_Y constant datatype indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Pts_Y(Position=p[2], Datatype=p[3], IndexIncr=p[4], Addressing=p[5])

    def p_AXIS_PTS_Z(self, p):
        """
        axis_pts_z     : AXIS_PTS_Z constant datatype indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Pts_Z(Position=p[2], Datatype=p[3], IndexIncr=p[4], Addressing=p[5])

    def p_AXIS_PTS_Z4(self, p):
        """
        axis_pts_z4     : AXIS_PTS_Z4 constant datatype indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Pts_Z4(Position=p[2], Datatype=p[3], IndexIncr=p[4], Addressing=p[5])

    def p_AXIS_PTS_Z5(self, p):
        """
        axis_pts_z5     : AXIS_PTS_Z5 constant datatype indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Pts_Z5(Position=p[2], Datatype=p[3], IndexIncr=p[4], Addressing=p[5])

    def p_AXIS_RESCALE_X(self, p):
        """
        axis_rescale_x     : AXIS_RESCALE_X constant datatype constant indexorder_enum addrtype_enum
        """
        p[0] = ASTNodes.Axis_Rescale_X(
            Position=p[2], Datatype=p[3], MaxNumberOfRescalePairs=p[4], IndexIncr=p[5], Addressing=p[6]
        )

    def p_BIT_MASK(self, p):
        """
        bit_mask     : BIT_MASK constant
        """
        p[0] = ASTNodes.Bit_Mask(p[2])

    def p_BIT_OPERATION(self, p):
        """
        bit_operation     : BEGIN BIT_OPERATION bit_operation_opt_list END BIT_OPERATION
        """
        if len(p) > 2:
            p[0] = ASTNodes.Bit_Operation(OptionalParams=p[3])
            self._remove_ast_node(ASTNodes.Bit_Operation_Opt)

    def p_BIT_OPERATION_opt(self, p):
        """
        bit_operation_opt   : left_shift
                            | right_shift
                            | sign_extend

        """
        node = self._get_or_create_ast_node(ASTNodes.Bit_Operation_Opt)
        self._add_ast_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Left_Shift,
                ASTNodes.Right_Shift,
                ASTNodes.Sign_Extend,
            ],
            param=p[1],
        )
        p[0] = node

    def p_BIT_OPERATION_opt_list(self, p):
        """
        bit_operation_opt_list    : bit_operation_opt
                | bit_operation_opt_list bit_operation_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_BYTE_ORDER(self, p):
        """
        byte_order     : BYTE_ORDER byte_order_enum
        """
        p[0] = ASTNodes.Byte_Order(p[2])

    def p_CALIBRATION_ACCESS(self, p):
        """
        calibration_access     : CALIBRATION_ACCESS calibration_access_enum
        """
        p[0] = ASTNodes.Calibration_Access(p[2])

    def p_CALIBRATION_HANDLE(self, p):
        """
        calibration_handle     : BEGIN CALIBRATION_HANDLE constant_list END CALIBRATION_HANDLE
                               | BEGIN CALIBRATION_HANDLE constant_list calibration_handle_opt_list END CALIBRATION_HANDLE
        """
        if len(p) > 2:
            p[0] = ASTNodes.Calibration_Handle(Handle=p[3])
            if len(p) == 7:
                p[0].Calibration_Handle_Text = p[4]

            self._remove_ast_node(ASTNodes.Calibration_Handle_Opt)

    def p_CALIBRATION_HANDLE_opt(self, p):
        """
        calibration_handle_opt  : calibration_handle_text

        """
        node = self._get_or_create_ast_node(ASTNodes.Calibration_Handle_Opt)
        self._add_ast_node_param(node_class=node, ast_node_names=[ASTNodes.Calibration_Handle_Text], param=p[1])
        p[0] = node

    def p_CALIBRATION_HANDLE_opt_list(self, p):
        """
        calibration_handle_opt_list : calibration_handle_opt
                                    | calibration_handle_opt_list calibration_handle_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_CALIBRATION_HANDLE_TEXT(self, p):
        """
        calibration_handle_text     : CALIBRATION_HANDLE_TEXT string_literal
        """
        p[0] = ASTNodes.Calibration_Handle_Text(p[2])

    def p_CALIBRATION_METHOD(self, p):
        """
        calibration_method     : BEGIN CALIBRATION_METHOD string_literal constant END CALIBRATION_METHOD
                               | BEGIN CALIBRATION_METHOD string_literal constant calibration_method_opt_list END CALIBRATION_METHOD
        """
        if len(p) > 2:
            if len(p) == 7:
                p[0] = ASTNodes.Calibration_Method(Method=p[3], Version=p[4])
            else:
                p[0] = ASTNodes.Calibration_Method(Method=p[3], Version=p[4], Calibration_Handle=p[5])

    def p_CALIBRATION_METHOD_opt(self, p):
        """
        calibration_method_opt  : calibration_handle

        """
        p[0] = p[1]

    def p_CALIBRATION_METHOD_opt_list(self, p):
        """
        calibration_method_opt_list     : calibration_method_opt
                                        | calibration_method_opt_list calibration_method_opt
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            if p[2] is not None:
                p[1].append(p[2])
            p[0] = p[1]

    def p_CHARACTERISTIC(self, p):
        """
        characteristic     : BEGIN CHARACTERISTIC ident string_literal characteristic_enum constant ident constant ident constant constant END CHARACTERISTIC
                           | BEGIN CHARACTERISTIC ident string_literal characteristic_enum constant ident constant ident constant constant characteristic_opt_list END CHARACTERISTIC
        """
        if len(p) > 2:
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

        self._remove_ast_node(ASTNodes.Characteristic_Opt)

    def p_CHARACTERISTIC_opt_params(self, p):
        """
        characteristic_opt    : bit_mask
                              | byte_order
                              | calibration_access
                              | comparison_quantity
                              | discrete
                              | display_identifier
                              | ecu_address_extension
                              | format
                              | guard_rails
                              | number
                              | phys_unit
                              | read_only
                              | ref_memory_segment
                              | step_size

        """
        node = self._get_or_create_ast_node(ASTNodes.Characteristic_Opt)
        self._add_ast_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Bit_Mask,
                ASTNodes.Byte_Order,
                ASTNodes.Calibration_Access,
                ASTNodes.Comparison_Quantity,
                ASTNodes.Discrete,
                ASTNodes.Display_Identifier,
                ASTNodes.Ecu_Address_Extension,
                ASTNodes.Format,
                ASTNodes.Guard_Rails,
                ASTNodes.Number,
                ASTNodes.Phys_Unit,
                ASTNodes.Read_Only,
                ASTNodes.Ref_Memory_Segment,
                ASTNodes.Step_Size,
            ],
            param=p[1],
        )
        p[0] = node

    def p_CHARACTERISTIC_opt_objects(self, p):
        """
        characteristic_opt    :  dependent_characteristic
                              |  extended_limits
                              |  function_list
                              |  map_list
                              |  matrix_dim
                              |  max_refresh
                              |  symbol_link
                              |  virtual_characteristic
        """
        node = self._get_or_create_ast_node(ASTNodes.Characteristic_Opt)
        self._add_ast_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Dependent_Characteristic,
                ASTNodes.Extended_Limits,
                ASTNodes.Function_List,
                ASTNodes.Map_List,
                ASTNodes.Matrix_Dim,
                ASTNodes.Max_Refresh,
                ASTNodes.Symbol_Link,
                ASTNodes.Virtual_Characteristic,
            ],
            param=p[1],
        )
        p[0] = node

    def p_CHARACTERISTIC_opt_objects_list(self, p):
        """
        characteristic_opt    :  annotation
                              |  axis_descr
                              |  if_data
        """
        node = self._get_or_create_ast_node(ASTNodes.Characteristic_Opt)
        self._add_ast_node_object_list(
            node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.Axis_Descr, ASTNodes.If_Data], param=p[1]
        )
        p[0] = node

    def p_CHARACTERISTIC_opt_list(self, p):
        """
        characteristic_opt_list    : characteristic_opt
                | characteristic_opt_list characteristic_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_COEFFS(self, p):
        """
        coeffs     : COEFFS constant constant constant constant constant constant
        """
        # float a b c d e f
        # f(x) = (axx + bx + c) / (dxx + ex + f)
        # INT = f(PHYS)
        p[0] = ASTNodes.Coeffs(a=p[2], b=p[3], c=p[4], d=p[5], e=p[6], f=p[7])

    def p_COEFFS_LINEAR(self, p):
        """
        coeffs_linear     : COEFFS_LINEAR constant constant
        """
        # float a b
        # f(x) = ax + b
        # PHYS = f(INT)
        p[0] = ASTNodes.Coeffs_Linear(a=p[2], b=p[3])

    def p_COMPARISON_QUANTITY(self, p):
        """
        comparison_quantity     : COMPARISON_QUANTITY ident
        """
        p[0] = ASTNodes.Comparison_Quantity(p[2])

    def p_COMPU_METHOD(self, p):
        """
        compu_method     : BEGIN COMPU_METHOD ident string_literal conversion_type_enum string_literal string_literal END COMPU_METHOD
                         | BEGIN COMPU_METHOD ident string_literal conversion_type_enum string_literal string_literal compu_method_opt_list END COMPU_METHOD
        """
        node = self._create_ast_node(
            ASTNodes.Compu_Method(Name=p[3], LongIdentifier=p[4], ConversionType=p[5], Format=p[6], Unit=p[7])
        )

        if len(p) == 11:
            node.OptionalParams = p[8]

        p[0] = node

        self._remove_ast_node(ASTNodes.Compu_Method)
        self._remove_ast_node(ASTNodes.Compu_Method_Opt)

    def p_COMPU_METHOD_opt_params(self, p):
        """
        compu_method_opt    : compu_tab_ref
                            | ref_unit
                            | status_string_ref


        """
        node = self._get_or_create_ast_node(ASTNodes.Compu_Method_Opt)
        self._add_ast_node_param(
            node_class=node, ast_node_names=[ASTNodes.Compu_Tab_Ref, ASTNodes.Ref_Unit, ASTNodes.Status_String_Ref], param=p[1]
        )

        p[0] = node

    def p_COMPU_METHOD_opt_objects(self, p):
        """
        compu_method_opt    : coeffs
                            | coeffs_linear
                            | formula

        """
        node = self._get_or_create_ast_node(ASTNodes.Compu_Method_Opt)
        self._add_ast_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Coeffs,
                ASTNodes.Coeffs_Linear,
                ASTNodes.Formula,
            ],
            param=p[1],
        )
        p[0] = node

    def p_COMPU_METHOD_opt_list(self, p):
        """
        compu_method_opt_list    : compu_method_opt
                                 | compu_method_opt_list compu_method_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_COMPU_TAB(self, p):
        """
        compu_tab     : BEGIN COMPU_TAB ident string_literal conversion_type_enum constant axis_points_list END COMPU_TAB
                      | BEGIN COMPU_TAB ident string_literal conversion_type_enum constant axis_points_list compu_tab_opt_list END COMPU_TAB
        """
        node = self._create_ast_node(
            ASTNodes.Compu_Tab(Name=p[3], LongIdentifier=p[4], ConversionType=p[5], NumberValuePairs=p[6], Axis_Points=p[7])
        )

        if len(p) == 11:
            node.OptionalParams = p[8]

        p[0] = node

        self._remove_ast_node(ASTNodes.Compu_Tab)
        self._remove_ast_node(ASTNodes.Compu_Tab_Opt)

    def p_COMPU_TAB_opt_params(self, p):
        """
        compu_tab_opt    : default_value
                         | default_value_numeric

        """
        node = self._get_or_create_ast_node(ASTNodes.Compu_Tab_Opt)
        self._add_ast_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Default_Value,
                ASTNodes.Default_Value_Numeric,
            ],
            param=p[1],
        )

        p[0] = node

    def p_COMPU_TAB_opt_list(self, p):
        """
        compu_tab_opt_list    : compu_tab_opt
                        | compu_tab_opt_list compu_tab_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_COMPU_TAB_REF(self, p):
        """
        compu_tab_ref     : COMPU_TAB_REF ident
        """
        p[0] = ASTNodes.Compu_Tab_Ref(p[2])

    def p_COMPU_VTAB(self, p):
        """
        compu_vtab     : BEGIN COMPU_VTAB ident string_literal conversion_type_enum constant inVal_outVal_list END COMPU_VTAB
                       | BEGIN COMPU_VTAB ident string_literal conversion_type_enum constant inVal_outVal_list default_value END COMPU_VTAB
        """
        p[0] = ASTNodes.Compu_Vtab(
            Name=p[3], LongIdentifier=p[4], ConversionType=p[5], NumberValuePairs=p[6], InVal_OutVal=p[7]
        )
        if len(p) == 11:
            p[0].Default_Value = getattr(p[8], p[8].__slots__[0])

    def p_COMPU_VTAB_RANGE(self, p):
        """
        compu_vtab_range     : BEGIN COMPU_VTAB_RANGE ident string_literal constant inVal_MinMax_outVal_list END COMPU_VTAB_RANGE
                             | BEGIN COMPU_VTAB_RANGE ident string_literal constant inVal_MinMax_outVal_list default_value END COMPU_VTAB_RANGE
        """
        p[0] = ASTNodes.Compu_Vtab_Range(Name=p[3], LongIdentifier=p[4], NumberValueTriples=p[5], InVal_MinMax_OutVal=p[6])
        if len(p) == 10:
            p[0].Default_Value = getattr(p[7], p[7].__slots__[0])

    def p_CPU_TYPE(self, p):
        """
        cpu_type     : CPU_TYPE string_literal
        """
        p[0] = ASTNodes.Cpu_Type(p[2])

    def p_CURVE_AXIS_REF(self, p):
        """
        curve_axis_ref     : CURVE_AXIS_REF ident
        """
        p[0] = ASTNodes.Curve_Axis_Ref(p[2])

    def p_CUSTOMER(self, p):
        """
        customer     : CUSTOMER string_literal
        """
        p[0] = ASTNodes.Customer(p[2])

    def p_CUSTOMER_NO(self, p):
        """
        customer_no     : CUSTOMER_NO string_literal
        """
        p[0] = ASTNodes.Customer_No(p[2])

    def p_DATA_SIZE(self, p):
        """
        data_size     : DATA_SIZE constant
        """
        p[0] = ASTNodes.Data_Size(p[2])

    def p_DEF_CHARACTERISTIC(self, p):
        """
        def_characteristic     : BEGIN DEF_CHARACTERISTIC ident_list END DEF_CHARACTERISTIC
        """
        p[0] = ASTNodes.Def_Characteristic(p[3])

    def p_DEFAULT_VALUE(self, p):
        """
        default_value     : DEFAULT_VALUE string_literal
        """
        p[0] = ASTNodes.Default_Value(p[2])

    def p_DEFAULT_VALUE_NUMERIC(self, p):
        """
        default_value_numeric     : DEFAULT_VALUE_NUMERIC constant
        """
        p[0] = ASTNodes.Default_Value_Numeric(p[2])

    def p_DEPENDENT_CHARACTERISTIC(self, p):
        """
        dependent_characteristic     : BEGIN DEPENDENT_CHARACTERISTIC string_literal ident_list END DEPENDENT_CHARACTERISTIC
        """
        p[0] = ASTNodes.Dependent_Characteristic(Formula=p[3], Characteristic=p[4])

    def p_DEPOSIT(self, p):
        """
        deposit     : DEPOSIT mode_enum
        """
        p[0] = ASTNodes.Deposit(p[2])

    def p_DISCRETE(self, p):
        """
        discrete     : DISCRETE
        """
        p[0] = ASTNodes.Discrete(Boolean=True)

    def p_DISPLAY_IDENTIFIER(self, p):
        """
        display_identifier     : DISPLAY_IDENTIFIER ident
        """
        p[0] = ASTNodes.Display_Identifier(p[2])

    def p_DIST_OP_X(self, p):
        """
        dist_op_x    : DIST_OP_X constant datatype
        """
        p[0] = ASTNodes.Dist_Op_X(Position=p[2], Datatype=p[3])

    def p_DIST_OP_Y(self, p):
        """
        dist_op_y    : DIST_OP_Y constant datatype
        """
        p[0] = ASTNodes.Dist_Op_Y(Position=p[2], Datatype=p[3])

    def p_DIST_OP_Z(self, p):
        """
        dist_op_z    : DIST_OP_Z constant datatype
        """
        p[0] = ASTNodes.Dist_Op_Z(Position=p[2], Datatype=p[3])

    def p_DIST_OP_Z4(self, p):
        """
        dist_op_z4    : DIST_OP_Z4 constant datatype
        """
        p[0] = ASTNodes.Dist_Op_Z4(Position=p[2], Datatype=p[3])

    def p_DIST_OP_Z5(self, p):
        """
        dist_op_z5    : DIST_OP_Z5 constant datatype
        """
        p[0] = ASTNodes.Dist_Op_Z5(Position=p[2], Datatype=p[3])

    def p_ECU(self, p):
        """
        ecu     : ECU string_literal
        """
        p[0] = ASTNodes.Ecu(p[2])

    def p_ECU_ADDRESS(self, p):
        """
        ecu_address     : ECU_ADDRESS constant
        """
        p[0] = ASTNodes.Ecu_Address(p[2])

    def p_ECU_ADDRESS_EXTENSION(self, p):
        """
        ecu_address_extension     : ECU_ADDRESS_EXTENSION constant
        """
        p[0] = ASTNodes.Ecu_Address_Extension(p[2])

    def p_ECU_CALIBRATION_OFFSET(self, p):
        """
        ecu_calibration_offset     : ECU_CALIBRATION_OFFSET constant
        """
        p[0] = ASTNodes.Ecu_Calibration_Offset(p[2])

    def p_EPK(self, p):
        """
        epk     : EPK string_literal
        """
        p[0] = ASTNodes.Epk(p[2])

    def p_ERROR_MASK(self, p):
        """
        error_mask     : ERROR_MASK constant
        """
        p[0] = ASTNodes.Error_Mask(p[2])

    def p_EXTENDED_LIMITS(self, p):
        """
        extended_limits     : EXTENDED_LIMITS constant constant
        """
        p[0] = ASTNodes.Extended_Limits(LowerLimit=p[2], UpperLimit=p[3])

    def p_FIX_AXIS_PAR(self, p):
        """
        fix_axis_par     : FIX_AXIS_PAR constant constant constant
        """
        p[0] = ASTNodes.Fix_Axis_Par(Offset=p[2], Shift=p[3], Numberapo=p[4])

    def p_FIX_AXIS_PAR_DIST(self, p):
        """
        fix_axis_par_dist     : FIX_AXIS_PAR_DIST constant constant constant
        """
        p[0] = ASTNodes.Fix_Axis_Par_Dist(Offset=p[2], Distance=p[3], Numberapo=p[4])

    def p_FIX_AXIS_PAR_LIST(self, p):
        """
        fix_axis_par_list     : BEGIN FIX_AXIS_PAR_LIST constant_list END FIX_AXIS_PAR_LIST
        """
        p[0] = ASTNodes.Fix_Axis_Par_List(p[3])

    def p_FIX_NO_AXIS_PTS_X(self, p):
        """
        fix_no_axis_pts_x     : FIX_NO_AXIS_PTS_X constant
        """
        p[0] = ASTNodes.Fix_No_Axis_Pts_X(p[2])

    def p_FIX_NO_AXIS_PTS_Y(self, p):
        """
        fix_no_axis_pts_y     : FIX_NO_AXIS_PTS_Y constant
        """
        p[0] = ASTNodes.Fix_No_Axis_Pts_Y(p[2])

    def p_FIX_NO_AXIS_PTS_Z(self, p):
        """
        fix_no_axis_pts_z     : FIX_NO_AXIS_PTS_Z constant
        """
        p[0] = ASTNodes.Fix_No_Axis_Pts_Z(p[2])

    def p_FIX_NO_AXIS_PTS_Z4(self, p):
        """
        fix_no_axis_pts_z4     : FIX_NO_AXIS_PTS_Z4 constant
        """
        p[0] = ASTNodes.Fix_No_Axis_Pts_Z4(p[2])

    def p_FIX_NO_AXIS_PTS_Z5(self, p):
        """
        fix_no_axis_pts_z5     : FIX_NO_AXIS_PTS_Z5 constant
        """
        p[0] = ASTNodes.Fix_No_Axis_Pts_Z5(p[2])

    def p_FNC_VALUES(self, p):
        """
        fnc_values     : FNC_VALUES constant datatype indexmode_enum addrtype_enum
        """
        p[0] = ASTNodes.Fnc_Values(Position=p[2], Datatype=p[3], IndexMode=p[4], AddressType=p[5])

    def p_FORMAT(self, p):
        """
        format     : FORMAT string_literal
        """
        p[0] = ASTNodes.Format(p[2])

    def p_FORMULA(self, p):
        """
        formula     : BEGIN FORMULA string_literal END FORMULA
                    | BEGIN FORMULA string_literal formula_inv END FORMULA
        """
        if len(p) == 6:
            p[0] = ASTNodes.Formula(f_x=p[3])
        else:
            p[0] = ASTNodes.Formula(f_x=p[3], Formula_Inv=p[4])

    def p_FORMULA_INV(self, p):
        """
        formula_inv     : FORMULA_INV string_literal
        """
        p[0] = ASTNodes.Formula_Inv(g_x=p[2])

    def p_FRAME(self, p):
        """
        frame     : BEGIN FRAME ident string_literal constant constant END FRAME
                  | BEGIN FRAME ident string_literal constant constant frame_opt_list END FRAME
        """
        node = self._create_ast_node(ASTNodes.Frame(Name=p[3], LongIdentifier=p[4], ScalingUnit=p[5], Rate=p[6]))

        if len(p) == 10:
            node.OptionalParams = p[7]

        p[0] = node

        self._remove_ast_node(ASTNodes.Frame)
        self._remove_ast_node(ASTNodes.Frame_Opt)

    def p_FRAME_opt_params(self, p):
        """
        frame_opt    : frame_measurement

        """
        node = self._get_or_create_ast_node(ASTNodes.Frame_Opt)
        self._add_ast_node_param(node_class=node, ast_node_names=[ASTNodes.Frame_Measurement], param=p[1])
        p[0] = node

    def p_FRAME_opt_objects_list(self, p):
        """
        frame_opt    : if_data
        """
        node = self._get_or_create_ast_node(ASTNodes.Frame_Opt)
        self._add_ast_node_object_list(node_class=node, ast_node_names=[ASTNodes.If_Data], param=p[1])
        p[0] = node

    def p_FRAME_opt_list(self, p):
        """
        frame_opt_list    : frame_opt
                        | frame_opt_list frame_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_FRAME_MEASUREMENT(self, p):
        """
        frame_measurement     : FRAME_MEASUREMENT ident_list
        """
        p[0] = ASTNodes.Frame_Measurement(p[2])

    def p_FUNCTION(self, p):
        """
        function     : BEGIN FUNCTION ident string_literal END FUNCTION
                     | BEGIN FUNCTION ident string_literal function_opt_list END FUNCTION
        """
        node = self._create_ast_node(ASTNodes.Function(Name=p[3], LongIdentifier=p[4]))

        if len(p) == 8:
            node.OptionalParams = p[5]

        p[0] = node

        self._remove_ast_node(ASTNodes.Function)
        self._remove_ast_node(ASTNodes.Function_Opt)

    def p_FUNCTION_opt_params(self, p):
        """
        function_opt    : function_version
        """
        node = self._get_or_create_ast_node(ASTNodes.Function_Opt)
        self._add_ast_node_param(node_class=node, ast_node_names=[ASTNodes.Function_Version], param=p[1])
        p[0] = node

    def p_FUNCTION_opt_objects(self, p):
        """
        function_opt    : def_characteristic
                        | in_measurement
                        | loc_measurement
                        | out_measurement
                        | ref_characteristic
        """
        node = self._get_or_create_ast_node(ASTNodes.Function_Opt)
        self._add_ast_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Def_Characteristic,
                ASTNodes.In_Measurement,
                ASTNodes.Loc_Measurement,
                ASTNodes.Out_Measurement,
                ASTNodes.Ref_Characteristic,
            ],
            param=p[1],
        )
        p[0] = node

    def p_FUNCTION_opt_objects_list(self, p):
        """
        function_opt    : annotation
                        | if_data
                        | sub_function
        """
        node = self._get_or_create_ast_node(ASTNodes.Function_Opt)
        self._add_ast_node_object_list(
            node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.If_Data, ASTNodes.Sub_Function], param=p[1]
        )
        p[0] = node

    def p_FUNCTION_opt_list(self, p):
        """
        function_opt_list    : function_opt
                        | function_opt_list function_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_FUNCTION_LIST(self, p):
        """
        function_list     : BEGIN FUNCTION_LIST ident_list END FUNCTION_LIST
        """
        p[0] = ASTNodes.Function_List(Name=p[3])

    def p_FUNCTION_VERSION(self, p):
        """
        function_version     : FUNCTION_VERSION string_literal
        """
        p[0] = ASTNodes.Function_Version(p[2])

    def p_GROUP(self, p):
        """
        group     : BEGIN GROUP ident string_literal END GROUP
                  | BEGIN GROUP ident string_literal group_opt_list END GROUP
        """
        node = self._create_ast_node(ASTNodes.Group(GroupName=p[3], GroupLongIdentifier=p[4]))

        if len(p) == 8:
            node.OptionalParams = p[5]

        p[0] = node

        self._remove_ast_node(ASTNodes.Group)
        self._remove_ast_node(ASTNodes.Group_Opt)

    def p_GROUP_opt_params(self, p):
        """
        group_opt    : root
        """
        node = self._get_or_create_ast_node(ASTNodes.Group_Opt)
        self._add_ast_node_param(node_class=node, ast_node_names=[ASTNodes.Root], param=p[1])

        p[0] = node

    def p_GROUP_opt_objects(self, p):
        """
        group_opt    : function_list
                     | ref_characteristic
                     | ref_measurement
                     | sub_group
        """
        node = self._get_or_create_ast_node(ASTNodes.Group_Opt)
        self._add_ast_node_object(
            node_class=node,
            ast_node_names=[ASTNodes.Function_List, ASTNodes.Ref_Characteristic, ASTNodes.Ref_Measurement, ASTNodes.Sub_Group],
            param=p[1],
        )
        p[0] = node

    def p_GROUP_opt_objects_list(self, p):
        """
        group_opt    : annotation
                     | if_data
        """
        node = self._get_or_create_ast_node(ASTNodes.Group_Opt)
        self._add_ast_node_object_list(node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.If_Data], param=p[1])
        p[0] = node

    def p_GROUP_opt_list(self, p):
        """
        group_opt_list    : group_opt
                            | group_opt_list group_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_GUARD_RAILS(self, p):
        """
        guard_rails     : GUARD_RAILS
        """
        p[0] = ASTNodes.Guard_Rails(Boolean=True)

    def p_HEADER(self, p):
        """
        header     : BEGIN HEADER string_literal END HEADER
                   | BEGIN HEADER string_literal header_opt_list END HEADER
        """
        node = self._create_ast_node(ASTNodes.Header(Comment=p[3]))

        if len(p) == 7:
            node.OptionalParams = p[4]

        p[0] = node

        self._remove_ast_node(ASTNodes.Header)
        self._remove_ast_node(ASTNodes.Header_Opt)

    def p_HEADER_opt(self, p):
        """
        header_opt    : project_no
                      | version
        """
        node = self._get_or_create_ast_node(ASTNodes.Header_Opt)
        self._add_ast_node_param(node_class=node, ast_node_names=[ASTNodes.Project_No, ASTNodes.Version], param=p[1])

        p[0] = node

    def p_HEADER_opt_list(self, p):
        """
        header_opt_list    : header_opt
                           | header_opt_list header_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_IDENTIFICATION(self, p):
        """
        identification     : IDENTIFICATION constant datatype
        """
        p[0] = ASTNodes.Identification(Position=p[2], Datatype=p[3])

    def p_IF_DATA(self, p):
        """
        if_data             : if_data_begin if_data_opt_list if_data_end
        """
        data_params = [x for x in p[2] if not isinstance(x, ASTNodes.If_Data_Block)]
        if_data_block = [x for x in p[2] if isinstance(x, ASTNodes.If_Data_Block)]
        p[0] = ASTNodes.If_Data(
            Name=p[1], OptionalParams=ASTNodes.If_Data_Opt(DataParams=data_params, If_Data_Block=if_data_block)
        )

    def p_IF_DATA_mandatory_only(self, p):
        """
        if_data             : if_data_begin if_data_end
        """
        p[0] = ASTNodes.If_Data(Name=p[1])

    def p_IF_DATA_begin(self, p):
        """
        if_data_begin   : BEGIN IF_DATA ident
        """
        p[0] = p[3]

    def p_IF_DATA_end(self, p):
        """
        if_data_end     : END IF_DATA
                        | END
        """

    def p_IF_DATA_opt_param(self, p):
        """
        if_data_opt     : constant
                        | string_literal
                        | ident
        """
        p[0] = p[1]

    def p_IF_DATA_opt_block(self, p):
        """
        if_data_opt     : if_data_block
        """
        p[0] = p[1]

    def p_IF_DATA_opt_list(self, p):
        """
        if_data_opt_list    : if_data_opt
                            | if_data_opt_list if_data_opt
        """
        if len(p) > 2:
            p[1].append(p[2])
            p[0] = p[1]
        else:
            p[0] = [p[1]]

    def p_IF_DATA_block(self, p):
        """
        if_data_block       : if_data_block_begin if_data_opt_list if_data_block_end
        """
        if_data_block = [x for x in p[2] if isinstance(x, ASTNodes.If_Data_Block)]
        data_params = [x for x in p[2] if not isinstance(x, ASTNodes.If_Data_Block)]
        p[0] = ASTNodes.If_Data_Block(Name=p[1], DataParams=data_params, If_Data_Block=if_data_block)

    def p_IF_DATA_block_begin(self, p):
        """
        if_data_block_begin : BEGIN ident
        """
        p[0] = p[2]

    def p_IF_DATA_block_end(self, p):
        """
        if_data_block_end   : END ident
        """
        p[0] = p[2]

    def p_IN_MEASUREMENT(self, p):
        """
        in_measurement     : BEGIN IN_MEASUREMENT ident_list END IN_MEASUREMENT
        """
        p[0] = ASTNodes.In_Measurement(p[3])

    def p_LAYOUT(self, p):
        """
        layout     : LAYOUT indexmode_enum
        """
        # Description: This keyword describes the layout of a
        # multi-dimensional measurement array.
        # It can be used at MEASUREMENT.
        p[0] = ASTNodes.Layout(p[2])

    def p_LEFT_SHIFT(self, p):
        """
        left_shift     : LEFT_SHIFT constant
        """
        # Description: The LEFT_SHIFT keyword is only used within the
        # BIT_OPERATION keyword. See description of BIT_OPERATION.
        p[0] = ASTNodes.Left_Shift(p[2])

    def p_LOC_MEASUREMENT(self, p):
        """
        loc_measurement     : BEGIN LOC_MEASUREMENT ident_list END LOC_MEASUREMENT
        """
        p[0] = ASTNodes.Loc_Measurement(p[3])

    def p_MAP_LIST(self, p):
        """
        map_list     : BEGIN MAP_LIST ident_list END MAP_LIST
        """
        p[0] = ASTNodes.Map_List(p[3])

    def p_MATRIX_DIM(self, p):
        """
        matrix_dim     : MATRIX_DIM constant constant constant
        """
        p[0] = ASTNodes.Matrix_Dim(xDim=p[2], yDim=p[3], zDim=p[4])

    def p_MAX_GRAD(self, p):
        """
        max_grad     : MAX_GRAD constant
        """
        p[0] = ASTNodes.Max_Grad(p[2])

    def p_MAX_REFRESH(self, p):
        """
        max_refresh     : MAX_REFRESH constant constant
        """
        p[0] = ASTNodes.Max_Refresh(ScalingUnit=p[2], Rate=p[3])

    def p_MEASUREMENT(self, p):
        """
        measurement     : BEGIN MEASUREMENT ident string_literal datatype ident constant constant constant constant END MEASUREMENT
                        | BEGIN MEASUREMENT ident string_literal datatype ident constant constant constant constant measurement_opt_list END MEASUREMENT
        """
        node = self._create_ast_node(
            ASTNodes.Measurement(
                Name=p[3],
                LongIdentifier=p[4],
                Datatype=p[5],
                Conversion=p[6],
                Resolution=p[7],
                Accuracy=p[8],
                LowerLimit=p[9],
                UpperLimit=p[10],
            )
        )

        if len(p) == 14:
            node.OptionalParams = p[11]

        p[0] = node

        self._remove_ast_node(ASTNodes.Measurement)
        self._remove_ast_node(ASTNodes.Measurement_Opt)

    def p_MEASUREMENT_opt_params(self, p):
        """
        measurement_opt    : array_size
                           | bit_mask
                           | byte_order
                           | discrete
                           | display_identifier
                           | ecu_address
                           | ecu_address_extension
                           | error_mask
                           | format
                           | layout
                           | phys_unit
                           | read_write
                           | ref_memory_segment

        """
        node = self._get_or_create_ast_node(ASTNodes.Measurement_Opt)
        self._add_ast_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Array_Size,
                ASTNodes.Bit_Mask,
                ASTNodes.Byte_Order,
                ASTNodes.Discrete,
                ASTNodes.Display_Identifier,
                ASTNodes.Ecu_Address,
                ASTNodes.Ecu_Address_Extension,
                ASTNodes.Error_Mask,
                ASTNodes.Format,
                ASTNodes.Layout,
                ASTNodes.Phys_Unit,
                ASTNodes.Read_Write,
                ASTNodes.Ref_Memory_Segment,
            ],
            param=p[1],
        )

        p[0] = node

    def p_MEASUREMENT_opt_objects(self, p):
        """
        measurement_opt    : bit_operation
                           | function_list
                           | matrix_dim
                           | max_refresh
                           | symbol_link
                           | virtual
        """
        node = self._get_or_create_ast_node(ASTNodes.Measurement_Opt)
        self._add_ast_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Bit_Operation,
                ASTNodes.Bit_Operation,
                ASTNodes.Function_List,
                ASTNodes.Max_Refresh,
                ASTNodes.Symbol_Link,
                ASTNodes.Virtual,
            ],
            param=p[1],
        )
        p[0] = node

    def p_MEASUREMENT_opt_objects_list(self, p):
        """
        measurement_opt    : annotation
                           | if_data
        """
        node = self._get_or_create_ast_node(ASTNodes.Measurement_Opt)
        self._add_ast_node_object_list(node_class=node, ast_node_names=[ASTNodes.Annotation, ASTNodes.If_Data], param=p[1])
        p[0] = node

    def p_MEASUREMENT_opt_list(self, p):
        """
        measurement_opt_list    : measurement_opt
                        | measurement_opt_list measurement_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_MEMORY_LAYOUT(self, p):
        """
        memory_layout     : BEGIN MEMORY_LAYOUT prgtype_enum constant constant constant_list END MEMORY_LAYOUT
                          | BEGIN MEMORY_LAYOUT prgtype_enum constant constant constant_list memory_layout_opt_list END MEMORY_LAYOUT
        """
        p[0] = ASTNodes.Memory_Layout(PrgType=p[3], Address=p[4], Size=p[5], Offset=p[6])
        if len(p) == 10:
            p[0].If_Data = p[7]

    def p_MEMORY_LAYOUT_opt(self, p):
        """
        memory_layout_opt   : if_data
        """
        p[0] = p[1]

    def p_MEMORY_LAYOUT_opt_list(self, p):
        """
        memory_layout_opt_list      : memory_layout_opt
                                    | memory_layout_opt_list memory_layout_opt
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_MEMORY_SEGMENT(self, p):
        """
        memory_segment     : BEGIN MEMORY_SEGMENT ident string_literal prgtype_enum memorytype_enum attribute_enum constant constant constant_list END MEMORY_SEGMENT
                           | BEGIN MEMORY_SEGMENT ident string_literal prgtype_enum memorytype_enum attribute_enum constant constant constant_list memory_segment_opt_list END MEMORY_SEGMENT
        """
        p[0] = ASTNodes.Memory_Segment(
            Name=p[3], LongIdentifier=p[4], PrgType=p[5], MemoryType=p[6], Attribute=p[7], Address=p[8], Size=p[9], Offset=p[10]
        )

        if len(p) == 14:
            p[0].If_Data = p[11]

    def p_MEMORY_SEGMENT_opt(self, p):
        """
        memory_segment_opt   : if_data
        """
        p[0] = p[1]

    def p_MEMORY_SEGMENT_opt_list(self, p):
        """
        memory_segment_opt_list      : memory_segment_opt
                                     | memory_segment_opt_list memory_segment_opt
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_MOD_COMMON(self, p):
        """
        mod_common     : BEGIN MOD_COMMON string_literal END MOD_COMMON
                       | BEGIN MOD_COMMON string_literal mod_common_opt_list END MOD_COMMON
        """
        node = self._create_ast_node(ASTNodes.Mod_Common(Comment=p[3]))

        if len(p) == 7:
            node.OptionalParams = p[4]

        p[0] = node

        self._remove_ast_node(ASTNodes.Mod_Common)
        self._remove_ast_node(ASTNodes.Mod_Common_Opt)

    def p_MOD_COMMON_opt(self, p):
        """
        mod_common_opt     : alignment_byte
                           | alignment_float32_ieee
                           | alignment_float64_ieee
                           | alignment_int64
                           | alignment_long
                           | alignment_word
                           | byte_order
                           | data_size
                           | deposit
        """
        node = self._get_or_create_ast_node(ASTNodes.Mod_Common_Opt)
        self._add_ast_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Alignment_Byte,
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

    def p_MOD_COMMON_opt_list(self, p):
        """
        mod_common_opt_list    : mod_common_opt
                               | mod_common_opt_list mod_common_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_MOD_PAR(self, p):
        """
        mod_par     : BEGIN MOD_PAR string_literal END MOD_PAR
                    | BEGIN MOD_PAR string_literal mod_par_opt_list END MOD_PAR
        """
        node = self._create_ast_node(ASTNodes.Mod_Par(Comment=p[3]))

        if len(p) == 7:
            node.OptionalParams = p[4]

        p[0] = node

        self._remove_ast_node(ASTNodes.Mod_Par)
        self._remove_ast_node(ASTNodes.Mod_Par_Opt)

    def p_MOD_PAR_opt_params(self, p):
        """
        mod_par_opt    : cpu_type
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
        node = self._get_or_create_ast_node(ASTNodes.Mod_Par_Opt)
        self._add_ast_node_param(
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

    def p_MOD_PAR_opt_objects_list(self, p):
        """
        mod_par_opt    : addr_epk
                       | calibration_method
                       | memory_layout
                       | memory_segment
                       | system_constant
        """
        node = self._get_or_create_ast_node(ASTNodes.Mod_Par_Opt)
        self._add_ast_node_object_list(
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

    def p_MOD_PAR_opt_list(self, p):
        """
        mod_par_opt_list    : mod_par_opt
                            | mod_par_opt_list mod_par_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_MODULE(self, p):
        """
        module     : BEGIN MODULE ident string_literal END MODULE
                   | BEGIN MODULE ident string_literal module_opt_list END MODULE
        """
        if len(p) == 5:
            node = self._create_ast_node(ASTNodes.Module(Name=None, LongIdentifier=None))
        else:
            node = self._create_ast_node(ASTNodes.Module(Name=p[3], LongIdentifier=p[4]))

        if len(p) == 8:
            node.OptionalParams = p[5]

        p[0] = node

        self._remove_ast_node(ASTNodes.Module)
        self._remove_ast_node(ASTNodes.Module_Opt)

    def p_MODULE_opt_objects(self, p):
        """
        module_opt    : mod_common
                      | mod_par
                      | variant_coding
        """
        node = self._get_or_create_ast_node(ASTNodes.Module_Opt)
        self._add_ast_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Mod_Common,
                ASTNodes.Mod_Par,
                ASTNodes.Variant_Coding,
            ],
            param=p[1],
        )
        p[0] = node

    def p_MODULE_opt_objects_list(self, p):
        """
        module_opt    : axis_pts
                      | characteristic
                      | compu_method
                      | compu_tab
                      | compu_vtab
                      | compu_vtab_range
                      | frame
                      | function
                      | group
                      | if_data
                      | measurement
                      | record_layout
                      | unit
                      | user_rights
        """
        node = self._get_or_create_ast_node(ASTNodes.Module_Opt)
        self._add_ast_node_object_list(
            node_class=node,
            ast_node_names=[
                ASTNodes.Axis_Pts,
                ASTNodes.Characteristic,
                ASTNodes.Compu_Method,
                ASTNodes.Compu_Tab,
                ASTNodes.Compu_Vtab,
                ASTNodes.Compu_Vtab_Range,
                ASTNodes.Frame,
                ASTNodes.Function,
                ASTNodes.Group,
                ASTNodes.If_Data,
                ASTNodes.Measurement,
                ASTNodes.Record_Layout,
                ASTNodes.Unit,
                ASTNodes.User_Rights,
            ],
            param=p[1],
        )
        p[0] = node

    def p_MODULE_opt_list(self, p):
        """
        module_opt_list    : module_opt
                        | module_opt_list module_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_MONOTONY(self, p):
        """
        monotony     : MONOTONY monotony_enum
        """
        p[0] = ASTNodes.Monotony(p[2])

    def p_NO_AXIS_PTS_X(self, p):
        """
        no_axis_pts_x     : NO_AXIS_PTS_X constant datatype
        """
        p[0] = ASTNodes.No_Axis_Pts_X(Position=p[2], Datatype=p[3])

    def p_NO_AXIS_PTS_Y(self, p):
        """
        no_axis_pts_y     : NO_AXIS_PTS_Y constant datatype
        """
        p[0] = ASTNodes.No_Axis_Pts_Y(Position=p[2], Datatype=p[3])

    def p_NO_AXIS_PTS_Z(self, p):
        """
        no_axis_pts_z     : NO_AXIS_PTS_Z constant datatype
        """
        p[0] = ASTNodes.No_Axis_Pts_Z(Position=p[2], Datatype=p[3])

    def p_NO_AXIS_PTS_Z4(self, p):
        """
        no_axis_pts_z4     : NO_AXIS_PTS_Z4 constant datatype
        """
        p[0] = ASTNodes.No_Axis_Pts_Z4(Position=p[2], Datatype=p[3])

    def p_NO_AXIS_PTS_Z5(self, p):
        """
        no_axis_pts_z5     : NO_AXIS_PTS_Z5 constant datatype
        """
        p[0] = ASTNodes.No_Axis_Pts_Z5(Position=p[2], Datatype=p[3])

    def p_NO_OF_INTERFACES(self, p):
        """
        no_of_interfaces     : NO_OF_INTERFACES constant
        """
        p[0] = ASTNodes.No_Of_Interfaces(p[2])

    def p_NO_RESCALE_X(self, p):
        """
        no_rescale_x     : NO_RESCALE_X constant datatype
        """
        p[0] = ASTNodes.No_Rescale_X(Position=p[2], Datatype=p[3])

    def p_NUMBER(self, p):
        """
        number     : NUMBER constant
        """
        p[0] = ASTNodes.Number(p[2])

    def p_OFFSET_X(self, p):
        """
        offset_x     : OFFSET_X constant datatype
        """
        p[0] = ASTNodes.Offset_X(Position=p[2], Datatype=p[3])

    def p_OFFSET_Y(self, p):
        """
        offset_y     : OFFSET_Y constant datatype
        """
        p[0] = ASTNodes.Offset_Y(Position=p[2], Datatype=p[3])

    def p_OFFSET_Z(self, p):
        """
        offset_z     : OFFSET_Z constant datatype
        """
        p[0] = ASTNodes.Offset_Z(Position=p[2], Datatype=p[3])

    def p_OFFSET_Z4(self, p):
        """
        offset_z4     : OFFSET_Z4 constant datatype
        """
        p[0] = ASTNodes.Offset_Z4(Position=p[2], Datatype=p[3])

    def p_OFFSET_Z5(self, p):
        """
        offset_z5     : OFFSET_Z5 constant datatype
        """
        p[0] = ASTNodes.Offset_Z5(Position=p[2], Datatype=p[3])

    def p_OUT_MEASUREMENT(self, p):
        """
        out_measurement     : BEGIN OUT_MEASUREMENT ident_list END OUT_MEASUREMENT
        """
        p[0] = ASTNodes.Out_Measurement(p[3])

    def p_PHONE_NO(self, p):
        """
        phone_no     : PHONE_NO string_literal
        """
        p[0] = ASTNodes.Phone_No(p[2])

    def p_PHYS_UNIT(self, p):
        """
        phys_unit     : PHYS_UNIT string_literal
        """
        p[0] = ASTNodes.Phys_Unit(p[2])

    def p_PROJECT(self, p):
        """
        project     : BEGIN PROJECT ident string_literal END PROJECT
                    | BEGIN PROJECT ident string_literal project_opt_list END PROJECT
        """
        node = self._create_ast_node(ASTNodes.Project(Name=p[3], LongIdentifier=p[4]))

        if len(p) == 8:
            node.OptionalParams = p[5]

        p[0] = node

        self._remove_ast_node(ASTNodes.Project)
        self._remove_ast_node(ASTNodes.Project_Opt)

    def p_PROJECT_opt_objects(self, p):
        """
        project_opt    : header
        """
        node = self._get_or_create_ast_node(ASTNodes.Project_Opt)
        self._add_ast_node_object(node_class=node, ast_node_names=[ASTNodes.Header], param=p[1])
        p[0] = node

    def p_PROJECT_opt_objects_list(self, p):
        """
        project_opt    : module
        """
        node = self._get_or_create_ast_node(ASTNodes.Project_Opt)
        self._add_ast_node_object_list(node_class=node, ast_node_names=[ASTNodes.Module], param=p[1])
        p[0] = node

    def p_PROJECT_opt_list(self, p):
        """
        project_opt_list    : project_opt
                        | project_opt_list project_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_PROJECT_NO(self, p):
        """
        project_no     : PROJECT_NO ident
        """
        p[0] = ASTNodes.Project_No(p[2])

    def p_READ_ONLY(self, p):
        """
        read_only     : READ_ONLY
        """
        # This keyword is used to indicate that an adjustable
        # object cannot be changed (but can only be read).
        p[0] = ASTNodes.Read_Only(Boolean=True)

    def p_READ_WRITE(self, p):
        """
        read_write     : READ_WRITE
        """
        # Description: This keyword is used to mark a measurement
        # object to be writeable.
        p[0] = ASTNodes.Read_Write(Boolean=True)

    def p_RECORD_LAYOUT(self, p):
        """
        record_layout     : BEGIN RECORD_LAYOUT ident END RECORD_LAYOUT
                          | BEGIN RECORD_LAYOUT ident record_layout_opt_list END RECORD_LAYOUT
        """
        self._create_ast_node(ASTNodes.Record_Layout(Name=p[3]))

        node = self._get_or_create_ast_node(ASTNodes.Record_Layout)

        if len(p) == 7:
            node.OptionalParams = p[4]

        p[0] = node

        self._remove_ast_node(ASTNodes.Record_Layout)
        self._remove_ast_node(ASTNodes.Record_Layout_Opt)

    def p_RECORD_LAYOUT_opt_params(self, p):
        """
        record_layout_opt    : alignment_byte
                             | alignment_float32_ieee
                             | alignment_float64_ieee
                             | alignment_int64
                             | alignment_long
                             | alignment_word
                             | fix_no_axis_pts_x
                             | fix_no_axis_pts_y
                             | fix_no_axis_pts_z
                             | fix_no_axis_pts_z4
                             | fix_no_axis_pts_z5
                             | static_record_layout
        """
        node = self._get_or_create_ast_node(ASTNodes.Record_Layout_Opt)
        self._add_ast_node_param(
            node_class=node,
            ast_node_names=[
                ASTNodes.Alignment_Byte,
                ASTNodes.Alignment_Float32_Ieee,
                ASTNodes.Alignment_Float64_Ieee,
                ASTNodes.Alignment_Int64,
                ASTNodes.Alignment_Long,
                ASTNodes.Alignment_Word,
                ASTNodes.Fix_No_Axis_Pts_X,
                ASTNodes.Fix_No_Axis_Pts_Y,
                ASTNodes.Fix_No_Axis_Pts_Z,
                ASTNodes.Fix_No_Axis_Pts_Z4,
                ASTNodes.Fix_No_Axis_Pts_Z5,
                ASTNodes.Static_Record_Layout,
            ],
            param=p[1],
        )

        p[0] = node

    def p_RECORD_LAYOUT_opt_objects(self, p):
        """
        record_layout_opt    : axis_pts_x
                             | axis_pts_y
                             | axis_pts_z
                             | axis_pts_z4
                             | axis_pts_z5
                             | axis_rescale_x
                             | dist_op_x
                             | dist_op_y
                             | dist_op_z
                             | dist_op_z4
                             | dist_op_z5
                             | fnc_values
                             | identification
                             | no_axis_pts_x
                             | no_axis_pts_y
                             | no_axis_pts_z
                             | no_axis_pts_z4
                             | no_axis_pts_z5
                             | no_rescale_x
                             | offset_x
                             | offset_y
                             | offset_z
                             | offset_z4
                             | offset_z5
                             | rip_addr_x
                             | rip_addr_w
                             | rip_addr_y
                             | rip_addr_z
                             | rip_addr_z4
                             | rip_addr_z5
                             | src_addr_x
                             | src_addr_y
                             | src_addr_z
                             | src_addr_z4
                             | src_addr_z5
                             | shift_op_x
                             | shift_op_y
                             | shift_op_z
                             | shift_op_z4
                             | shift_op_z5
        """
        node = self._get_or_create_ast_node(ASTNodes.Record_Layout_Opt)
        self._add_ast_node_object(
            node_class=node,
            ast_node_names=[
                ASTNodes.Axis_Pts_X,
                ASTNodes.Axis_Pts_Y,
                ASTNodes.Axis_Pts_Z,
                ASTNodes.Axis_Pts_Z4,
                ASTNodes.Axis_Pts_Z5,
                ASTNodes.Axis_Rescale_X,
                ASTNodes.Dist_Op_X,
                ASTNodes.Dist_Op_Y,
                ASTNodes.Dist_Op_Z,
                ASTNodes.Dist_Op_Z4,
                ASTNodes.Dist_Op_Z5,
                ASTNodes.Fnc_Values,
                ASTNodes.Identification,
                ASTNodes.No_Axis_Pts_X,
                ASTNodes.No_Axis_Pts_Y,
                ASTNodes.No_Axis_Pts_Z,
                ASTNodes.No_Axis_Pts_Z4,
                ASTNodes.No_Axis_Pts_Z5,
                ASTNodes.No_Rescale_X,
                ASTNodes.Offset_X,
                ASTNodes.Offset_Y,
                ASTNodes.Offset_Z,
                ASTNodes.Offset_Z4,
                ASTNodes.Offset_Z5,
                ASTNodes.Rip_Addr_W,
                ASTNodes.Rip_Addr_X,
                ASTNodes.Rip_Addr_Y,
                ASTNodes.Rip_Addr_Z,
                ASTNodes.Rip_Addr_Z4,
                ASTNodes.Rip_Addr_Z5,
                ASTNodes.Src_Addr_X,
                ASTNodes.Src_Addr_Y,
                ASTNodes.Src_Addr_Z,
                ASTNodes.Src_Addr_Z4,
                ASTNodes.Src_Addr_Z5,
                ASTNodes.Shift_Op_X,
                ASTNodes.Shift_Op_Y,
                ASTNodes.Shift_Op_Z,
                ASTNodes.Shift_Op_Z4,
                ASTNodes.Shift_Op_Z5,
            ],
            param=p[1],
        )
        p[0] = node

    def p_RECORD_LAYOUT_opt_objects_list(self, p):
        """
        record_layout_opt    : reserved
        """
        node = self._get_or_create_ast_node(ASTNodes.Record_Layout_Opt)
        self._add_ast_node_object_list(node_class=node, ast_node_names=[ASTNodes.Reserved], param=p[1])
        p[0] = node

    def p_RECORD_LAYOUT_opt_list(self, p):
        """
        record_layout_opt_list    : record_layout_opt
                        | record_layout_opt_list record_layout_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_REF_CHARACTERISTIC(self, p):
        """
        ref_characteristic     : BEGIN REF_CHARACTERISTIC ident_list END REF_CHARACTERISTIC
        """
        p[0] = ASTNodes.Ref_Characteristic(Identifier=p[3])

    def p_REF_GROUP(self, p):
        """
        ref_group     : BEGIN REF_GROUP ident_list END REF_GROUP
        """
        p[0] = ASTNodes.Ref_Group(Identifier=p[3])

    def p_REF_MEASUREMENT(self, p):
        """
        ref_measurement     : BEGIN REF_MEASUREMENT ident_list END REF_MEASUREMENT
        """
        p[0] = ASTNodes.Ref_Measurement(Identifier=p[3])

    def p_REF_MEMORY_SEGMENT(self, p):
        """
        ref_memory_segment     : REF_MEMORY_SEGMENT ident
        """
        p[0] = ASTNodes.Ref_Memory_Segment(p[2])

    def p_REF_UNIT(self, p):
        """
        ref_unit     : REF_UNIT ident
        """
        p[0] = ASTNodes.Ref_Unit(p[2])

    def p_RESERVED(self, p):
        """
        reserved     : RESERVED constant datasize
        """
        p[0] = ASTNodes.Reserved(Position=p[2], DataSize=p[3])

    def p_RIGHT_SHIFT(self, p):
        """
        right_shift     : RIGHT_SHIFT constant
        """
        p[0] = ASTNodes.Right_Shift(p[2])

    def p_RIP_ADDR_X(self, p):
        """
        rip_addr_x     : RIP_ADDR_X constant datatype
        """
        p[0] = ASTNodes.Rip_Addr_X(Position=p[2], Datatype=p[3])

    def p_RIP_ADDR_W(self, p):
        """
        rip_addr_w     : RIP_ADDR_W constant datatype
        """
        p[0] = ASTNodes.Rip_Addr_W(Position=p[2], Datatype=p[3])

    def p_RIP_ADDR_Y(self, p):
        """
        rip_addr_y     : RIP_ADDR_Y constant datatype
        """
        p[0] = ASTNodes.Rip_Addr_Y(Position=p[2], Datatype=p[3])

    def p_RIP_ADDR_Z(self, p):
        """
        rip_addr_z     : RIP_ADDR_Z constant datatype
        """
        p[0] = ASTNodes.Rip_Addr_Z(Position=p[2], Datatype=p[3])

    def p_RIP_ADDR_Z4(self, p):
        """
        rip_addr_z4     : RIP_ADDR_Z4 constant datatype
        """
        p[0] = ASTNodes.Rip_Addr_Z4(Position=p[2], Datatype=p[3])

    def p_RIP_ADDR_Z5(self, p):
        """
        rip_addr_z5     : RIP_ADDR_Z5 constant datatype
        """
        p[0] = ASTNodes.Rip_Addr_Z5(Position=p[2], Datatype=p[3])

    def p_ROOT(self, p):
        """
        root     : ROOT
        """
        p[0] = ASTNodes.Root(Boolean=True)

    def p_SHIFT_OP_X(self, p):
        """
        shift_op_x     : SHIFT_OP_X constant datatype
        """
        p[0] = ASTNodes.Shift_Op_X(Position=p[2], Datatype=p[3])

    def p_SHIFT_OP_Y(self, p):
        """
        shift_op_y     : SHIFT_OP_Y constant datatype
        """
        p[0] = ASTNodes.Shift_Op_Y(Position=p[2], Datatype=p[3])

    def p_SHIFT_OP_Z(self, p):
        """
        shift_op_z     : SHIFT_OP_Z constant datatype
        """
        p[0] = ASTNodes.Shift_Op_Z(Position=p[2], Datatype=p[3])

    def p_SHIFT_OP_Z4(self, p):
        """
        shift_op_z4     : SHIFT_OP_Z4 constant datatype
        """
        p[0] = ASTNodes.Shift_Op_Z4(Position=p[2], Datatype=p[3])

    def p_SHIFT_OP_Z5(self, p):
        """
        shift_op_z5     : SHIFT_OP_Z5 constant datatype
        """
        p[0] = ASTNodes.Shift_Op_Z5(Position=p[2], Datatype=p[3])

    def p_SIGN_EXTEND(self, p):
        """
        sign_extend     : SIGN_EXTEND
        """
        p[0] = ASTNodes.Sign_Extend(Boolean=True)

    def p_SI_EXPONENTS(self, p):
        """
        si_exponents     : SI_EXPONENTS constant constant constant constant constant constant constant
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

    def p_SRC_ADDR_X(self, p):
        """
        src_addr_x     : SRC_ADDR_X constant datatype
        """
        p[0] = ASTNodes.Src_Addr_X(Position=p[2], Datatype=p[3])

    def p_SRC_ADDR_Y(self, p):
        """
        src_addr_y     : SRC_ADDR_Y constant datatype
        """
        p[0] = ASTNodes.Src_Addr_Y(Position=p[2], Datatype=p[3])

    def p_SRC_ADDR_Z(self, p):
        """
        src_addr_z     : SRC_ADDR_Z constant datatype
        """
        p[0] = ASTNodes.Src_Addr_Z(Position=p[2], Datatype=p[3])

    def p_SRC_ADDR_Z4(self, p):
        """
        src_addr_z4     : SRC_ADDR_Z4 constant datatype
        """
        p[0] = ASTNodes.Src_Addr_Z4(Position=p[2], Datatype=p[3])

    def p_SRC_ADDR_Z5(self, p):
        """
        src_addr_z5     : SRC_ADDR_Z5 constant datatype
        """
        p[0] = ASTNodes.Src_Addr_Z5(Position=p[2], Datatype=p[3])

    def p_STATIC_RECORD_LAYOUT(self, p):
        """
        static_record_layout     : STATIC_RECORD_LAYOUT
        """
        p[0] = ASTNodes.Static_Record_Layout(Boolean=True)

    def p_STATUS_STRING_REF(self, p):
        """
        status_string_ref     : STATUS_STRING_REF ident
        """
        # ConversionTable
        p[0] = ASTNodes.Status_String_Ref(p[2])

    def p_STEP_SIZE(self, p):
        """
        step_size     : STEP_SIZE constant
        """
        p[0] = ASTNodes.Step_Size(p[2])

    def p_SUB_FUNCTION(self, p):
        """
        sub_function     : BEGIN SUB_FUNCTION ident_list END SUB_FUNCTION
        """
        p[0] = ASTNodes.Sub_Function(Identifier=p[3])

    def p_SUB_GROUP(self, p):
        """
        sub_group     : BEGIN SUB_GROUP ident_list END SUB_GROUP
        """
        p[0] = ASTNodes.Sub_Group(p[3])

    def p_SUPPLIER(self, p):
        """
        supplier     : SUPPLIER string_literal
        """
        p[0] = ASTNodes.Supplier(p[2])

    def p_SYMBOL_LINK(self, p):
        """
        symbol_link     : SYMBOL_LINK string_literal constant
        """
        p[0] = ASTNodes.Symbol_Link(SymbolName=p[2], Offset=p[3])

    def p_SYSTEM_CONSTANT(self, p):
        """
        system_constant     : SYSTEM_CONSTANT string_literal string_literal
        """
        p[0] = ASTNodes.System_Constant(Name=p[2], Value=p[3])

    def p_UNIT(self, p):
        """
        unit     : BEGIN UNIT ident string_literal string_literal unit_type_enum END UNIT
                 | BEGIN UNIT ident string_literal string_literal unit_type_enum unit_opt_list END UNIT
        """
        node = self._create_ast_node(ASTNodes.Unit(Name=p[3], LongIdentifier=p[4], Display=p[5], Type=p[6]))

        if len(p) == 10:
            node.OptionalParams = p[7]

        p[0] = node

        self._remove_ast_node(ASTNodes.Unit)
        self._remove_ast_node(ASTNodes.Unit_Opt)

    def p_UNIT_opt_params(self, p):
        """
        unit_opt    : ref_unit
        """
        node = self._get_or_create_ast_node(ASTNodes.Unit_Opt)
        self._add_ast_node_param(node_class=node, ast_node_names=[ASTNodes.Ref_Unit], param=p[1])

        p[0] = node

    def p_UNIT_opt_objects(self, p):
        """
        unit_opt    : si_exponents
                    | unit_conversion
        """
        node = self._get_or_create_ast_node(ASTNodes.Unit_Opt)
        self._add_ast_node_object(node_class=node, ast_node_names=[ASTNodes.Si_Exponents, ASTNodes.Unit_Conversion], param=p[1])
        p[0] = node

    def p_UNIT_opt_list(self, p):
        """
        unit_opt_list    : unit_opt
                        | unit_opt_list unit_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_UNIT_CONVERSION(self, p):
        """
        unit_conversion     : UNIT_CONVERSION constant constant
        """
        p[0] = ASTNodes.Unit_Conversion(Gradient=p[2], Offset=p[3])

    def p_USER(self, p):
        """
        user     : USER string_literal
        """
        p[0] = ASTNodes.User(p[2])

    def p_USER_RIGHTS(self, p):
        """
        user_rights     : BEGIN USER_RIGHTS ident END USER_RIGHTS
                        | BEGIN USER_RIGHTS ident user_rights_opt_list END USER_RIGHTS
        """
        node = self._create_ast_node(ASTNodes.User_Rights(UserLevelId=p[3]))

        if len(p) == 7:
            node.OptionalParams = p[4]

        p[0] = node

        self._remove_ast_node(ASTNodes.User_Rights)
        self._remove_ast_node(ASTNodes.User_Rights_Opt)

    def p_USER_RIGHTS_opt_params(self, p):
        """
        user_rights_opt    : read_only
        """
        node = self._get_or_create_ast_node(ASTNodes.User_Rights_Opt)
        self._add_ast_node_param(node_class=node, ast_node_names=[ASTNodes.Read_Only], param=p[1])
        p[0] = node

    def p_USER_RIGHTS_opt_objects_list(self, p):
        """
        user_rights_opt    : ref_group
        """
        node = self._get_or_create_ast_node(ASTNodes.User_Rights_Opt)
        self._add_ast_node_object_list(node_class=node, ast_node_names=[ASTNodes.Ref_Group], param=p[1])
        p[0] = node

    def p_USER_RIGHTS_opt_list(self, p):
        """
        user_rights_opt_list    : user_rights_opt
                        | user_rights_opt_list user_rights_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_VAR_ADDRESS(self, p):
        """
        var_address     : BEGIN VAR_ADDRESS constant_list END VAR_ADDRESS
        """
        if len(p) > 2:
            p[0] = ASTNodes.Var_Address(p[3])

    def p_VAR_CHARACTERISTIC(self, p):
        """
        var_characteristic     : BEGIN VAR_CHARACTERISTIC ident ident_list END VAR_CHARACTERISTIC
                               | BEGIN VAR_CHARACTERISTIC ident ident_list var_address END VAR_CHARACTERISTIC
                               | BEGIN VAR_CHARACTERISTIC ident ident_list meta_block_empty END VAR_CHARACTERISTIC
        """
        if len(p) == 7:
            p[0] = ASTNodes.Var_Characteristic(Name=p[3], CriterionName=p[4])
        else:
            p[0] = ASTNodes.Var_Characteristic(Name=p[3], CriterionName=p[4], Var_Address=p[5])

    def p_VAR_CRITERION(self, p):
        """
        var_criterion     : BEGIN VAR_CRITERION ident string_literal ident_list END VAR_CRITERION
                          | BEGIN VAR_CRITERION ident string_literal ident_list var_criterion_opt_list END VAR_CRITERION
        """
        node = self._create_ast_node(ASTNodes.Var_Criterion(Name=p[3], LongIdentifier=p[4], Value=p[5]))

        if len(p) == 9:
            node.OptionalParams = p[6]

        p[0] = node

        self._remove_ast_node(ASTNodes.Var_Criterion)
        self._remove_ast_node(ASTNodes.Var_Criterion_Opt)

    def p_VAR_CRITERION_opt(self, p):
        """
        var_criterion_opt    : var_measurement
                             | var_selection_characteristic

        """
        node = self._get_or_create_ast_node(ASTNodes.Var_Criterion_Opt)
        self._add_ast_node_param(
            node_class=node, ast_node_names=[ASTNodes.Var_Measurement, ASTNodes.Var_Selection_Characteristic], param=p[1]
        )

        p[0] = node

    def p_VAR_CRITERION_opt_list(self, p):
        """
        var_criterion_opt_list    : var_criterion_opt
                        | var_criterion_opt_list var_criterion_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_VAR_FORBIDDEN_COMB(self, p):
        """
        var_forbidden_comb     : BEGIN VAR_FORBIDDEN_COMB ident_ident_list END VAR_FORBIDDEN_COMB
        """
        p[0] = ASTNodes.Var_Forbidden_Comb(p[3])

    def p_VAR_MEASUREMENT(self, p):
        """
        var_measurement     : VAR_MEASUREMENT ident
        """
        p[0] = ASTNodes.Var_Measurement(p[2])

    def p_VAR_NAMING(self, p):
        """
        var_naming     : VAR_NAMING tag_enum
        """
        p[0] = ASTNodes.Var_Naming(p[2])

    def p_VAR_SELECTION_CHARACTERISTIC(self, p):
        """
        var_selection_characteristic     : VAR_SELECTION_CHARACTERISTIC ident
        """
        p[0] = ASTNodes.Var_Selection_Characteristic(p[2])

    def p_VAR_SEPARATOR(self, p):
        """
        var_seperator     : VAR_SEPARATOR string_literal
        """
        p[0] = ASTNodes.Var_Separator(p[2])

    def p_VARIANT_CODING(self, p):
        """
        variant_coding     : BEGIN VARIANT_CODING variant_coding_opt_list END VARIANT_CODING
        """
        node = self._create_ast_node(ASTNodes.Variant_Coding())

        if len(p) == 6:
            node.OptionalParams = p[3]

        p[0] = node

        self._remove_ast_node(ASTNodes.Variant_Coding)
        self._remove_ast_node(ASTNodes.Variant_Coding_Opt)

    def p_VARIANT_CODING_opt_params(self, p):
        """
        variant_coding_opt    : var_naming
                              | var_seperator

        """
        node = self._get_or_create_ast_node(ASTNodes.Variant_Coding_Opt)
        self._add_ast_node_param(node_class=node, ast_node_names=[ASTNodes.Var_Naming, ASTNodes.Var_Separator], param=p[1])

        p[0] = node

    def p_VARIANT_CODING_opt_objects_list(self, p):
        """
        variant_coding_opt    : var_characteristic
                              | var_criterion
                              | var_forbidden_comb
        """
        node = self._get_or_create_ast_node(ASTNodes.Variant_Coding_Opt)
        self._add_ast_node_object_list(
            node_class=node,
            ast_node_names=[ASTNodes.Var_Characteristic, ASTNodes.Var_Criterion, ASTNodes.Var_Forbidden_Comb],
            param=p[1],
        )
        p[0] = node

    def p_VARIANT_CODING_opt_list(self, p):
        """
        variant_coding_opt_list    : variant_coding_opt
                        | variant_coding_opt_list variant_coding_opt
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_VERSION(self, p):
        """
        version     : VERSION string_literal
        """
        p[0] = ASTNodes.Version(p[2])

    def p_VIRTUAL(self, p):
        """
        virtual     : BEGIN VIRTUAL ident_list END VIRTUAL
        """
        p[0] = ASTNodes.Virtual(MeasuringChannel=p[3])

    def p_VIRTUAL_CHARACTERISTIC(self, p):
        """
        virtual_characteristic     : BEGIN VIRTUAL_CHARACTERISTIC string_literal ident_list END VIRTUAL_CHARACTERISTIC
        """
        p[0] = ASTNodes.Virtual_Characteristic(Formula=p[3], Characteristic=p[4])

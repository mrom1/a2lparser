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


import os, sys
from a2lparser.logger.logger import Logger


class Config():
    def __init__(self,
                 debug = False,
                 gen_dir = 'gen',
                 optimize = 1,
                 write_buffer='sys.stdout',
                 write_tables = True,
                 error_resolve = False,
                 verbosity=0,
                 a2l_yacc_tab_name = '_a2l_yacctables',
                 a2l_lex_tab_name = '_a2l_lextables',
                 ):


        self.debug_active = debug
        self.error_resolve_active = error_resolve
        self.gen_dir = gen_dir
        self.optimize = optimize
        self.write_buffer = write_buffer
        self.write_tables = write_tables
        self.verbosity = verbosity
        self.yacc_tab = a2l_yacc_tab_name
        self.lex_tab = a2l_lex_tab_name

        self.logger_manager = Logger()
        self.logger = self.logger_manager.new_module("CONFIG")

        try:
            from a2lparser.a2l.ast import a2l_ast as A2l_ast
        except ImportError:
            try:
                from a2lparser.a2l.config.config_builder import ConfigBuilder
                cfg_file_name = os.getcwd() + "/gen/_A2L_ast.cfg"
                out_filename = os.getcwd() + "/a2l/ast/a2l_ast.py"
                cfg_file = open(cfg_file_name, "w")
                cfg_file.write(_DEFAULT_CONFIG)
                cfg_file.close()
                ConfigBuilder(config=cfg_file_name, output_filename=out_filename)
                sys.exit()
            except ImportError:
                pass

            from a2lparser.a2l.ast import a2l_ast as A2l_ast

        fn = A2l_ast.__dict__
        self.ast_a2l_nodes = {i:fn[i] for i in fn if (i != 'sys' and not i.startswith('_')) and (not(i.endswith('_Opt') or i.endswith('_Opt_List') or i == 'Abstract_Syntax_Tree' or i == 'If_Data_Block_List')) }
        self.ast_a2l_nodes_opt_only = {i:fn[i] for i in fn if (i != 'sys' and not i.startswith('_')) and (i.endswith('_Opt') or i.endswith('_Opt_List')) or (i == 'Abstract_Syntax_Tree' or i == 'If_Data_Block_List')}

        self.xml_types = ["Measurement", "Characteristic", "Compu_Method", "Compu_Tab"]
        self.xml_types_ref = ["Ref_Measurement", "Ref_Characteristic"]
        self.xml_ref_names = {"Measurement" : "signalMeasurementId",
                              "Characteristic" : "characteristicId",
                              "Compu_Method" : "compuMethodId",
                              "Compu_Tab" : "compuTabId",
                              "Ref_Measurement" : "signalMeasurementId",
                              "Ref_Characteristic" : "characteristicId"
                              }
        if verbosity > 1:
            self.printConfiguration()


    def printConfiguration(self):
        self.logger_manager.set_level("INFO")
        self.logger.info("Configuration initilized with params:")
        self.logger.info("Debugging active: %s" % bool(self.debug_active))
        self.logger.info("Error resolving active: %s" % bool(self.error_resolve_active))
        self.logger.info("Optimiziation active: %s" % bool(self.optimize))
        self.logger.info("Write YACC Tables: %s" % bool(self.write_tables))
        self.logger.info("Generation Files Folder: %s" % os.path.abspath(self.gen_dir))


    def validateAST(self, AST):
        if hasattr(AST, "children"):
            children = AST.children()
            for (child_name, child) in children:
                if child.__class__.__name__ in self.ast_a2l_nodes:
                    return True
        return False


_DEFAULT_CONFIG = """
ABSTRACT_SYNTAX_TREE : (node**)
A2ML_VERSION: (VersionNo*, UpgradeNo*)
ADDR_EPK: (Address)
ALIGNMENT_BYTE: (AlignmentBorder)
ALIGNMENT_FLOAT32_IEEE: (AlignmentBorder)
ALIGNMENT_FLOAT64_IEEE: (AlignmentBorder)
ALIGNMENT_INT64: (AlignmentBorder)
ALIGNMENT_LONG: (AlignmentBorder)
ALIGNMENT_WORD: (AlignmentBorder)
ANNOTATION: (?OptionalParams*)
ANNOTATION_OPT: (?Annotation_Label, ?Annotation_Origin, ?Annotation_Text)
ANNOTATION_LABEL: (label)
ANNOTATION_ORIGIN: (origin)
ANNOTATION_TEXT: (annotation_text)
ARRAY_SIZE: (Number)
ASAP2_VERSION:  (VersionNo, UpgradeNo)
AXIS_DESCR: (Attribute, InputQuantity, Conversion, MaxAxisPoints, LowerLimit, UpperLimit, ?OptionalParams*)
AXIS_DESCR_OPT : (?Annotation**, ?Axis_Pts_Ref, ?Byte_Order, ?Curve_Axis_Ref, ?Deposit, ?Extended_Limits*, ?Fix_Axis_Par*, ?Fix_Axis_Par_Dist*,  ?Fix_Axis_Par_List*, ?Format, ?Max_Grad, ?Monotony, ?Phys_Unit, ?Read_Only, ?Step_Size)
AXIS_PTS: (Name, LongIdentifier, Address, InputQuantity, Deposit_Ref, MaxDiff, Conversion, MaxAxisPoints, LowerLimit, UpperLimit, ?OptionalParams* )
AXIS_PTS_OPT : (?Annotation**, ?Byte_Order, ?Calibration_Access, ?Display_Identifier, ?Deposit, ?Ecu_Address_Extension, ?Extended_Limits*, ?Format, ?Function_List*, ?Guard_Rails, ?If_Data**, ?Monotony, ?Phys_Unit, ?Read_Only, ?Ref_Memory_Segment, ?Step_Size, ?Symbol_Link*)
AXIS_PTS_REF: (AxisPoints)
AXIS_PTS_X :(Position, Datatype, IndexIncr, Addressing)
AXIS_PTS_Y :(Position, Datatype, IndexIncr, Addressing)
AXIS_PTS_Z :(Position, Datatype, IndexIncr, Addressing)
AXIS_PTS_Z4 :(Position, Datatype, IndexIncr, Addressing)
AXIS_PTS_Z5 :(Position, Datatype, IndexIncr, Addressing)
AXIS_RESCALE_X: (Position, Datatype, MaxNumberOfRescalePairs, IndexIncr, Addressing)
BIT_MASK: (Mask)
BIT_OPERATION :(?OptionalParams*)
BIT_OPERATION_OPT : (?Left_Shift*, ?Right_Shift*, ?Sign_Extend*)
BYTE_ORDER: (Byte_Order)
CALIBRATION_ACCESS :(Type)
CALIBRATION_HANDLE :(Handle, ?Calibration_Handle_Text*)
CALIBRATION_HANDLE_OPT : (?Calibration_Handle_Text)
CALIBRATION_HANDLE_TEXT: (Text)
CALIBRATION_METHOD: (Method, Version, ?Calibration_Handle**)
CHARACTERISTIC: (Name, LongIdentifier, Type, Address, Deposit_Ref, MaxDiff, Conversion, LowerLimit, UpperLimit, ?OptionalParams* )
CHARACTERISTIC_OPT : (?Annotation**, ?Axis_Descr**, ?Bit_Mask, ?Byte_Order, ?Calibration_Access, ?Comparison_Quantity, ?Dependent_Characteristic*, ?Discrete, ?Display_Identifier, ?Ecu_Address_Extension, ?Extended_Limits*, ?Format, ?Function_List*, ?Guard_Rails, ?If_Data**, ?Map_List*, ?Matrix_Dim*, ?Max_Refresh*, ?Number, ?Phys_Unit, ?Read_Only, ?Ref_Memory_Segment, ?Step_Size, ?Symbol_Link*, ?Virtual_Characteristic*)
COEFFS: (a, b, c, d, e, f)
COEFFS_LINEAR: (a, b)
COMPARISON_QUANTITY: (Name)
COMPU_METHOD : (Name, LongIdentifier, ConversionType, Format, Unit, ?OptionalParams*)
COMPU_METHOD_OPT : (?Coeffs*, ?Coeffs_Linear*, ?Compu_Tab_Ref, ?Formula*, ?Ref_Unit, ?Status_String_Ref)
COMPU_TAB : (Name, LongIdentifier, ConversionType, NumberValuePairs, Axis_Points, ?OptionalParams*)
COMPU_TAB_OPT : (?Default_Value, ?Default_Value_Numeric)
COMPU_TAB_REF : (ConversionTable)
COMPU_VTAB : (Name, LongIdentifier, ConversionType, NumberValuePairs, InVal_OutVal, ?Default_Value)
COMPU_VTAB_RANGE : (Name, LongIdentifier, NumberValueTriples, InVal_MinMax_OutVal, ?Default_Value)
CPU_TYPE : (CPU)
CURVE_AXIS_REF: (CurveAxis)
CUSTOMER: (Customer)
CUSTOMER_NO: (Number)
DATA_SIZE: (Size)
DEF_CHARACTERISTIC: (Identifier)
DEFAULT_VALUE :(display_string)
DEFAULT_VALUE_NUMERIC: (display_value)
DEPENDENT_CHARACTERISTIC: (Formula, Characteristic)
DEPOSIT : (Mode)
DISCRETE: (Boolean)
DISPLAY_IDENTIFIER :(display_name)
DIST_OP_X :(Position, Datatype)
DIST_OP_Y :(Position, Datatype)
DIST_OP_Z :(Position, Datatype)
DIST_OP_Z4 :(Position, Datatype)
DIST_OP_Z5 :(Position, Datatype)
ECU : (ControlUnit)
ECU_ADDRESS :(Address)
ECU_ADDRESS_EXTENSION :(Extension)
ECU_CALIBRATION_OFFSET : (Offset)
EPK : (Identifier)
ERROR_MASK : (Mask)
EXTENDED_LIMITS : (LowerLimit, UpperLimit)
FIX_AXIS_PAR : (Offset, Shift, Numberapo)
FIX_AXIS_PAR_DIST : (Offset, Distance, Numberapo)
FIX_AXIS_PAR_LIST : (AxisPts_Value)
FIX_NO_AXIS_PTS_X : (NumberOfAxisPoints)
FIX_NO_AXIS_PTS_Y : (NumberOfAxisPoints)
FIX_NO_AXIS_PTS_Z : (NumberOfAxisPoints)
FIX_NO_AXIS_PTS_Z4 : (NumberOfAxisPoints)
FIX_NO_AXIS_PTS_Z5 : (NumberOfAxisPoints)
FNC_VALUES : (Position, Datatype, IndexMode, AddressType)
FORMAT : (FormatString)
FORMULA : (f_x, ?Formula_Inv*)
FORMULA_INV : (g_x)
FRAME : (Name, LongIdentifier, ScalingUnit, Rate, ?OptionalParams*)
FRAME_OPT : (?Frame_Measurement, ?If_Data**)
FRAME_MEASUREMENT : (Identifier)
FUNCTION : (Name, LongIdentifier, ?OptionalParams*)
FUNCTION_OPT : (?Annotation**, ?Def_Characteristic*, ?Function_Version, ?If_Data**, ?In_Measurement*, ?Loc_Measurement*, ?Out_Measurement*, ?Ref_Characteristic*, ?Sub_Function**)
FUNCTION_LIST : (Name)
FUNCTION_VERSION : (VersionIdentifier)
GROUP : (GroupName, GroupLongIdentifier, ?OptionalParams*)
GROUP_OPT : (?Annotation**, ?Function_List*, ?If_Data**, ?Ref_Characteristic*, ?Ref_Measurement*, ?Root, ?Sub_Group*)
GUARD_RAILS : (Boolean)
HEADER : (Comment, ?OptionalParams*)
HEADER_OPT : (?Project_No, ?Version)
IDENTIFICATION : (Position, Datatype)
IF_DATA : (Name, ?OptionalParams*)
IF_DATA_OPT : (?DataParams, ?If_Data_Block**)
IF_DATA_BLOCK : (?Name, ?DataParams, ?If_Data_Block**)
IN_MEASUREMENT : (Identifier)
LAYOUT : (IndexMode)
LEFT_SHIFT : (Bitcount)
LOC_MEASUREMENT : (Identifier)
MAP_LIST : (Name)
MATRIX_DIM : (xDim, yDim, zDim)
MAX_GRAD : (MaxGradient)
MAX_REFRESH : (ScalingUnit, Rate)
MEASUREMENT : (Name, LongIdentifier, Datatype, Conversion, Resolution, Accuracy, LowerLimit, UpperLimit, ?OptionalParams*)
MEASUREMENT_OPT : (?Annotation**, ?Array_Size, ?Bit_Mask, ?Bit_Operation*, ?Byte_Order, ?Discrete, ?Display_Identifier, ?Ecu_Address, ?Ecu_Address_Extension, ?Error_Mask, ?Format, ?Function_List*, ?If_Data**, ?Layout, ?Matrix_Dim*, ?Max_Refresh*, ?Phys_Unit, ?Read_Write, ?Ref_Memory_Segment, ?Symbol_Link*, ?Virtual*)
MEMORY_LAYOUT : (PrgType, Address, Size, Offset, ?If_Data**)
MEMORY_SEGMENT : (Name, LongIdentifier, PrgType, MemoryType, Attribute, Address, Size, Offset, ?If_Data**)
MOD_COMMON : (Comment, ?OptionalParams*)
MOD_COMMON_OPT : (?Alignment_Byte, ?Alignment_Float32_Ieee, ?Alignment_Float64_Ieee, ?Alignment_Int64, ?Alignment_Long, ?Alignment_Word, ?Byte_Order, ?Data_Size, ?Deposit)
MOD_PAR : (Comment, ?OptionalParams*)
MOD_PAR_OPT : (?Addr_Epk**, ?Calibration_Method**, ?Cpu_Type, ?Customer, ?Customer_No, ?Ecu, ?Ecu_Calibration_Offset, ?Epk, ?Memory_Layout**, ?Memory_Segment**, ?No_Of_Interfaces, ?Phone_No, ?Supplier, ?System_Constant**, ?User, ?Version)
MODULE : (Name, LongIdentifier, ?OptionalParams*)
MODULE_OPT : (?Axis_Pts**, ?Characteristic**, ?Compu_Method**, ?Compu_Tab**, ?Compu_Vtab**, ?Compu_Vtab_Range**, ?Frame**, ?Function**, ?Group**, ?If_Data**, ?Measurement**, ?Mod_Common*, ?Mod_Par*, ?Record_Layout**, ?Unit**, ?User_Rights**, ?Variant_Coding*)
MONOTONY : (Monotony)
NO_AXIS_PTS_X : (Position, Datatype)
NO_AXIS_PTS_Y : (Position, Datatype)
NO_AXIS_PTS_Z : (Position, Datatype)
NO_AXIS_PTS_Z4 : (Position, Datatype)
NO_AXIS_PTS_Z5 : (Position, Datatype)
NO_OF_INTERFACES  : (Num)
NO_RESCALE_X  : (Position, Datatype)
NUMBER : (Number)
OFFSET_X : (Position, Datatype)
OFFSET_Y : (Position, Datatype)
OFFSET_Z : (Position, Datatype)
OFFSET_Z4 : (Position, Datatype)
OFFSET_Z5 : (Position, Datatype)
OUT_MEASUREMENT : (Identifier)
PHONE_NO : (Telnum)
PHYS_UNIT : (Unit)
PROJECT : (Name, LongIdentifier, ?OptionalParams*)
PROJECT_OPT : (?Header*, ?Module**)
PROJECT_NO : (ProjectNumber)
READ_ONLY : (Boolean)
READ_WRITE : (Boolean)
RECORD_LAYOUT : (Name, ?OptionalParams*)
RECORD_LAYOUT_OPT : (?Alignment_Byte, ?Alignment_Float32_Ieee, ?Alignment_Float64_Ieee, ?Alignment_Int64, ?Alignment_Long, ?Alignment_Word, ?Axis_Pts_X*, ?Axis_Pts_Y*, ?Axis_Pts_Z*, ?Axis_Pts_Z4*, ?Axis_Pts_Z5*, ?Axis_Rescale_X*, ?Dist_Op_X*, ?Dist_Op_Y*, ?Dist_Op_Z*, ?Dist_Op_Z4*, ?Dist_Op_Z5*, ?Fix_No_Axis_Pts_X, ?Fix_No_Axis_Pts_Y, ?Fix_No_Axis_Pts_Z, ?Fix_No_Axis_Pts_Z4, ?Fix_No_Axis_Pts_Z5, ?Fnc_Values*, ?Identification*, ?No_Axis_Pts_X*, ?No_Axis_Pts_Y*, ?No_Axis_Pts_Z*, ?No_Axis_Pts_Z4*, ?No_Axis_Pts_Z5*, ?No_Rescale_X*, ?Offset_X*, ?Offset_Y*, ?Offset_Z*, ?Offset_Z4*, ?Offset_Z5*, ?Reserved**, ?Rip_Addr_X*, ?Rip_Addr_W*, ?Rip_Addr_Y*, ?Rip_Addr_Z*, ?Rip_Addr_Z4*, ?Rip_Addr_Z5*, ?Src_Addr_X*, ?Src_Addr_Y*, ?Src_Addr_Z*, ?Src_Addr_Z4*, ?Src_Addr_Z5*, ?Shift_Op_X*, ?Shift_Op_Y*, ?Shift_Op_Z*, ?Shift_Op_Z4*, ?Shift_Op_Z5*, ?Static_Record_Layout)
REF_CHARACTERISTIC : (Identifier)
REF_GROUP : (Identifier)
REF_MEASUREMENT : (Identifier)
REF_MEMORY_SEGMENT : (Name)
REF_UNIT : (Unit)
RESERVED : (Position, DataSize)
RIGHT_SHIFT : (Bitcount)
RIP_ADDR_X  : (Position, Datatype)
RIP_ADDR_W  : (Position, Datatype)
RIP_ADDR_Y  : (Position, Datatype)
RIP_ADDR_Z  : (Position, Datatype)
RIP_ADDR_Z4 : (Position, Datatype)
RIP_ADDR_Z5 : (Position, Datatype)
ROOT : (Boolean)
SHIFT_OP_X : (Position, Datatype)
SHIFT_OP_Y : (Position, Datatype)
SHIFT_OP_Z : (Position, Datatype)
SHIFT_OP_Z4 : (Position, Datatype)
SHIFT_OP_Z5 : (Position, Datatype)
SIGN_EXTEND : (Boolean)
SI_EXPONENTS : (Length, Mass, Time, ElectricCurrent, Temperature, AmountOfSubstance, LuminousIntensity)
SRC_ADDR_X : (Position, Datatype)
SRC_ADDR_Y : (Position, Datatype)
SRC_ADDR_Z : (Position, Datatype)
SRC_ADDR_Z4 : (Position, Datatype)
SRC_ADDR_Z5 : (Position, Datatype)
STATIC_RECORD_LAYOUT : (Boolean)
STATUS_STRING_REF : (ConversionTable)
STEP_SIZE : (StepSize)
SUB_FUNCTION : (Identifier)
SUB_GROUP : (Identifier)
SUPPLIER : (Manufacturer)
SYMBOL_LINK : (SymbolName, Offset)
SYSTEM_CONSTANT : (Name, Value)
UNIT : (Name, LongIdentifier, Display, Type, ?OptionalParams*)
UNIT_OPT : (?Ref_Unit, ?Si_Exponents*, ?Unit_Conversion*)
UNIT_CONVERSION : (Gradient, Offset)
USER : (UserName)
USER_RIGHTS : (UserLevelId, ?OptionalParams*)
USER_RIGHTS_OPT : (?Read_Only, ?Ref_Group**)
VAR_ADDRESS : (Address)
VAR_CHARACTERISTIC  : (Name, CriterionName, ?Var_Address*)
VAR_CRITERION : (Name, LongIdentifier, Value, ?OptionalParams*)
VAR_CRITERION_OPT : (?Var_Measurement, ?Var_Selection_Characteristic)
VAR_FORBIDDEN_COMB : (CriterionList)
VAR_MEASUREMENT : (Name)
VAR_NAMING : (Tag)
VAR_SELECTION_CHARACTERISTIC : (Name)
VAR_SEPARATOR : (Separator)
VARIANT_CODING : (?OptionalParams*)
VARIANT_CODING_OPT : (?Var_Characteristic**, ?Var_Criterion**, ?Var_Forbidden_Comb**, ?Var_Naming, ?Var_Separator)
VERSION : (VersoinIdentifier)
VIRTUAL : (MeasuringChannel)
VIRTUAL_CHARACTERISTIC : (Formula, Characteristic)
"""

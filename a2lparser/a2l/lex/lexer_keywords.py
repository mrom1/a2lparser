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


class LexerKeywords:
    """
    Holds a collection of keyword tags used in an A2L file.
    """

    #############################################
    # Keywords for parsing A2L sections.        #
    # All section keywords are enclosed by an   #
    # interpreted "/begin" and an "/end" token. #
    #                                           #
    # Example:                                  #
    # /begin VAR_ADDRESS                        #
    #   0x8840                                  #
    #   0x8858                                  #
    #   0x8870                                  #
    #   0x8888                                  #
    # /end VAR_ADDRESS                          #
    #############################################
    keywords_section: list = [
        # A2ML format keyword
        "A2ML",
        # Annotation
        "ANNOTATION",
        "ANNOTATION_TEXT",
        # Axis description and points
        "AXIS_DESCR",
        "AXIS_PTS",
        # Calibartion
        "CALIBRATION_HANDLE",
        "CALIBRATION_METHOD",
        # Characteristic section
        "CHARACTERISTIC",
        # Computation
        "COMPU_METHOD",
        "COMPU_TAB",
        "COMPU_VTAB",
        "COMPU_VTAB_RANGE",
        # Dependent characteristic
        "DEPENDENT_CHARACTERISTIC",
        # Fix axis par
        "FIX_AXIS_PAR_LIST"
        # Formula
        "FORMULA",
        # Frame
        "FRAME",
        # Function
        "FUNCTION",
        "FUNCTION_LIST",
        # Group
        "GROUP",
        # Header
        "HEADER"
        # Interface data
        "IF_DATA",
        # Measurement
        "IN_MEASUREMENT",
        "LOC_MEASUREMENT",
        "MEASUREMENT",
        # MAP_LIST
        "MAP_LIST",
        # MEMORY_LAYOUT
        "MEMORY_LAYOUT",
        # MEMORY_SEGMENT
        "MEMORY_SEGMENT",
        # MOD_COMMON
        "MOD_COMMON",
        # MOD_PAR
        "MOD_PAR",
        # MODULE
        "MODULE",
        # OUT_MEASUREMENT
        "OUT_MEASUREMENT",
        # PROJECT
        "PROJECT",
        # RECORD_LAYOUT
        "RECORD_LAYOUT",
        # REF_CHARACTERISTIC
        "REF_CHARACTERISTIC",
        "REF_GROUP",
        "REF_MEASUREMENT",
        # SUB_FUNCTION
        "SUB_FUNCTION",
        # SUB_GROUP
        "SUB_GROUP",
        # UNIT
        "UNIT",
        # USER_RIGHTS
        "USER_RIGHTS",
        # Variant sections
        "VAR_ADDRESS",
        "VAR_CHARACTERISTIC",
        "VAR_CRITERION",
        "VAR_FORBIDDEN_COMB",
        "VARIANT_CODING",
        # Virtual
        "VIRTUAL",
        "VIRTUAL_CHARACTERISTIC",
    ]

    ################################################
    # Keywords for parsing A2L types.              #
    # All type keywords are followed by some data. #
    # These keywords do not use an enclosing       #
    # BEGIN and END section.                       #
    #                                              #
    # Example:                                     #
    # A2ML_VERSION                                 #
    #   1                                          #
    #   61  // Version 1.6.1                       #
    ################################################
    keywords_type: list = [
        # A2ML_VERSION
        "A2ML_VERSION",
        # ADDR_EPK
        "ADDR_EPK",
        # Alignment Tokens
        "ALIGNMENT_BYTE",
        "ALIGNMENT_FLOAT32_IEEE",
        "ALIGNMENT_FLOAT64_IEEE",
        "ALIGNMENT_INT64",
        "ALIGNMENT_LONG",
        "ALIGNMENT_WORD",
        # Single optional annotation types
        "ANNOTATION_LABEL",
        "ANNOTATION_ORIGIN",
        "ARRAY_SIZE",
        "ASAP2_VERSION",
        # Axis points
        "AXIS_PTS_REF",
        "AXIS_PTS_X",
        "AXIS_PTS_Y",
        "AXIS_PTS_Z",
        "AXIS_PTS_4",
        "AXIS_PTS_5",
        "AXIS_RESCALE_X",
        # Bit operations
        "BIT_MASK",
        "BIT_OPERATION",
        "BYTE_ORDER",
        # Calibration keywords
        "CALIBRATION_ACCESS",
        "CALIBRATION_HANDLE_TEXT",
        # Coefficients keywords
        "COEFFS",
        "COEFFS_LINEAR",
        "COMPARISON_QUANTITY",
        # Computation
        "COMPU_TAB_REF",
        # Cpu
        "CPU_TYPE",
        # Curve charactersitic
        "CURVE_AXIS_REF",
        # Customer keywords
        "CUSTOMER",
        "CUSTOMER_NO",
        # Datasize
        "DATA_SIZE",
        # Default Values
        "DEF_CHARACTERISTIC",
        "DEFAULT_VALUE",
        "DEFAULT_VALUE_NUMERIC",
        # Deposit
        "DEPOSIT",
        # Discrete
        "DISCRETE",
        # Display identifier
        "DISPLAY_IDENTIFIER",
        # Distance operation
        "DIST_OP_X",
        "DIST_OP_Y",
        "DIST_OP_Z",
        "DIST_OP_4",
        "DIST_OP_5",
        # ECU keywords
        "ECU",
        "ECU_ADDRESS",
        "ECU_ADDRESS_EXTENSION",
        "ECU_CALIBRATION_OFFSET",
        # EPROM
        "EPK",
        # Error mask
        "ERROR_MASK",
        # Limits
        "EXTENDED_LIMITS",
        # Fix axis
        "FIX_AXIS_PAR",
        "FIX_AXIS_PAR_DIST",
        "FIX_NO_AXIS_PTS_X",
        "FIX_NO_AXIS_PTS_Y",
        "FIX_NO_AXIS_PTS_Z",
        "FIX_NO_AXIS_PTS_4",
        "FIX_NO_AXIS_PTS_5",
        # Function values
        "FNC_VALUES",
        # Format for strings / display
        "FORMAT",
        # Formula inverse function
        "FORMULA_INV",
        # Frame
        "FRAME_MEASUREMENT",
        # Function
        "FUNCTION_VERSION",
        # Guard rails for curves, maps, axis points
        "GUARD_RAILS",
        # Description of an 'identifier' in an adjustable object.
        "IDENTIFICATION",
        # LAYOUT keyword describes the layout of a multi-dimensional measurement array.
        "LAYOUT",
        # LEFT_SHIFT keyword used within the BIT_OPERATION keyword.
        "LEFT_SHIFT",
        # MATRIX_DIM
        "MATRIX_DIM",
        # MAX_GRAD
        "MAX_GRAD",
        # MAX_REFRESH
        "MAX_REFRESH",
        # MONOTONY
        "MONOTONY"
        # NO_AXIS_PTS
        "NO_AXIS_PTS_X",
        "NO_AXIS_PTS_Y",
        "NO_AXIS_PTS_Z",
        "NO_AXIS_PTS_4",
        "NO_AXIS_PTS_5",
        # NO_OF_INTERFACES
        "NO_OF_INTERFACES",
        # NO_RESCALE_X
        "NO_RESCALE_X",
        # NUMBER
        "NUMBER",
        # OFFSET
        "OFFSET_X",
        "OFFSET_Y",
        "OFFSET_Z",
        "OFFSET_4",
        "OFFSET_5",
        # PHONE_NO
        "PHONE_NO",
        # PHYS_UNIT
        "PHYS_UNIT",
        # Project number
        "PROJECT_NO",
        # Read write flags
        "READ_ONLY",
        "READ_WRITE"
        # REF_MEMORY_SEGMENT
        "REF_MEMORY_SEGMENT",
        "REF_UNIT",
        # RESERVED
        "RESERVED",
        # RIGHT_SHIFT
        "RIGHT_SHIFT",
        # RIP_ADDR
        "RIP_ADDR_W",
        "RIP_ADDR_X",
        "RIP_ADDR_Y",
        "RIP_ADDR_Z",
        "RIP_ADDR_4",
        "RIP_ADDR_5",
        # ROOT
        "ROOT",
        # SHIFT_OP
        "SHIFT_OP_X",
        "SHIFT_OP_Y",
        "SHIFT_OP_Z",
        "SHIFT_OP_4",
        "SHIFT_OP_5",
        # SIGN_EXTEND Bitoperation
        "SIGN_EXTEND",
        # SI_EXPONENTS
        "SI_EXPONENTS",
        # SRC_ADDR
        "SRC_ADDR_X",
        "SRC_ADDR_Y",
        "SRC_ADDR_Z",
        "SRC_ADDR_4",
        "SRC_ADDR_5",
        # STATIC_RECORD_LAYOUT
        "STATIC_RECORD_LAYOUT",
        # STATUS_STRING_REF
        "STATUS_STRING_REF",
        # STEP_SIZE
        "STEP_SIZE",
        # SUPPLIER
        "SUPPLIER",
        # SYMBOL_LINK
        "SYMBOL_LINK",
        # SYSTEM_CONSTANT
        "SYSTEM_CONSTANT",
        # UNIT_CONVERSION
        "UNIT_CONVERSION",
        # USER
        "USER",
        # Variants
        "VAR_MEASUREMENT",
        "VAR_NAMING",
        "VAR_SELECTION_CHARACTERISTIC",
        "VAR_SEPARATOR",
        # Version
        "VERSION",
    ]

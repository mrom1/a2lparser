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


class A2LKeywordsTypes:
    """
    Keywords for parsing A2L types.
    All type keywords are followed by some data.
    These keywords do not use an enclosing "BEGIN" and "END" section.

    Example:
        A2ML_VERSION
          1
          61  // Version 1.6.1
    """

    keywords: list = [
        # A2ML_VERSION
        "A2ML_VERSION",
        # ADDR_EPK
        "ADDR_EPK",
        # Alignment Tokens
        "ALIGNMENT_BYTE",
        "ALIGNMENT_FLOAT16_IEEE",
        "ALIGNMENT_FLOAT32_IEEE",
        "ALIGNMENT_FLOAT64_IEEE",
        "ALIGNMENT_INT64",
        "ALIGNMENT_LONG",
        "ALIGNMENT_WORD",
        # Single optional annotation types
        "ANNOTATION_LABEL",
        "ANNOTATION_ORIGIN",
        "ARRAY_SIZE",
        "AR_PROTOTYPE_OF",
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
        "CONSISTENT_EXCHANGE",
        "CONVERSION",
        # Coefficients keywords
        "COEFFS",
        "COEFFS_LINEAR",
        # Computation
        "COMPU_TAB_REF",
        "COMPARISON_QUANTITY",
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
        "IDENTIFICATION",
        "INPUT_QUANTITY",
        "LAYOUT",
        "LEFT_SHIFT",
        "LIMITS",
        "MATRIX_DIM",
        "MAX_GRAD",
        "MAX_REFRESH",
        "MODEL_LINK",
        "MONOTONY",
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
        "READ_WRITE",
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
        # STATICS
        "STATIC_ADDRESS_OFFSETS",
        "STATIC_RECORD_LAYOUT",
        # STATUS_STRING_REF
        "STATUS_STRING_REF",
        # STEP_SIZE
        "STEP_SIZE",
        # SUPPLIER
        "SUPPLIER",
        # SYMBOL_LINK
        "SYMBOL_LINK",
        "SYMBOL_TYPE_LINK",
        # SYSTEM_CONSTANT
        "SYSTEM_CONSTANT",
        "TRANSFORMER_IN_OBJECTS",
        "TRANSFORMER_OUT_OBJECTS",
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

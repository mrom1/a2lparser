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


from ply.lex import lex, LexToken, TOKEN
from a2lparser.logger.logger import Logger


class A2LLex:
    """
    Lexer class for the A2L parser.
    An object of this class may be passed to the ply yacc object as the lexer for parsing.

    Usage:
        >>> lexer = A2LLex()
        >>> y = yacc(...)
        >>> y.parse(lexer=lexer, input=...)
    """
    def __init__(self, **args) -> None:
        """
        A2L Lexer Constructor.
        Builds an instance of the ply lex object with an A2L configuration.

        Args:
            - **args: Arguments to be passed to ply.lex(**args)
        """
        self.logger_manager = Logger()
        self.logger = self.logger_manager.new_module("LEX")
        self.start_of_a2ml = 0
        self.end_of_a2ml = 0

        self.filename = ''
        self.last_token: LexToken

        self.lexer = lex(object=self, **args)
        self.lexer.lineno = 1

    def token(self) -> LexToken:
        """
        Retruns the current token the lexer processes.
        """
        self.last_token = self.lexer.token()
        return self.last_token

    def get_line_number(self):
        """
        Get the current line number.
        """
        return self.lexer.lineno

    def reset_line_number(self):
        """
        Resets the current line number of the lexer to 1.
        """
        self.lexer.lineno = 1

    def set_line_numer(self, lineno):
        """
        Sets the current line number to lineno.
        """
        self.lexer.lineno = lineno

    def input(self, text):
        """
        Passes the input text to the lexer.
        """
        self.lexer.input(text)

    def _error_handling(self, msg, token):
        """
        This function is called when an error occurs.
        Error handling is to report the error and skip the token.
        """
        self.logger.error(f"{msg} at {self.lexer.lineno} on {token}")
        self.lexer.skip(1)

    # A2L Keywords
    keywords = ('BEGIN', 'END',

                # Predefined Keywords
                'A2ML_VERSION', 'ADDR_EPK', 'ASAP2_VERSION',

                # Alignments
                'ALIGNMENT_BYTE', 'ALIGNMENT_FLOAT32_IEEE', 'ALIGNMENT_FLOAT64_IEEE',
                'ALIGNMENT_INT64', 'ALIGNMENT_LONG', 'ALIGNMENT_WORD',

                # Annoation
                'ANNOTATION', 'ANNOTATION_LABEL', 'ANNOTATION_ORIGIN', 'ANNOTATION_TEXT',

                'ARRAY_SIZE',

                # Description of Axis Points
                'AXIS_DESCR', 'AXIS_PTS', 'AXIS_PTS_REF', 'AXIS_RESCALE_X',
                'AXIS_PTS_X', 'AXIS_PTS_Y', 'AXIS_PTS_Z', 'AXIS_PTS_Z4', 'AXIS_PTS_Z5',

                # Bit / Byte operations
                'BIT_MASK', 'BIT_OPERATION', 'BYTE_ORDER',

                # Calibrations
                'CALIBRATION_ACCESS', 'CALIBRATION_HANDLE', 'CALIBRATION_HANDLE_TEXT',
                'CALIBRATION_METHOD',

                'CHARACTERISTIC', 'COEFFS', 'COEFFS_LINEAR', 'COMPARISON_QUANTITY',

                'COMPU_METHOD', 'COMPU_TAB', 'COMPU_TAB_REF', 'COMPU_VTAB', 'COMPU_VTAB_RANGE',

                'CPU_TYPE',

                'CURVE_AXIS_REF', 'CUSTOMER', 'CUSTOMER_NO',

                'DATA_SIZE', 'DEF_CHARACTERISTIC', 'DEFAULT_VALUE',
                'DEFAULT_VALUE_NUMERIC',

                'DEPENDENT_CHARACTERISTIC', 'DEPOSIT', 'DISCRETE', 'DISPLAY_IDENTIFIER',
                'DIST_OP_X', 'DIST_OP_Y', 'DIST_OP_Z', 'DIST_OP_Z4', 'DIST_OP_Z5',

                # ECU keywords
                'ECU', 'ECU_ADDRESS', 'ECU_ADDRESS_EXTENSION', 'ECU_CALIBRATION_OFFSET',

                'EPK', 'ERROR_MASK', 'EXTENDED_LIMITS', 'FIX_AXIS_PAR', 'FIX_AXIS_PAR_DIST',
                'FIX_AXIS_PAR_LIST',

                'FIX_NO_AXIS_PTS_X', 'FIX_NO_AXIS_PTS_Y', 'FIX_NO_AXIS_PTS_Z', 'FIX_NO_AXIS_PTS_Z4', 'FIX_NO_AXIS_PTS_Z5',

                'FNC_VALUES', 'FORMAT', 'FORMULA', 'FORMULA_INV', 'FRAME', 'FRAME_MEASUREMENT',
                'FUNCTION', 'FUNCTION_LIST', 'FUNCTION_VERSION',

                'GROUP', 'GUARD_RAILS', 'HEADER', 'IDENTIFICATION', 'IF_DATA',
                'IN_MEASUREMENT', 'LAYOUT', 'LEFT_SHIFT', 'LOC_MEASUREMENT',

                'MAP_LIST', 'MATRIX_DIM', 'MAX_GRAD', 'MAX_REFRESH',

                'MEASUREMENT', 'MEMORY_LAYOUT', 'MEMORY_SEGMENT',

                'MOD_COMMON', 'MOD_PAR', 'MODULE', 'MONOTONY',

                'NO_AXIS_PTS_X', 'NO_AXIS_PTS_Y', 'NO_AXIS_PTS_Z', 'NO_AXIS_PTS_Z4', 'NO_AXIS_PTS_Z5',
                'NO_OF_INTERFACES',
                'NO_RESCALE_X',
                'NUMBER', 'OUT_MEASUREMENT', 'PHONE_NO', 'PHYS_UNIT',

                'OFFSET_X', 'OFFSET_Y', 'OFFSET_Z', 'OFFSET_Z4', 'OFFSET_Z5',

                'PROJECT', 'PROJECT_NO', 'READ_ONLY', 'READ_WRITE', 'RECORD_LAYOUT',

                'REF_CHARACTERISTIC', 'REF_GROUP', 'REF_MEASUREMENT',
                'REF_MEMORY_SEGMENT', 'REF_UNIT', 'RIGHT_SHIFT',

                'RIP_ADDR_X', 'RIP_ADDR_W', 'RIP_ADDR_Y', 'RIP_ADDR_Z', 'RIP_ADDR_Z4', 'RIP_ADDR_Z5',
                'ROOT',

                'SHIFT_OP_X', 'SHIFT_OP_Y', 'SHIFT_OP_Z', 'SHIFT_OP_Z4', 'SHIFT_OP_Z5',

                'SIGN_EXTEND', 'SI_EXPONENTS',
                'SRC_ADDR_X', 'SRC_ADDR_Y', 'SRC_ADDR_Z', 'SRC_ADDR_Z4', 'SRC_ADDR_Z5',

                'STATIC_RECORD_LAYOUT',

                'STATUS_STRING_REF', 'STEP_SIZE', 'SUB_FUNCTION', 'SUB_GROUP',
                'SUPPLIER', 'SYMBOL_LINK', 'SYSTEM_CONSTANT', 'UNIT',
                'UNIT_CONVERSION', 'USER',  'USER_RIGHTS',

                'VAR_ADDRESS',  'VAR_CHARACTERISTIC',  'VAR_CRITERION',
                'VAR_FORBIDDEN_COMB',  'VAR_MEASUREMENT',  'VAR_NAMING',
                'VAR_SELECTION_CHARACTERISTIC',  'VAR_SEPARATOR',

                'VARIANT_CODING',  'VERSION',  'VIRTUAL',
                'VIRTUAL_CHARACTERISTIC',


                # byte_order_enum
                'MSB_FIRST', 'MSB_LAST', 'LITTLE_ENDIAN', 'BIG_ENDIAN',

                # axis_descr_enum
                'CURVE_AXIS', 'COM_AXIS', 'FIX_AXIS', 'RES_AXIS', 'STD_AXIS',

                # calibration_access_enum
                'CALIBRATION', 'NO_CALIBRATION', 'NOT_IN_MCD_SYSTEM', 'OFFLINE_CALIBRATION',

                # conversion_type_enum
                'IDENTICAL', 'FORM', 'LINEAR', 'RAT_FUNC', 'TAB_INTP', 'TAB_NOINTP', 'TAB_VERB',

                # monotony_enum
                'MON_DECREASE', 'MON_INCREASE', 'STRICT_DECREASE', 'STRICT_INCREASE', 'MONOTONOUS', 'STRICT_MON', 'NOT_MON',

                # unit_type_enum
                'DERIVED', 'EXTENDED_SI',

                # tag_enum
                'NUMERIC', 'ALPHA',

                # enum_mode
                'ABSOLUTE', 'DIFFERENCE',

                # addrtype_enum
                'PBYTE', 'PWORD', 'PLONG', 'DIRECT',

                # characteristic_enum
                'ASCII', 'CURVE', 'MAP', 'CUBOID', 'CUBE_4', 'CUBE_5', 'VAL_BLK', 'VALUE',

                # prgtype_enum
                'PRG_CODE', 'PRG_DATA', 'PRG_RESERVED',
                'CALIBRATION_VARIABLES', 'CODE', 'DATA', 'EXCLUDE_FROM_FLASH', 'OFFLINE_DATA', 'RESERVED', 'SERAM', 'VARIABLES',

                # indexmode_enum
                'ALTERNATE_CURVES', 'ALTERNATE_WITH_X', 'ALTERNATE_WITH_Y', 'COLUMN_DIR', 'ROW_DIR',

                # memorytype_enum
                'EEPROM', 'EPROM', 'FLASH', 'RAM', 'ROM', 'REGISTER',

                # attribute_enum
                'INTERN', 'EXTERN',

                # indexorder_enum
                'INDEX_INCR', 'INDEX_DECR',

                'BYTE', 'WORD', 'LONG',

                'UBYTE',
                'SBYTE',

                'UWORD',
                'SWORD',

                'ULONG',
                'SLONG',

                'A_UINT64',
                'A_INT64',
                'FLOAT32_IEEE',
                'FLOAT64_IEEE',
                )

    map = {}
    for keyword in keywords:
        map[keyword.upper()] = keyword

    tokens = keywords + ('ID', 'STRING_LITERAL', 'INT_CONST_DEC', 'INT_CONST_HEX', 'FLOAT_CONST', 'HEX_FLOAT_CONST')

    # Identifier RegEx
    identifier = r'[a-zA-Z_][0-9a-zA-Z_\-.\[\]]*'

    # Constant Numbers RegEx
    hex_prefix = '[+-]?0[xX]'
    hex_digits = '[0-9a-fA-F]+'
    bin_prefix = '[+-]?0[bB]'
    # bin_digits = '[01]+'
    integer_suffix_opt = r'(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?'
    decimal_constant = '([+-]?0' + integer_suffix_opt + ')|([+-]?[1-9][0-9]*' + integer_suffix_opt + ')'
    hex_constant = hex_prefix + hex_digits + integer_suffix_opt

    exponent_part = r"""([eE][-+]?[0-9]+)"""
    fractional_constant = r"""([+-]?[0-9]+\.[0-9]+)|([+-]?\.[0-9]+)|([+-]?[0-9]+\.)"""
    floating_constant = (
        '( ( ((' + fractional_constant + ')' + exponent_part + '?)'
        ' | ([0-9]+' + exponent_part + ')'
        ' | ([+-]?[0-9]+' + exponent_part + ') )'
        '[FfLl]?)'
    )
    binary_exponent_part = r'''([pP][+-]?[0-9]+)'''
    hex_fractional_constant = '(((' + hex_digits + r""")?\.""" + hex_digits + ')|(' + hex_digits + r"""\.))"""
    hex_floating_constant = (
        '(' + hex_prefix + '('
        + hex_digits + '|' + hex_fractional_constant +
        ')' + binary_exponent_part + '[FfLl]?)'
    )

    # Constant String RegEx
    simple_escape = r"""([a-zA-Z._~!=&\^\-\\?'"])"""
    decimal_escape = r"""(\d+)"""
    hex_escape = r"""(x[0-9a-fA-F]+)"""
    escape_sequence = r"""(\\(""" + simple_escape + '|' + decimal_escape + '|' + hex_escape + '))'
    string_char = r"""([^"\\\n]|""" + escape_sequence + ')'
    # string_literal = '"'+string_char+'*"'

    string_literal = r'("(\\"|[^"])*")|(\'(\\\'|[^\'])*\')'

    # a2ml_regex = r'[a-zA-Z0-9\"\{\};\/\'\*\\\[\]_\s\:\(\)\.\=\,\-\&\>\%\']+'
    # a2ml_regex = r'/begin A2ML((.|\n)*)/end A2ML'

    newline = r'\n+'

#    comment_singleline = r'\/\/.*\n'
#    comment_multiline = r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'
    comment_singleline = r"\/\/.*"
    comment_multiline = r"\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/"

    t_STRING_LITERAL = string_literal
    t_ignore = ' \t\r'

    # Disable docstring and camel case
    # pylint: disable=C0103, C0116
    @TOKEN(newline)
    def t_NEWLINE(self, t):
        if self.lexer.lineno == self.start_of_a2ml:
            self.lexer.lineno = self.end_of_a2ml
        else:
            self.lexer.lineno += len(t.value)

    @TOKEN(identifier)
    def t_ID(self, t):
        t.type = self.map.get(t.value, "ID")
        return t

    @TOKEN(floating_constant)
    def t_FLOAT_CONST(self, t):
        return t

    @TOKEN(hex_floating_constant)
    def t_HEX_FLOAT_CONST(self, t):
        return t

    @TOKEN(hex_constant)
    def t_INT_CONST_HEX(self, t):
        return t

    @TOKEN(decimal_constant)
    def t_INT_CONST_DEC(self, t):
        return t

    @TOKEN(r'/begin')
    def t_BEGIN(self, t):
        return t

    @TOKEN(r'/end')
    def t_END(self, t):
        return t

    @TOKEN(comment_singleline)
    def t_COMMENT_SINGLELINE(self, t):
        # t.lexer.lineno += len([a for a in t.value if a == "\n"])
        pass

    @TOKEN(comment_multiline)
    def t_COMMENT_MULTILINE(self, t):
        # if t.value.startswith("/**") or t.value.startswith("/*!"):
        #     v = t.value.replace("\n\n", "\n")
        #
        #     v = re.sub(r"\n[\s]+\*", "\n*", v)
        # t.lexer.lineno += len([a for a in t.value if a == "\n"])
        pass

    def t_error(self, t):
        msg = f"Illegal character {repr(t.value[0])}"
        self._error_handling(msg, t)

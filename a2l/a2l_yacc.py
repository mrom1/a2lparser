import sys,re

from a2l.a2l_lex import A2lLex
from a2l.config.config import Config
from logger.logger import Logger
from libs.ply.yacc import yacc

try:
    from a2l.ast import a2l_ast as A2l_ast
except:
    pass


class A2lYacc(object):
    def __init__(self,
                 config
                 # lex_optimize = False,
                 # yacc_optimize = False,
                 #
                 # lextab = '_a2l_lextables',
                 # yacctab = '_a2l_yacctables',
                 # taboutputdir = '',
                 #
                 # yacc_debug = False,
                 # debug_output=0,
                 # gen_tables = 1,
                 #
                 # error_buffer = sys.stderr,
                 # error_resolve = False
                 ):

        self.logger_manager = Logger()
        self.logger = self.logger_manager.new_module("YACC")
        if not isinstance(config, Config):
            self.logger_manager.set_level("ERROR")
            self.logger.error("msg")
        else:
            self.config = config

        self.debug = config.debug_active
        self.error_resolve_active = config.error_resolve_active

        self.a2lLex = A2lLex()
        self.a2lLex.build_lexer(
            optimize=config.optimize,
            lextab=config.lex_tab,
            outputdir=config.gen_dir
            )

        self.tokens = self.a2lLex.tokens

        self.a2lYacc = yacc(
            module=self,
            start='abstract_syntax_tree_final',
            debug=config.debug_active,
            optimize=config.optimize,
            tabmodule=config.yacc_tab,
            outputdir=config.gen_dir,
            write_tables=config.write_tables
            )


        self.Ast_Scope_Stack = []
        self.file_len = 0


    def parse(self, input_string, filename, filelength, start_of_a2ml, end_of_a2ml):
        self.filename = filename
        self.a2lLex.reset_line_number()

        self.Ast_Scope_Stack = []

        self.file_len = filelength
        self.a2lLex.start_of_a2ml = start_of_a2ml
        self.a2lLex.end_of_a2ml = end_of_a2ml

        return self.a2lYacc.parse(input=input_string,
                                    lexer=self.a2lLex,
                                    debug=self.debug)

    ################################################################
    ## <Private Functions>                                        ##
    ################################################################
    def __update_progress(self, progress):
        if self.config.verbosity > 0:
            if progress > 100:
                progress = 100
            sys.stdout.write('\r[PARSER][INFO] Progress: [{0}] {1}%'.format('#'*(progress/5), progress))


    def __update_progress_finish(self):
        if self.config.verbosity > 0:
            progress = 100
            sys.stdout.write('\r[PARSER][INFO] Progress: [{0}] {1}%'.format('#'*(progress/5), progress))
            sys.stdout.write("\n")
            sys.stdout.flush()


    def __pretty_names(self, s):
        s = s.lower()
        s = s[0].upper() + s[1:]
        if '_' in s:
            index = [i for i, ltr in enumerate(s) if ltr == '_']
            indices = [i + 1 for i in index]
            s = "".join(c.upper() if i in indices else c for i, c in enumerate(s))
        return s


    def __create_AST_Node(self, Node):
        self.Ast_Scope_Stack.append(Node)
        return self.Ast_Scope_Stack[-1]


    def __get_AST_Node(self, Node, reverse=True):
        if reverse:
            for n in reversed(self.Ast_Scope_Stack):
                if isinstance(n, Node):
                    return n
        else:
            for n in self.Ast_Scope_Stack:
                if isinstance(n, Node):
                    return n


    def __get_or_create_AST_Node(self, Node, reverse=True):
        node = self.__get_AST_Node(Node=Node, reverse=reverse)
        if node is None:
            node = self.__create_AST_Node(Node=Node())

        return node


    def __remove_AST_Node(self, Node, reverse=True, single_remove=False):
        if reverse:
            for n in reversed(self.Ast_Scope_Stack):
                if isinstance(n, Node):
                    self.Ast_Scope_Stack.remove(n)
                    if single_remove:
                        break
        else:
            for n in self.Ast_Scope_Stack:
                if isinstance(n, Node):
                    self.Ast_Scope_Stack.remove(n)


    def __add_AST_Node_Object(self, NodeClass, AstNodeNames, Param):
        for n in AstNodeNames:
            if isinstance(Param, n):
                 setattr(NodeClass, Param.__class__.__name__, Param)


    def __add_AST_Node_Object_List(self, NodeClass, AstNodeNames, Param):
        for n in AstNodeNames:
            if isinstance(Param, n):
                if getattr(NodeClass, Param.__class__.__name__) is None:
                    setattr(NodeClass, Param.__class__.__name__, [Param])
                else:
                    getattr(NodeClass, Param.__class__.__name__).append(Param)


    def __add_AST_Node_Param(self, NodeClass, AstNodeNames, Param):
        for n in AstNodeNames:
            if isinstance(Param, n):
                setattr(NodeClass, Param.__class__.__name__, getattr(Param, Param.__slots__[0]))


    ################################################################
    # Parsing Rules                                               ##
    # translation unit section                                    ##
    ################################################################
    def p_empty(self, p):
        """
        empty :
        """
        p[0] = None


    def p_abstract_syntax_tree_final(self, p):
        """
        abstract_syntax_tree_final  : a2l_final
                                    | empty
        """
        if p[1] is None:
            p[0] = A2l_ast.Abstract_Syntax_Tree([])
        else:
            p[0] = A2l_ast.Abstract_Syntax_Tree(p[1])

        self.__update_progress_finish()


    def p_a2l_final(self, p):
        """
        a2l_final   : a2l_statement_ext
        """
        p[0] = p[1]


    def p_a2l_final_ext(self, p):
        """
        a2l_final   : a2l_final a2l_statement_ext
        """
        self.__update_progress(int(float(self.a2lLex.get_line_number()) / float(self.file_len)) * 100)
        if p[2] and p[1]:
            p[1].extend(p[2])
        p[0] = p[1]


    def p_a2l_statement_ext(self, p):
        """
        a2l_statement_ext   : a2l_statement
        """
        if p[1]:
            p[0] = [p[1]]


    # def p_a2l_statement_error(self, p):
    #     """
    #     a2l_statement    : meta_block_empty
    #                      | error_resolve
    #     """
    #     pass


    def p_a2l_statement(self, p):
        """
        a2l_statement    : meta_block
                         | meta_block_empty
        """
        p[0] = p[1]


    ################################################################
    # Meta tags section:                                          ##
    # token deduction (regex integer, string, float etc.)         ##
    # keywords, abstract error handling, abstract types           ##
    ################################################################
    def p_error(self, p):
        self.logger_manager.set_level("ERROR")
        if p:
            if p.value == '/end':
                self.a2lYacc.errok()
            else:
                return self.a2lLex.token()
            # if self.config.verbosity > 0:
            #     msg = "Parsing Error in File %s at line %s on symbol %s\n" % (self.filename, p.lineno, p.value)
            #     self.logger.error(msg)
            #self.error_buffer.write("\nERROR: Parsing Error in File %s at line %s on symbol %s\n" % (self.filename, p.lineno, p.value))

        else:
            self.logger.error("EOF reached without rule deduction")

    def p_META_string_literal(self, p):
        """
        string_literal    : STRING_LITERAL
        """
        p[0] = p[1]


    def p_META_string_literal_list(self, p):
        """
        string_literal_list     : string_literal
                                | string_literal_list string_literal
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]


    def p_META_ident(self, p):
        """
        ident    : ID
        """
        p[0] = p[1]


    def p_META_ident_list(self, p):
        """
        ident_list    : ident
                      | ident_list ident
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]


    def p_META_ident_ident(self, p):
        """
        ident_ident    : ident ident
        """
        p[0] = [p[1], p[2]]


    def p_META_ident_ident_list(self, p):
        """
        ident_ident_list    : ident_ident
                            | ident_ident_list ident_ident
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]


    def p_META_inVal_outVal(self, p):
        """
        inVal_outVal    : constant string_literal
        """
        p[0] = [p[1], p[2]]


    def p_META_inVal_outVal_list(self, p):
        """
        inVal_outVal_list    : inVal_outVal
                             | inVal_outVal_list inVal_outVal
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]


    def p_META_inVal_MinMax_outVal(self, p):
        """
        inVal_MinMax_outVal    : constant constant string_literal
        """
        p[0] = [p[1], p[2], p[3]]


    def p_META_inVal_MinMax_outVal_list(self, p):
        """
        inVal_MinMax_outVal_list    : inVal_MinMax_outVal
                                    | inVal_MinMax_outVal_list inVal_MinMax_outVal
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]


    def p_META_constant(self, p):
        """
        constant    : INT_CONST_DEC
                    | INT_CONST_HEX
                    | FLOAT_CONST
                    | HEX_FLOAT_CONST
        """
        p[0] = p[1]


    def p_META_constant_list(self, p):
        """
        constant_list    : constant
                         | constant_list constant
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]


    def p_META_axis_points(self, p):
        """
        axis_points    : constant constant
        """
        p[0] = [p[1], p[2]]


    def p_META_axis_points_list(self, p):
        """
        axis_points_list    : axis_points
                            | axis_points_list axis_points
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]


    def p_META_datatype(self, p):
        """
        datatype    : SBYTE
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


    def p_META_datasize(self, p):
        """
        datasize    : BYTE
                    | WORD
                    | LONG
        """
        p[0] = p[1]


    #def p_META_single_keywords(self, p):
    #    """
    #    meta_single_keyword     : A2ML_VERSION
    #                            | ADDR_EPK
    #                            | ASAP2_VERSION
    #                            | ALIGNMENT_BYTE
    #                            | ALIGNMENT_FLOAT32_IEEE
    #                            | ALIGNMENT_FLOAT64_IEEE
    #                            | ALIGNMENT_INT64
    #                            | ALIGNMENT_LONG
    #                            | ALIGNMENT_WORD
    #                            | ANNOTATION_LABEL
    #                            | ANNOTATION_ORIGIN
    #                            | ARRAY_SIZE
    #                            | AXIS_PTS_REF
    #                            | AXIS_PTS_X
    #                            | AXIS_RESCALE_X
    #                            | BIT_MASK
    #                            | BYTE_ORDER
    #                            | CALIBRATION_ACCESS
    #                            | CALIBRATION_HANDLE_TEXT
    #                            | COEFFS
    #                            | COEFFS_LINEAR
    #                            | COMPARISON_QUANTITY
    #                            | CPU_TYPE
    #                            | CURVE_AXIS_REF
    #                            | CUSTOMER
    #                            | CUSTOMER_NO
    #                            | DATA_SIZE
    #                            | DEFAULT_VALUE
    #                            | DEFAULT_VALUE_NUMERIC
    #                            | DEPOSIT
    #                            | DISCRETE
    #                            | DISPLAY_IDENTIFIER
    #                            | DIST_OP_X
    #                            | DIST_OP_Y
    #                            | DIST_OP_Z
    #                            | DIST_OP_Z4
    #                            | DIST_OP_Z5
    #                            | ECU
    #                            | ECU_ADDRESS
    #                            | ECU_ADDRESS_EXTENSION
    #                            | ECU_CALIBRATION_OFFSET
    #                            | EPK
    #                            | ERROR_MASK
    #                            | EXTENDED_LIMITS
    #                            | FIX_AXIS_PAR
    #                            | FIX_AXIS_PAR_DIST
    #                            | FIX_NO_AXIS_PTS_X
    #                            | FIX_NO_AXIS_PTS_Y
    #                            | FIX_NO_AXIS_PTS_Z
    #                            | FIX_NO_AXIS_PTS_Z4
    #                            | FIX_NO_AXIS_PTS_Z5
    #                            | FNC_VALUES
    #                            | FORMAT
    #                            | FORMULA_INV
    #                            | FRAME_MEASUREMENT
    #                            | GUARD_RAILS
    #                            | IDENTIFICATION
    #                            | LAYOUT
    #                            | LEFT_SHIFT
    #                            | MATRIX_DIM
    #                            | MAX_GRAD
    #                            | MAX_REFRESH
    #                            | MONOTONY
    #                            | NO_AXIS_PTS_X
    #                            | NO_AXIS_PTS_Y
    #                            | NO_AXIS_PTS_Z
    #                            | NO_AXIS_PTS_Z4
    #                            | NO_AXIS_PTS_Z5
    #                            | NO_OF_INTERFACES
    #                            | NO_RESCALE_X
    #                            | NUMBER
    #                            | OFFSET_X
    #                            | OFFSET_Y
    #                            | OFFSET_Z
    #                            | OFFSET_Z4
    #                            | OFFSET_Z5
    #                            | PHONE_NO
    #                            | PHYS_UNIT
    #                            | PROJECT_NO
    #                            | REF_MEMORY_SEGMENT
    #                            | REF_UNIT
    #                            | RIGHT_SHIFT
    #                            | RIP_ADDR_X
    #                            | ROOT
    #                            | SHIFT_OP_X
    #                            | SIGN_EXTEND
    #                            | SI_EXPONENTS
    #                            | SRC_ADDR_X
    #                            | STATIC_RECORD_LAYOUT
    #                            | STATUS_STRING_REF
    #                            | STEP_SIZE
    #                            | SUPPLIER
    #                            | SYMBOL_LINK
    #                            | SYSTEM_CONSTANT
    #                            | VAR_MEASUREMENT
    #                            | VAR_NAMING
    #                            | VAR_SELECTION_CHARACTERISTIC
    #                            | VAR_SEPARATOR
    #                            | VERSION
    #    """
    #    p[0] = p[1]


    def p_META_block_keywords(self, p):
        """
        meta_block_keyword  : ANNOTATION
                            | ANNOTATION_TEXT
                            | AXIS_DESCR
                            | AXIS_PTS
                            | BIT_OPERATION
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
                            | LOC_MEASUREMENT
                            | MAP_LIST
                            | MEASUREMENT
                            | MEMORY_LAYOUT
                            | MEMORY_SEGMENT
                            | MOD_COMMON
                            | MOD_PAR
                            | MODULE
                            | OUT_MEASUREMENT
                            | PROJECT
                            | RECORD_LAYOUT
                            | REF_CHARACTERISTIC
                            | REF_GROUP
                            | REF_MEASUREMENT
                            | SUB_FUNCTION
                            | SUB_GROUP
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


    # def p_META_ident_keywords(self, p):
    #     """
    #     ident   : addrtype_enum
    #             | attribute_enum
    #             | axis_descr_enum
    #             | byte_order_enum
    #             | calibration_access_enum
    #             | characteristic_enum
    #             | conversion_type_enum
    #             | datasize
    #             | datatype
    #             | mode_enum
		# 		| indexorder_enum
		# 		| indexmode_enum
		# 		| memorytype_enum
		# 		| monotony_enum
		# 		| meta_block_keyword
		# 		| meta_single_keyword
		# 		| prgtype_enum
		# 		| tag_enum
		# 		| unit_type_enum
    #     """
    #     p[0] = p[1]


    def p_META_block_empty(self, p):
        """
        meta_block_empty    : BEGIN meta_block_keyword END meta_block_keyword
                            | BEGIN meta_block_keyword END
        """
        pass


    # def p_META_error_resolve(self, p):
    #     """
    #     error_resolve    : meta_single_tag_error
    #                      | meta_block_error
    #     """
    #     p[0] = p[1]
    #
    #
    # def p_META_error_resolve_empty(self, p):
    #     """
    #     error_resolve    : meta_block_empty
    #     """
    #     pass
    #
    #
    # def p_META_single_tag_error(self, p):
    #     """
    #     meta_single_tag_error   : meta_single_keyword error
    #     """
    #     if hasattr(p[2], "value") and len(self.Ast_Scope_Stack) > 0:
    #         ast_err_class_name = self.__pretty_names(str(p[1]))
    #
    #         if len(self.Ast_Scope_Stack) > 0:
    #             ast_last_node = self.Ast_Scope_Stack[-1]
    #
    #             if hasattr(ast_last_node, ast_err_class_name):
    #                 setattr(ast_last_node, ast_err_class_name, p[2].value)
    #                 msg = "ERROR_RESOLVE: %s has been set to %s in %s at line %s\n" % (p[1],
    #                                                                                                      p[2].value,
    #                                                                                                      ast_last_node.__class__.__name__.replace("_Opt_List", "").replace("_Opt",  "").upper(),
    #                                                                                                      p[2].lineno
    #                                                                                                      )
    #                 self.logger_manager.set_level("WARNING")
    #                 self.logger.warning(msg)
    #                 #self.error_buffer.write()
    #
    #         # elif hasattr(A2l_ast, ast_err_class_name):
    #         #     node = getattr(A2l_ast, ast_err_class_name)
    #         #     n = node(p[2].value)
    #         #     self.error_buffer.write("ERROR_RESOLVE: %s has been set to %s in %s at line %s\n" % (p[1],
    #         #                                                                                          p[2].value,
    #         #                                                                                          n.__class__.__name__.replace(
    #         #                                                                                              "_Opt_List",
    #         #                                                                                              "").replace(
    #         #                                                                                              "_Opt",
    #         #                                                                                              "").upper(),
    #         #                                                                                          p[2].lineno
    #         #                                                                                          ))
    #         #     return n
    #
    #
    # def p_META_block_tag_error(self, p):
    #     """
    #     meta_block_error    : BEGIN meta_block_keyword error END
    #                         | BEGIN meta_block_keyword error END meta_block_keyword
    #     """
    #     if self.config.verbosity > 0:
    #         msg = "ERROR_THROW_AWAY: unable to parse %s in %s object at line %s. %s object will be thrown away!\n" % (p[3].value,
    #                                                                                                                                 p[2],
    #                                                                                                                                 p[3].lineno,
    #                                                                                                                                 p[2]
    #                                                                                                                                 )
    #         self.logger_manager.set_level("ERROR")
    #         self.logger.error(msg)
    #     #self.error_buffer.write()


    def p_META_block(self, p):
        """
        meta_block       : project
                         | a2ml_version
                         | asap2_version
                         | annotation
                         | axis_descr
                         | axis_pts
                         | bit_operation
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
                         | loc_measurement
                         | map_list
                         | measurement
                         | memory_layout
                         | memory_segment
                         | mod_common
                         | mod_par
                         | module
                         | out_measurement
                         | record_layout
                         | ref_characteristic
                         | ref_group
                         | ref_measurement
                         | sub_function
                         | sub_group
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
        self.__update_progress(int((float(self.a2lLex.get_line_number()) / float(self.file_len)) * 100))
        p[0] = p[1]



    ################################################################
    # A2l enum section:                                           ##
    # definition of specific a2l enum types                       ##
    ################################################################
    def p_addrtype_enum(self, p):
        """
        addrtype_enum    : PBYTE
                         | PWORD
                         | PLONG
                         | DIRECT
        """
        p[0] = p[1]


    def p_attribute_enum(self, p):
        """
        attribute_enum    : INTERN
                          | EXTERN
        """
        p[0] = p[1]


    def p_axis_descr_enum(self, p):
        """
        axis_descr_enum    : CURVE_AXIS
                           | COM_AXIS
                           | FIX_AXIS
                           | RES_AXIS
                           | STD_AXIS
        """
        p[0] = p[1]


    def p_byte_order_enum(self, p):
        """
        byte_order_enum    : MSB_FIRST
                           | MSB_LAST
                           | LITTLE_ENDIAN
                           | BIG_ENDIAN
        """
        p[0] = p[1]


    def p_calibration_access_enum(self, p):
        """
        calibration_access_enum     : CALIBRATION
                                    | NO_CALIBRATION
                                    | NOT_IN_MCD_SYSTEM
                                    | OFFLINE_CALIBRATION
        """
        p[0] = p[1]


    def p_characteristic_enum(self, p):
        """
        characteristic_enum    : ASCII
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
        conversion_type_enum             : IDENTICAL
                                         | FORM
                                         | LINEAR
                                         | RAT_FUNC
                                         | TAB_INTP
                                         | TAB_NOINTP
                                         | TAB_VERB
        """
        p[0] = p[1]


    def p_mode_enum(self, p):
        """
        mode_enum    : ABSOLUTE
                     | DIFFERENCE
        """
        p[0] = p[1]


    def p_indexorder_enum(self, p):
        """
        indexorder_enum     : INDEX_INCR
                            | INDEX_DECR
        """
        p[0] = p[1]


    def p_indexmode_enum(self, p):
        """
        indexmode_enum    : ALTERNATE_CURVES
                          | ALTERNATE_WITH_X
                          | ALTERNATE_WITH_Y
                          | COLUMN_DIR
                          | ROW_DIR
        """
        p[0] = p[1]


    def p_memorytype_enum(self, p):
        """
        memorytype_enum    : EEPROM
                           | EPROM
                           | FLASH
                           | RAM
                           | ROM
                           | REGISTER
        """
        p[0] = p[1]


    def p_monotony_enum(self, p ):
        """
        monotony_enum    : MON_DECREASE
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
        prgtype_enum    : PRG_CODE
                        | PRG_DATA
                        | PRG_RESERVED
        """
        p[0] = p[1]


    def p_prgtype_enum_2(self, p):
        """
        prgtype_enum    : CALIBRATION_VARIABLES
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
        unit_type_enum    : DERIVED
                          | EXTENDED_SI
        """
        p[0] = p[1]


    def p_tag_enum(self, p):
        """
        tag_enum    : NUMERIC
                    | ALPHA
        """
        p[0] = p[1]



    ################################################################
    # A2l main rules section                                      ##
    ################################################################
    def p_A2ML_VERSION(self, p):
        """
        a2ml_version     : A2ML_VERSION constant constant
        """
        p[0] = A2l_ast.A2ml_Version(VersionNo=p[2], UpgradeNo=p[3])


    def p_ADDR_EPK(self, p):
        """
        addr_epk     : ADDR_EPK constant
        """
        p[0] = A2l_ast.Addr_Epk(Address=p[2])


    def p_ASAP2_VERSION(self, p):
        """
        asap2_version     : ASAP2_VERSION constant constant
        """
        p[0] = A2l_ast.Asap2_Version(VersionNo=p[2], UpgradeNo=p[3])


    def p_ALIGNMENT_BYTE(self, p):
        """
        alignment_byte     : ALIGNMENT_BYTE constant
        """
        p[0] = A2l_ast.Alignment_Byte(AlignmentBorder=p[2])


    def p_ALIGNMENT_FLOAT32_IEEE(self, p):
        """
        alignment_float32_ieee     : ALIGNMENT_FLOAT32_IEEE constant
        """
        p[0] = A2l_ast.Alignment_Float32_Ieee(AlignmentBorder=p[2])


    def p_ALIGNMENT_FLOAT64_IEEE(self, p):
        """
        alignment_float64_ieee     : ALIGNMENT_FLOAT64_IEEE constant
        """
        p[0] = A2l_ast.Alignment_Float64_Ieee(AlignmentBorder=p[2])


    def p_ALIGNMENT_INT64(self, p):
        """
        alignment_int64     : ALIGNMENT_INT64 constant
        """
        p[0] = A2l_ast.Alignment_Int64(AlignmentBorder=p[2])


    def p_ALIGNMENT_LONG(self, p):
        """
        alignment_long     : ALIGNMENT_LONG constant
        """
        p[0] = A2l_ast.Alignment_Long(AlignmentBorder=p[2])


    def p_ALIGNMENT_WORD(self, p):
        """
        alignment_word     : ALIGNMENT_WORD constant
        """
        p[0] = A2l_ast.Alignment_Word(AlignmentBorder=p[2])


    def p_ANNOTATION(self, p):
        """
        annotation     : BEGIN ANNOTATION annotation_opt_list END ANNOTATION
                       
        """
        if len(p) > 2 and p[3]:
            p[0] = A2l_ast.Annotation(OptionalParams=p[3])
        self.__remove_AST_Node(A2l_ast.Annotation_Opt)


    def p_ANNOTATION_opt(self, p):
        """
        annotation_opt    : annotation_label
                          | annotation_origin
                          | annotation_text
                          
        """
        if p[1]:
            node = self.__get_or_create_AST_Node(A2l_ast.Annotation_Opt)
            self.__add_AST_Node_Param(node,
                                     [A2l_ast.Annotation_Label,
                                      A2l_ast.Annotation_Origin,
                                      A2l_ast.Annotation_Text],
                                     p[1])
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
        p[0] = A2l_ast.Annotation_Label(label=p[2])


    def p_ANNOTATION_ORIGIN(self, p):
        """
        annotation_origin     : ANNOTATION_ORIGIN string_literal
        """
        p[0] = A2l_ast.Annotation_Origin(origin=p[2])


    def p_ANNOTATION_TEXT(self, p):
        """
        annotation_text     : BEGIN ANNOTATION_TEXT string_literal_list END ANNOTATION_TEXT
        """
        if len(p) > 2:
            p[0] = A2l_ast.Annotation_Text(annotation_text=p[3])


    def p_ARRAY_SIZE(self, p):
        """
        array_size     : ARRAY_SIZE constant
        """
        p[0] = A2l_ast.Array_Size(p[2])


    def p_AXIS_DESCR(self, p):
        """
        axis_descr     : BEGIN AXIS_DESCR axis_descr_enum ident ident constant constant constant END AXIS_DESCR
                       | BEGIN AXIS_DESCR axis_descr_enum ident ident constant constant constant axis_descr_opt_list END AXIS_DESCR
        """
        if len(p) > 2:
            p[0] = A2l_ast.Axis_Descr(Attribute = p[3],
                                      InputQuantity = p[4],
                                      Conversion = p[5],
                                      MaxAxisPoints = p[6],
                                      LowerLimit = p[7],
                                      UpperLimit = p[8])

            if len (p) == 12:
                p[0].OptionalParams = p[9]

            self.__remove_AST_Node(A2l_ast.Axis_Descr_Opt)


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
        node = self.__get_or_create_AST_Node(A2l_ast.Axis_Descr_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                  AstNodeNames = [A2l_ast.Axis_Pts_Ref,
                                                  A2l_ast.Byte_Order,
                                                  A2l_ast.Curve_Axis_Ref,
                                                  A2l_ast.Deposit,
                                                  A2l_ast.Format,
                                                  A2l_ast.Max_Grad,
                                                  A2l_ast.Monotony,
                                                  A2l_ast.Phys_Unit,
                                                  A2l_ast.Read_Only,
                                                  A2l_ast.Step_Size
                                                  ],
                                  Param = p[1])

        p[0] = node


    def p_AXIS_DESCR_opt_objects(self, p):
        """
        axis_descr_opt    : extended_limits
                          | fix_axis_par
                          | fix_axis_par_dist
                          | fix_axis_par_list
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Axis_Descr_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                  AstNodeNames= [A2l_ast.Extended_Limits,
                                                 A2l_ast.Fix_Axis_Par,
                                                 A2l_ast.Fix_Axis_Par_Dist,
                                                 A2l_ast.Fix_Axis_Par_List
                                                 ],
                                  Param = p[1])
        p[0] = node


    def p_AXIS_DESCR_opt_objects_list(self, p):
        """
        axis_descr_opt    : annotation
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Axis_Descr_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Annotation],
                                       Param = p[1])
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
            p[0] = self.__create_AST_Node(A2l_ast.Axis_Pts(Name=p[3],
                                                   LongIdentifier=p[4],
                                                   Address=p[5],
                                                   InputQuantity=p[6],
                                                   Deposit_Ref=p[7],
                                                   MaxDiff=p[8],
                                                   Conversion=p[9],
                                                   MaxAxisPoints=p[10],
                                                   LowerLimit=p[11],
                                                   UpperLimit=p[12]))

            if len (p) == 16:
                p[0].OptionalParams = p[13]

            self.__remove_AST_Node(A2l_ast.Axis_Pts_Opt)


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
        node = self.__get_or_create_AST_Node(A2l_ast.Axis_Pts_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Byte_Order,
                                                 A2l_ast.Calibration_Access,
                                                 A2l_ast.Deposit,
                                                 A2l_ast.Display_Identifier,
                                                 A2l_ast.Ecu_Address_Extension,
                                                 A2l_ast.Format,
                                                 A2l_ast.Guard_Rails,
                                                 A2l_ast.Monotony,
                                                 A2l_ast.Phys_Unit,
                                                 A2l_ast.Read_Only,
                                                 A2l_ast.Ref_Memory_Segment,
                                                 A2l_ast.Step_Size
                                                 ],
                                 Param = p[1])

        p[0] = node


    def p_AXIS_PTS_opt_objects(self, p):
        """
        axis_pts_opt    : extended_limits
                        | symbol_link
                        | function_list
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Axis_Pts_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                  AstNodeNames= [A2l_ast.Extended_Limits,
                                                 A2l_ast.Symbol_Link,
                                                 A2l_ast.Function_List
                                                 ],
                                  Param = p[1])
        p[0] = node


    def p_AXIS_PTS_opt_objects_list(self, p):
        """
        axis_pts_opt    : annotation
                        | if_data
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Axis_Pts_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Annotation,
                                                      A2l_ast.If_Data],
                                       Param = p[1])
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
        p[0] = A2l_ast.Axis_Pts_Ref(p[2])


    def p_AXIS_PTS_X(self, p):
        """
        axis_pts_x     : AXIS_PTS_X constant datatype indexorder_enum addrtype_enum
        """
        p[0] = A2l_ast.Axis_Pts_X(Position=p[2],
                                  Datatype=p[3],
                                  IndexIncr=p[4],
                                  Addressing=p[5])


    def p_AXIS_PTS_Y(self, p):
        """
        axis_pts_y     : AXIS_PTS_Y constant datatype indexorder_enum addrtype_enum
        """
        p[0] = A2l_ast.Axis_Pts_Y(Position=p[2],
                                  Datatype=p[3],
                                  IndexIncr=p[4],
                                  Addressing=p[5])


    def p_AXIS_PTS_Z(self, p):
        """
        axis_pts_z     : AXIS_PTS_Z constant datatype indexorder_enum addrtype_enum
        """
        p[0] = A2l_ast.Axis_Pts_Z(Position=p[2],
                                  Datatype=p[3],
                                  IndexIncr=p[4],
                                  Addressing=p[5])


    def p_AXIS_PTS_Z4(self, p):
        """
        axis_pts_z4     : AXIS_PTS_Z4 constant datatype indexorder_enum addrtype_enum
        """
        p[0] = A2l_ast.Axis_Pts_Z4(Position=p[2],
                                  Datatype=p[3],
                                  IndexIncr=p[4],
                                  Addressing=p[5])


    def p_AXIS_PTS_Z5(self, p):
        """
        axis_pts_z5     : AXIS_PTS_Z5 constant datatype indexorder_enum addrtype_enum
        """
        p[0] = A2l_ast.Axis_Pts_Z5(Position=p[2],
                                  Datatype=p[3],
                                  IndexIncr=p[4],
                                  Addressing=p[5])

    def p_AXIS_RESCALE_X(self, p):
        """
        axis_rescale_x     : AXIS_RESCALE_X constant datatype constant indexorder_enum addrtype_enum
        """
        p[0] = A2l_ast.Axis_Rescale_X(Position=p[2],
                                      Datatype=p[3],
                                      MaxNumberOfRescalePairs=p[4],
                                      IndexIncr=p[5],
                                      Addressing=p[6])


    def p_BIT_MASK(self, p):
        """
        bit_mask     : BIT_MASK constant
        """
        p[0] = A2l_ast.Bit_Mask(p[2])


    def p_BIT_OPERATION(self, p):
        """
        bit_operation     : BEGIN BIT_OPERATION bit_operation_opt_list END BIT_OPERATION
        """
        if len(p) > 2:
            p[0] = A2l_ast.Bit_Operation(OptionalParams=p[3])
            self.__remove_AST_Node(A2l_ast.Bit_Operation_Opt)


    def p_BIT_OPERATION_opt(self, p):
        """
        bit_operation_opt   : left_shift
                            | right_shift
                            | sign_extend

        """
        node = self.__get_or_create_AST_Node(A2l_ast.Bit_Operation_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                  AstNodeNames= [A2l_ast.Left_Shift,
                                                 A2l_ast.Right_Shift,
                                                 A2l_ast.Sign_Extend,
                                                 ],
                                  Param = p[1])
        p[0] = node


    def p_BIT_OPERATION_opt_list (self, p):
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
        p[0] = A2l_ast.Byte_Order(p[2])


    def p_CALIBRATION_ACCESS(self, p):
        """
        calibration_access     : CALIBRATION_ACCESS calibration_access_enum
        """
        p[0] = A2l_ast.Calibration_Access(p[2])


    def p_CALIBRATION_HANDLE(self, p):
        """
        calibration_handle     : BEGIN CALIBRATION_HANDLE constant_list END CALIBRATION_HANDLE
                               | BEGIN CALIBRATION_HANDLE constant_list calibration_handle_opt_list END CALIBRATION_HANDLE
        """
        if len(p) > 2:
            p[0] = A2l_ast.Calibration_Handle(Handle=p[3])
            if len(p) == 7:
                p[0].Calibration_Handle_Text=(p[4])

            self.__remove_AST_Node(A2l_ast.Calibration_Handle_Opt)


    def p_CALIBRATION_HANDLE_opt(self, p):
        """
        calibration_handle_opt  : calibration_handle_text

        """
        node = self.__get_or_create_AST_Node(A2l_ast.Calibration_Handle_Opt)
        self.__add_AST_Node_Param(NodeClass=node,
                                   AstNodeNames=[A2l_ast.Calibration_Handle_Text],
                                   Param=p[1])
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
        p[0] = A2l_ast.Calibration_Handle_Text(p[2])


    def p_CALIBRATION_METHOD(self, p):
        """
        calibration_method     : BEGIN CALIBRATION_METHOD string_literal constant END CALIBRATION_METHOD
                               | BEGIN CALIBRATION_METHOD string_literal constant calibration_method_opt_list END CALIBRATION_METHOD
        """
        if len(p) > 2:
            if len(p) == 7:
                p[0] = A2l_ast.Calibration_Method(Method=p[3],
                                                  Version=p[4])
            else:
                p[0] = A2l_ast.Calibration_Method(Method=p[3],
                                                  Version=p[4],
                                                  Calibration_Handle=p[5])

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
            p[0]= A2l_ast.Characteristic(Name=p[3],
                                                         LongIdentifier=p[4],
                                                         Type=p[5],
                                                         Address=p[6],
                                                         Deposit_Ref=p[7],
                                                         MaxDiff=p[8],
                                                         Conversion=p[9],
                                                         LowerLimit=p[10],
                                                         UpperLimit=p[11])

            if len (p) == 15:
                p[0].OptionalParams = p[12]

        self.__remove_AST_Node(A2l_ast.Characteristic_Opt)


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
        node = self.__get_or_create_AST_Node(A2l_ast.Characteristic_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Bit_Mask,
                                                 A2l_ast.Byte_Order,
                                                 A2l_ast.Calibration_Access,
                                                 A2l_ast.Comparison_Quantity,
                                                 A2l_ast.Discrete,
                                                 A2l_ast.Display_Identifier,
                                                 A2l_ast.Ecu_Address_Extension,
                                                 A2l_ast.Format,
                                                 A2l_ast.Guard_Rails,
                                                 A2l_ast.Number,
                                                 A2l_ast.Phys_Unit,
                                                 A2l_ast.Read_Only,
                                                 A2l_ast.Ref_Memory_Segment,
                                                 A2l_ast.Step_Size
                                                 ],
                                 Param = p[1])
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
        node = self.__get_or_create_AST_Node(A2l_ast.Characteristic_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                  AstNodeNames= [A2l_ast.Dependent_Characteristic,
                                                 A2l_ast.Extended_Limits,
                                                 A2l_ast.Function_List,
                                                 A2l_ast.Map_List,
                                                 A2l_ast.Matrix_Dim,
                                                 A2l_ast.Max_Refresh,
                                                 A2l_ast.Symbol_Link,
                                                 A2l_ast.Virtual_Characteristic
                                                 ],
                                  Param = p[1])
        p[0] = node


    def p_CHARACTERISTIC_opt_objects_list(self, p):
        """
        characteristic_opt    :  annotation
                              |  axis_descr
                              |  if_data
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Characteristic_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Annotation,
                                                      A2l_ast.Axis_Descr,
                                                      A2l_ast.If_Data
                                                      ],
                                       Param = p[1])
        p[0] = node


    def p_CHARACTERISTIC_opt_list (self, p):
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
        p[0] = A2l_ast.Coeffs(a = p[2],
                              b = p[3],
                              c = p[4],
                              d = p[5],
                              e = p[6],
                              f = p[7])


    def p_COEFFS_LINEAR(self, p):
        """
        coeffs_linear     : COEFFS_LINEAR constant constant
        """
        # float a b
        # f(x) = ax + b
        # PHYS = f(INT)
        p[0] = A2l_ast.Coeffs_Linear(a=p[2],
                                     b=p[3])


    def p_COMPARISON_QUANTITY(self, p):
        """
        comparison_quantity     : COMPARISON_QUANTITY ident
        """
        p[0] = A2l_ast.Comparison_Quantity(p[2])


    def p_COMPU_METHOD(self, p):
        """
        compu_method     : BEGIN COMPU_METHOD ident string_literal conversion_type_enum string_literal string_literal END COMPU_METHOD
                         | BEGIN COMPU_METHOD ident string_literal conversion_type_enum string_literal string_literal compu_method_opt_list END COMPU_METHOD
        """
        node = self.__create_AST_Node(A2l_ast.Compu_Method(Name = p[3],
                                                           LongIdentifier = p[4],
                                                           ConversionType = p[5],
                                                           Format = p[6],
                                                           Unit = p[7]))

        if len (p) == 11:
            node.OptionalParams = p[8]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Compu_Method)
        self.__remove_AST_Node(A2l_ast.Compu_Method_Opt)


    def p_COMPU_METHOD_opt_params(self, p):
        """
        compu_method_opt    : compu_tab_ref
                            | ref_unit
                            | status_string_ref


        """
        node = self.__get_or_create_AST_Node(A2l_ast.Compu_Method_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Compu_Tab_Ref,
                                                 A2l_ast.Ref_Unit,
                                                 A2l_ast.Status_String_Ref
                                                 ],
                                 Param = p[1])

        p[0] = node


    def p_COMPU_METHOD_opt_objects(self, p):
        """
        compu_method_opt    : coeffs
                            | coeffs_linear
                            | formula

        """
        node = self.__get_or_create_AST_Node(A2l_ast.Compu_Method_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                  AstNodeNames= [A2l_ast.Coeffs,
                                                 A2l_ast.Coeffs_Linear,
                                                 A2l_ast.Formula,
                                                 ],
                                  Param = p[1])
        p[0] = node



    def p_COMPU_METHOD_opt_list (self, p):
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
        node = self.__create_AST_Node(A2l_ast.Compu_Tab(Name = p[3],
                                                          LongIdentifier = p[4],
                                                          ConversionType = p[5],
                                                          NumberValuePairs= p[6],
                                                          Axis_Points=p[7]))

        if len (p) == 11:
            node.OptionalParams = p[8]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Compu_Tab)
        self.__remove_AST_Node(A2l_ast.Compu_Tab_Opt)


    def p_COMPU_TAB_opt_params(self, p):
        """
        compu_tab_opt    : default_value
                         | default_value_numeric

        """
        node = self.__get_or_create_AST_Node(A2l_ast.Compu_Tab_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Default_Value,
                                                 A2l_ast.Default_Value_Numeric,
                                                 ],
                                 Param = p[1])

        p[0] = node


    def p_COMPU_TAB_opt_list (self, p):
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
        p[0] = A2l_ast.Compu_Tab_Ref(p[2])


    def p_COMPU_VTAB(self, p):
        """
        compu_vtab     : BEGIN COMPU_VTAB ident string_literal conversion_type_enum constant inVal_outVal_list END COMPU_VTAB
                       | BEGIN COMPU_VTAB ident string_literal conversion_type_enum constant inVal_outVal_list default_value END COMPU_VTAB
        """
        p[0] = A2l_ast.Compu_Vtab(Name=p[3],
                                  LongIdentifier=p[4],
                                  ConversionType=p[5],
                                  NumberValuePairs=p[6],
                                  InVal_OutVal=p[7])
        if len(p) == 11:
            p[0].Default_Value=getattr(p[8], p[8].__slots__[0])


    def p_COMPU_VTAB_RANGE(self, p):
        """
        compu_vtab_range     : BEGIN COMPU_VTAB_RANGE ident string_literal constant inVal_MinMax_outVal_list END COMPU_VTAB_RANGE
                             | BEGIN COMPU_VTAB_RANGE ident string_literal constant inVal_MinMax_outVal_list default_value END COMPU_VTAB_RANGE
        """
        p[0] = A2l_ast.Compu_Vtab_Range(Name=p[3],
                                        LongIdentifier=p[4],
                                        NumberValueTriples=p[5],
                                        InVal_MinMax_OutVal=p[6])
        if len(p) == 10:
            p[0].Default_Value = getattr(p[7], p[7].__slots__[0])


    def p_CPU_TYPE(self, p):
        """
        cpu_type     : CPU_TYPE string_literal
        """
        p[0] = A2l_ast.Cpu_Type(p[2])


    def p_CURVE_AXIS_REF(self, p):
        """
        curve_axis_ref     : CURVE_AXIS_REF ident
        """
        p[0] = A2l_ast.Curve_Axis_Ref(p[2])


    def p_CUSTOMER(self, p):
        """
        customer     : CUSTOMER string_literal
        """
        p[0] = A2l_ast.Customer(p[2])


    def p_CUSTOMER_NO(self, p):
        """
        customer_no     : CUSTOMER_NO string_literal
        """
        p[0] = A2l_ast.Customer_No(p[2])


    def p_DATA_SIZE(self, p):
        """
        data_size     : DATA_SIZE constant
        """
        p[0] = A2l_ast.Data_Size(p[2])


    def p_DEF_CHARACTERISTIC(self, p):
        """
        def_characteristic     : BEGIN DEF_CHARACTERISTIC ident_list END DEF_CHARACTERISTIC
        """
        p[0] = A2l_ast.Def_Characteristic(p[3])


    def p_DEFAULT_VALUE(self, p):
        """
        default_value     : DEFAULT_VALUE string_literal
        """
        p[0] = A2l_ast.Default_Value(p[2])


    def p_DEFAULT_VALUE_NUMERIC(self, p):
        """
        default_value_numeric     : DEFAULT_VALUE_NUMERIC constant
        """
        p[0] = A2l_ast.Default_Value_Numeric(p[2])


    def p_DEPENDENT_CHARACTERISTIC(self, p):
        """
        dependent_characteristic     : BEGIN DEPENDENT_CHARACTERISTIC string_literal ident_list END DEPENDENT_CHARACTERISTIC
        """
        p[0] = A2l_ast.Dependent_Characteristic(Formula=p[3],
                                                Characteristic=p[4])

    def p_DEPOSIT(self, p):
        """
        deposit     : DEPOSIT mode_enum
        """
        p[0] = A2l_ast.Deposit(p[2])


    def p_DISCRETE(self, p):
        """
        discrete     : DISCRETE
        """
        p[0] = A2l_ast.Discrete(Boolean=True)


    def p_DISPLAY_IDENTIFIER(self, p):
        """
        display_identifier     : DISPLAY_IDENTIFIER ident
        """
        p[0] = A2l_ast.Display_Identifier(p[2])


    def p_DIST_OP_X(self, p):
        """
        dist_op_x    : DIST_OP_X constant datatype
        """
        p[0] = A2l_ast.Dist_Op_X(Position=p[2],
                                 Datatype=p[3])


    def p_DIST_OP_Y(self, p):
        """
        dist_op_y    : DIST_OP_Y constant datatype
        """
        p[0] = A2l_ast.Dist_Op_Y(Position=p[2],
                                 Datatype=p[3])


    def p_DIST_OP_Z(self, p):
        """
        dist_op_z    : DIST_OP_Z constant datatype
        """
        p[0] = A2l_ast.Dist_Op_Z(Position=p[2],
                                 Datatype=p[3])


    def p_DIST_OP_Z4(self, p):
        """
        dist_op_z4    : DIST_OP_Z4 constant datatype
        """
        p[0] = A2l_ast.Dist_Op_Z4(Position=p[2],
                                  Datatype=p[3])


    def p_DIST_OP_Z5(self, p):
        """
        dist_op_z5    : DIST_OP_Z5 constant datatype
        """
        p[0] = A2l_ast.Dist_Op_Z5(Position=p[2],
                                  Datatype=p[3])

    def p_ECU(self, p):
        """
        ecu     : ECU string_literal
        """
        p[0] = A2l_ast.Ecu(p[2])


    def p_ECU_ADDRESS(self, p):
        """
        ecu_address     : ECU_ADDRESS constant
        """
        p[0]  = A2l_ast.Ecu_Address(p[2])


    def p_ECU_ADDRESS_EXTENSION(self, p):
        """
        ecu_address_extension     : ECU_ADDRESS_EXTENSION constant
        """
        p[0] = A2l_ast.Ecu_Address_Extension(p[2])


    def p_ECU_CALIBRATION_OFFSET(self, p):
        """
        ecu_calibration_offset     : ECU_CALIBRATION_OFFSET constant
        """
        p[0] = A2l_ast.Ecu_Calibration_Offset(p[2])


    def p_EPK(self, p):
        """
        epk     : EPK string_literal
        """
        p[0] = A2l_ast.Epk(p[2])


    def p_ERROR_MASK(self, p):
        """
        error_mask     : ERROR_MASK constant
        """
        p[0] = A2l_ast.Error_Mask(p[2])


    def p_EXTENDED_LIMITS(self, p):
        """
        extended_limits     : EXTENDED_LIMITS constant constant
        """
        p[0] = A2l_ast.Extended_Limits(LowerLimit=p[2],
                                       UpperLimit=p[3])

    def p_FIX_AXIS_PAR(self, p):
        """
        fix_axis_par     : FIX_AXIS_PAR constant constant constant
        """
        p[0] = A2l_ast.Fix_Axis_Par(Offset=p[2],
                                    Shift=p[3],
                                    Numberapo=p[4])


    def p_FIX_AXIS_PAR_DIST(self, p):
        """
        fix_axis_par_dist     : FIX_AXIS_PAR_DIST constant constant constant
        """
        p[0] = A2l_ast.Fix_Axis_Par_Dist(Offset=p[2],
                                         Distance=p[3],
                                         Numberapo=p[4])


    def p_FIX_AXIS_PAR_LIST(self, p):
        """
        fix_axis_par_list     : BEGIN FIX_AXIS_PAR_LIST constant_list END FIX_AXIS_PAR_LIST
        """
        p[0] = A2l_ast.Fix_Axis_Par_List(p[3])


    def p_FIX_NO_AXIS_PTS_X(self, p):
        """
        fix_no_axis_pts_x     : FIX_NO_AXIS_PTS_X constant
        """
        p[0] = A2l_ast.Fix_No_Axis_Pts_X(p[2])


    def p_FIX_NO_AXIS_PTS_Y(self, p):
        """
        fix_no_axis_pts_y     : FIX_NO_AXIS_PTS_Y constant
        """
        p[0] = A2l_ast.Fix_No_Axis_Pts_Y(p[2])


    def p_FIX_NO_AXIS_PTS_Z(self, p):
        """
        fix_no_axis_pts_z     : FIX_NO_AXIS_PTS_Z constant
        """
        p[0] = A2l_ast.Fix_No_Axis_Pts_Z(p[2])


    def p_FIX_NO_AXIS_PTS_Z4(self, p):
        """
        fix_no_axis_pts_z4     : FIX_NO_AXIS_PTS_Z4 constant
        """
        p[0] = A2l_ast.Fix_No_Axis_Pts_Z4(p[2])


    def p_FIX_NO_AXIS_PTS_Z5(self, p):
        """
        fix_no_axis_pts_z5     : FIX_NO_AXIS_PTS_Z5 constant
        """
        p[0] = A2l_ast.Fix_No_Axis_Pts_Z5(p[2])


    def p_FNC_VALUES(self, p):
        """
        fnc_values     : FNC_VALUES constant datatype indexmode_enum addrtype_enum
        """
        p[0] = A2l_ast.Fnc_Values(Position=p[2],
                                  Datatype=p[3],
                                  IndexMode=p[4],
                                  AddressType=p[5])


    def p_FORMAT(self, p):
        """
        format     : FORMAT string_literal
        """
        p[0] = A2l_ast.Format(p[2])


    def p_FORMULA(self, p):
        """
        formula     : BEGIN FORMULA string_literal END FORMULA
                    | BEGIN FORMULA string_literal formula_inv END FORMULA
        """
        if len(p) == 6:
            p[0] = A2l_ast.Formula(f_x=p[3])
        else:
            p[0] = A2l_ast.Formula(f_x=p[3],
                                   Formula_Inv=p[4])


    def p_FORMULA_INV(self, p):
        """
        formula_inv     : FORMULA_INV string_literal
        """
        p[0] = A2l_ast.Formula_Inv(g_x=p[2])


    def p_FRAME(self, p):
        """
        frame     : BEGIN FRAME ident string_literal constant constant END FRAME
                  | BEGIN FRAME ident string_literal constant constant frame_opt_list END FRAME
        """
        node = self.__create_AST_Node(A2l_ast.Frame(Name = p[3],
                                                    LongIdentifier=p[4],
                                                    ScalingUnit=p[5],
                                                    Rate=p[6]))

        if len (p) == 10:
            node.OptionalParams = p[7]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Frame)
        self.__remove_AST_Node(A2l_ast.Frame_Opt)


    def p_FRAME_opt_params(self, p):
        """
        frame_opt    : frame_measurement

        """
        node = self.__get_or_create_AST_Node(A2l_ast.Frame_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Frame_Measurement],
                                 Param = p[1])
        p[0] = node


    def p_FRAME_opt_objects_list(self, p):
        """
        frame_opt    : if_data
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Frame_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.If_Data],
                                       Param = p[1])
        p[0] = node


    def p_FRAME_opt_list (self, p):
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
        p[0] = A2l_ast.Frame_Measurement(p[2])


    def p_FUNCTION(self, p):
        """
        function     : BEGIN FUNCTION ident string_literal END FUNCTION
                     | BEGIN FUNCTION ident string_literal function_opt_list END FUNCTION
        """
        node = self.__create_AST_Node(A2l_ast.Function(Name=p[3],
                                                       LongIdentifier=p[4]))

        if len (p) == 8:
            node.OptionalParams = p[5]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Function)
        self.__remove_AST_Node(A2l_ast.Function_Opt)


    def p_FUNCTION_opt_params(self, p):
        """
        function_opt    : function_version
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Function_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Function_Version],
                                 Param = p[1])
        p[0] = node


    def p_FUNCTION_opt_objects(self, p):
        """
        function_opt    : def_characteristic
                        | in_measurement
                        | loc_measurement
                        | out_measurement
                        | ref_characteristic
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Function_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Def_Characteristic,
                                                 A2l_ast.In_Measurement,
                                                 A2l_ast.Loc_Measurement,
                                                 A2l_ast.Out_Measurement,
                                                 A2l_ast.Ref_Characteristic
                                                 ],
                                 Param = p[1])
        p[0] = node


    def p_FUNCTION_opt_objects_list(self, p):
        """
        function_opt    : annotation
                        | if_data
                        | sub_function
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Function_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Annotation,
                                                      A2l_ast.If_Data,
                                                      A2l_ast.Sub_Function
                                                      ],
                                       Param = p[1])
        p[0] = node


    def p_FUNCTION_opt_list (self, p):
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
        p[0] = A2l_ast.Function_List(Name=p[3])


    def p_FUNCTION_VERSION(self, p):
        """
        function_version     : FUNCTION_VERSION string_literal
        """
        p[0] = A2l_ast.Function_Version(p[2])


    def p_GROUP(self, p):
        """
        group     : BEGIN GROUP ident string_literal END GROUP
                  | BEGIN GROUP ident string_literal group_opt_list END GROUP
        """
        node = self.__create_AST_Node(A2l_ast.Group(GroupName=p[3],
                                                    GroupLongIdentifier=p[4]))

        if len (p) == 8:
            node.OptionalParams = p[5]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Group)
        self.__remove_AST_Node(A2l_ast.Group_Opt)


    def p_GROUP_opt_params(self, p):
        """
        group_opt    : root
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Group_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Root],
                                 Param = p[1])

        p[0] = node


    def p_GROUP_opt_objects(self, p):
        """
        group_opt    : function_list
                     | ref_characteristic
                     | ref_measurement
                     | sub_group
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Group_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                  AstNodeNames= [A2l_ast.Function_List,
                                                 A2l_ast.Ref_Characteristic,
                                                 A2l_ast.Ref_Measurement,
                                                 A2l_ast.Sub_Group
                                                ],
                                       Param = p[1])
        p[0] = node


    def p_GROUP_opt_objects_list(self, p):
        """
        group_opt    : annotation
                     | if_data
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Group_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Annotation,
                                                      A2l_ast.If_Data
                                                      ],
                                       Param = p[1])
        p[0] = node


    def p_GROUP_opt_list (self, p):
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
        p[0] = A2l_ast.Guard_Rails(Boolean=True)


    def p_HEADER(self, p):
        """
        header     : BEGIN HEADER string_literal END HEADER
                   | BEGIN HEADER string_literal header_opt_list END HEADER
        """
        node = self.__create_AST_Node(A2l_ast.Header(Comment=p[3]))

        if len (p) == 7:
            node.OptionalParams = p[4]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Header)
        self.__remove_AST_Node(A2l_ast.Header_Opt)


    def p_HEADER_opt(self, p):
        """
        header_opt    : project_no
                      | version
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Header_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Project_No,
                                                 A2l_ast.Version
                                                 ],
                                 Param = p[1])

        p[0] = node


    def p_HEADER_opt_list (self, p):
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
        p[0] = A2l_ast.Identification(Position=p[2],
                                      Datatype=p[3])


    def p_IF_DATA(self, p):
        """
        if_data             : if_data_begin if_data_opt_list if_data_end
        """
        data_params = [x for x in p[2] if not isinstance(x, A2l_ast.If_Data_Block)]
        if_data_block = [x for x in p[2] if isinstance(x, A2l_ast.If_Data_Block)]
        p[0] = A2l_ast.If_Data(Name=p[1],
                               OptionalParams=A2l_ast.If_Data_Opt(DataParams=data_params,
                                                                  If_Data_Block=if_data_block))


    def p_IF_DATA_mandatory_only(self, p):
        """
        if_data             : if_data_begin if_data_end
        """
        p[0] = A2l_ast.If_Data(Name=p[1])


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
        pass


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
        if_data_block = [x for x in p[2] if isinstance(x, A2l_ast.If_Data_Block)]
        data_params = [x for x in p[2] if not isinstance(x, A2l_ast.If_Data_Block)]
        p[0] = A2l_ast.If_Data_Block(Name=p[1],
                                     DataParams=data_params,
                                     If_Data_Block=if_data_block)


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
        p[0] = A2l_ast.In_Measurement(p[3])


    def p_LAYOUT(self, p):
        """
        layout     : LAYOUT indexmode_enum
        """
        # Description: This keyword describes the layout of a
        # multi-dimensional measurement array.
        # It can be used at MEASUREMENT.
        p[0] = A2l_ast.Layout(p[2])


    def p_LEFT_SHIFT(self, p):
        """
        left_shift     : LEFT_SHIFT constant
        """
        # Description: The LEFT_SHIFT keyword is only used within the
        # BIT_OPERATION keyword. See description of BIT_OPERATION.
        p[0] = A2l_ast.Left_Shift(p[2])


    def p_LOC_MEASUREMENT(self, p):
        """
        loc_measurement     : BEGIN LOC_MEASUREMENT ident_list END LOC_MEASUREMENT
        """
        p[0] = A2l_ast.Loc_Measurement(p[3])


    def p_MAP_LIST(self, p):
        """
        map_list     : BEGIN MAP_LIST ident_list END MAP_LIST
        """
        p[0] = A2l_ast.Map_List(p[3])


    def p_MATRIX_DIM(self, p):
        """
        matrix_dim     : MATRIX_DIM constant constant constant
        """
        p[0] = A2l_ast.Matrix_Dim(xDim=p[2],
                                  yDim=p[3],
                                  zDim=p[4])


    def p_MAX_GRAD(self, p):
        """
        max_grad     : MAX_GRAD constant
        """
        p[0] = A2l_ast.Max_Grad(p[2])


    def p_MAX_REFRESH(self, p):
        """
        max_refresh     : MAX_REFRESH constant constant
        """
        p[0] = A2l_ast.Max_Refresh(ScalingUnit=p[2],
                                   Rate=p[3])


    def p_MEASUREMENT(self, p):
        """
        measurement     : BEGIN MEASUREMENT ident string_literal datatype ident constant constant constant constant END MEASUREMENT
                        | BEGIN MEASUREMENT ident string_literal datatype ident constant constant constant constant measurement_opt_list END MEASUREMENT
        """
        node = self.__create_AST_Node(A2l_ast.Measurement(Name=p[3],
                                                      LongIdentifier=p[4],
                                                      Datatype=p[5],
                                                      Conversion=p[6],
                                                      Resolution=p[7],
                                                      Accuracy=p[8],
                                                      LowerLimit=p[9],
                                                      UpperLimit=p[10]))

        if len(p) == 14:
            node.OptionalParams = p[11]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Measurement)
        self.__remove_AST_Node(A2l_ast.Measurement_Opt)


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
        node = self.__get_or_create_AST_Node(A2l_ast.Measurement_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Array_Size,
                                                 A2l_ast.Bit_Mask,
                                                 A2l_ast.Byte_Order,
                                                 A2l_ast.Discrete,
                                                 A2l_ast.Display_Identifier,
                                                 A2l_ast.Ecu_Address,
                                                 A2l_ast.Ecu_Address_Extension,
                                                 A2l_ast.Error_Mask,
                                                 A2l_ast.Format,
                                                 A2l_ast.Layout,
                                                 A2l_ast.Phys_Unit,
                                                 A2l_ast.Read_Write,
                                                 A2l_ast.Ref_Memory_Segment
                                                 ],
                                 Param = p[1])

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
        node = self.__get_or_create_AST_Node(A2l_ast.Measurement_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                  AstNodeNames= [A2l_ast.Bit_Operation,
                                                 A2l_ast.Bit_Operation,
                                                 A2l_ast.Function_List,
                                                 A2l_ast.Max_Refresh,
                                                 A2l_ast.Symbol_Link,
                                                 A2l_ast.Virtual
                                                 ],
                                  Param = p[1])
        p[0] = node


    def p_MEASUREMENT_opt_objects_list(self, p):
        """
        measurement_opt    : annotation
                           | if_data
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Measurement_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Annotation,
                                                      A2l_ast.If_Data],
                                       Param = p[1])
        p[0] = node


    def p_MEASUREMENT_opt_list (self, p):
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
        p[0] = A2l_ast.Memory_Layout(PrgType=p[3],
                                     Address=p[4],
                                     Size=p[5],
                                     Offset=p[6])
        if len (p)==10:
            p[0].If_Data=p[7]


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
        p[0] = A2l_ast.Memory_Segment(Name=p[3],
                                      LongIdentifier=p[4],
                                      PrgType=p[5],
                                      MemoryType=p[6],
                                      Attribute=p[7],
                                      Address=p[8],
                                      Size=p[9],
                                      Offset=p[10])

        if len(p) == 14:
            p[0].If_Data=p[11]


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
        node = self.__create_AST_Node(A2l_ast.Mod_Common(Comment=p[3]))

        if len(p) == 7:
            node.OptionalParams = p[4]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Mod_Common)
        self.__remove_AST_Node(A2l_ast.Mod_Common_Opt)


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
        node = self.__get_or_create_AST_Node(A2l_ast.Mod_Common_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Alignment_Byte,
                                                 A2l_ast.Alignment_Float32_Ieee,
                                                 A2l_ast.Alignment_Float64_Ieee,
                                                 A2l_ast.Alignment_Int64,
                                                 A2l_ast.Alignment_Long,
                                                 A2l_ast.Alignment_Word,
                                                 A2l_ast.Byte_Order,
                                                 A2l_ast.Data_Size,
                                                 A2l_ast.Deposit
                                                 ],
                                 Param = p[1])

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
        node = self.__create_AST_Node(A2l_ast.Mod_Par(Comment=p[3]))

        if len(p) == 7:
            node.OptionalParams = p[4]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Mod_Par)
        self.__remove_AST_Node(A2l_ast.Mod_Par_Opt)


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
        node = self.__get_or_create_AST_Node(A2l_ast.Mod_Par_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Cpu_Type,
                                                 A2l_ast.Customer,
                                                 A2l_ast.Customer_No,
                                                 A2l_ast.Ecu,
                                                 A2l_ast.Ecu_Calibration_Offset,
                                                 A2l_ast.Epk,
                                                 A2l_ast.No_Of_Interfaces,
                                                 A2l_ast.Phone_No,
                                                 A2l_ast.Supplier,
                                                 A2l_ast.User,
                                                 A2l_ast.Version
                                                 ],
                                 Param = p[1])
        p[0] = node


    def p_MOD_PAR_opt_objects_list(self, p):
        """
        mod_par_opt    : addr_epk
                       | calibration_method
                       | memory_layout
                       | memory_segment
                       | system_constant
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Mod_Par_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Addr_Epk,
                                                      A2l_ast.Calibration_Method,
                                                      A2l_ast.Memory_Layout,
                                                      A2l_ast.Memory_Segment,
                                                      A2l_ast.System_Constant,],
                                       Param = p[1])
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
            node = self.__create_AST_Node(A2l_ast.Module(Name=None,
                                                 LongIdentifier=None))
        else:
            node = self.__create_AST_Node(A2l_ast.Module(Name=p[3],
                                                 LongIdentifier=p[4]))

        if len(p) == 8:
            node.OptionalParams = p[5]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Module)
        self.__remove_AST_Node(A2l_ast.Module_Opt)


    def p_MODULE_opt_objects(self, p):
        """
        module_opt    : mod_common
                      | mod_par
                      | variant_coding
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Module_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                  AstNodeNames= [A2l_ast.Mod_Common,
                                                 A2l_ast.Mod_Par,
                                                 A2l_ast.Variant_Coding,
                                                 ],
                                  Param = p[1])
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
        node = self.__get_or_create_AST_Node(A2l_ast.Module_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Axis_Pts,
                                                      A2l_ast.Characteristic,
                                                      A2l_ast.Compu_Method,
                                                      A2l_ast.Compu_Tab,
                                                      A2l_ast.Compu_Vtab,
                                                      A2l_ast.Compu_Vtab_Range,
                                                      A2l_ast.Frame,
                                                      A2l_ast.Function,
                                                      A2l_ast.Group,
                                                      A2l_ast.If_Data,
                                                      A2l_ast.Measurement,
                                                      A2l_ast.Record_Layout,
                                                      A2l_ast.Unit,
                                                      A2l_ast.User_Rights
                                                      ],
                                       Param = p[1])
        p[0] = node


    def p_MODULE_opt_list (self, p):
        """
        module_opt_list    : module_opt
                        | module_opt_list module_opt
        """
        self.__update_progress(int((float(self.a2lLex.get_line_number())/float(self.file_len))*100))

        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]


    def p_MONOTONY(self, p):
        """
        monotony     : MONOTONY monotony_enum
        """
        p[0] = A2l_ast.Monotony(p[2])


    def p_NO_AXIS_PTS_X(self, p):
        """
        no_axis_pts_x     : NO_AXIS_PTS_X constant datatype
        """
        p[0] = A2l_ast.No_Axis_Pts_X(Position=p[2],
                                     Datatype=p[3])


    def p_NO_AXIS_PTS_Y(self, p):
        """
        no_axis_pts_y     : NO_AXIS_PTS_Y constant datatype
        """
        p[0] = A2l_ast.No_Axis_Pts_Y(Position=p[2],
                                     Datatype=p[3])


    def p_NO_AXIS_PTS_Z(self, p):
        """
        no_axis_pts_z     : NO_AXIS_PTS_Z constant datatype
        """
        p[0] = A2l_ast.No_Axis_Pts_Z(Position=p[2],
                                     Datatype=p[3])


    def p_NO_AXIS_PTS_Z4(self, p):
        """
        no_axis_pts_z4     : NO_AXIS_PTS_Z4 constant datatype
        """
        p[0] = A2l_ast.No_Axis_Pts_Z4(Position=p[2],
                                     Datatype=p[3])


    def p_NO_AXIS_PTS_Z5(self, p):
        """
        no_axis_pts_z5     : NO_AXIS_PTS_Z5 constant datatype
        """
        p[0] = A2l_ast.No_Axis_Pts_Z5(Position=p[2],
                                     Datatype=p[3])


    def p_NO_OF_INTERFACES(self, p):
        """
        no_of_interfaces     : NO_OF_INTERFACES constant
        """
        p[0] = A2l_ast.No_Of_Interfaces(p[2])


    def p_NO_RESCALE_X(self, p):
        """
        no_rescale_x     : NO_RESCALE_X constant datatype
        """
        p[0] = A2l_ast.No_Rescale_X(Position=p[2],
                                    Datatype=p[3])


    def p_NUMBER(self, p):
        """
        number     : NUMBER constant
        """
        p[0] = A2l_ast.Number(p[2])


    def p_OFFSET_X(self, p):
        """
        offset_x     : OFFSET_X constant datatype
        """
        p[0] = A2l_ast.Offset_X(Position=p[2],
                                Datatype=p[3])


    def p_OFFSET_Y(self, p):
        """
        offset_y     : OFFSET_Y constant datatype
        """
        p[0] = A2l_ast.Offset_Y(Position=p[2],
                                Datatype=p[3])


    def p_OFFSET_Z(self, p):
        """
        offset_z     : OFFSET_Z constant datatype
        """
        p[0] = A2l_ast.Offset_Z(Position=p[2],
                                Datatype=p[3])


    def p_OFFSET_Z4(self, p):
        """
        offset_z4     : OFFSET_Z4 constant datatype
        """
        p[0] = A2l_ast.Offset_Z4(Position=p[2],
                                Datatype=p[3])


    def p_OFFSET_Z5(self, p):
        """
        offset_z5     : OFFSET_Z5 constant datatype
        """
        p[0] = A2l_ast.Offset_Z5(Position=p[2],
                                Datatype=p[3])



    def p_OUT_MEASUREMENT(self, p):
        """
        out_measurement     : BEGIN OUT_MEASUREMENT ident_list END OUT_MEASUREMENT
        """
        p[0] = A2l_ast.Out_Measurement(p[3])


    def p_PHONE_NO(self, p):
        """
        phone_no     : PHONE_NO string_literal
        """
        p[0] = A2l_ast.Phone_No(p[2])


    def p_PHYS_UNIT(self, p):
        """
        phys_unit     : PHYS_UNIT string_literal
        """
        p[0] = A2l_ast.Phys_Unit(p[2])


    def p_PROJECT(self, p):
        """
        project     : BEGIN PROJECT ident string_literal END PROJECT
                    | BEGIN PROJECT ident string_literal project_opt_list END PROJECT
        """
        node = self.__create_AST_Node(A2l_ast.Project(Name=p[3],
                                                  LongIdentifier=p[4]))

        if len(p) == 8:
            node.OptionalParams = p[5]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Project)
        self.__remove_AST_Node(A2l_ast.Project_Opt)


    def p_PROJECT_opt_objects(self, p):
        """
        project_opt    : header
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Project_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                  AstNodeNames= [A2l_ast.Header],
                                  Param = p[1])
        p[0] = node


    def p_PROJECT_opt_objects_list(self, p):
        """
        project_opt    : module
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Project_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Module],
                                       Param = p[1])
        p[0] = node


    def p_PROJECT_opt_list (self, p):
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
        p[0] = A2l_ast.Project_No(p[2])


    def p_READ_ONLY(self, p):
        """
        read_only     : READ_ONLY
        """
        # This keyword is used to indicate that an adjustable
        # object cannot be changed (but can only be read).
        p[0] = A2l_ast.Read_Only(Boolean=True)


    def p_READ_WRITE(self, p):
        """
        read_write     : READ_WRITE
        """
        # Description: This keyword is used to mark a measurement
        # object to be writeable.
        p[0] = A2l_ast.Read_Write(Boolean=True)


    def p_RECORD_LAYOUT(self, p):
        """
        record_layout     : BEGIN RECORD_LAYOUT ident END RECORD_LAYOUT
                          | BEGIN RECORD_LAYOUT ident record_layout_opt_list END RECORD_LAYOUT
        """
        self.__create_AST_Node(A2l_ast.Record_Layout(Name=p[3]))

        node = self.__get_AST_Node(A2l_ast.Record_Layout)

        if len(p) == 7:
            node.OptionalParams = p[4]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Record_Layout)
        self.__remove_AST_Node(A2l_ast.Record_Layout_Opt)

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
        node = self.__get_or_create_AST_Node(A2l_ast.Record_Layout_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Alignment_Byte,
                                                 A2l_ast.Alignment_Float32_Ieee,
                                                 A2l_ast.Alignment_Float64_Ieee,
                                                 A2l_ast.Alignment_Int64,
                                                 A2l_ast.Alignment_Long,
                                                 A2l_ast.Alignment_Word,
                                                 A2l_ast.Fix_No_Axis_Pts_X,
                                                 A2l_ast.Fix_No_Axis_Pts_Y,
                                                 A2l_ast.Fix_No_Axis_Pts_Z,
                                                 A2l_ast.Fix_No_Axis_Pts_Z4,
                                                 A2l_ast.Fix_No_Axis_Pts_Z5,
                                                 A2l_ast.Static_Record_Layout
                                                 ],
                                 Param = p[1])

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
        node = self.__get_or_create_AST_Node(A2l_ast.Record_Layout_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                  AstNodeNames= [A2l_ast.Axis_Pts_X,
                                                 A2l_ast.Axis_Pts_Y,
                                                 A2l_ast.Axis_Pts_Z,
                                                 A2l_ast.Axis_Pts_Z4,
                                                 A2l_ast.Axis_Pts_Z5,
                                                 A2l_ast.Axis_Rescale_X,
                                                 A2l_ast.Dist_Op_X,
                                                 A2l_ast.Dist_Op_Y,
                                                 A2l_ast.Dist_Op_Z,
                                                 A2l_ast.Dist_Op_Z4,
                                                 A2l_ast.Dist_Op_Z5,
                                                 A2l_ast.Fnc_Values,
                                                 A2l_ast.Identification,
                                                 A2l_ast.No_Axis_Pts_X,
                                                 A2l_ast.No_Axis_Pts_Y,
                                                 A2l_ast.No_Axis_Pts_Z,
                                                 A2l_ast.No_Axis_Pts_Z4,
                                                 A2l_ast.No_Axis_Pts_Z5,
                                                 A2l_ast.No_Rescale_X,
                                                 A2l_ast.Offset_X,
                                                 A2l_ast.Offset_Y,
                                                 A2l_ast.Offset_Z,
                                                 A2l_ast.Offset_Z4,
                                                 A2l_ast.Offset_Z5,
                                                 A2l_ast.Rip_Addr_W,
                                                 A2l_ast.Rip_Addr_X,
                                                 A2l_ast.Rip_Addr_Y,
                                                 A2l_ast.Rip_Addr_Z,
                                                 A2l_ast.Rip_Addr_Z4,
                                                 A2l_ast.Rip_Addr_Z5,
                                                 A2l_ast.Src_Addr_X,
                                                 A2l_ast.Src_Addr_Y,
                                                 A2l_ast.Src_Addr_Z,
                                                 A2l_ast.Src_Addr_Z4,
                                                 A2l_ast.Src_Addr_Z5,
                                                 A2l_ast.Shift_Op_X,
                                                 A2l_ast.Shift_Op_Y,
                                                 A2l_ast.Shift_Op_Z,
                                                 A2l_ast.Shift_Op_Z4,
                                                 A2l_ast.Shift_Op_Z5,
                                                 ],
                                  Param = p[1])
        p[0] = node


    def p_RECORD_LAYOUT_opt_objects_list(self, p):
        """
        record_layout_opt    : reserved
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Record_Layout_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Reserved],
                                       Param = p[1])
        p[0] = node


    def p_RECORD_LAYOUT_opt_list (self, p):
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
        p[0] = A2l_ast.Ref_Characteristic(Identifier=p[3])


    def p_REF_GROUP(self, p):
        """
        ref_group     : BEGIN REF_GROUP ident_list END REF_GROUP
        """
        p[0] = A2l_ast.Ref_Group(Identifier=p[3])


    def p_REF_MEASUREMENT(self, p):
        """
        ref_measurement     : BEGIN REF_MEASUREMENT ident_list END REF_MEASUREMENT
        """
        p[0] = A2l_ast.Ref_Measurement(Identifier=p[3])


    def p_REF_MEMORY_SEGMENT(self, p):
        """
        ref_memory_segment     : REF_MEMORY_SEGMENT ident
        """
        p[0] = A2l_ast.Ref_Memory_Segment(p[2])


    def p_REF_UNIT(self, p):
        """
        ref_unit     : REF_UNIT ident
        """
        p[0] = A2l_ast.Ref_Unit(p[2])


    def p_RESERVED(self, p):
        """
        reserved     : RESERVED constant datasize
        """
        p[0] = A2l_ast.Reserved(Position=p[2],
                                DataSize=p[3])


    def p_RIGHT_SHIFT(self, p):
        """
        right_shift     : RIGHT_SHIFT constant
        """
        p[0] = A2l_ast.Right_Shift(p[2])


    def p_RIP_ADDR_X(self, p):
        """
        rip_addr_x     : RIP_ADDR_X constant datatype
        """
        p[0] = A2l_ast.Rip_Addr_X(Position=p[2],
                                  Datatype=p[3])


    def p_RIP_ADDR_W(self, p):
        """
        rip_addr_w     : RIP_ADDR_W constant datatype
        """
        p[0] = A2l_ast.Rip_Addr_W(Position=p[2],
                                  Datatype=p[3])


    def p_RIP_ADDR_Y(self, p):
        """
        rip_addr_y     : RIP_ADDR_Y constant datatype
        """
        p[0] = A2l_ast.Rip_Addr_Y(Position=p[2],
                                  Datatype=p[3])


    def p_RIP_ADDR_Z(self, p):
        """
        rip_addr_z     : RIP_ADDR_Z constant datatype
        """
        p[0] = A2l_ast.Rip_Addr_Z(Position=p[2],
                                  Datatype=p[3])


    def p_RIP_ADDR_Z4(self, p):
        """
        rip_addr_z4     : RIP_ADDR_Z4 constant datatype
        """
        p[0] = A2l_ast.Rip_Addr_Z4(Position=p[2],
                                  Datatype=p[3])


    def p_RIP_ADDR_Z5(self, p):
        """
        rip_addr_z5     : RIP_ADDR_Z5 constant datatype
        """
        p[0] = A2l_ast.Rip_Addr_Z5(Position=p[2],
                                  Datatype=p[3])


    def p_ROOT(self, p):
        """
        root     : ROOT
        """
        p[0] = A2l_ast.Root(Boolean=True)


    def p_SHIFT_OP_X(self, p):
        """
        shift_op_x     : SHIFT_OP_X constant datatype
        """
        p[0] = A2l_ast.Shift_Op_X(Position=p[2],
                                  Datatype=p[3])


    def p_SHIFT_OP_Y(self, p):
        """
        shift_op_y     : SHIFT_OP_Y constant datatype
        """
        p[0] = A2l_ast.Shift_Op_Y(Position=p[2],
                                  Datatype=p[3])


    def p_SHIFT_OP_Z(self, p):
        """
        shift_op_z     : SHIFT_OP_Z constant datatype
        """
        p[0] = A2l_ast.Shift_Op_Z(Position=p[2],
                                  Datatype=p[3])


    def p_SHIFT_OP_Z4(self, p):
        """
        shift_op_z4     : SHIFT_OP_Z4 constant datatype
        """
        p[0] = A2l_ast.Shift_Op_Z4(Position=p[2],
                                  Datatype=p[3])


    def p_SHIFT_OP_Z5(self, p):
        """
        shift_op_z5     : SHIFT_OP_Z5 constant datatype
        """
        p[0] = A2l_ast.Shift_Op_Z5(Position=p[2],
                                   Datatype=p[3])

    def p_SIGN_EXTEND(self, p):
        """
        sign_extend     : SIGN_EXTEND
        """
        p[0] = A2l_ast.Sign_Extend(Boolean=True)


    def p_SI_EXPONENTS(self, p):
        """
        si_exponents     : SI_EXPONENTS constant constant constant constant constant constant constant
        """
        p[0] = A2l_ast.Si_Exponents(Length=p[2],
                                    Mass=p[3],
                                    Time=p[4],
                                    ElectricCurrent=p[5],
                                    Temperature=p[6],
                                    AmountOfSubstance=p[7],
                                    LuminousIntensity=p[8])


    def p_SRC_ADDR_X(self, p):
        """
        src_addr_x     : SRC_ADDR_X constant datatype
        """
        p[0] = A2l_ast.Src_Addr_X(Position=p[2],
                                  Datatype=p[3])


    def p_SRC_ADDR_Y(self, p):
        """
        src_addr_y     : SRC_ADDR_Y constant datatype
        """
        p[0] = A2l_ast.Src_Addr_Y(Position=p[2],
                                  Datatype=p[3])


    def p_SRC_ADDR_Z(self, p):
        """
        src_addr_z     : SRC_ADDR_Z constant datatype
        """
        p[0] = A2l_ast.Src_Addr_Z(Position=p[2],
                                  Datatype=p[3])


    def p_SRC_ADDR_Z4(self, p):
        """
        src_addr_z4     : SRC_ADDR_Z4 constant datatype
        """
        p[0] = A2l_ast.Src_Addr_Z4(Position=p[2],
                                  Datatype=p[3])


    def p_SRC_ADDR_Z5(self, p):
        """
        src_addr_z5     : SRC_ADDR_Z5 constant datatype
        """
        p[0] = A2l_ast.Src_Addr_Z5(Position=p[2],
                                  Datatype=p[3])


    def p_STATIC_RECORD_LAYOUT(self, p):
        """
        static_record_layout     : STATIC_RECORD_LAYOUT
        """
        p[0] = A2l_ast.Static_Record_Layout(Boolean=True)


    def p_STATUS_STRING_REF(self, p):
        """
        status_string_ref     : STATUS_STRING_REF ident
        """
        # ConversionTable
        p[0] = A2l_ast.Status_String_Ref(p[2])


    def p_STEP_SIZE(self, p):
        """
        step_size     : STEP_SIZE constant
        """
        p[0] = A2l_ast.Step_Size(p[2])


    def p_SUB_FUNCTION(self, p):
        """
        sub_function     : BEGIN SUB_FUNCTION ident_list END SUB_FUNCTION
        """
        p[0] = A2l_ast.Sub_Function(Identifier=p[3])


    def p_SUB_GROUP(self, p):
        """
        sub_group     : BEGIN SUB_GROUP ident_list END SUB_GROUP
        """
        p[0] = A2l_ast.Sub_Group(p[3])


    def p_SUPPLIER(self, p):
        """
        supplier     : SUPPLIER string_literal
        """
        p[0] = A2l_ast.Supplier(p[2])


    def p_SYMBOL_LINK(self, p):
        """
        symbol_link     : SYMBOL_LINK string_literal constant
        """
        p[0] = A2l_ast.Symbol_Link(SymbolName=p[2],
                                   Offset=p[3])


    def p_SYSTEM_CONSTANT(self, p):
        """
        system_constant     : SYSTEM_CONSTANT string_literal string_literal
        """
        p[0] = A2l_ast.System_Constant(Name=p[2],
                                       Value=p[3])


    def p_UNIT(self, p):
        """
        unit     : BEGIN UNIT ident string_literal string_literal unit_type_enum END UNIT
                 | BEGIN UNIT ident string_literal string_literal unit_type_enum unit_opt_list END UNIT
        """
        node = self.__create_AST_Node(A2l_ast.Unit(Name=p[3],
                                               LongIdentifier=p[4],
                                               Display=p[5],
                                               Type=p[6]))

        if len(p) == 10:
            node.OptionalParams = p[7]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Unit)
        self.__remove_AST_Node(A2l_ast.Unit_Opt)



    def p_UNIT_opt_params(self, p):
        """
        unit_opt    : ref_unit
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Unit_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Ref_Unit],
                                 Param = p[1])

        p[0] = node


    def p_UNIT_opt_objects(self, p):
        """
        unit_opt    : si_exponents
                    | unit_conversion
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Unit_Opt)
        self.__add_AST_Node_Object(NodeClass = node,
                                  AstNodeNames= [A2l_ast.Si_Exponents,
                                                 A2l_ast.Unit_Conversion
                                                 ],
                                  Param = p[1])
        p[0] = node


    def p_UNIT_opt_list (self, p):
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
        p[0] = A2l_ast.Unit_Conversion(Gradient=p[2],
                                       Offset=p[3])


    def p_USER(self, p):
        """
        user     : USER string_literal
        """
        p[0] = A2l_ast.User(p[2])


    def p_USER_RIGHTS(self, p):
        """
        user_rights     : BEGIN USER_RIGHTS ident END USER_RIGHTS
                        | BEGIN USER_RIGHTS ident user_rights_opt_list END USER_RIGHTS
        """
        node = self.__create_AST_Node(A2l_ast.User_Rights(UserLevelId=p[3]))

        if len(p) == 7:
            node.OptionalParams = p[4]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.User_Rights)
        self.__remove_AST_Node(A2l_ast.User_Rights_Opt)

    def p_USER_RIGHTS_opt_params(self, p):
        """
        user_rights_opt    : read_only
        """
        node = self.__get_or_create_AST_Node(A2l_ast.User_Rights_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Read_Only],
                                 Param = p[1])
        p[0] = node


    def p_USER_RIGHTS_opt_objects_list(self, p):
        """
        user_rights_opt    : ref_group
        """
        node = self.__get_or_create_AST_Node(A2l_ast.User_Rights_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Ref_Group],
                                       Param = p[1])
        p[0] = node


    def p_USER_RIGHTS_opt_list (self, p):
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
            p[0] = A2l_ast.Var_Address(p[3])


    def p_VAR_CHARACTERISTIC(self, p):
        """
        var_characteristic     : BEGIN VAR_CHARACTERISTIC ident ident_list END VAR_CHARACTERISTIC
                               | BEGIN VAR_CHARACTERISTIC ident ident_list var_address END VAR_CHARACTERISTIC
                               | BEGIN VAR_CHARACTERISTIC ident ident_list meta_block_empty END VAR_CHARACTERISTIC
        """
        if len(p) == 7:
            p[0] = A2l_ast.Var_Characteristic(Name=p[3],
                                              CriterionName=p[4])
        else:
            p[0] = A2l_ast.Var_Characteristic(Name=p[3],
                                              CriterionName=p[4],
                                              Var_Address=p[5])


    def p_VAR_CRITERION(self, p):
        """
        var_criterion     : BEGIN VAR_CRITERION ident string_literal ident_list END VAR_CRITERION
                          | BEGIN VAR_CRITERION ident string_literal ident_list var_criterion_opt_list END VAR_CRITERION
        """
        node = self.__create_AST_Node(A2l_ast.Var_Criterion(Name=p[3],
                                                        LongIdentifier=p[4],
                                                        Value=p[5]))

        if len(p) == 9:
            node.OptionalParams = p[6]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Var_Criterion)
        self.__remove_AST_Node(A2l_ast.Var_Criterion_Opt)


    def p_VAR_CRITERION_opt(self, p):
        """
        var_criterion_opt    : var_measurement
                             | var_selection_characteristic
                             
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Var_Criterion_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Var_Measurement,
                                                 A2l_ast.Var_Selection_Characteristic
                                                 ],
                                 Param = p[1])

        p[0] = node


    def p_VAR_CRITERION_opt_list (self, p):
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
        p[0] = A2l_ast.Var_Forbidden_Comb(p[3])


    def p_VAR_MEASUREMENT(self, p):
        """
        var_measurement     : VAR_MEASUREMENT ident
        """
        p[0] = A2l_ast.Var_Measurement(p[2])


    def p_VAR_NAMING(self, p):
        """
        var_naming     : VAR_NAMING tag_enum
        """
        p[0] = A2l_ast.Var_Naming(p[2])


    def p_VAR_SELECTION_CHARACTERISTIC(self, p):
        """
        var_selection_characteristic     : VAR_SELECTION_CHARACTERISTIC ident
        """
        p[0] = A2l_ast.Var_Selection_Characteristic(p[2])


    def p_VAR_SEPARATOR(self, p):
        """
        var_seperator     : VAR_SEPARATOR string_literal
        """
        p[0] = A2l_ast.Var_Separator(p[2])


    def p_VARIANT_CODING(self, p):
        """
        variant_coding     : BEGIN VARIANT_CODING variant_coding_opt_list END VARIANT_CODING
        """
        node = self.__create_AST_Node(A2l_ast.Variant_Coding())

        if len(p) == 6:
            node.OptionalParams = p[3]

        p[0] = node

        self.__remove_AST_Node(A2l_ast.Variant_Coding)
        self.__remove_AST_Node(A2l_ast.Variant_Coding_Opt)



    def p_VARIANT_CODING_opt_params(self, p):
        """
        variant_coding_opt    : var_naming
                              | var_seperator
                              
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Variant_Coding_Opt)
        self.__add_AST_Node_Param(NodeClass = node,
                                 AstNodeNames = [A2l_ast.Var_Naming,
                                                 A2l_ast.Var_Separator
                                                 ],
                                 Param = p[1])

        p[0] = node


    def p_VARIANT_CODING_opt_objects_list(self, p):
        """
        variant_coding_opt    : var_characteristic
                              | var_criterion
                              | var_forbidden_comb
        """
        node = self.__get_or_create_AST_Node(A2l_ast.Variant_Coding_Opt)
        self.__add_AST_Node_Object_List(NodeClass = node,
                                       AstNodeNames= [A2l_ast.Var_Characteristic,
                                                      A2l_ast.Var_Criterion,
                                                      A2l_ast.Var_Forbidden_Comb
                                                      ],
                                       Param = p[1])
        p[0] = node



    def p_VARIANT_CODING_opt_list (self, p):
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
        p[0] = A2l_ast.Version(p[2])


    def p_VIRTUAL(self, p):
        """
        virtual     : BEGIN VIRTUAL ident_list END VIRTUAL
        """
        p[0] = A2l_ast.Virtual(MeasuringChannel=p[3])


    def p_VIRTUAL_CHARACTERISTIC(self, p):
        """
        virtual_characteristic     : BEGIN VIRTUAL_CHARACTERISTIC string_literal ident_list END VIRTUAL_CHARACTERISTIC
        """
        p[0] = A2l_ast.Virtual_Characteristic(Formula=p[3],
                                              Characteristic=p[4])
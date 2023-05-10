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


# @TODO: refactor "addrtype_enum" etc to "addrtype" in rules
class RulesDatatypes:
    """
    Rules for parsing datatypes.
    """

    def p_constant(self, p):
        """
        constant : INT_CONST_DEC
                 | INT_CONST_HEX
                 | FLOAT_CONST
                 | HEX_FLOAT_CONST
        """
        p[0] = p[1]

    def p_constant_list(self, p):
        """
        constant_list : constant
                      | constant_list constant
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_ident(self, p):
        """
        ident : ID
        """
        p[0] = p[1]

    def p_ident_list(self, p):
        """
        ident_list : ident
                   | ident_list ident
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_ident_ident(self, p):
        """
        ident_ident : ident ident
        """
        p[0] = [p[1], p[2]]

    def p_ident_ident_list(self, p):
        """
        ident_ident_list : ident_ident
                         | ident_ident_list ident_ident
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_string_literal(self, p):
        """
        string_literal : STRING_LITERAL
        """
        p[0] = p[1]

    def p_string_literal_list(self, p):
        """
        string_literal_list : string_literal
                            | string_literal_list string_literal
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_axis_points(self, p):
        """
        axis_points : constant constant
        """
        p[0] = [p[1], p[2]]

    def p_axis_points_list(self, p):
        """
        axis_points_list : axis_points
                         | axis_points_list axis_points
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_inval_outval(self, p):
        """
        inVal_outVal : constant string_literal
        """
        p[0] = [p[1], p[2]]

    def p_inval_outval_list(self, p):
        """
        inVal_outVal_list : inVal_outVal
                          | inVal_outVal_list inVal_outVal
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_inval_minmax_outval(self, p):
        """
        inVal_MinMax_outVal : constant constant string_literal
        """
        p[0] = [p[1], p[2], p[3]]

    def p_inval_minmax_outval_list(self, p):
        """
        inVal_MinMax_outVal_list : inVal_MinMax_outVal
                                 | inVal_MinMax_outVal_list inVal_MinMax_outVal
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[1].append(p[2])
            p[0] = p[1]

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


class LexerRegex:
    """
    Holds a collection of regular expressions used in the lexer to identify tokens.
    """

    ######################################
    # RegEx for "BEGIN" and "END" tokens #
    ######################################
    begin_section = r"/\s*begin|/\s*BEGIN"
    end_section = r"/\s*end|/\s*END"

    #########################################
    # RegEx for parsing regular identifiers #
    #########################################
    identifier = r"[a-zA-Z_][0-9a-zA-Z_\-.\[\]]*"

    #############################
    # RegEx for parsing numbers #
    #############################
    hex_digits = "[0-9a-fA-F]+"
    bin_prefix = "[+-]?0[bB]"
    integer_suffix_opt = r"(([uU]ll)|([uU]LL)|(ll[uU]?)|(LL[uU]?)|([uU][lL])|([lL][uU]?)|[uU])?"
    decimal_constant = f"([+-]?0{integer_suffix_opt})|([+-]?[1-9][0-9]*{integer_suffix_opt})"
    hex_prefix = "[+-]?0[xX]"
    hex_constant = hex_prefix + hex_digits + integer_suffix_opt
    exponent_part = r"""([eE][-+]?[0-9]+)"""
    fractional_constant = r"""([+-]?[0-9]+\.[0-9]+)|([+-]?\.[0-9]+)|([+-]?[0-9]+\.)"""
    floating_constant = (
        f"( ( (({fractional_constant}){exponent_part}?) | ([0-9]+{exponent_part}) | ([+-]?[0-9]+{exponent_part}) )[FfLl]?)"
    )
    binary_exponent_part = r"""([pP][+-]?[0-9]+)"""
    hex_fractional_constant = f"((({hex_digits}" + r""")?\.""" + hex_digits + ")|(" + hex_digits + r"""\.))"""
    hex_floating_constant = f"({hex_prefix}({hex_digits}|{hex_fractional_constant}){binary_exponent_part}[FfLl]?)"

    #############################
    # RegEx for parsing strings #
    #############################
    simple_escape = r"""([a-zA-Z._~!=&\^\-\\?'"])"""
    decimal_escape = r"""(\d+)"""
    hex_escape = r"""(x[0-9a-fA-F]+)"""
    escape_sequence = r"""(\\(""" + simple_escape + "|" + decimal_escape + "|" + hex_escape + "))"
    string_char = r"""([^"\\\n]|""" + escape_sequence + ")"
    string_literal = r'("(\\"|[^"])*")|(\'(\\\'|[^\'])*\')'

    ##########################################
    # Regex for parsing comments and newline #
    ##########################################
    newline = r"\n+"
    comment_singleline = r"\/\/.*"
    comment_multiline = r"\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/"

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


from a2lparser.a2l.a2l_yacc import A2LYacc


def test_rules_compu_method():
    """
    Tests parsing a valid "COMPU_METHOD" block.
    """
    compu_method_block = """
    /begin COMPU_METHOD CM_FIXED_SB_06 "LongIdentifier"
        TAB_INTP "%4.3" "UNIT_STRING"
        COEFFS 0 4 8 3 2 5
        COEFFS_LINEAR 1.25 -2.0
        COMPU_TAB_REF TEMP_TAB
        /begin FORMULA
            "sqrt( 3 - 4*sin(X1) )"
            FORMULA_INV "asin( sqrt( (3 - X1)/4 ) )"
        /end FORMULA
        REF_UNIT kms_per_hour
        STATUS_STRING_REF CT_SensorStatus
    /end COMPU_METHOD
    """
    parser = A2LYacc()
    ast = parser.generate_ast(compu_method_block)
    assert ast

    compu_method = ast["COMPU_METHOD"]
    assert compu_method
    assert compu_method["Name"] == "CM_FIXED_SB_06"
    assert compu_method["LongIdentifier"] == '"LongIdentifier"'
    assert compu_method["ConversionType"] == "TAB_INTP"
    assert compu_method["FORMAT"] == '"%4.3"'
    assert compu_method["UNIT"] == '"UNIT_STRING"'
    assert compu_method["COMPU_TAB_REF"] == "TEMP_TAB"
    assert compu_method["REF_UNIT"] == "kms_per_hour"
    assert compu_method["STATUS_STRING_REF"] == "CT_SensorStatus"
    assert compu_method["COEFFS"]["a"] == "0"
    assert compu_method["COEFFS"]["b"] == "4"
    assert compu_method["COEFFS"]["c"] == "8"
    assert compu_method["COEFFS"]["d"] == "3"
    assert compu_method["COEFFS"]["e"] == "2"
    assert compu_method["COEFFS"]["f"] == "5"
    assert compu_method["COEFFS_LINEAR"]["a"] == "1.25"
    assert compu_method["COEFFS_LINEAR"]["b"] == "-2.0"
    assert compu_method["FORMULA"]["f_x"] == '"sqrt( 3 - 4*sin(X1) )"'
    assert compu_method["FORMULA"]["FORMULA_INV"]["g_x"] == '"asin( sqrt( (3 - X1)/4 ) )"'

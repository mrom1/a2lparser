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


def test_rules_unit():
    """
    Tests parsing a valid "UNIT" block.
    """
    unit_block = """
    /begin UNIT kms_per_hour
        "derived unit for velocity: kilometres per hour"
        "[km/h]"
        DERIVED
        REF_UNIT metres_per_second
        UNIT_CONVERSION 3.6 0.0 /* y [km/h] = (60*60/1000) * x [m/s] + 0.0 */
        SI_EXPONENTS 1 2 -2 4 3 -4 -5 /*[N] = [m]*[kg]*[s]-2 */
    /end UNIT
    """
    parser = A2LYacc()
    ast = parser.generate_ast(unit_block)
    assert ast

    unit = ast["UNIT"]
    assert unit
    assert unit["Name"] == "kms_per_hour"
    assert unit["LongIdentifier"] == '"derived unit for velocity: kilometres per hour"'
    assert unit["Display"] == '"[km/h]"'
    assert unit["Type"] == "DERIVED"
    assert unit["REF_UNIT"] == "metres_per_second"

    assert unit["SI_EXPONENTS"]["Length"] == "1"
    assert unit["SI_EXPONENTS"]["Mass"] == "2"
    assert unit["SI_EXPONENTS"]["Time"] == "-2"
    assert unit["SI_EXPONENTS"]["ElectricCurrent"] == "4"
    assert unit["SI_EXPONENTS"]["Temperature"] == "3"
    assert unit["SI_EXPONENTS"]["AmountOfSubstance"] == "-4"
    assert unit["SI_EXPONENTS"]["LuminousIntensity"] == "-5"

    assert unit["UNIT_CONVERSION"]["Gradient"] == "3.6"
    assert unit["UNIT_CONVERSION"]["Offset"] == "0.0"

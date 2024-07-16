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


def test_rules_variant_coding():
    """
    Tests parsing a valid "VARIANT_CODING" block.
    """
    variant_coding_block = """
    /begin VARIANT_CODING
        VAR_SEPARATOR "." /* PUMKF.1 */
        VAR_NAMING NUMERIC /* variant criterion "Car body" with three variants */
        /begin VAR_CRITERION
            Car
            "Car body"
            Limousine Kombi Cabrio
            VAR_MEASUREMENT S_CAR
            VAR_SELECTION_CHARACTERISTIC V_CAR
        /end VAR_CRITERION /* variant criterion "Type of gear box" with two variants */
        /begin VAR_CRITERION
            Gear
            "Type of gear box"
            Manual Automatic
        /end VAR_CRITERION
        /begin VAR_FORBIDDEN_COMB /* forbidden: Limousine-Manual*/
            Car Limousine
            Gear Manual
        /end VAR_FORBIDDEN_COMB
        /begin VAR_FORBIDDEN_COMB /* forbidden: Cabrio-Automatic*/
            Car Cabrio
            Gear Automatic
        /end VAR_FORBIDDEN_COMB
        /begin VAR_CHARACTERISTIC
            PUMKF /*define PUMKF as variant coded*/
            Gear Car /* Gear box variants */
            /begin VAR_ADDRESS
            /end VAR_ADDRESS
        /end VAR_CHARACTERISTIC
        /begin VAR_CHARACTERISTIC
            NLLM /*define NLLM as variant coded */
            Gear Car /*car body and gear box variants*/
            /begin VAR_ADDRESS
                0x8840
                0x8858
                0x8870
                0x8888
            /end VAR_ADDRESS
        /end VAR_CHARACTERISTIC
    /end VARIANT_CODING
    """
    parser = A2LYacc()
    ast = parser.generate_ast(variant_coding_block)
    assert ast

    variant_coding = ast["VARIANT_CODING"]
    assert variant_coding
    assert variant_coding['VAR_NAMING'] == 'NUMERIC'
    assert variant_coding['VAR_SEPARATOR'] == '"."'
    assert variant_coding['VAR_CHARACTERISTIC'][0]['Name'] == 'PUMKF'
    assert variant_coding['VAR_CHARACTERISTIC'][0]['CriterionName'][0] == 'Gear'
    assert variant_coding['VAR_CHARACTERISTIC'][0]['CriterionName'][1] == 'Car'
    assert variant_coding['VAR_CHARACTERISTIC'][1]['Name'] == 'NLLM'
    assert variant_coding['VAR_CHARACTERISTIC'][1]['CriterionName'][0] == 'Gear'
    assert variant_coding['VAR_CHARACTERISTIC'][1]['CriterionName'][1] == 'Car'
    assert variant_coding['VAR_CHARACTERISTIC'][1]['VAR_ADDRESS']['Address'][0] == '0x8840'
    assert variant_coding['VAR_CHARACTERISTIC'][1]['VAR_ADDRESS']['Address'][1] == '0x8858'
    assert variant_coding['VAR_CHARACTERISTIC'][1]['VAR_ADDRESS']['Address'][2] == '0x8870'
    assert variant_coding['VAR_CHARACTERISTIC'][1]['VAR_ADDRESS']['Address'][3] == '0x8888'
    assert variant_coding['VAR_CRITERION'][0]['Name'] == 'Car'
    assert variant_coding['VAR_CRITERION'][0]['LongIdentifier'] == '"Car body"'
    assert variant_coding['VAR_CRITERION'][0]['VALUE'][0] == 'Limousine'
    assert variant_coding['VAR_CRITERION'][0]['VALUE'][1] == 'Kombi'
    assert variant_coding['VAR_CRITERION'][0]['VALUE'][2] == 'Cabrio'
    assert variant_coding['VAR_CRITERION'][0]['VAR_MEASUREMENT'] == 'S_CAR'
    assert variant_coding['VAR_CRITERION'][0]['VAR_SELECTION_CHARACTERISTIC'] == 'V_CAR'
    assert variant_coding['VAR_CRITERION'][1]['Name'] == 'Gear'
    assert variant_coding['VAR_CRITERION'][1]['LongIdentifier'] == '"Type of gear box"'
    assert variant_coding['VAR_CRITERION'][1]['VALUE'][0] == 'Manual'
    assert variant_coding['VAR_CRITERION'][1]['VALUE'][1] == 'Automatic'
    assert variant_coding['VAR_FORBIDDEN_COMB'][0]['CriterionList'][0][0] == 'Car'
    assert variant_coding['VAR_FORBIDDEN_COMB'][0]['CriterionList'][0][1] == 'Limousine'
    assert variant_coding['VAR_FORBIDDEN_COMB'][0]['CriterionList'][1][0] == 'Gear'
    assert variant_coding['VAR_FORBIDDEN_COMB'][0]['CriterionList'][1][1] == 'Manual'
    assert variant_coding['VAR_FORBIDDEN_COMB'][1]['CriterionList'][0][0] == 'Car'
    assert variant_coding['VAR_FORBIDDEN_COMB'][1]['CriterionList'][0][1] == 'Cabrio'
    assert variant_coding['VAR_FORBIDDEN_COMB'][1]['CriterionList'][1][0] == 'Gear'
    assert variant_coding['VAR_FORBIDDEN_COMB'][1]['CriterionList'][1][1] == 'Automatic'

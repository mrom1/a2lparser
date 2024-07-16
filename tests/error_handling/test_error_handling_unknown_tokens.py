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


def test_error_handling_unknown_tokens_pre():
    """
    Test for error handling of unknown tokens at the beginning of the grammar stack.
    """
    erroneous_input = """
    /begin MODULE ERROR_MODULE
        "Error Module for testing"
        /BEGIN UKNOWN_ERROR_SECTION_TOKEN
            /* ! This section ends should trigger an error and not be parsed ! */
            "erroneous section which does not exist in A2L grammar"
        /END UKNOWN_ERROR_SECTION_TOKEN

        /begin INSTANCE TEST_INSTANCE
            /* This is a valid INSTANCE section and should be parsed. */
            ""
            REF_TYPE_DEF_TEST
            0xEECCDD00
        /end INSTANCE
    /end MODULE
    """
    parser = A2LYacc()
    ast = parser.generate_ast(erroneous_input)
    assert ast

    module = ast["MODULE"]
    assert module
    assert module["Name"] == "ERROR_MODULE"
    assert module["LongIdentifier"] == '"Error Module for testing"'
    assert module["INSTANCE"]["Name"] == "TEST_INSTANCE"
    assert module["INSTANCE"]["LongIdentifier"] == '""'
    assert module["INSTANCE"]["TypedefName"] == "REF_TYPE_DEF_TEST"
    assert module["INSTANCE"]["Address"] == "0xEECCDD00"


def test_error_handling_unknown_tokens_post():
    """
    Test for error handling of unknown tokens at the end of the grammar stack.
    """
    erroneous_input = """
    /begin MODULE ERROR_MODULE
        "Error Module for testing"

        /begin INSTANCE TEST_INSTANCE
            /* This is a valid INSTANCE section and should be parsed. */
            ""
            REF_TYPE_DEF_TEST
            0xEECCDD00
        /end INSTANCE

        /BEGIN UKNOWN_ERROR_SECTION_TOKEN
            /* ! This section ends should trigger an error and not be parsed ! */
            "erroneous section which does not exist in A2L grammar"
        /END UKNOWN_ERROR_SECTION_TOKEN

        /begin IF_DATA ISO SND
            0x10
            0x00
            0x05
            0x08
            RCV
            4
            long
        /end IF_DATA

        /BEGIN UKNOWN_ERROR_SECTION_TOKEN
            /* ! This section ends should trigger an error and not be parsed ! */
            "erroneous section which does not exist in A2L grammar"
        /END UKNOWN_ERROR_SECTION_TOKEN

        /begin FRAME TEST_FRAME
            "Frame Test"
            2 3
        /end FRAME

        /BEGIN UKNOWN_ERROR_SECTION_TOKEN
            /* ! This section ends should trigger an error and not be parsed ! */
            "erroneous section which does not exist in A2L grammar"
        /END UKNOWN_ERROR_SECTION_TOKEN

    /end MODULE
    """
    parser = A2LYacc()
    ast = parser.generate_ast(erroneous_input)
    assert ast

    module = ast["MODULE"]
    assert module
    assert module["Name"] == "ERROR_MODULE"
    assert module["LongIdentifier"] == '"Error Module for testing"'
    assert module["INSTANCE"]["Name"] == "TEST_INSTANCE"
    assert module["INSTANCE"]["LongIdentifier"] == '""'
    assert module["INSTANCE"]["TypedefName"] == "REF_TYPE_DEF_TEST"
    assert module["INSTANCE"]["Address"] == "0xEECCDD00"
    assert module["FRAME"]["Name"] == "TEST_FRAME"
    assert module["FRAME"]["LongIdentifier"] == '"Frame Test"'
    assert module["FRAME"]["ScalingUnit"] == "2"
    assert module["FRAME"]["Rate"] == "3"
    assert module["IF_DATA"]["Name"] == "ISO"
    assert module["IF_DATA"]["DataParams"] == ['SND', '0x10', '0x00', '0x05', '0x08', 'RCV', '4', 'long']

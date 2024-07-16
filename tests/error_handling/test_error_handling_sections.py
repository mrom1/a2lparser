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


def test_error_handling_measurement_subsection_error():
    """
    Tests if an erroneous measurement subsection is handled correctly.
    """
    erroneous_input = """
    /begin MEASUREMENT N /* name */
        "Engine speed" /* long identifier */
        UWORD /* datatype */
        R_SPEED_3 /* conversion */
        1 /* resolution */
        0 /* accuracy */
        120.0 /* lower limit */
        8400.0 /* upper limit */
        PHYS_UNIT "mph"
        BIT_MASK 0x0FFF
        BYTE_ORDER MSB_FIRST
        REF_MEMORY_SEGMENT Data2
        /begin IF_DATA ISO SND
            0x10
            0x00
            0x05
            0x08
            RCV
            4
            long
        /end IF_DATA
        /begin ANNOTATION
            ANNOTATION_LABEL "annotation test label"
            /begin ANNOTATION_TEXT
                "annotation text example"
            /end ANNOTATION_TEXT
            ANNOTATION_LABEL 0x00EE00FF     /* WILL PROVOKE AN ERROR */
        /end ANNOTATION
        /begin FUNCTION_LIST ID_ADJUSTM
            FL_ADJUSTM
        /end FUNCTION_LIST
    /end MEASUREMENT
    """
    parser = A2LYacc()
    ast = parser.generate_ast(erroneous_input)
    assert ast

    measurement = ast["MEASUREMENT"]
    assert measurement
    assert measurement["Name"] == "N"
    assert measurement["LongIdentifier"] == '"Engine speed"'
    assert measurement["Datatype"] == "UWORD"
    assert measurement["CONVERSION"] == "R_SPEED_3"
    assert measurement["Resolution"] == "1"
    assert measurement["Accuracy"] == "0"
    assert measurement["LowerLimit"] == "120.0"
    assert measurement["UpperLimit"] == "8400.0"
    assert measurement["BIT_MASK"] == "0x0FFF"
    assert measurement["BYTE_ORDER"] == "MSB_FIRST"
    assert measurement["REF_MEMORY_SEGMENT"] == "Data2"
    assert measurement["PHYS_UNIT"] == '"mph"'
    assert measurement["FUNCTION_LIST"] == {'Name': ['ID_ADJUSTM', 'FL_ADJUSTM']}
    assert measurement["IF_DATA"] == {'Name': 'ISO',
                                      'DataParams': ['SND', '0x10', '0x00', '0x05', '0x08', 'RCV', '4', 'long']}
    assert measurement["ANNOTATION"]["ANNOTATION_LABEL"] == '"annotation test label"'
    assert measurement["ANNOTATION"]["ANNOTATION_TEXT"] == ['"annotation text example"']


def test_error_handling_measurement_subsection_nested_error():
    """
    This tests aims to check that an error can occur in a nested section.
    Expected behavior is for the error handling to allow all valid parts.
    """
    erroneous_input = """
    /begin MEASUREMENT
        N /* name */
        "Engine speed" /* long identifier */
        UWORD /* datatype */
        R_SPEED_3 /* conversion */
        2 /* resolution */
        2.5 /* accuracy */
        120.0 /* lower limit */
        8400.0 /* upper limit */
        /begin ANNOTATION
            ANNOTATION_LABEL "first valid label"
            /begin ANNOTATION_TEXT
                "first valid annotation text"
            /end ANNOTATION_TEXT
            ANNOTATION_ORIGIN "first valid annotation origin"
        /end ANNOTATION
        /begin ANNOTATION
            ANNOTATION_LABEL "label inside erroneous section"
            /begin ANNOTATION_TEXT
                0xee00ee00              /* ! ERROR PROVOKING TOKEN ! */
            /end ANNOTATION_TEXT
            ANNOTATION_ORIGIN "origin inside erroneous section"
        /end ANNOTATION
        /begin ANNOTATION
            ANNOTATION_LABEL "second valid label"
            /begin ANNOTATION_TEXT
                "second valid annotation text"
            /end ANNOTATION_TEXT
            ANNOTATION_ORIGIN "second valid annotation origin"
        /end ANNOTATION
        /begin FUNCTION_LIST
            ID_ADJUSTX  /* Valid function name */
            ID_ADJUSTY  /* Valid function name */
        /end FUNCTION_LIST
    /end MEASUREMENT
    """
    parser = A2LYacc()
    ast = parser.generate_ast(erroneous_input)
    assert ast

    measurement = ast["MEASUREMENT"]
    assert measurement
    assert measurement["Name"] == "N"
    assert measurement["LongIdentifier"] == '"Engine speed"'
    assert measurement["Datatype"] == "UWORD"
    assert measurement["CONVERSION"] == "R_SPEED_3"
    assert measurement["Resolution"] == "2"
    assert measurement["Accuracy"] == "2.5"
    assert measurement["LowerLimit"] == "120.0"
    assert measurement["UpperLimit"] == "8400.0"
    assert measurement["FUNCTION_LIST"] == {"Name": ["ID_ADJUSTX", "ID_ADJUSTY"]}

    assert len(measurement["ANNOTATION"]) == 3
    assert measurement["ANNOTATION"][0]["ANNOTATION_LABEL"] == '"first valid label"'
    assert measurement["ANNOTATION"][0]["ANNOTATION_TEXT"] == ['"first valid annotation text"']
    assert measurement["ANNOTATION"][0]["ANNOTATION_ORIGIN"] == '"first valid annotation origin"'
    assert measurement["ANNOTATION"][1]["ANNOTATION_LABEL"] == '"label inside erroneous section"'
    assert measurement["ANNOTATION"][1]["ANNOTATION_ORIGIN"] == '"origin inside erroneous section"'
    assert measurement["ANNOTATION"][2]["ANNOTATION_LABEL"] == '"second valid label"'
    assert measurement["ANNOTATION"][2]["ANNOTATION_TEXT"] == ['"second valid annotation text"']
    assert measurement["ANNOTATION"][2]["ANNOTATION_ORIGIN"] == '"second valid annotation origin"'

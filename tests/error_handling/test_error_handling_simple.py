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


def test_error_handling_pre_type():
    """
    Tests an error invoking out of place string literal.
    Expected behaviour is to verify that the correct parts are parsed.

    Structure:
        [keyword] error
        [valid keyword]
    """
    erroneous_input = """
    "some error invoking string out of place"
    A2ML_VERSION 1 61 /* Version 1.6.1 */
    """
    parser = A2LYacc()
    ast = parser.generate_ast(erroneous_input)
    assert ast

    a2ml_version = ast["A2ML_VERSION"]
    assert a2ml_version
    assert a2ml_version["VersionNo"] == "1"
    assert a2ml_version["UpgradeNo"] == "61"


def test_error_handling_pre_section():
    """
    Tests an error invoking out of place string literal.
    Expected behaviour is to verify that the correct parts are parsed.

    Structure:
        [keyword] error
        [correct section]
    """
    erroneous_input = """
    "some error invoking string out of place"
    /begin ANNOTATION
        ANNOTATION_LABEL "annotation test label"
        /begin ANNOTATION_TEXT
            "annotation text example"
        /end ANNOTATION_TEXT
        ANNOTATION_ORIGIN "annotation test origin"
    /end ANNOTATION
    """
    parser = A2LYacc()
    ast = parser.generate_ast(erroneous_input)
    assert ast

    annotation = ast["ANNOTATION"]
    assert annotation
    assert annotation["ANNOTATION_LABEL"] == '"annotation test label"'
    assert annotation["ANNOTATION_TEXT"] == ['"annotation text example"']
    assert annotation["ANNOTATION_ORIGIN"] == '"annotation test origin"'


def test_error_handling_post_type():  # sourcery skip: extract-duplicate-method
    """
    Tests an error invoking out of place string literal.
    Expected behaviour is to verify that the correct parts are parsed.

    Structure:
        [correct keyword]
        [keyword] error
        [correct keyword]
    """
    erroneous_input = """
    A2ML_VERSION 1 31 /* Version 1.3.1 */
    "some error invoking string out of place"
    ASAP2_VERSION 2 34
    """
    parser = A2LYacc()
    ast = parser.generate_ast(erroneous_input)
    assert ast

    a2ml_version = ast["A2ML_VERSION"]
    assert a2ml_version
    assert a2ml_version["VersionNo"] == "1"
    assert a2ml_version["UpgradeNo"] == "31"

    asap2_version = ast["ASAP2_VERSION"]
    assert asap2_version
    assert asap2_version["VersionNo"] == "2"
    assert asap2_version["UpgradeNo"] == "34"


def test_error_handling_post_section():
    """
    Tests an error invoking out of place string literal.
    Expected behaviour is to verify that the correct parts are parsed.

    Structure:
        [valid keyword]
        [valid section]
        [keyword] error
        [valid section]
    """
    erroneous_input = """
    A2ML_VERSION 1 61 /* Version 1.6.1 */
    /begin ANNOTATION
        ANNOTATION_LABEL "first annotation test label"
        /begin ANNOTATION_TEXT
            "first annotation text example"
        /end ANNOTATION_TEXT
        ANNOTATION_ORIGIN "first annotation test origin"
    /end ANNOTATION
    "some error invoking string out of place"
    /begin ANNOTATION
        ANNOTATION_LABEL "second annotation test label"
        /begin ANNOTATION_TEXT
            "second annotation text example"
        /end ANNOTATION_TEXT
        ANNOTATION_ORIGIN "second annotation test origin"
    /end ANNOTATION
    """
    parser = A2LYacc()
    ast = parser.generate_ast(erroneous_input)
    assert ast

    a2ml_version = ast["A2ML_VERSION"]
    assert a2ml_version
    assert a2ml_version["VersionNo"] == "1"
    assert a2ml_version["UpgradeNo"] == "61"

    annotation_1 = ast["ANNOTATION"][0]
    assert annotation_1
    assert annotation_1["ANNOTATION_LABEL"] == '"first annotation test label"'
    assert annotation_1["ANNOTATION_TEXT"] == ['"first annotation text example"']
    assert annotation_1["ANNOTATION_ORIGIN"] == '"first annotation test origin"'

    annotation_2 = ast["ANNOTATION"][1]
    assert annotation_2
    assert annotation_2["ANNOTATION_LABEL"] == '"second annotation test label"'
    assert annotation_2["ANNOTATION_TEXT"] == ['"second annotation text example"']
    assert annotation_2["ANNOTATION_ORIGIN"] == '"second annotation test origin"'

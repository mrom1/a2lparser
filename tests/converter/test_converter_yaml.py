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


import yaml
from a2lparser.a2l.a2l_yacc import A2LYacc
from a2lparser.converter.yaml_converter import YAMLConverter


def test_converter_yaml_multiple_root_entries():
    """
    Tests converting a dictionary with multiple root entries which are not A2L keywords.
    """
    ast_dict = {"root1.a2l": {"key1": "value1"}, "root2.a2l": {"key2": "value2"}}
    converted_yaml_list = YAMLConverter().convert_to_string(ast_dict)
    assert converted_yaml_list
    assert len(converted_yaml_list) == 2

    root1_filename, root1_yaml = converted_yaml_list[0]
    root1_parsed_yaml = yaml.safe_load(root1_yaml)
    assert root1_filename == "root1.yml"
    assert root1_parsed_yaml["A2L-File"]["key1"] == "value1"

    root2_filename, root2_yaml = converted_yaml_list[1]
    root2_parsed_yaml = yaml.safe_load(root2_yaml)
    assert root2_filename == "root2.yml"
    assert root2_parsed_yaml["A2L-File"]["key2"] == "value2"


def test_converter_yaml_single_measurement_entry():
    """
    Tests converting an abstract syntax tree to an yaml file.
    """
    measurement_block = """
    /begin MEASUREMENT xxx4b4b52c91215c8.xc33258c9abefff4284.x87f0.x871bxxx "ex1"
        SWORD NO_FORMULA 0 0 -32768 32767
        BIT_MASK 0xFFFF
        BYTE_ORDER MSB_FIRST
        ECU_ADDRESS 0x2DDDD
        ECU_ADDRESS_EXTENSION 0x0
        FORMAT "%.3"
        DISCRETE
        /begin IF_DATA CANAPE_EXT
            100
            LINK_MAP "xxx79c13e523bc16dfbba3285.x794ec36d9751f96100" 0x2D474 0x0 0 0x0 1 0xCF 0x0
            DISPLAY 0 -36044.75 36043.75
        /end IF_DATA
        /begin IF_DATA CANAPE
            DISPLAY 0 -36044.75 36043.75
        /end IF_DATA
        ERROR_MASK 0x00000001
        LAYOUT ALTERNATE_WITH_Y
        MATRIX_DIM 2 4 3
        MAX_REFRESH 998 2
        PHYS_UNIT "Nm"
        READ_WRITE
        REF_MEMORY_SEGMENT Data1
        /begin ANNOTATION
            ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_1"
            ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_1"
        /end ANNOTATION
        /begin ANNOTATION
            ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_2"
            ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_2"
        /end ANNOTATION
        /begin VIRTUAL
            PHI_BASIS
            PHI_CORR
        /end VIRTUAL
        SYMBOL_LINK
            "_VehicleSpeed" /* Symbol name */
            0 /* Offset */
    /end MEASUREMENT
    """
    ast = A2LYacc().generate_ast(measurement_block)
    assert ast
    yaml_measurement = YAMLConverter().convert_to_string(
        ast.get_dict(), output_filename="measurement"
    )
    assert yaml_measurement

    yaml_measurement_filename, yaml_measurement_root = yaml_measurement[0]
    assert yaml_measurement_filename == "measurement.yml"
    parsed_yaml_dict = yaml.safe_load(yaml_measurement_root)
    assert parsed_yaml_dict
    yaml_measurement_parsed = parsed_yaml_dict["A2L-File"]["MEASUREMENT"]
    ast_measurement = ast["MEASUREMENT"]
    assert ast_measurement
    assert yaml_measurement_parsed

    assert ast_measurement["Name"] == yaml_measurement_parsed["Name"]
    assert ast_measurement["LongIdentifier"] == yaml_measurement_parsed["LongIdentifier"]
    assert ast_measurement["Datatype"] == yaml_measurement_parsed["Datatype"]
    assert ast_measurement["CONVERSION"] == yaml_measurement_parsed["CONVERSION"]
    assert ast_measurement["Resolution"] == yaml_measurement_parsed["Resolution"]
    assert ast_measurement["Accuracy"] == yaml_measurement_parsed["Accuracy"]
    assert ast_measurement["LowerLimit"] == yaml_measurement_parsed["LowerLimit"]
    assert ast_measurement["UpperLimit"] == yaml_measurement_parsed["UpperLimit"]
    assert ast_measurement["BIT_MASK"] == yaml_measurement_parsed["BIT_MASK"]
    assert ast_measurement["BYTE_ORDER"] == yaml_measurement_parsed["BYTE_ORDER"]
    assert (
        str(ast_measurement["DISCRETE"]).lower() == str(yaml_measurement_parsed["DISCRETE"]).lower()
    )
    assert ast_measurement["ECU_ADDRESS"] == yaml_measurement_parsed["ECU_ADDRESS"]
    assert (
        ast_measurement["ECU_ADDRESS_EXTENSION"] == yaml_measurement_parsed["ECU_ADDRESS_EXTENSION"]
    )
    assert ast_measurement["ERROR_MASK"] == yaml_measurement_parsed["ERROR_MASK"]
    assert ast_measurement["FORMAT"] == yaml_measurement_parsed["FORMAT"]
    assert ast_measurement["LAYOUT"] == yaml_measurement_parsed["LAYOUT"]
    assert ast_measurement["PHYS_UNIT"] == yaml_measurement_parsed["PHYS_UNIT"]
    assert (
        str(ast_measurement["READ_WRITE"]).lower()
        == str(yaml_measurement_parsed["READ_WRITE"]).lower()
    )
    assert ast_measurement["REF_MEMORY_SEGMENT"] == yaml_measurement_parsed["REF_MEMORY_SEGMENT"]
    assert ast_measurement["MAX_REFRESH"] == yaml_measurement_parsed["MAX_REFRESH"]
    assert ast_measurement["SYMBOL_LINK"] == yaml_measurement_parsed["SYMBOL_LINK"]
    assert ast_measurement["VIRTUAL"] == yaml_measurement_parsed["VIRTUAL"]
    assert ast_measurement["ANNOTATION"] == yaml_measurement_parsed["ANNOTATION"]
    assert ast_measurement["IF_DATA"] == yaml_measurement_parsed["IF_DATA"]

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


import os
import tempfile
import pytest
from a2lparser import A2L_PACKAGE_DIR
from a2lparser.a2lparser import A2LParser


@pytest.fixture
def a2l_content_sections_tuple() -> tuple:
    """
    Returns a tuple of A2L content sections for testing the include mechanism.

    Returns:
        tuple: (project, module, header, characteristic, measurement, if_data)
    """
    project = """
    /begin PROJECT My_Project ""
        /include My_Header.a2l
        /include "my_modules/My_Module.a2l"
    /end PROJECT
    """
    module = """
    /begin MODULE
        /include "my_characteristics/My_Characteristic.a2l"
        /include "my_measurements/My_Measurement.a2l"
    /end MODULE
    """
    header = '/begin HEADER "Test Project for include mechanism" "T_P1" TP1 /end HEADER'
    characteristic = (
        '/begin CHARACTERISTIC NAME "" MAP 0x7140 DAMOS_KF 10.0 R_VOLTAGE 0.0 15.0'
        "/end CHARACTERISTIC"
    )
    measurement = """
    /begin MEASUREMENT N ""
        UWORD R_VOLTAGE 1 0 0.0 100.0
        /include "../my_if_data/XCP_ref.a2l"
    /end MEASUREMENT
    """
    if_data = "/begin IF_DATA XCP LINK_MAP ref_name 0x003432 /end IF_DATA"
    return (project, module, header, characteristic, measurement, if_data)


def test_parser_load_file_simple(create_file, a2l_content_sections_tuple):
    """
    Tests loading files containing include tags.
    """
    # Test files content
    _, _, _, _, measurement, if_data = a2l_content_sections_tuple

    # Expected output
    expected_content = """
    /begin MEASUREMENT N ""
        UWORD R_VOLTAGE 1 0 0.0 100.0
        /begin IF_DATA XCP LINK_MAP ref_name 0x003432 /end IF_DATA
    /end MEASUREMENT
    """

    # Path for temporary directory and files
    temp_test_output_path = A2L_PACKAGE_DIR / "../testfiles"
    temp_test_dir_prefix = "temp_dir_output_"

    # Parser object
    parser = A2LParser()

    # Create temporary directory and files
    with tempfile.TemporaryDirectory(
        dir=temp_test_output_path, prefix=temp_test_dir_prefix
    ) as tempdir:
        my_measurements_dir = os.path.join(tempdir, "my_measurements")
        os.makedirs(my_measurements_dir)
        measurement_file = create_file(my_measurements_dir, "My_Measurement.a2l", measurement)
        assert os.path.exists(measurement_file)

        my_if_data_dir = os.path.join(tempdir, "my_if_data")
        os.makedirs(my_if_data_dir)
        if_data_file = create_file(my_if_data_dir, "XCP_ref.a2l", if_data)
        assert os.path.exists(if_data_file)

        content = parser._load_file(measurement_file)
        assert content
        assert content == expected_content


def test_parser_load_file_complex(create_file, a2l_content_sections_tuple):
    """
    Tests loading files recursively containing include tags.

    Include Structure:
    My_Project.a2l -> My_Module.a2l -> My_Characteristic.a2l & My_Measurement.a2l
    """
    # Test files content
    (my_project, my_module, my_header, my_characteristic, my_measurement, my_if_data) = (
        a2l_content_sections_tuple
    )

    # Expected content after includes
    expected_content = (
        """
    /begin PROJECT My_Project ""
        /begin HEADER "Test Project for include mechanism" "T_P1" TP1 /end HEADER
        /begin MODULE
            /begin CHARACTERISTIC NAME "" MAP 0x7140 DAMOS_KF 10.0 R_VOLTAGE 0.0 15.0
            /end CHARACTERISTIC
            /begin MEASUREMENT N ""
                UWORD R_VOLTAGE 1 0 0.0 100.0
                /begin IF_DATA XCP LINK_MAP ref_name 0x003432 /end IF_DATA
            /end MEASUREMENT
        /end MODULE
    /end PROJECT
    """.replace(
            "  ", ""
        )
        .replace("\n", "")
        .replace("\t", "")
    )

    # Path for temporary directory and files
    temp_test_output_path = A2L_PACKAGE_DIR / "../testfiles"
    temp_test_dir_prefix = "temp_dir_output_"

    # Parser object
    parser = A2LParser()

    # Create temporary directory and files
    with tempfile.TemporaryDirectory(
        dir=temp_test_output_path, prefix=temp_test_dir_prefix
    ) as tempdir:
        project_file = create_file(tempdir, "My_Project.a2l", my_project)
        header_file = create_file(tempdir, "My_Header.a2l", my_header)
        assert os.path.exists(project_file)
        assert os.path.exists(header_file)

        my_modules_dir = os.path.join(tempdir, "my_modules")
        os.makedirs(my_modules_dir)
        module_file = create_file(my_modules_dir, "My_Module.a2l", my_module)
        assert os.path.exists(module_file)

        my_characteristics_dir = os.path.join(my_modules_dir, "my_characteristics")
        os.makedirs(my_characteristics_dir)
        characteristic_file = create_file(
            my_characteristics_dir, "My_Characteristic.a2l", my_characteristic
        )
        assert os.path.exists(characteristic_file)

        my_measurements_dir = os.path.join(my_modules_dir, "my_measurements")
        os.makedirs(my_measurements_dir)
        measurement_file = create_file(my_measurements_dir, "My_Measurement.a2l", my_measurement)
        assert os.path.exists(measurement_file)

        my_if_data_dir = os.path.join(my_modules_dir, "my_if_data")
        os.makedirs(my_if_data_dir)
        if_data_file = create_file(my_if_data_dir, "XCP_ref.a2l", my_if_data)
        assert os.path.exists(if_data_file)

        content = parser._load_file(project_file)
        content_cleaned = content.replace("  ", "").replace("\n", "").replace("\t", "")
        assert content_cleaned == expected_content

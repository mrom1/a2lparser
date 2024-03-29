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


import unittest
from a2lparser.unittests.units import *
from a2lparser.unittests.testhandler import Testhandler


class Testsuite():
    def __init__(self, parser, debug=0, optimize=0, gen_tables=0, xml_output_file=None):
        self.parser = parser
        self.ast_node_counter = 0


        suite = unittest.TestSuite()

        suite.addTest(Testhandler.parametrize(test_annotation.TestAnnotation, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_axis_descr.TestAxisDescr, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_axis_pts.TestAxisPts, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_bit_operation.TestBitOperation, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_calibration_handle.TestCalibrationHandle, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_calibration_method.TestCalibrationMethod, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_characteristic.TestCharacteristic, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_compu_method.TestCompuMethod, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_compu_tab.TestCompuTab, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_compu_vtab.TestCompuVtab, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_compu_vtab_range.TestCompuVtabRange, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_encoding.TestEncoding, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_frame.TestFrame, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_function.TestFunction, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_function_list.TestFunctionList, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_group.TestGroup, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_header.TestHeader, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_if_data.TestIfData, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_logger.TestLogger, param=None))
        suite.addTest(Testhandler.parametrize(test_measurement.TestMeasurement, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_memory_layout.TestMemoryLayout, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_memory_segment.TestMemorySegment, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_mod_common.TestModCommon, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_mod_par.TestModPar, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_module.TestModule, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_record_layout.TestRecordLayout, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_string_handling.TestStringHandling, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_unit.TestUnit, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_user_rights.TestUserRights, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_var_characteristic.TestVarCharacteristic, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_var_criterion.TestVarCriterion, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_var_forbidden_comb.TestVarForbiddenComb, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_variant_coding.TestVariantCoding, param=self.parser))
        suite.addTest(Testhandler.parametrize(test_xml_escape.TestXmlEscape, param=self.parser))

        unittest.TextTestRunner(verbosity=2).run(suite)

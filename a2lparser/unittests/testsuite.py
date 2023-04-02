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
from a2lparser.a2l.parser import Parser
from a2lparser.unittests.testhandler import Testhandler
from a2lparser.unittests.units.test_annotation import TestAnnotation
from a2lparser.unittests.units.test_axis_descr import TestAxisDescr
from a2lparser.unittests.units.test_axis_pts import TestAxisPts
from a2lparser.unittests.units.test_bit_operation import TestBitOperation
from a2lparser.unittests.units.test_calibration_handle import TestCalibrationHandle
from a2lparser.unittests.units.test_calibration_method import TestCalibrationMethod
from a2lparser.unittests.units.test_characteristic import TestCharacteristic
from a2lparser.unittests.units.test_compu_method import TestCompuMethod
from a2lparser.unittests.units.test_compu_tab import TestCompuTab
from a2lparser.unittests.units.test_compu_vtab import TestCompuVtab
from a2lparser.unittests.units.test_compu_vtab_range import TestCompuVtabRange
from a2lparser.unittests.units.test_encoding import TestEncoding
from a2lparser.unittests.units.test_frame import TestFrame
from a2lparser.unittests.units.test_function import TestFunction
from a2lparser.unittests.units.test_function_list import TestFunctionList
from a2lparser.unittests.units.test_group import TestGroup
from a2lparser.unittests.units.test_header import TestHeader
from a2lparser.unittests.units.test_if_data import TestIfData
from a2lparser.unittests.units.test_measurement import TestMeasurement
from a2lparser.unittests.units.test_memory_layout import TestMemoryLayout
from a2lparser.unittests.units.test_memory_segment import TestMemorySegment
from a2lparser.unittests.units.test_mod_common import TestModCommon
from a2lparser.unittests.units.test_mod_par import TestModPar
from a2lparser.unittests.units.test_module import TestModule
from a2lparser.unittests.units.test_record_layout import TestRecordLayout
from a2lparser.unittests.units.test_string_handling import TestStringHandling
from a2lparser.unittests.units.test_unit import TestUnit
from a2lparser.unittests.units.test_user_rights import TestUserRights
from a2lparser.unittests.units.test_var_characteristic import TestVarCharacteristic
from a2lparser.unittests.units.test_var_criterion import TestVarCriterion
from a2lparser.unittests.units.test_var_forbidden_comb import TestVarForbiddenComb
from a2lparser.unittests.units.test_variant_coding import TestVariantCoding


class Testsuite:
    """
    Test suite for testing the A2L units.

    Usage:
        >>> parser = Parser()
        >>> suite = Testsuite(parser)
        >>> suite.run()
    """

    def __init__(self, parser: Parser) -> None:
        """
        Testsuite Constructor.
        Will automatically add the unit tests to the test suite.

        Args:
            - parser: Initialized Parser object.
        """
        self.parser = parser
        self.ast_node_counter = 0

        suite = unittest.TestSuite()
        suite.addTest(Testhandler.parametrize(TestAnnotation, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestAxisDescr, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestAxisPts, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestBitOperation, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestCalibrationHandle, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestCalibrationMethod, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestCharacteristic, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestCompuMethod, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestCompuTab, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestCompuVtab, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestCompuVtabRange, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestEncoding, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestFrame, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestFunction, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestFunctionList, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestGroup, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestHeader, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestIfData, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestMeasurement, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestMemoryLayout, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestMemorySegment, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestModCommon, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestModPar, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestModule, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestRecordLayout, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestStringHandling, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestUnit, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestUserRights, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestVarCharacteristic, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestVarCriterion, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestVarForbiddenComb, param=self.parser))
        suite.addTest(Testhandler.parametrize(TestVariantCoding, param=self.parser))
        self.suite = suite

    def run(self, verbosity: int = 2) -> None:
        """
        Runs the registered unit tests.

        Args:
            - verbosity: Integer value for verbosity level.
        """
        unittest.TextTestRunner(verbosity=verbosity).run(self.suite)

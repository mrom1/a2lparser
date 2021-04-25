import unittest

from tests.testcases import *
from tests.testhandler import Testhandler

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

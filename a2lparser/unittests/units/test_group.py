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


from a2lparser.unittests.testhandler import Testhandler


_TEST_GROUP_BLOCK = """
/begin GROUP
	CUSTBSW
	"Subsystem"
	ROOT
	/begin ANNOTATION
        ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_1"
        ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_1"
        /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_1"
        /end ANNOTATION_TEXT
    /end ANNOTATION
    /begin ANNOTATION
		ANNOTATION_LABEL "ANNOTATION_LABEL_BLOCK_2"
        ANNOTATION_ORIGIN "ANNOTATION_ORIGIN_BLOCK_2"
        /begin ANNOTATION_TEXT "ANNOTATION_TEXT_BLOCK_2"
        /end ANNOTATION_TEXT
	/end ANNOTATION
	/begin SUB_GROUP
		AAS
		LRG
		Sar
	/end SUB_GROUP
	/begin REF_MEASUREMENT
		CustBsw_Init_Current_Loop
		CustBsw_Init_Previous_Loop
	/end REF_MEASUREMENT
	/begin REF_CHARACTERISTIC
		ENG_SPEED_CORR_CURVE
		XAS_ENG_SPEED_CORR_CURVE
	/end REF_CHARACTERISTIC
	/begin FUNCTION_LIST
		ID_ADJUSTM
		FL_ADJUSTM
		SPEED_LIM
	/end FUNCTION_LIST
/end GROUP
"""

_TEST_GROUP_BLOCK_EMPTY = """
/begin GROUP
	/begin ANNOTATION
		/begin ANNOTATION_TEXT
		/end ANNOTATION_TEXT
	/end ANNOTATION
	/begin SUB_GROUP
	/end SUB_GROUP
	/begin REF_MEASUREMENT
	/end REF_MEASUREMENT
	/begin REF_CHARACTERISTIC
	/end REF_CHARACTERISTIC
	/begin FUNCTION_LIST
	/end FUNCTION_LIST
/end GROUP
"""


class TestGroup(Testhandler):
    def test_group_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_group_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_GROUP_BLOCK,
                      filelength=_TEST_GROUP_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//GroupName').text, "CUSTBSW")
        self.assertEqual(tree.find('.//GroupLongIdentifier').text, "Subsystem")

        self.assertEqual(tree.find('.//Function_List/Name').text, "ID_ADJUSTM, FL_ADJUSTM, SPEED_LIM")
        self.assertEqual(tree.find('.//Sub_Group/Identifier').text, "AAS, LRG, Sar")
        self.assertEqual(tree.find('.//Root').text, "True")

        ref_characteristic = tree.find('.//Ref_Characteristic')
        self.assertEqual(len(ref_characteristic), 2)
        self.assertEqual(ref_characteristic[0].get('characteristicId'), "ENG_SPEED_CORR_CURVE")
        self.assertEqual(ref_characteristic[1].get('characteristicId'), "XAS_ENG_SPEED_CORR_CURVE")

        ref_measurement = tree.find('.//Ref_Measurement')
        self.assertEqual(len(ref_measurement), 2)
        self.assertEqual(ref_measurement[0].get('signalMeasurementId'), "CustBsw_Init_Current_Loop")
        self.assertEqual(ref_measurement[1].get('signalMeasurementId'), "CustBsw_Init_Previous_Loop")

        annotation = tree.findall('.//Annotation')
        self.assertEqual(len(annotation), 2)
        self.assertEqual(annotation[0].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_BLOCK_1")
        self.assertEqual(annotation[0].find('.//Annotation_Label').text, "ANNOTATION_LABEL_BLOCK_1")
        self.assertEqual(annotation[0].find('.//Annotation_Text').text, "ANNOTATION_TEXT_BLOCK_1")
        self.assertEqual(annotation[1].find('.//Annotation_Origin').text, "ANNOTATION_ORIGIN_BLOCK_2")
        self.assertEqual(annotation[1].find('.//Annotation_Label').text, "ANNOTATION_LABEL_BLOCK_2")
        self.assertEqual(annotation[1].find('.//Annotation_Text').text, "ANNOTATION_TEXT_BLOCK_2")

        # ToDo: If_Data

    def test_group_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_group_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_GROUP_BLOCK_EMPTY,
                      filelength=_TEST_GROUP_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

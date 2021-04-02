from tests.testhandler import Testhandler

_TEST_MODULE_BLOCK = """
/begin MODULE
    _default_ModuleName
    "_default_ModuleLongIdentifier"

    /begin AXIS_PTS STV_N "first block" 0x9876 N DAMOS_SST 100.0 R_SPEED 21 0.0 5800.0
    /end AXIS_PTS
    /begin AXIS_PTS STV_N "first block" 0x9876 N DAMOS_SST 100.0 R_SPEED 21 0.0 5800.0
    /end AXIS_PTS

    /begin CHARACTERISTIC PUMKF "Pump characteristic map" MAP 0x7140 DAMOS_KF 100.0 R_VOLTAGE 0.0 5000.0
	/end CHARACTERISTIC
    /begin CHARACTERISTIC PUMKF "Pump characteristic map" MAP 0x7140 DAMOS_KF 100.0 R_VOLTAGE 0.0 5000.0
	/end CHARACTERISTIC

	/begin COMPU_METHOD CM_FIXED_SB_06 "LongIdentifier" TAB_INTP "%4.3" "UNIT_STRING"
	/end COMPU_METHOD
    /begin COMPU_METHOD CM_FIXED_SB_06 "LongIdentifier" TAB_INTP "%4.3" "UNIT_STRING"
	/end COMPU_METHOD

	/begin COMPU_TAB TT  "conversion table for oil temperatures" TAB_NOINTP 7
	    1 4.3 2 4.7 3 5.8 4 14.2 5 16.8 6 17.2 7 19.4 /* value pairs */
	/end COMPU_TAB
	/begin COMPU_TAB TT  "conversion table for oil temperatures" TAB_NOINTP 7
	    1 4.3 2 4.7 3 5.8 4 14.2 5 16.8 6 17.2 7 19.4 /* value pairs */
	/end COMPU_TAB

    /begin COMPU_VTAB CM_BuiltInDTypeId "LONG" TAB_VERB 9
      0 "SS_DOUBLE"
      1 "SS_SINGLE"
    /end COMPU_VTAB
    /begin COMPU_VTAB CM_BuiltInDTypeId "LONG" TAB_VERB 9
      0 "SS_DOUBLE"
      1 "SS_SINGLE"
    /end COMPU_VTAB

    /begin COMPU_VTAB_RANGE SAR_ASS_REQ_AX "Active assistant"
	    33
	    0 0 "IDLE"
	    1 1 "NDEF1"
	    2 2 "ACTV"
    /end COMPU_VTAB_RANGE
    /begin COMPU_VTAB_RANGE SAR_ASS_REQ_AX "Active assistant"
	    399
	    3 3 "XT_ACTV"
	    64 255 "not defined"
    /end COMPU_VTAB_RANGE

    /begin FRAME ABS_ADJUSTM "function group ABS adjustment" 3 2
    /end FRAME
    /begin FRAME ABS_ADJUSTN "function group ABS" 8 4
    /end FRAME

    /begin FUNCTION CalcStopDynDecel "IDENT_LNG"
	/end FUNCTION
	/begin FUNCTION CalcStartIncr "IDENT_BYTE"
	/end FUNCTION

	/begin GROUP CUSTSWC "Subsys"
	/end GROUP
	/begin GROUP CUSTBSW "Subsystem"
	/end GROUP

	/begin IF_DATA XCP LINK_MAP ref_name 0x003432
	/end IF_DATA
	/begin IF_DATA CANAPE STATIC ref_name 0xFF
	/end IF_DATA

	/begin MEASUREMENT measurement_1 "ID" SWORD DC_PCT_100 1 100. -327.68 327.67
    /end MEASUREMENT
    /begin MEASUREMENT measurement_2 "ID" UBYTE DC_PCT_100 1 100. -327.68 327.67
    /end MEASUREMENT

    /begin RECORD_LAYOUT record_layout_1
    /end RECORD_LAYOUT
    /begin RECORD_LAYOUT record_layout_2
    /end RECORD_LAYOUT

    /begin UNIT kms_per_hour
		"derived unit for velocity: kilometres per hour"
		"[km/h]"
		DERIVED
	/end UNIT
	/begin UNIT kms_per_hour
		"derived unit for velocity: kilometres per hour"
		"[km/h]"
		DERIVED
	/end UNIT

    /begin USER_RIGHTS user_group_1
    /end USER_RIGHTS
    /begin USER_RIGHTS user_group_2
    /end USER_RIGHTS

    /begin MOD_COMMON "_default_ModCommonComment"
    /end MOD_COMMON

    /begin MOD_PAR "_default_ModParComment"
    /end MOD_PAR
/end MODULE
"""

_TEST_MODULE_BLOCK_EMPTY = """
/begin MODULE
/end MODULE
"""


class TestModule(Testhandler):
    def test_module_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_module_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_MODULE_BLOCK,
                      filelength=_TEST_MODULE_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)

        axis_pts = tree.findall('.//Axis_Pts')
        self.assertEqual(len(axis_pts), 2)
        self.assertEqual(axis_pts[0].find('.//Name').text, "STV_N")
        self.assertEqual(axis_pts[0].find('.//LongIdentifier').text, "first block")
        self.assertEqual(axis_pts[0].find('.//InputQuantity').text, "N")
        self.assertEqual(axis_pts[0].find('.//Deposit_Ref').text, "DAMOS_SST")
        self.assertEqual(axis_pts[0].find('.//MaxDiff').text, "100.0")
        self.assertEqual(axis_pts[0].find('.//Conversion').text, "R_SPEED")
        self.assertEqual(axis_pts[0].find('.//MaxAxisPoints').text, "21")
        self.assertEqual(axis_pts[0].find('.//LowerLimit').text, "0.0")
        self.assertEqual(axis_pts[0].find('.//UpperLimit').text, "5800.0")
        self.assertEqual(axis_pts[1].find('.//Name').text, "STV_N")
        self.assertEqual(axis_pts[1].find('.//LongIdentifier').text, "first block")
        self.assertEqual(axis_pts[1].find('.//InputQuantity').text, "N")
        self.assertEqual(axis_pts[1].find('.//Deposit_Ref').text, "DAMOS_SST")
        self.assertEqual(axis_pts[1].find('.//MaxDiff').text, "100.0")
        self.assertEqual(axis_pts[1].find('.//Conversion').text, "R_SPEED")
        self.assertEqual(axis_pts[1].find('.//MaxAxisPoints').text, "21")
        self.assertEqual(axis_pts[1].find('.//LowerLimit').text, "0.0")
        self.assertEqual(axis_pts[1].find('.//UpperLimit').text, "5800.0")

        characteristic = tree.findall('.//Characteristic')
        self.assertEqual(len(characteristic), 2)
        self.assertEqual(characteristic[0].find('.//Name').text, "PUMKF")
        self.assertEqual(characteristic[0].find('.//LongIdentifier').text, "Pump characteristic map")
        self.assertEqual(characteristic[0].find('.//Type').text, "MAP")
        self.assertEqual(characteristic[0].find('.//Address').text, "0x7140")
        self.assertEqual(characteristic[0].find('.//Deposit_Ref').text, "DAMOS_KF")
        self.assertEqual(characteristic[0].find('.//MaxDiff').text, "100.0")
        self.assertEqual(characteristic[0].find('.//Conversion').text, "R_VOLTAGE")
        self.assertEqual(characteristic[0].find('.//LowerLimit').text, "0.0")
        self.assertEqual(characteristic[0].find('.//UpperLimit').text, "5000.0")
        self.assertEqual(characteristic[1].find('.//Name').text, "PUMKF")
        self.assertEqual(characteristic[1].find('.//LongIdentifier').text, "Pump characteristic map")
        self.assertEqual(characteristic[1].find('.//Type').text, "MAP")
        self.assertEqual(characteristic[1].find('.//Address').text, "0x7140")
        self.assertEqual(characteristic[1].find('.//Deposit_Ref').text, "DAMOS_KF")
        self.assertEqual(characteristic[1].find('.//MaxDiff').text, "100.0")
        self.assertEqual(characteristic[1].find('.//Conversion').text, "R_VOLTAGE")
        self.assertEqual(characteristic[1].find('.//LowerLimit').text, "0.0")
        self.assertEqual(characteristic[1].find('.//UpperLimit').text, "5000.0")

        compu_method = tree.findall('.//Compu_Method')
        self.assertEqual(len(compu_method), 2)
        self.assertEqual(compu_method[0].find('.//Name').text, "CM_FIXED_SB_06")
        self.assertEqual(compu_method[0].find('.//LongIdentifier').text, "LongIdentifier")
        self.assertEqual(compu_method[0].find('.//ConversionType').text, "TAB_INTP")
        self.assertEqual(compu_method[0].find('.//Format').text, "%4.3")
        self.assertEqual(compu_method[0].find('.//Unit').text, "UNIT_STRING")
        self.assertEqual(compu_method[1].find('.//Name').text, "CM_FIXED_SB_06")
        self.assertEqual(compu_method[1].find('.//LongIdentifier').text, "LongIdentifier")
        self.assertEqual(compu_method[1].find('.//ConversionType').text, "TAB_INTP")
        self.assertEqual(compu_method[1].find('.//Format').text, "%4.3")
        self.assertEqual(compu_method[1].find('.//Unit').text, "UNIT_STRING")

        compu_tab = tree.findall('.//Compu_Tab')
        self.assertEqual(len(compu_tab), 2)
        self.assertEqual(compu_tab[0].find('.//Name').text, "TT")
        self.assertEqual(compu_tab[0].find('.//LongIdentifier').text, "conversion table for oil temperatures")
        self.assertEqual(compu_tab[0].find('.//ConversionType').text, "TAB_NOINTP")
        self.assertEqual(compu_tab[0].find('.//NumberValuePairs').text, "7")
        self.assertEqual(compu_tab[0].find('.//Axis_Points').text, "['1', '4.3'], ['2', '4.7'], ['3', '5.8'], ['4', '14.2'], ['5', '16.8'], ['6', '17.2'], ['7', '19.4']")
        self.assertEqual(compu_tab[1].find('.//Name').text, "TT")
        self.assertEqual(compu_tab[1].find('.//LongIdentifier').text, "conversion table for oil temperatures")
        self.assertEqual(compu_tab[1].find('.//ConversionType').text, "TAB_NOINTP")
        self.assertEqual(compu_tab[1].find('.//NumberValuePairs').text, "7")
        self.assertEqual(compu_tab[1].find('.//Axis_Points').text, "['1', '4.3'], ['2', '4.7'], ['3', '5.8'], ['4', '14.2'], ['5', '16.8'], ['6', '17.2'], ['7', '19.4']")

        compu_vtab = tree.findall('.//Compu_Vtab')
        self.assertEqual(len(compu_vtab), 2)
        self.assertEqual(compu_vtab[0].find('.//Name').text, "CM_BuiltInDTypeId")
        self.assertEqual(compu_vtab[0].find('.//LongIdentifier').text, "LONG")
        self.assertEqual(compu_vtab[0].find('.//ConversionType').text, "TAB_VERB")
        self.assertEqual(compu_vtab[0].find('.//NumberValuePairs').text, "9")
        self.assertEqual(compu_vtab[0].find('.//InVal_OutVal').text, "['0', 'SS_DOUBLE'], ['1', 'SS_SINGLE']")
        self.assertEqual(compu_vtab[1].find('.//Name').text, "CM_BuiltInDTypeId")
        self.assertEqual(compu_vtab[1].find('.//LongIdentifier').text, "LONG")
        self.assertEqual(compu_vtab[1].find('.//ConversionType').text, "TAB_VERB")
        self.assertEqual(compu_vtab[1].find('.//NumberValuePairs').text, "9")
        self.assertEqual(compu_vtab[1].find('.//InVal_OutVal').text, "['0', 'SS_DOUBLE'], ['1', 'SS_SINGLE']")


        frame = tree.findall('.//Frame')
        self.assertEqual(len(frame), 2)
        self.assertEqual(frame[0].find('.//Name').text, "ABS_ADJUSTM")
        self.assertEqual(frame[0].find('.//LongIdentifier').text, "function group ABS adjustment")
        self.assertEqual(frame[0].find('.//ScalingUnit').text, "3")
        self.assertEqual(frame[0].find('.//Rate').text, "2")
        self.assertEqual(frame[1].find('.//Name').text, "ABS_ADJUSTN")
        self.assertEqual(frame[1].find('.//LongIdentifier').text, "function group ABS")
        self.assertEqual(frame[1].find('.//ScalingUnit').text, "8")
        self.assertEqual(frame[1].find('.//Rate').text, "4")

        function = tree.findall('.//Function')
        self.assertEqual(len(function), 2)
        self.assertEqual(function[0].find('.//Name').text, "CalcStopDynDecel")
        self.assertEqual(function[0].find('.//LongIdentifier').text, "IDENT_LNG")
        self.assertEqual(function[1].find('.//Name').text, "CalcStartIncr")
        self.assertEqual(function[1].find('.//LongIdentifier').text, "IDENT_BYTE")

        group = tree.findall('.//Group')
        self.assertEqual(len(group), 2)
        self.assertEqual(group[0].find('.//GroupName').text, "CUSTSWC")
        self.assertEqual(group[0].find('.//GroupLongIdentifier').text, "Subsys")
        self.assertEqual(group[1].find('.//GroupName').text, "CUSTBSW")
        self.assertEqual(group[1].find('.//GroupLongIdentifier').text, "Subsystem")

        if_data = tree.findall('.//If_Data')
        self.assertEqual(len(if_data), 2)
        self.assertEqual(if_data[0].find('.//Name').text, "XCP")
        self.assertEqual(if_data[0].find('.//DataParams').text, "LINK_MAP, ref_name, 0x003432")
        self.assertEqual(if_data[1].find('.//Name').text, "CANAPE")
        self.assertEqual(if_data[1].find('.//DataParams').text, "STATIC, ref_name, 0xFF")

        measurement = tree.findall('.//Measurement')
        self.assertEqual(len(measurement), 2)
        self.assertEqual(measurement[0].find('.//Name').text, "measurement_1")
        self.assertEqual(measurement[0].find('.//LongIdentifier').text, "ID")
        self.assertEqual(measurement[0].find('.//Datatype').text, "SWORD")
        self.assertEqual(measurement[0].find('.//Conversion').text, "DC_PCT_100")
        self.assertEqual(measurement[0].find('.//Resolution').text, "1")
        self.assertEqual(measurement[0].find('.//Accuracy').text, "100.")
        self.assertEqual(measurement[0].find('.//LowerLimit').text, "-327.68")
        self.assertEqual(measurement[0].find('.//UpperLimit').text, "327.67")
        self.assertEqual(measurement[1].find('.//Name').text, "measurement_2")
        self.assertEqual(measurement[1].find('.//LongIdentifier').text, "ID")
        self.assertEqual(measurement[1].find('.//Datatype').text, "UBYTE")
        self.assertEqual(measurement[1].find('.//Conversion').text, "DC_PCT_100")
        self.assertEqual(measurement[1].find('.//Resolution').text, "1")
        self.assertEqual(measurement[1].find('.//Accuracy').text, "100.")
        self.assertEqual(measurement[1].find('.//LowerLimit').text, "-327.68")
        self.assertEqual(measurement[1].find('.//UpperLimit').text, "327.67")

        record_layout = tree.findall('.//Record_Layout')
        self.assertEqual(len(record_layout), 2)
        self.assertEqual(record_layout[0].find('.//Name').text, "record_layout_1")
        self.assertEqual(record_layout[1].find('.//Name').text, "record_layout_2")

        unit = tree.findall('.//Unit')
        #self.assertEqual(len(unit), 2)
        self.assertEqual(unit[2].find('.//Name').text, "kms_per_hour")
        self.assertEqual(unit[2].find('.//LongIdentifier').text, "derived unit for velocity: kilometres per hour")
        self.assertEqual(unit[2].find('.//Display').text, "[km/h]")
        self.assertEqual(unit[2].find('.//Type').text, "DERIVED")
        self.assertEqual(unit[3].find('.//Name').text, "kms_per_hour")
        self.assertEqual(unit[3].find('.//LongIdentifier').text, "derived unit for velocity: kilometres per hour")
        self.assertEqual(unit[3].find('.//Display').text, "[km/h]")
        self.assertEqual(unit[3].find('.//Type').text, "DERIVED")

        user_rights = tree.findall('.//User_Rights')
        self.assertEqual(len(user_rights), 2)
        self.assertEqual(user_rights[0].find('.//UserLevelId').text, "user_group_1")
        self.assertEqual(user_rights[1].find('.//UserLevelId').text, "user_group_2")

        mod_common = tree.findall('.//Mod_Common')
        self.assertEqual(len(mod_common), 1)
        self.assertEqual(mod_common[0].find('.//Comment').text, "_default_ModCommonComment")

        mod_par = tree.findall('.//Mod_Par')
        self.assertEqual(len(mod_par), 1)
        self.assertEqual(mod_par[0].find('.//Comment').text, "_default_ModParComment")



    def test_module_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_module_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_MODULE_BLOCK_EMPTY,
                      filelength=_TEST_MODULE_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

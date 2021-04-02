from tests.testhandler import Testhandler

_TEST_FRAME_BLOCK = """
/begin MOD_PAR
	"comment"
	/begin CALIBRATION_METHOD
		"InCircuit"
		2
		/begin CALIBRATION_HANDLE
            0                    /* EmuRAM page identifier */
            0xBF000000           /* Original RAM Address */
            0x10000               /* Page size */
        /end CALIBRATION_HANDLE
	/end CALIBRATION_METHOD
	/begin CALIBRATION_METHOD
		"Example"
		4
		/begin CALIBRATION_HANDLE
            1                    /* EmuRAM page identifier */
            0xBF100000           /* Original RAM Address */
            0x90000               /* Page size */
        /end CALIBRATION_HANDLE
	/end CALIBRATION_METHOD
	ADDR_EPK 0x14567
	ADDR_EPK 0x76541
	CPU_TYPE "INTEL 4711"
	CUSTOMER "Company - Name"
	CUSTOMER_NO "191188"
	ECU "Steering control"
	ECU_CALIBRATION_OFFSET 0x1000
	EPK "EPROM identifier test"
	/begin MEMORY_LAYOUT
		PRG_RESERVED
		0x0000
		0x0400
		-1 -1 -1 -1 -1
	/end MEMORY_LAYOUT
	/begin MEMORY_LAYOUT
		PRG_RESERVED
		0x8000
		0x0300
		-3 -2 -5 1 99
	/end MEMORY_LAYOUT
	/begin MEMORY_SEGMENT
		Data1
		"comment"
		DATA
		FLASH
		EXTERN
		0x4000
		0x3000
		-1 -1 -1 -1 -1
	/end MEMORY_SEGMENT
	/begin MEMORY_SEGMENT
		Data2
		"Data external Flash"
		DATA
		FLASH
		EXTERN
		0x7000
		0x2000
		-1 -1 -1 -1 -1
	/end MEMORY_SEGMENT
	NO_OF_INTERFACES 3
	PHONE_NO "09498 594562"
	SUPPLIER "Smooth and Easy"
	USER "Username"
	SYSTEM_CONSTANT "Fd" "1.10"
	SYSTEM_CONSTANT "Ts" "0.010"
	SYSTEM_CONSTANT "Zd" "0.3"
	SYSTEM_CONSTANT "Zn" "0.07"
	VERSION "BG5.0815"
/end MOD_PAR
"""

_TEST_FRAME_BLOCK_EMPTY = """
/begin MOD_PAR
    "comment"
    /begin CALIBRATION_METHOD
	/end CALIBRATION_METHOD
	/begin MEMORY_LAYOUT
	/end MEMORY_LAYOUT
    /begin MEMORY_SEGMENT
	/end MEMORY_SEGMENT
/end MOD_PAR
"""


class TestModPar(Testhandler):
    def test_mod_par_block(self):
        p = self.param.parser
        ast = p.parse(filename="test_mod_par_block",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FRAME_BLOCK,
                      filelength=_TEST_FRAME_BLOCK.count('\n'))

        tree = self.getXmlFromAst(ast)
        self.assertEqual(tree.find('.//Comment').text, "comment")

        self.assertEqual(tree.find('.//Cpu_Type').text, "INTEL 4711")
        self.assertEqual(tree.find('.//Customer').text, "Company - Name")
        self.assertEqual(tree.find('.//Customer_No').text, "191188")
        self.assertEqual(tree.find('.//Ecu').text, "Steering control")
        self.assertEqual(tree.find('.//Ecu_Calibration_Offset').text, "0x1000")
        self.assertEqual(tree.find('.//Epk').text, "EPROM identifier test")
        self.assertEqual(tree.find('.//No_Of_Interfaces').text, "3")
        self.assertEqual(tree.find('.//Phone_No').text, "09498 594562")
        self.assertEqual(tree.find('.//Supplier').text, "Smooth and Easy")
        self.assertEqual(tree.find('.//User').text, "Username")
        self.assertEqual(tree.find('.//Version').text, "BG5.0815")

        addr_epk = tree.findall('.//Addr_Epk')
        self.assertEqual(len(addr_epk), 2)
        self.assertEqual(addr_epk[0].find('.//Address').text, "0x14567")
        self.assertEqual(addr_epk[1].find('.//Address').text, "0x76541")

        calibration_methods = tree.findall('.//Calibration_Method')
        self.assertEqual(len(calibration_methods), 2)
        self.assertEqual(calibration_methods[0].find('.//Method').text, "InCircuit")
        self.assertEqual(calibration_methods[0].find('.//Version').text, "2")
        self.assertEqual(calibration_methods[0].find('.//Calibration_Handle/Handle').text, "0, 0xBF000000, 0x10000")
        self.assertEqual(calibration_methods[1].find('.//Method').text, "Example")
        self.assertEqual(calibration_methods[1].find('.//Version').text, "4")
        self.assertEqual(calibration_methods[1].find('.//Calibration_Handle/Handle').text, "1, 0xBF100000, 0x90000")

        memory_layouts = tree.findall('.//Memory_Layout')
        self.assertEqual(len(memory_layouts), 2)
        self.assertEqual(memory_layouts[0].find('.//PrgType').text, "PRG_RESERVED")
        self.assertEqual(memory_layouts[0].find('.//Address').text, "0x0000")
        self.assertEqual(memory_layouts[0].find('.//Size').text, "0x0400")
        self.assertEqual(memory_layouts[0].find('.//Offset').text, "-1, -1, -1, -1, -1")
        self.assertEqual(memory_layouts[1].find('.//PrgType').text, "PRG_RESERVED")
        self.assertEqual(memory_layouts[1].find('.//Address').text, "0x8000")
        self.assertEqual(memory_layouts[1].find('.//Size').text, "0x0300")
        self.assertEqual(memory_layouts[1].find('.//Offset').text, "-3, -2, -5, 1, 99")

        memory_segments = tree.findall('.//Memory_Segment')
        self.assertEqual(len(memory_layouts), 2)
        self.assertEqual(memory_segments[0].find('.//Name').text, "Data1")
        self.assertEqual(memory_segments[0].find('.//LongIdentifier').text, "comment")
        self.assertEqual(memory_segments[0].find('.//PrgType').text, "DATA")
        self.assertEqual(memory_segments[0].find('.//MemoryType').text, "FLASH")
        self.assertEqual(memory_segments[0].find('.//Attribute').text, "EXTERN")
        self.assertEqual(memory_segments[0].find('.//Address').text, "0x4000")
        self.assertEqual(memory_segments[0].find('.//Size').text, "0x3000")
        self.assertEqual(memory_segments[0].find('.//Offset').text, "-1, -1, -1, -1, -1")
        self.assertEqual(memory_segments[1].find('.//Name').text, "Data2")
        self.assertEqual(memory_segments[1].find('.//LongIdentifier').text, "Data external Flash")
        self.assertEqual(memory_segments[1].find('.//PrgType').text, "DATA")
        self.assertEqual(memory_segments[1].find('.//MemoryType').text, "FLASH")
        self.assertEqual(memory_segments[1].find('.//Attribute').text, "EXTERN")
        self.assertEqual(memory_segments[1].find('.//Address').text, "0x7000")
        self.assertEqual(memory_segments[1].find('.//Size').text, "0x2000")
        self.assertEqual(memory_segments[1].find('.//Offset').text, "-1, -1, -1, -1, -1")

        system_constants = tree.findall('.//System_Constant')
        self.assertEqual(len(system_constants), 4)
        self.assertEqual(system_constants[0].find('.//Name').text, "Fd")
        self.assertEqual(system_constants[0].find('.//Value').text, "1.10")
        self.assertEqual(system_constants[1].find('.//Name').text, "Ts")
        self.assertEqual(system_constants[1].find('.//Value').text, "0.010")
        self.assertEqual(system_constants[2].find('.//Name').text, "Zd")
        self.assertEqual(system_constants[2].find('.//Value').text, "0.3")
        self.assertEqual(system_constants[3].find('.//Name').text, "Zn")
        self.assertEqual(system_constants[3].find('.//Value').text, "0.07")

    def test_mod_par_block_empty(self):
        p = self.param.parser
        ast = p.parse(filename="test_mod_par_block_empty",
                      start_of_a2ml=0,
                      end_of_a2ml=0,
                      input_string=_TEST_FRAME_BLOCK_EMPTY,
                      filelength=_TEST_FRAME_BLOCK_EMPTY.count('\n'))

        self.assertEqual(p.config.validateAST(ast), False)

import unittest

from src.main.python.functions import Functions
from src.main.python.logger import Logger


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.logger = Logger(False, False)
        self.functions = Functions(self.logger)

    def test_lsls_Rd_Rm_imm5(self):
        expression = ["lsls", "r1", "r1", "#1"]
        result = self.functions.lsls_Rd_Rm_imm5(expression)
        expected = "0000000001001001"
        self.assertEqual(expected, result)

    def test_lsrs_Rd_Rm_imm5(self):
        expression = ["lsrs", "r2", "r2", "#1"]
        result = self.functions.lsrs_Rd_Rm_imm5(expression)
        expected = "0000100001010010"
        self.assertEqual(expected, result)

    def test_asrs_Rd_Rm_imm5(self):
        expression = ["asrs", "r4", "r4", "#1"]
        result = self.functions.asrs_Rd_Rm_imm5(expression)
        expected = "0001000001100100"
        self.assertEqual(expected, result)

    def test_adds_Rd_Rn_Rm(self):
        expression = ["adds", "r3", "r0", "r2"]
        result = self.functions.adds_Rd_Rn_Rm(expression)
        expected = "0001100010000011"
        self.assertEqual(expected, result)

    def test_subs_Rd_Rn_Rm(self):
        expression = ["subs", "r4", "r3", "r2"]
        result = self.functions.subs_Rd_Rn_Rm(expression)
        expected = "0001101010011100"
        self.assertEqual(expected, result)

    def test_adds_Rd_Rn_imm3(self):
        expression = ["adds", "r5", "r2", "#5"]
        result = self.functions.adds_Rd_Rn_imm3(expression)
        expected = "0001110101010101"
        self.assertEqual(expected, result)

    def test_subs_Rd_Rn_imm3(self):
        expression = ["sub", "r6", "r0", "#5"]
        result = self.functions.subs_Rd_Rn_imm3(expression)
        expected = "0001111101000110"
        self.assertEqual(expected, result)

    def test_movs_r0_0(self):
        expression = ["movs", "r0", "#0"]
        result = self.functions.movs_Rd_imm8(expression)
        expected = "0010000000000000"
        self.assertEqual(expected, result)

    def test_movs_r1_1(self):
        expression = ["movs", "r1", "#1"]
        result = self.functions.movs_Rd_imm8(expression)
        expected = "0010000100000001"
        self.assertEqual(expected, result)

    def test_movs_r2_20(self):
        expression = ["movs", "r2", "#20"]
        result = self.functions.movs_Rd_imm8(expression)
        expected = "0010001000010100"
        self.assertEqual(expected, result)

    def test_movs_r2_255(self):
        expression = ["movs", "r2", "#255"]
        result = self.functions.movs_Rd_imm8(expression)
        expected = "0010001011111111"
        self.assertEqual(expected, result)

    def test_cmp_Rd_imm8(self):
        expression = ["cmp", "r0", "#1"]
        result = self.functions.cmp_Rd_imm8(expression)
        expected = "0010100000000001"
        self.assertEqual(expected, result)

    def test_adds_Rd_imm8(self):
        expression = ["adds", "r0", "#1"]
        result = self.functions.adds_Rd_imm8(expression)
        expected = "0011000000000001"
        self.assertEqual(expected, result)

    def test_ands_Rdn_Rm(self):
        expression = ["ands", "r3", "r1"]
        result = self.functions.ands_Rdn_Rm(expression)
        expected = "0100000000001011"
        self.assertEqual(expected, result)

    def test_eors_Rdn_Rm(self):
        expression = ["eors", "r4", "r1"]
        result = self.functions.eors_Rdn_Rm(expression)
        expected = "0100000001001100"
        self.assertEqual(expected, result)

    def test_lsls_Rdn_Rm(self):
        expression = ["lsls", "r6", "r5"]
        result = self.functions.lsls_Rdn_Rm(expression)
        expected = "0100000010101110"
        self.assertEqual(expected, result)

    def test_lsrs_Rdn_Rm(self):
        expression = ["lsrs", "r6", "r7"]
        result = self.functions.lsrs_Rdn_Rm(expression)
        expected = "0100000011111110"
        self.assertEqual(expected, result)

    def test_asrs_2_parameters(self):
        expression = ["asrs", "r1", "r2"]
        result = self.functions.asr_2_parameters(expression)
        expected = "0100000100010001"
        self.assertEqual(expected, result)

    def test_adcs(self):
        expression = ["adcs", "r5", "r1"]
        result = self.functions.adc(expression)
        expected = "0100000101001101"
        self.assertEqual(expected, result)

    def test_sbcs_1(self):
        expression = ["sbcs", "r5", "r1"]
        result = self.functions.sbc(expression)
        expected = "0100000110001101"
        self.assertEqual(expected, result)

    def test_rors(self):
        expression = ["ror", "r6", "r1"]
        result = self.functions.ror(expression)
        expected = "0100000111001110"
        self.assertEqual(expected, result)

    def test_tst(self):
        expression = ["tst", "r2", "r6"]
        result = self.functions.tst(expression)
        expected = "0100001000110010"
        self.assertEqual(expected, result)

    def test_rsbs(self):
        expression = ["rsbs", "r4", "r4", '#0']
        result = self.functions.rsb(expression)
        expected = "0100001001100100"
        self.assertEqual(expected, result)

    def test_cmp_r0_r1(self):
        expression = ["cmp", "r0", "r1"]
        result = self.functions.cmp_2_registers(expression)
        expected = "0100001010001000"
        self.assertEqual(expected, result)

    def test_cmn_1(self):
        expression = ["cmn", "r3", "r1"]
        result = self.functions.cmn(expression)
        expected = "0100001011001011"
        self.assertEqual(expected, result)

    def test_cmn_2(self):
        expression = ["cmn", "r2", "r1"]
        result = self.functions.cmn(expression)
        expected = "0100001011001010"
        self.assertEqual(expected, result)

    def test_orrs(self):
        expression = ["orrs", "r4", "r2"]
        result = self.functions.orr(expression)
        expected = "0100001100010100"
        self.assertEqual(expected, result)

    def test_muls(self):
        expression = ["muls", "r5", "r2", "r5"]
        result = self.functions.mul(expression)
        expected = "0100001101010101"
        self.assertEqual(expected, result)

    def test_bics(self):
        expression = ["bics", "r6", "r2"]
        result = self.functions.bic(expression)
        expected = "0100001110010110"
        self.assertEqual(expected, result)

    def test_mvns(self):
        expression = ["mvns", "r7", "r2"]
        result = self.functions.mvn(expression)
        expected = "0100001111010111"
        self.assertEqual(expected, result)

    def test_str_2_parameters(self):
        expression = ["str", "r1", "#0"]
        result = self.functions.str_2_parameters(expression)
        expected = "1001000100000000"
        self.assertEqual(expected, result)

    def test_ldr(self):
        expression = ["ldr", "r2", "#4"]
        result = self.functions.ldr(expression)
        expected = "1001101000000001"
        self.assertEqual(expected, result)

    def test_add_immediate_to_sp(self):
        expression = ["add", "sp,", "#16"]
        result = self.functions.add_immediate_to_sp(expression)
        expected = "1011000000000100"
        self.assertEqual(expected, result)

    def test_sub_immediate_to_sp(self):
        expression = ["sub", "sp", "#508"]
        result = self.functions.sub_immediate_to_sp(expression)
        expected = "1011000011111111"
        self.assertEqual(expected, result)

    def test_b_endif1(self):
        # define the label
        self.functions.labels[".ENDIF1"] = 7
        expression = ["b", ".endif1"]
        result = self.functions.b(expression, 5)
        expected = "1110011111111111"
        self.assertEqual(expected, result)

    def test_b_endif2(self):
        # define the label
        self.functions.labels[".ENDIF2"] = 12
        expression = ["b", ".endif2"]
        result = self.functions.b(expression, 9)
        expected = "1110000000000000"
        self.assertEqual(expected, result)

    def test_b_goto(self):
        # define the label
        self.functions.labels[".GOTO"] = 2
        expression = ["b", ".goto"]
        result = self.functions.b(expression, 11)
        expected = "1110011111110100"
        self.assertEqual(expected, result)

    def test_bne(self):
        # define the label
        self.functions.labels[".LBB0_5"] = 22
        expression = ["bne", ".LBB0_5"]
        result = self.functions.bne(expression, 15)
        expected = "1101000100000100"
        self.assertEqual(expected, result)

    def test_bmi_then1(self):
        # define the label
        self.functions.labels[".THEN1"] = 6
        expression = ["bmi", ".then1"]
        result = self.functions.bmi(expression, 4)
        expected = "1101010011111111"
        self.assertEqual(expected, result)

    def test_blt_then2(self):
        # define the label
        self.functions.labels[".THEN2"] = 10
        expression = ["blt", ".then2"]
        result = self.functions.blt(expression, 8)
        expected = "1101101111111111"
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

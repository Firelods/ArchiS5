import unittest

from src.main.python.functions import Functions


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.functions = Functions()

    def test_lsl(self):
        expression = ["lsl", "r1", "r2", "#3"]
        result = self.functions.lsl(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_lsr(self):
        expression = ["lsr", "r1", "r2", "#3"]
        result = self.functions.lsr(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_asr(self):
        expression = ["asr", "r1", "r2", "#3"]
        result = self.functions.asr(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_add_register(self):
        expression = ["adds", "r3", "r0", "r2"]
        result = self.functions.add_register(expression)
        expected = "0001100010000011"
        self.assertEqual(expected, result)

    def test_sub_register(self):
        expression = ["sub", "r1", "r2", "r3"]
        result = self.functions.sub_register(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_add_3bit_intermediate(self):
        expression = ["add", "r1", "r2", "#3"]
        result = self.functions.add_3bit_intermediate(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_sub_3bit_intermediate(self):
        expression = ["sub", "r6", "r0", "#5"]
        result = self.functions.sub_3bit_intermediate(expression)
        expected = "0001111101000110"
        self.assertEqual(expected, result)

    def test_mov_r0_0(self):
        expression = ["movs", "r0", "#0"]
        result = self.functions.mov(expression)
        expected = "0010000000000000"
        self.assertEqual(expected, result)

    def test_mov_r1_1(self):
        expression = ["movs", "r1", "#1"]
        result = self.functions.mov(expression)
        expected = "0010000100000001"
        self.assertEqual(expected, result)

    def test_mov_r2_20(self):
        expression = ["movs", "r2", "#20"]
        result = self.functions.mov(expression)
        expected = "0010001000010100"
        self.assertEqual(expected, result)

    def test_and_bitwise(self):
        expression = ["and", "r1", "r2"]
        result = self.functions.and_bitwise(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_eor(self):
        expression = ["eor", "r1", "r2"]
        result = self.functions.eor(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_lsl_2_parameters(self):
        expression = ["lsl", "r1", "r2"]
        result = self.functions.lsl_2_parameters(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_lsr_2_parameters(self):
        expression = ["lsr", "r1", "r2"]
        result = self.functions.lsr_2_parameters(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_asr_2_parameters(self):
        expression = ["asr", "r1", "r2"]
        result = self.functions.asr_2_parameters(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_adc(self):
        expression = ["adc", "r1", "r2"]
        result = self.functions.adc(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_sbc(self):
        expression = ["sbc", "r1", "r2"]
        result = self.functions.sbc(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_ror(self):
        expression = ["ror", "r1", "r2"]
        result = self.functions.ror(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_tst(self):
        expression = ["tst", "r1", "r2"]
        result = self.functions.tst(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_rsb(self):
        expression = ["rsb", "r1", "r2"]
        result = self.functions.rsb(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_cmp_r0_r1(self):
        expression = ["cmp", "r0", "r1"]
        result = self.functions.cmp(expression)
        expected = "0100001010001000"
        self.assertEqual(expected, result)

    def test_cmn(self):
        expression = ["cmn", "r1", "r2"]
        result = self.functions.cmn(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_orr(self):
        expression = ["orr", "r1", "r2"]
        result = self.functions.orr(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_mul(self):
        expression = ["mul", "r1", "r2"]
        result = self.functions.mul(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_bic(self):
        expression = ["bic", "r1", "r2"]
        result = self.functions.bic(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_mvn(self):
        expression = ["mvn", "r1", "r2"]
        result = self.functions.mvn(expression)
        expected = "EXPECTED_BINARY_RESULT"
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
        expression = ["sub", "sp", "#3"]
        result = self.functions.sub_immediate_to_sp(expression)
        expected = "EXPECTED_BINARY_RESULT"
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

    def test_beq(self):
        expression = ["beq", "#3"]
        result = self.functions.beq(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_bne(self):
        expression = ["bne", "#3"]
        result = self.functions.bne(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_bcs(self):
        expression = ["bcs", "#3"]
        result = self.functions.bcs(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_bcc(self):
        expression = ["bcc", "#3"]
        result = self.functions.bcc(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_bmi_then1(self):
        # define the label
        self.functions.labels[".THEN1"] = 6
        expression = ["bmi", ".then1"]
        result = self.functions.bmi(expression, 4)
        expected = "1101010011111111"
        self.assertEqual(expected, result)

    def test_bpl(self):
        expression = ["bpl", "#3"]
        result = self.functions.bpl(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_bvs(self):
        expression = ["bvs", "#3"]
        result = self.functions.bvs(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_bvc(self):
        expression = ["bvc", "#3"]
        result = self.functions.bvc(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_bhi(self):
        expression = ["bhi", "#3"]
        result = self.functions.bhi(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_bls(self):
        expression = ["bls", "#3"]
        result = self.functions.bls(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_bge(self):
        expression = ["bge", "#3"]
        result = self.functions.bge(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_blt_then2(self):
        # define the label
        self.functions.labels[".THEN2"] = 10
        expression = ["blt", ".then2"]
        result = self.functions.blt(expression, 8)
        expected = "1101101111111111"
        self.assertEqual(expected, result)

    def test_bgt(self):
        expression = ["bgt", "#3"]
        result = self.functions.bgt(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_ble(self):
        expression = ["ble", "#3"]
        result = self.functions.ble(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

    def test_bal(self):
        expression = ["bal", "#3"]
        result = self.functions.bal(expression)
        expected = "EXPECTED_BINARY_RESULT"
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

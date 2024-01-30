import unittest

from parser.asm_instructions import AsmInstructions
from tools.logger import Logger


class TestAsmInstructions(unittest.TestCase):
    
    def setUp(self):
        self.logger = Logger(False, False)
        self.functions = AsmInstructions(self.logger)

    def test_get_immediate(self):
        result = self.functions.get_immediate("3", 3)
        expected = "011"
        self.assertEqual(expected, result)

    def test_get_immediate_2(self):
        result = self.functions.get_immediate("3", 5)
        expected = "00011"
        self.assertEqual(expected, result)

    def test_get_immediate_8(self):
        result = self.functions.get_immediate("20", 8)
        expected = "00010100"
        self.assertEqual(expected, result)

    def test_get_immediate_8_1(self):
        result = self.functions.get_immediate("8", 8)
        expected = "00001000"
        self.assertEqual(expected, result)
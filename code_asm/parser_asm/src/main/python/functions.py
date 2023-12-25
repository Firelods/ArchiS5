from src.main.python.asm_instructions import AsmInstructions


class Functions:

    def __init__(self):
        self.number_of_labels = 0
        self.number_of_instructions_labels = 0
        self.labels = {}
        self.labels_source = {}
        self.asm_instructions = AsmInstructions()

    # Shift, add, sub, mov: LSL, LSR, ASR, ADD, SUB, ADD3, SUB3, MOV

    def lsl(self, expression: list):
        """
        :param expression: list
        :return: 16 bits
        """
        # example of expression : ["lsl", "r1", "r2", "#3"]
        return self.asm_instructions.instruction_imm5_rd_rm(expression, "000")

    def lsr(self, expression: list):
        """
        :param expression: list
        :return: 16 bits
        """
        # example of expression : ["lsr", "r1", "r2", "#3"]
        return self.asm_instructions.instruction_imm5_rd_rm(expression, "001")

    def asr(self, expression: list):
        """
        :param expression: list
        :return: 16 bits
        """
        # example of expression : ["asr", "r1", "r2", "#3"]
        return self.asm_instructions.instruction_imm5_rd_rm(expression, "010")

    def add_register(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["add", "r1", "r2", "r3"]
        return self.asm_instructions.instruction_rm_rd_rn(expression, "01100")

    def sub_register(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["sub", "r1", "r2", "r3"]
        return self.asm_instructions.instruction_rm_rd_rn(expression, "01101")

    def add_3bit_intermediate(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["add", "r1", "r2", "#3"]
        return self.asm_instructions.instruction_imm3_rd_rn(expression, "01110")

    def sub_3bit_intermediate(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["sub", "r1", "r2", "#3"]
        return self.asm_instructions.instruction_imm3_rd_rn(expression, "01111")

    def mov(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["mov", "r1", "#3"]
        return self.asm_instructions.instruction_rd_imm8(expression, "100")

    # Data processing : AND, EOR, LSL, LSR, ASR, ADC, SBC, ROR, TST, RSB, CMP, CNN, ORR, MUL, BIC, MVN

    def and_bitwise(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["and", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0000")

    def eor(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["eor", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0001")

    def lsl_2_parameters(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["lsl", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0010")

    def lsr_2_parameters(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["lsr", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0011")

    def asr_2_parameters(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["asr", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0100")

    def adc(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["adc", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0101")

    def sbc(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["sbc", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0110")

    def ror(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["ror", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0111")

    def tst(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["tst", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1000")

    def rsb(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["rsb", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1001")

    def cmp(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["cmp", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1010")

    def cmn(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["cmn", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1011")

    def orr(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["orr", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1100")

    def mul(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["mul", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1101")

    def bic(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["bic", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1110")

    def mvn(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["mvn", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1111")

    # Load / Store: STR, LDR

    def str_2_parameters(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["str", "r1", "#3"]
        return self.asm_instructions.instruction_rt_imm8(expression, "0")

    def ldr(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["ldr", "r1", "#3"]
        return self.asm_instructions.instruction_rt_imm8(expression, "1")

    # Miscellaneous 16-bit instructions: ADD, SUB

    def add_immediate_to_sp(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["add", "sp", "#3"]
        return self.asm_instructions.instruction_sp_imm7(expression, "00000")

    def sub_immediate_to_sp(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["sub", "sp", "#3"]
        return self.asm_instructions.instruction_sp_imm7(expression, "00001")

    # Unconditional branch: B

    def b(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["b", "#3"]
        return self.asm_instructions.unconditional_branch(expression, self.labels, label_source)

    # Conditionnal Branch: BEQ, BNE, BCS, BCC, BMI, BPL, BVS, BVC, BHI, BLS, BGE, BLT, BGT, BLE, BAL

    def beq(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["beq", "#3"]
        return self.asm_instructions.conditional_branch(expression, "0000", self.labels,
                                                        label_source)

    def bne(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["bne", "#3"]
        return self.asm_instructions.conditional_branch(expression, "0001", self.labels,
                                                        label_source)

    def bcs(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["bcs", "#3"]
        return self.asm_instructions.conditional_branch(expression, "0010", self.labels,
                                                        label_source)

    def bcc(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["bcc", "#3"]
        return self.asm_instructions.conditional_branch(expression, "0011", self.labels,
                                                        label_source)

    def bmi(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression: list
        :return: 16 bits
        """
        # example of self.expression: ["bmi", "#3"]
        return self.asm_instructions.conditional_branch(expression, "0100", self.labels,
                                                        label_source)

    def bpl(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["bpl", "#3"]
        return self.asm_instructions.conditional_branch(expression, "0101", self.labels,
                                                        label_source)

    def bvs(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["bvs", "#3"]
        return self.asm_instructions.conditional_branch(expression, "0110", self.labels,
                                                        label_source)

    def bvc(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["bvc", "#3"]
        return self.asm_instructions.conditional_branch(expression, "0111", self.labels,
                                                        label_source)

    def bhi(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["bhi", "#3"]
        return self.asm_instructions.conditional_branch(expression, "1000", self.labels,
                                                        label_source)

    def bls(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["bls", "#3"]
        return self.asm_instructions.conditional_branch(expression, "1001", self.labels,
                                                        label_source)

    def bge(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["bge", "#3"]
        return self.asm_instructions.conditional_branch(expression, "1010", self.labels,
                                                        label_source)

    def blt(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression: list
        :return: 16 bits
        """
        # example of expression: ["blt", "#3"]
        return self.asm_instructions.conditional_branch(expression, "1011", self.labels,
                                                        label_source)

    def bgt(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["bgt", "#3"]
        return self.asm_instructions.conditional_branch(expression, "1100", self.labels,
                                                        label_source)

    def ble(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["ble", "#3"]
        return self.asm_instructions.conditional_branch(expression, "1101", self.labels,
                                                        label_source)

    def bal(self, expression: list, label_source: int):
        """
        :param label_source:
        :param expression:
        :return:
        """
        # example of expression : ["bal", "#3"]
        return self.asm_instructions.conditional_branch(expression, "1110", self.labels,
                                                        label_source)

    # Commons methods

    def define_label(self, line: str, number_of_instructions_labels: int):
        """
        Define a label
        :param line:
        :rtype: str
        :param number_of_instructions_labels:
        :rtype: int
        :return:
        """
        line = line.strip()
        if self.is_label(line):
            label = line[:-1]
            self.labels[label.upper()] = number_of_instructions_labels

    @staticmethod
    def is_label(line: str):
        """
        Check if the line is a label
        :param line: string
        :return: boolean
        """
        if line == "": return False
        if line[0] == "." and line[-1] == ":":
            return True
        return False

    def set_number_of_instructions_labels(self, number_of_instructions_labels):
        """

        :param number_of_instructions_labels:
        :return:
        """
        self.number_of_instructions_labels = number_of_instructions_labels

    def set_number_of_labels(self, nbr_of_labels):
        """

        :param nbr_of_labels:
        :return:
        """
        self.number_of_labels = nbr_of_labels

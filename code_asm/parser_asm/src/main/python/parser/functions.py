from parser.asm_instructions import AsmInstructions
from tools.logger import Logger


class Functions:

    def __init__(self, logger: Logger):
        self.number_of_labels = 0
        self.number_of_instructions_labels = 0
        self.labels = {}
        self.labels_source = {}
        self.asm_instructions = AsmInstructions(logger)
        self.logger = logger
        self.class_name = type(self).__name__

    # Shift, add, sub, mov: LSL, LSR, ASR, ADD, SUB, ADD3, SUB3, MOV

    def lsls_Rd_Rm_imm5(self, expression: list):
        """
        :param expression: list
        :return: 16 bits
        """
        # example of expression : ["lsl", "r1", "r2", "#3"]
        return self.asm_instructions.instruction_imm5_rd_rm(expression, "000")

    def lsrs_Rd_Rm_imm5(self, expression: list):
        """
        :param expression: list
        :return: 16 bits
        """
        # example of expression : ["lsr", "r1", "r2", "#3"]
        return self.asm_instructions.instruction_imm5_rd_rm(expression, "001")

    def asrs_Rd_Rm_imm5(self, expression: list):
        """
        :param expression: list
        :return: 16 bits
        """
        # example of expression : ["asr", "r1", "r2", "#3"]
        return self.asm_instructions.instruction_imm5_rd_rm(expression, "010")

    def adds_Rd_Rn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["add", "r1", "r2", "r3"]
        return self.asm_instructions.instruction_rm_rd_rn(expression, "01100")

    def subs_Rd_Rn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["sub", "r1", "r2", "r3"]
        return self.asm_instructions.instruction_rm_rd_rn(expression, "01101")

    def adds_Rd_Rn_imm3(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["add", "r1", "r2", "#3"]
        return self.asm_instructions.instruction_imm3_rd_rn(expression, "01110")

    def subs_Rd_Rn_imm3(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["sub", "r1", "r2", "#3"]
        return self.asm_instructions.instruction_imm3_rd_rn(expression, "01111")

    def movs_Rd_imm8(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["movs", "r1", "#3"]
        return self.asm_instructions.instruction_rd_imm8(expression, "100")

    def cmp_Rd_imm8(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["cmp", "r1", "#8"]
        return self.asm_instructions.instruction_rd_imm8(expression, "101")

    def adds_Rd_imm8(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["adds", "r1", "#8"]
        return self.asm_instructions.instruction_rd_imm8(expression, "110")

    def add_Rd_sp_imm8(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["add", "r1", "sp", "#8"]
        return self.asm_instructions.instruction_rd_sp_imm8(expression, "110")

    def subs_8bit_immediate(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["subs", "r1", "#8"]
        return self.asm_instructions.instruction_rd_imm8(expression, "111")


    # Data processing : AND, EOR, LSL, LSR, ASR, ADC, SBC, ROR, TST, RSB, CMP, CNN, ORR, MUL, BIC, MVN

    def ands_Rdn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["and", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0000")

    def eors_Rdn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["eor", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0001")

    def lsls_Rdn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["lsl", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0010")

    def lsrs_Rdn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["lsr", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0011")

    def asrs_Rdn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["asr", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0100")

    def adcs_Rdn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["adc", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0101")

    def sbcs_Rdn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["sbc", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0110")

    def rors_Rdn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["ror", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "0111")

    def tst_Rn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["tst", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1000")

    def rsbs_Rd_Rn(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["rsb", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1001")

    def cmp_Rn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["cmp", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1010")

    def cmn_Rn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["cmn", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1011")

    def orrs_Rdn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["orr", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1100")

    def muls_Rdm_Rn_Rdm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["mul", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1101")

    def bics_Rdn_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["bic", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1110")

    def mvns_Rd_Rm(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["mvn", "r1", "r2"]
        return self.asm_instructions.instruction_rm_rdn(expression, "1111")

    # Load / Store: STR, LDR

    def str_Rt_imm8(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["str", "r1", "#3"]
        return self.asm_instructions.instruction_rt_imm8(expression, "0")

    def ldr_Rt_imm8(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["ldr", "r1", "#3"]
        return self.asm_instructions.instruction_rt_imm8(expression, "1")

    # Miscellaneous 16-bit instructions: ADD, SUB

    def add_imm7(self, expression: list):
        """
        :param expression:
        :return:
        """
        # example of expression : ["add", "sp", "#3"]
        return self.asm_instructions.instruction_sp_imm7(expression, "00000")

    def sub_imm7(self, expression: list):
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
        message = f"Define label {line}"
        self.logger.log(self.class_name, self.define_label.__name__, message)
        if self.is_label(line):
            label = line[:-1]
            self.labels[label.upper()] = number_of_instructions_labels
            message = f"Label {label} defined"
            self.logger.log(self.class_name, self.define_label.__name__, message)

    def is_label(self, line: str):
        """
        Check if the line is a label
        :param line: string
        :return: boolean
        """
        message = f"Check if {line} is a label"
        self.logger.log(self.class_name, self.is_label.__name__, message)
        if line == "":
            self.logger.error(self.class_name, self.is_label.__name__, "The line is empty")
            return False
        if line[0] == "." and line[-1] == ":":
            message = f"{line} is a label"
            self.logger.log(self.class_name, self.is_label.__name__, message)
            return True
        message = f"{line} is not a label"
        self.logger.log(self.class_name, self.is_label.__name__, message)
        return False

    def set_number_of_instructions_labels(self, number_of_instructions_labels):
        """

        :param number_of_instructions_labels:
        :return:
        """
        message = f"Set number of instructions labels to {number_of_instructions_labels}"
        self.logger.log(self.class_name, self.set_number_of_instructions_labels.__name__, message)
        self.number_of_instructions_labels = number_of_instructions_labels

    def set_number_of_labels(self, nbr_of_labels):
        """

        :param nbr_of_labels:
        :return:
        """
        message = f"Set number of labels to {nbr_of_labels}"
        self.logger.log(self.class_name, self.set_number_of_labels.__name__, message)
        self.number_of_labels = nbr_of_labels

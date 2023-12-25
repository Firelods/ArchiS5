class AsmInstructions:

    def instruction_imm5_rd_rm(self, expression: list, codop: str):
        """
        This function is used to generate the binary code of the instructions that have the following structure:
        instruction imm5r, d, rm
        """
        rd = expression[1]
        rm = expression[2]
        imm5 = expression[3][1:]
        rd = self.get_register_number(rd)
        rm = self.get_register_number(rm)
        imm5 = self.get_immediate(imm5, 5)
        return "00" + codop + imm5 + rm + rd

    def instruction_imm3_rd_rn(self, expression: list, codop: str):
        """
        This function is used to generate the binary code of the instructions that have the following structure:
        instruction imm3, rd, rn
        """
        rd = expression[1]
        rn = expression[2]
        imm3 = expression[3][1:]
        rd = self.get_register_number(rd)
        rn = self.get_register_number(rn)
        imm3 = self.get_immediate(imm3, 3)
        return "00" + codop + imm3 + rn + rd

    def instruction_rm_rdn(self, expression: list, codop: str):
        """
        This function is used to generate the binary code of the instructions that have the following structure:
        instruction rm, rdn
        """
        rdn = expression[1]
        rm = expression[2]
        rdn = self.get_register_number(rdn)
        rm = self.get_register_number(rm)
        return "010000" + codop + rm + rdn

    def instruction_rm_rd_rn(self, expression: list, codop: str):
        """
        This function is used to generate the binary code of the instructions that have the following structure:
        instruction rm, rd, rn
        """
        rd = expression[1]
        rn = expression[2]
        rm = expression[3]
        rd = self.get_register_number(rd)
        rn = self.get_register_number(rn)
        rm = self.get_register_number(rm)
        return "00" + codop + rm + rn + rd

    def instruction_rd_imm8(self, expression: list, codop: str):
        """
        This function is used to generate the binary code of the instructions that have the following structure:
        instruction rd, imm8
        """
        rd = expression[1]
        imm8 = expression[2][1:]
        rd = self.get_register_number(rd)
        imm8 = self.get_immediate(imm8, 8)
        return "00" + codop + rd + imm8

    def instruction_rt_imm8(self, expression: list, codop: str):
        """
        This function is used to generate the binary code of the instructions that have the following structure:
        instruction rt, imm8
        """
        rt = expression[1]
        imm8 = expression[2][1:]
        rt = self.get_register_number(rt)
        imm8 = self.get_immediate(str(int(int(imm8) / 4)), 8)
        return "1001" + codop + rt + imm8

    def instruction_sp_imm7(self, expression: list, codop: str):
        """
        This function is used to generate the binary code of the instructions that have the following structure:
        instruction sp, imm7
        """
        imm7: str = expression[2][1:]
        imm7 = self.get_immediate(str(int(int(imm7) / 4)), 7)
        return "1011" + codop + imm7

    def conditional_branch(self, expression: list, cond: str, labels: dict, number_line: int):
        """
        This function is used to generate the binary code of the instructions that have the following structure:
        instruction label
        :param expression: The input assembly instruction as a string.
        :param cond: The condition code for the conditional branch
        :param labels: A map containing label-to-line-number mappings.
        :param number_line: The current line number of the assembly code.
        :return:
        """
        label = expression[1].upper()
        line_label = labels[label]
        offset = line_label - number_line - 3
        if offset < 0:
            imm8 = self.get_immediate_negative(offset, 8)
        else:
            imm8 = self.get_immediate(offset, 8)
        return "1101" + cond + imm8

    def unconditional_branch(self, expression: list, labels: dict, number_line: int):
        """
        This function is used to generate the binary code of the instructions that have the following structure:
        instruction label
        :param expression: The input assembly instruction as a string.
        :param labels: A map containing label-to-line-number mappings.
        :param number_line: The current line number of the assembly code.
        :return:
        """
        label = expression[1].upper()
        line_label = labels[label]
        offset = line_label - number_line - 3
        if offset < 0:
            imm11 = self.get_immediate_negative(offset, 11)
        else:
            imm11 = self.get_immediate(offset, 11)
        return "11100" + imm11

    @staticmethod
    def get_register_number(register: str):
        """
        Get the register binary number from the register name
        :param register: string
        :return: string
        """
        # if there is a comma at the end of the register, remove it
        if register[-1] == ",":
            register = register[:-1]
        if register == "r0":
            return "000"
        elif register == "r1":
            return "001"
        elif register == "r2":
            return "010"
        elif register == "r3":
            return "011"
        elif register == "r4":
            return "100"
        elif register == "r5":
            return "101"
        elif register == "r6":
            return "110"
        elif register == "r7":
            return "111"
        return "000"

    @staticmethod
    def get_immediate(number: str, bits: int):
        """
        Get the binary number from the number
        :param number: the value base 10
        :param bits: the number of bits of the binary number
        :return: the base 2 number
        """
        binaries = ""
        number = int(number)
        while number > 0:
            binaries = str(number % 2) + binaries
            number = number // 2
        while len(binaries) < bits:
            binaries = "0" + binaries
        return binaries

    @staticmethod
    def get_immediate_negative(number: str, bits: int):
        """
        Get the binary number from the number
        :param number: the value base 10
        :param bits: the number of bits of the binary number
        :return: the base 2 number
        """
        binaries = ""
        # The number is negative
        number = int(number)
        number = -number
        # Convert the number to binary
        while number > 0:
            binaries = str(number % 2) + binaries
            number = number // 2
        # Add 0 until the number of bits is reached
        while len(binaries) < bits:
            binaries = "0" + binaries

        # Invert the bits
        binaries = binaries.replace("0", "2")
        binaries = binaries.replace("1", "0")
        binaries = binaries.replace("2", "1")

        # Add 1 to the binary number
        a = int(binaries, 2)
        b = int("1", 2)
        binaries = a + b
        binaries = bin(binaries)[2:]

        return binaries



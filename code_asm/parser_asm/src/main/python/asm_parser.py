import inspect
import json

from asm_reader import AsmReader
from bcolors import bcolors
from functions import Functions
from logger import Logger


class AsmParser:

    def __init__(self, logger: Logger):
        self._function = Functions(logger)
        self.instructions_set = None
        self.get_instruction_set()
        self.class_name = type(self).__name__
        self.logger = logger

    def run(self, assembly_code: list, expected: list, path: str, asm_reader: AsmReader):
        self.fill_labels(assembly_code)

        # Parse the assembly code
        binary = self.parse_asm(assembly_code)

        # Convert the binary into hexadecimal
        hexa = self.binary_to_hexa(binary)

        path = path.replace("asm_files", "output_binaries").replace(".s", ".bin")

        # Save the hexadecimal in a binary file
        self.save_hexa_as_bin(path, hexa)

        # Read the binary file
        actual = asm_reader.read_bin_file(path)

        # Show the difference between the expected and actual output
        if expected is not None:
            self.show_difference(expected, actual)

    def get_instruction_set(self):
        # Read the json file locate at : src/main/resources/instructions_set.json
        with open("../../../src/main/resources/instructions_set.json", 'r') as file:
            instructions_json = json.load(file)
            self.instructions_set = [instructions_json[key] for key in instructions_json]

    @staticmethod
    def instruction_to_upper(instruction: list):
        """
        Convert instruction to upper case
        :param instruction:
        :return:
        """
        instruction[0] = instruction[0].upper()
        return instruction

    def fill_labels(self, asm_lines: list):
        """

        :param asm_lines:
        :return:
        """
        number_of_instructions_labels = 0
        line_number = 0
        for line in asm_lines:
            self._function.define_label(line, number_of_instructions_labels)
            line_number += 1
            if self.is_valid_line(line):
                number_of_instructions_labels += 1

        self._function.set_number_of_instructions_labels(number_of_instructions_labels)
        self._function.set_number_of_labels(line_number)

    @staticmethod
    def is_valid_line(line: str):
        """
        Check if the line is valid
        :param line:
        :return:
        """
        line = line.replace("\t", "").replace("\n", "")
        # if it's an empty line return false
        if line == "": return False
        # if the line start with @ in the line, return false
        if line[0] == "@": return False
        # if the line start with . in the line, return false
        if line[0] == ".": return False
        # if the line start wth add r7
        if line.split()[0] == "add" and line.split()[1] == "r7": return False
        # if the line start with push or pop in the line, return false
        if line.split()[0] == "push" or line.split()[0] == "pop": return False
        # if the line start with run: in the line, return false
        if line.split()[0] == "run:": return False
        return True

    def parse_asm(self, asm_lines: list):
        """

        :param asm_lines:
        :return:
        """
        binary = []
        line_number = 0
        for line in asm_lines:
            b = self.parse_line(line, line_number)
            if b is not None:
                binary.append(b)
                line_number += 1
        return binary

    def parse_line(self, line: str, line_number: int):
        """

        :param line_number:
        :param line:
        :return:
        """
        binary = None
        if self.is_valid_line(line):
            line = line.replace("\t", " ").replace("\n", "")
            binary = self.convert_into_binary(line.split(), line_number)
        return binary

    def convert_into_binary(self, line: list, line_number: int):
        """
        Convert assembly into binary
        :param line_number:
        :param line:
        :return:
        """
        binaries = ""
        line = self.instruction_to_upper(line)
        # check to witch instruction set the instruction belongs
        for instruction in self.instructions_set:
            for key, values in instruction.items():
                if line[0] == key and not values["doublon"]:
                    line = self.filter_operands(line)
                    self.logger.log(self.class_name, self.convert_into_binary.__name__, line)
                    binaries = self.call_function(line, instruction[key]["function"], line_number)
                elif line[0] == key and values["doublon"]:
                    # check to wich double instruction set the instruction belongs
                    # for that we need to check if all the operands correspond to one of the double instruction set
                    # if it does we can call the function
                    # if not we can't call the function
                    temp = self.filter_operands(line)
                    # Count the number of r and the number of #imm
                    r, imm = self.number_of_r_and_imm(temp)
                    # Check if the number of r and #imm correspond to the double instruction set
                    if r == values["R"] and imm == values["#imm"]:
                        self.logger.log(self.class_name, self.convert_into_binary.__name__, line)
                        binaries = self.call_function(line, instruction[key]["function"], line_number)
        if binaries == "":
            message = f"Error: {line} is not a valid instruction"
            self.logger.error(self.class_name, self.convert_into_binary.__name__, message)
        return binaries

    @staticmethod
    def filter_operands(instructions: list):
        """
        Filter operands
        :param instructions:
        :return:
        """
        _next = False
        filtered_instructions = []
        for instruction in instructions:
            # Replace 'sp' with '#0' if no '#' follows 'sp'
            if _next:
                _next = False
                instruction = instruction.replace(']', '')
                filtered_instructions.append(instruction)
                continue
            if 'sp' == instruction:
                filtered_instructions.append('sp')
                filtered_instructions.append('#0')
            elif 'sp,' == instruction:
                filtered_instructions.append('sp')
            # elif r{number},[sp, replace with r{number}
            elif instruction[0] == 'r' and instruction[-2] == 'p':
                _next = True
                if len(instruction[:1]) == 2:
                    filtered_instructions.append(instruction[:1])
                elif len(instruction[:1]) == 1:
                    filtered_instructions.append(instruction[:2])
            elif '[sp,' in instruction:
                _next = True
            elif '[sp]' == instruction:
                filtered_instructions.append('#0')
            # else if the last character is : remove it
            elif instruction[-1] == ':':
                filtered_instructions.append(instruction[:-1])
            # else if there is a \n remove it
            elif instruction[-1] == "\n":
                filtered_instructions.append(instruction[:-1])
            else:
                filtered_instructions.append(instruction)
        return filtered_instructions

    def call_function(self, instruction: list, method_name: str, line_number: int):
        """
        Call the function
        :param instruction:
        :param method_name:
        :param line_number:
        :return:
        """
        # Check if the method_name exists in the _function class
        if hasattr(self._function, method_name):
            # Get the method using getattr
            method = getattr(self._function, method_name)
            signature = inspect.signature(method)
            message = f"Calling {method_name} with {signature.parameters}"
            self.logger.log(self.class_name, self.call_function.__name__, message)
            if len(signature.parameters) == 2:
                return method(instruction, line_number)
            # Call the method with the instruction as an argument
            return method(instruction)
        else:
            # Handle the case when the method is not found
            message = f"Error: Method {method_name} not found in class {type(self._function).__name__}"
            self.logger.error(self.class_name, self.call_function.__name__, message)
            return None

    @staticmethod
    def number_of_r_and_imm(operands: list):
        """
        Count the number of r and #imm
        :param operands:
        :return:
        """
        r = 0
        imm = 0
        for operand in operands:
            if operand[0] == "r":
                r += 1
            elif operand[0] == "#":
                imm += 1
        return r, imm

    def binary_to_hexa(self, binary_list: list):
        """
        Convert all the binaries in to hexadecimal
        :param binary_list:
        :return:
        """
        message = "Converting binary to hexadecimal"
        hexa = [hex(int(binary, 2))[2:].zfill(4) for binary in binary_list]
        self.logger.log(self.class_name, self.binary_to_hexa.__name__, message)
        self.logger.log(self.class_name, self.binary_to_hexa.__name__, hexa)
        return hexa

    def show_difference(self, expected: list, actual: list):
        """
        Show the difference between the expected and actual output and display the percentage of correctness
        :param expected: List of expected strings
        :param actual: List of actual strings
        :return: None
        """
        correct_count = 0

        for i in range(len(expected)):
            if expected[i] != actual[i]:
                # print the characters that change in red
                message = "Expected/Actual: "
                self.logger.log(self.class_name, self.show_difference.__name__, message, end="")
                for j in range(len(expected[i])):
                    if expected[i][j] != actual[i][j]:
                        message = bcolors.FAIL + expected[i][j] + bcolors.ENDC
                        self.logger.log(self.class_name, self.show_difference.__name__, message, end="")
                    else:
                        message = expected[i][j]
                        self.logger.log(self.class_name, self.show_difference.__name__, message, end="")
                message = f"/{actual[i]} [KO]\n"
                self.logger.log(self.class_name, self.show_difference.__name__, message)
            else:
                correct_count += 1
                message = f"Expected/Actual: {bcolors.OKGREEN + expected[i] + bcolors.ENDC}/{actual[i]} [OK]\n"
                self.logger.log(self.class_name, self.show_difference.__name__, message)

        percentage_correct = (correct_count / len(expected)) * 100
        message = f"Percentage of Correctness: {percentage_correct:.2f}%"
        self.logger.log(self.class_name, self.show_difference.__name__, message)

    def save_hexa_as_bin(self, path: str, hexa: list):
        """
        Save the hexadecimal in a binary file
        :param path: path of the file
        :param hexa: hexadecimal to save
        :return:
        """
        message = f"Saving the hexadecimal in {path}"
        self.logger.log(self.class_name, self.save_hexa_as_bin.__name__, message)
        with open(path, 'w') as file:
            file.write("v2.0 raw\n")
            for hexa_line in hexa:
                file.write(hexa_line + " ")

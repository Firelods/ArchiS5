import inspect
import os
import json

from bcolors import bcolors
from src.main.python.functions import Functions

def get_instruction_set():
    # Read the json file locate at : src/main/resources/instructions_set.json
    with open("../../../src/main/resources/instructions_set.json", 'r') as file:
        return json.load(file)

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


def instruction_to_upper(instruction: list):
    """
    Convert instruction to upper case
    :param instruction:
    :return:
    """
    instruction[0] = instruction[0].upper()
    return instruction


def fill_labels(_function: Functions, asm_lines: list):
    """

    :param _function:
    :param asm_lines:
    :return:
    """
    number_of_instructions_labels = 0
    line_number = 0
    for line in asm_lines:
        _function.define_label(line, number_of_instructions_labels)
        line_number += 1
        if is_valid_line(line):
            number_of_instructions_labels += 1

    _function.set_number_of_instructions_labels(number_of_instructions_labels)
    _function.set_number_of_labels(line_number)


def parse_asm(_function: Functions, instruction_sets: list, asm_lines: list):
    """

    :param _function:
    :param instruction_sets:
    :param asm_lines:
    :return:
    """
    binary = []
    line_number = 0
    for line in asm_lines:
        b = parse_line(_function, instruction_sets, line, line_number)
        if b is not None:
            binary.append(b)
            line_number += 1
    return binary


def parse_line(_function: Functions, instruction_sets: list, line: str, line_number: int):
    """

    :param line_number:
    :param _function:
    :param instruction_sets:
    :param line:
    :return:
    """
    binary = None
    if is_valid_line(line):
        line = line.replace("\t", " ").replace("\n", "")
        binary = convert_into_binary(_function, instruction_sets, line.split(), line_number)
    return binary


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


def convert_into_binary(_function: Functions, instruction_set: list, line: list, line_number: int):
    """
    Convert assembly into binary
    :param _function:
    :param instruction_set:
    :param line:
    :return:
    """
    binaries = ""
    line = instruction_to_upper(line)
    # check to witch instruction set the instruction belongs
    for instruction in instruction_set:
        for key, values in instruction.items():
            if line[0] == key and not values["doublon"]:
                line = filter_operands(line)
                print(line)
                binaries = call_function(_function, line, instruction[key]["function"], line_number)
            elif line[0] == key and values["doublon"]:
                # check to wich double instruction set the instruction belongs
                # for that we need to check if all the operands correspond to one of the double instruction set
                # if it does we can call the function
                # if not we can't call the function
                temp = filter_operands(line)
                # Count the number of r and the number of #imm
                r, imm = number_of_r_and_imm(temp)
                # Check if the number of r and #imm correspond to the double instruction set
                if r == values["R"] and imm == values["#imm"]:
                    print(line)
                    binaries = call_function(_function, line, instruction[key]["function"], line_number)
    if binaries == "":
        print(f"Error: {line} is not a valid instruction")
    return binaries


def call_function(_function: Functions, instruction: list, method_name: str, line_number: int):
    """
    Call the function
    :param line_number:
    :param _function:
    :param instruction:
    :param method_name:
    :return:
    """
    # Check if the method_name exists in the _function class
    if hasattr(_function, method_name):
        # Get the method using getattr
        method = getattr(_function, method_name)
        signature = inspect.signature(method)
        if len(signature.parameters) == 2:
            return method(instruction, line_number)
        # Call the method with the instruction as an argument
        return method(instruction)
    else:
        # Handle the case when the method is not found
        print(f"Error: Method {method_name} not found in class {type(_function).__name__}")
        return None


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


def binary_to_hexa(binary_list: list):
    """
    Convert all the binaries in to hexadecimal
    :param binary_list:
    :return:
    """
    return [hex(int(binary, 2))[2:].zfill(4) for binary in binary_list]


def read_asm_file(path: str):
    """
    Read the assembly file
    :param path: path of the file
    :return: list of lines of the file
    """
    print(f"Reading {path}")
    lines = []
    with open(path, 'r') as file:
        # if the file is empty return None
        if file.readline() == "":
            return None
        file.seek(0)
        for line in file.readlines():
            # if the line start with @ in the line, don't take it
            if line == "\n":
                continue
            if line[0] == "@":
                continue
            # if the line start with push or pop in the line, don't take it
            if line.split()[0] == "push" or line.split()[0] == "pop":
                continue
            # if the line start with run: in the line, don't take it
            if line.split()[0] == "run:":
                continue
            # else take the line
            lines.append(line)
    return lines


def read_bin_file(path: str):
    """
    Read the binary file
    :param path: path of the file
    :return: list of lines of the file
    """
    bin_list = []
    with open(path, 'r') as file:
        for line in file.readlines():
            # skip the first line
            if line == "v2.0 raw\n":
                continue
            bin_list = line.split()
    return bin_list


def print_all_files(all_files: dict):
    """
    Print all the files in the directory
    :param all_files:
    :return:
    """
    print("List of all files:")
    for directory, files in all_files.items():
        # print the last / and the directory
        print(f"Directory: {directory.split('/')[-1]}")
        for file in files:
            print(f"\t{file}")
    print()


def ask_file_name():
    """
    Ask the name of the file
    :return:
    """
    # print all the files in the directory
    all_files, number_of_files = found_all_files()
    print_all_files(all_files)
    # ask the name of the file
    file_name = list(str((input("Enter the number(s) of the file(s) you want to convert (all) for all the files: "))).split())
    if file_name[0] == "all":
        file_name = [str(i) for i in range(number_of_files)]
    file_names = found_file_from_number(all_files, file_name)
    return file_names


def found_file_from_number(all_files: dict, file_numbers: list):
    """
    Found all the files from the number
    :param all_files:
    :param file_numbers:
    :return:
    """
    file_names = []
    for file_number in file_numbers:
        for directory, files in all_files.items():
            for file in files:
                if file_number == file.split()[0]:
                    file_names.append(f"{directory}/{file.split()[1]}")
    return file_names


def found_all_files():
    """
    Found all files in the directory : src/tests/resources/asm_files
    :return:
    """
    all_directory = os.listdir("../../../src/tests/resources/asm_files")
    all_files = {}
    # the key will be the path to the directory
    # and the value all the files in the directory
    count = 0
    for directory in all_directory:
        all_files[f"../../../src/tests/resources/asm_files/{directory}"] = os.listdir(
            f"../../../src/tests/resources/asm_files/{directory}")
        # add a specific number for the file
        for i in range(len(all_files[f"../../../src/tests/resources/asm_files/{directory}"])):
            all_files[f"../../../src/tests/resources/asm_files/{directory}"][
                i] = f"{count} {all_files[f'../../../src/tests/resources/asm_files/{directory}'][i]}"
            count += 1
    return all_files, count


def show_difference(expected: list, actual: list):
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
            print("Expected/Actual:", end=" ")
            for j in range(len(expected[i])):
                if expected[i][j] != actual[i][j]:
                    print(bcolors.FAIL + expected[i][j] + bcolors.ENDC, end="")
                else:
                    print(expected[i][j], end="")
            print(f"/{actual[i]} [KO]\n")
        else:
            correct_count += 1
            print(f"Expected/Actual: {bcolors.OKGREEN + expected[i] + bcolors.ENDC}/{actual[i]} [OK]\n")

    percentage_correct = (correct_count / len(expected)) * 100
    print(f"Percentage of Correctness: {percentage_correct:.2f}%")


def save_hexa_as_bin(path: str, hexa: list):
    """
    Save the hexadecimal in a binary file
    :param path: path of the file
    :param hexa: hexadecimal to save
    :return:
    """
    print(f"Saving the hexadecimal in {path}")
    with open(path, 'w') as file:
        file.write("v2.0 raw\n")
        for hexa_line in hexa:
            file.write(hexa_line + " ")


def main():
    instruction_sets = get_instruction_set()
    # transform it to list of shift_add_sub_mov, adds_subs, data_processing, load_store, miscellaneous_16_bits,
    # unconditional_branch, conditional_branch
    instruction_sets = [instruction_sets[key] for key in instruction_sets]

    # Ask the name of the file
    file_names = ask_file_name()

    # Read the assembly file
    assembly_code = []
    for file_name in file_names:
        asm_file_lines = read_asm_file(file_name)
        if len(asm_file_lines) != 0:
            assembly_code.append(asm_file_lines)

    # Read the binary file
    expected = []
    for file_name in file_names:
        file_name = file_name.replace("asm_files", "expected_binaries").replace(".s", ".bin")
        expected.append(read_bin_file(file_name))

    # Fill the labels
    _function = Functions()
    for i in range(len(assembly_code)):
        run(_function, instruction_sets, assembly_code[i], expected[i], file_names[i])


def run(_function: Functions, instruction_sets: list, assembly_code: list, expected: list, path: str):
    fill_labels(_function, assembly_code)

    # Parse the assembly code
    binary = parse_asm(_function, instruction_sets, assembly_code)

    # Convert the binary into hexadecimal
    hexa = binary_to_hexa(binary)

    path = path.replace("asm_files", "output_binaries").replace(".s", ".bin")

    # Save the hexadecimal in a binary file
    save_hexa_as_bin(path, hexa)

    # Read the binary file
    actual = read_bin_file(path)

    # Show the difference between the expected and actual output
    show_difference(expected, actual)


if __name__ == '__main__':
    main()

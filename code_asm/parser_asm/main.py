shift_add_sub_mov = {
    "LSL": {"opcode": "00000", "#imm": 5, "Rm": 3, "Rd": 3},
    "LSR": {"opcode": "00001", "#imm": 5, "Rm": 3, "Rd": 3},
    "ASR": {"opcode": "00010", "#imm": 5, "Rm": 3, "Rd": 3},
    "ADD": {"opcode": "0001110", "#imm": 3, "Rm": 3, "Rd": 3},
    "SUB": {"opcode": "0001111", "#imm": 3, "Rm": 3, "Rd": 3},
    "MOV": {"opcode": "00100", "Rd": 3, "#imm": 8},
}

add_sub_specials = {
    "ADD": {"opcode": "0001100", "Rm": 3, "Rn": 3, "Rd": 3},
    "SUB": {"opcode": "0001101", "Rm": 3, "Rn": 3, "Rd": 3},
}

data_processing = {
    "AND": {"opcode": "0100000000", "Rm": 3, "Rdn": 3},
    "EOR": {"opcode": "0100000001", "Rm": 3, "Rdn": 3},
    "LSL": {"opcode": "0100000010", "Rm": 3, "Rdn": 3},
    "LSR": {"opcode": "0100000011", "Rm": 3, "Rdn": 3},
    "ASR": {"opcode": "0100000100", "Rm": 3, "Rdn": 3},
    "ADC": {"opcode": "0100000101", "Rm": 3, "Rdn": 3},
    "SBC": {"opcode": "0100000110", "Rm": 3, "Rdn": 3},
    "ROR": {"opcode": "0100000111", "Rm": 3, "Rdn": 3},
    "TST": {"opcode": "0100001000", "Rm": 3, "Rn": 3},
    "RSB": {"opcode": "0100001001", "Rn": 3, "Rd": 3},
    "CMP": {"opcode": "0100001010", "Rm": 3, "Rn": 3},
    "CMN": {"opcode": "0100001011", "Rm": 3, "Rn": 3},
    "ORR": {"opcode": "0100001100", "Rm": 3, "Rdn": 3},
    "MUL": {"opcode": "0100001101", "Rn": 3, "Rdm": 3},
    "BIC": {"opcode": "0100001110", "Rm": 3, "Rdn": 3},
    "MVN": {"opcode": "0100001111", "Rm": 3, "Rd": 3},
}

load_store = {
    "STR": {"opcode": "10010", "Rt": 3, "#imm": 8},
    "LDR": {"opcode": "10011", "Rt": 3, "#imm": 8},
}

miscellaneous_16_bits = {
    "ADD": {"opcode": "101100000", "#imm": 7},
    "SUB": {"opcode": "101100001", "#imm": 7},
}

conditional_branch = {
    "BEQ": {"opcode": "11010000", "#imm": 8},
    "BNE": {"opcode": "11010001", "#imm": 8},
    "BCS": {"opcode": "11010010", "#imm": 8},
    "BCC": {"opcode": "11010011", "#imm": 8},
    "BMI": {"opcode": "11010100", "#imm": 8},
    "BPL": {"opcode": "11010101", "#imm": 8},
    "BVS": {"opcode": "11010110", "#imm": 8},
    "BVC": {"opcode": "11010111", "#imm": 8},
    "BHI": {"opcode": "11011000", "#imm": 8},
    "BLS": {"opcode": "11011001", "#imm": 8},
    "BGE": {"opcode": "11011010", "#imm": 8},
    "BLT": {"opcode": "11011011", "#imm": 8},
    "BGT": {"opcode": "11011100", "#imm": 8},
    "BLE": {"opcode": "11011101", "#imm": 8},
    "BAL": {"opcode": "11011110", "#imm": 8},
}


def filter_operands(operands: list):
    """
    Remove the # from the operands
    Remove the sp from the operands
    Add #0 if there is sp without #imm
    :param operands:
    :rtype: list
    :return:
    """
    # if there is sp, #imm we need to remove sp
    # if there is sp without #imm we need to remove sp and replace with #0
    # and after we need to check to which key: value the instruction corresponds
    # The operands looks like this: ["sp", "#3"], ["sp"], ["r0", "r1", "r2"], ["r0", [sp, #3]]
    precedent = None
    if len(operands) == 1:
        if operands[0] == "sp":
            operands[0] = "#0"
    else:
        for operand in operands:
            # check if it's a list
            if isinstance(operand, list):
                # iterate over the list
                if len(operand) != 1:
                    for element in operand:
                        # if the element is sp, remove it
                        if element == "sp":
                            operand.remove(element)
                else:
                    if operand[0] == "sp":
                        operand[0] = "#0"
            elif operand == "sp":
                    operands.remove(operand)
            else:
                 # check all the r
                 # if r is different from the precedent
                pass

def get_opcode(instruction, operands, instruction_sets):
    """
    Return the opcode of the instruction,
    in function of the instruction and the number of operands
    :param instruction_sets: list of instruction sets
    :param instruction: mnemonic of the instruction
    :param operands: number of operands of the instruction
    :return: opcode of the instruction
    """
    for instruction_set in instruction_sets:
        for key, value in instruction_set.items():
            print(key, instruction, value, operands)
            if key == instruction:
                filter_operands(operands)
                print(operands, value, len(operands))
                if len(operands) == len(value) - 1:
                    return {key: value}

    print("Error: Instruction not found")
    exit(1)


def instruction_to_uppercase(instruction):
    """
    Return the instruction in uppercase
    :param instruction: instruction to convert
    :return: instruction in uppercase
    """
    return instruction.upper()


# Example usage
instruction_sets = [shift_add_sub_mov, add_sub_specials, data_processing, load_store, miscellaneous_16_bits,
                    conditional_branch]

assembly_code = [
    "sub sp, #12",
    "movs r0, #0",
    "str r0, [sp, #8]",
    "movs r1, #1",
    "str r1, [sp, #4]",
    "ldr r1, [sp, #8]",
    "ldr r2, [sp, #4]",
    "adds r1, r1, r2",
    "str r1, [sp]",
    "add sp, #12"
]


def assemble(assembly_code, instruction_sets):
    binary_instructions = []

    for assembly_instruction in assembly_code:
        # Tokenize assembly instruction
        tokens = assembly_instruction.replace(",", "").split()

        # Extract operation and operands
        operation = instruction_to_uppercase(tokens[0])
        operands = tokens[1:]

        # Get opcode from instruction sets
        opcode = get_opcode(operation, operands, instruction_sets)
        """
        # Convert operands to binary
        binary_operands = []
        for operand in operands:
            if operand.startswith("r"):
                # Register operand
                binary_operands.append(format(int(operand[1:]), '03b'))
            elif operand.startswith("#"):
                # Immediate operand
                binary_operands.append(format(int(operand[1:]), '08b'))
            else:
                # Other operands (e.g., [sp, #8])
                # Handle these cases based on your specific requirements
                pass

        # Combine opcode and operands to get the binary instruction
        binary_instruction = opcode + ''.join(binary_operands)

        binary_instructions.append(binary_instruction)
    """
    return binary_instructions


# Example usage
binary_instructions = assemble(assembly_code, instruction_sets)

# Print the binary representation of each instruction
for i, binary_instruction in enumerate(binary_instructions):
    print(f"Instruction {i + 1}: {binary_instruction}")

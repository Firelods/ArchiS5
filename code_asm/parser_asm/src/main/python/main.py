import sys

from src.main.python.asm_parser import AsmParser
from src.main.python.asm_reader import AsmReader
from src.main.python.file_founder import FilesFounder
from src.main.python.functions import Functions
from src.main.python.logger import Logger


def main(_verbose: bool, _save_log: bool):
    print("\nWelcome to the assembler")
    print("This program will convert assembly code to binary code")
    print("You can find the assembly code in the directory: src/tests/resources/asm_files")
    print("You can find the binary code in the directory: src/tests/resources/bin_files")
    print("You can find the expected binary code in the directory: src/tests/resources/expected_bin_files")
    print("You can find the output file in the directory: src/main/resources/output_files")
    print("You can find the log file in the directory: src/main/resources/log_files\n")

    logger = Logger(_verbose, _save_log)
    asm_parser = AsmParser(logger)
    files_founder = FilesFounder(logger)
    asm_reader = AsmReader(logger)

    # Ask the user for file names
    files_founder.ask_file_name()

    # Read the assembly file
    assembly_code = []
    expected = []
    for file_name in files_founder.file_names:
        asm_file_lines = asm_reader.read_asm_file(file_name)
        asm_bin_file_lines = asm_reader.read_bin_file(file_name)
        if len(asm_file_lines) != 0:
            assembly_code.append(asm_file_lines)
            expected.append(asm_bin_file_lines)

    # Fill the labels
    _function = Functions(logger)
    for i in range(len(assembly_code)):
        asm_parser.run(assembly_code[i], expected[i], files_founder.file_names[i], asm_reader)


if __name__ == '__main__':
    # Get the arguments
    verbose = False
    save_log = False
    # get the list of arguments
    arguments = sys.argv
    # check if the user want to save the log
    if "-sl" in arguments or "--save-log" in arguments:
        save_log = True
    # check if the user want to have a verbose mode
    if "-v" in arguments or "--verbose" in arguments:
        verbose = True
    main(verbose, save_log)

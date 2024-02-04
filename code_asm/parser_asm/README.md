# Assembly to Binary Converter

## Introduction

Welcome to the assembler! This program converts assembly code to binary code. It provides a simple and efficient way to
translate assembly instructions into their corresponding binary representations.

## Usage

Follow these steps to use the assembler:

1. **Clone the Repository:**

```bash
git clone https://github.com/Firelods/ArchiS5.git
```

2. **Navigate to the Project Directory:**

```bash
cd code_asm/src/main/python
```

3. **Run the Program:**

````
python main.py [-v/--verbose] [-sl/--save-log]
````

- Use the `-v` or `--verbose` option for verbose mode.
- Use the `-sl` or `--save-log` option to save logs.
<br>
4. **Provide Assembly Files:**
- Place your assembly code files in the directory: `src/tests/resources/asm_files`.

5. **View Output:**

- The binary code will be generated and stored in the directory: `src/main/resources/output_files`.
- Logs will be saved in the directory: `src/main/resources/log_files`.

## Testing

Unit tests are provided to ensure the correctness of the assembler. Run the tests using:

The test files are located in the `tests` directory.

```bash
python -m unittest
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.

To add new functions to parse in the parser, you would follow these steps:

1. **Understanding the JSON Structure:**
   Review the structure of the JSON file provided. Each key in the JSON corresponds to a category of assembly
   instructions, and each value is a dictionary containing information about the instructions within that category.

2. **Identify the Relevant Category:**
   Determine which category your new instruction falls under based on its functionality. For example, if your
   instruction is a data processing operation like AND, EOR, or LSL, it would fall under the `data_processing` category.

3. **Define the Instruction Function:**
   Create a new function in the `Functions` class in `functions.py` that implements the parsing logic for your
   instruction. This function should accept an expression (list of tokens) representing the assembly instruction and any
   other necessary parameters. Implement the logic to generate the corresponding binary representation of the
   instruction.

4. **Update the JSON File:**
   Add an entry for your new instruction in the JSON file under the appropriate category. Provide information such as
   whether the instruction has any duplicates, the number of immediate operands (`#imm`), the number of register
   operands (`R`), and the name of the function you defined in step 3.

5. **Modify the Parser Logic:**
   Update the parser logic in `asm_instructions.py` to handle your new instruction. You may need to modify existing
   methods or add new ones to support the parsing and generation of binary code for the new instruction.

6. **Test the Implementation:**
   Test your implementation to ensure that the new instruction is correctly parsed and converted into binary code. You
   can use unit tests or sample assembly code files to verify the functionality of your parser.

7. **Document the Changes:**
   Update the README or any relevant documentation to include information about the new instruction you added, its
   syntax, and how to use it in the parser.

By following these steps, you can extend the functionality of the parser to support additional assembly instructions.



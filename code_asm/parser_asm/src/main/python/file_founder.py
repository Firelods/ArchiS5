import os

from src.main.python.logger import Logger


class FilesFounder:

    def __init__(self, logger: Logger):
        self.all_files = None
        self.file_names = None
        self.count = None
        self.logger = logger
        self.class_name = type(self).__name__
        self.found_all_files()

    def found_all_files(self):
        """
        Found all files in the directory : src/tests/resources/asm_files
        :return:
        """
        all_directory = os.listdir("../../../src/tests/resources/asm_files")
        all_files = {}
        # the key will be the path to the directory
        # and the value all the files in the directory
        count = 0
        message = "Scanning directories"
        self.logger.log(self.class_name, self.found_all_files.__name__, message)
        for directory in all_directory:
            message = f"Scanning {directory}"
            self.logger.log(self.class_name, self.found_all_files.__name__, message)
            all_files[f"../../../src/tests/resources/asm_files/{directory}"] = os.listdir(
                f"../../../src/tests/resources/asm_files/{directory}")
            # add a specific number for the file
            for i in range(len(all_files[f"../../../src/tests/resources/asm_files/{directory}"])):
                message = f"Scanning {all_files[f'../../../src/tests/resources/asm_files/{directory}'][i]}"
                self.logger.log(self.class_name, self.found_all_files.__name__, message)
                all_files[f"../../../src/tests/resources/asm_files/{directory}"][
                    i] = f"{count} {all_files[f'../../../src/tests/resources/asm_files/{directory}'][i]}"
                count += 1
        self.count = count
        self.all_files = all_files

    def print_all_files(self):
        """
        Print all the files in the directory
        :return:
        """
        print("List of all files:")
        for directory, files in self.all_files.items():
            # print the last / and the directory
            print(f"Directory: {directory.split('/')[-1]}")
            for file in files:
                print(f"\t{file}")
        print()

    def ask_file_name(self):
        """
        Ask the name of the file
        :return:
        """
        # print all the files in the directory
        self.print_all_files()
        # ask the name of the file
        file_name = list(
            str((input("Enter the number(s) of the file(s) you want to convert (all) for all the files: "))).split())
        if file_name[0] == "all":
            file_name = [str(i) for i in range(self.count)]
        self.file_names = self.found_file_from_number(file_name)

    def found_file_from_number(self, file_numbers: list):
        """
        Found all the files from the number
        :param file_numbers:
        :return:
        """
        file_names = []
        message = f"Found files from numbers {file_numbers}"
        self.logger.log(self.class_name, self.found_file_from_number.__name__, message)
        for file_number in file_numbers:
            for directory, files in self.all_files.items():
                for file in files:
                    message = f"Found {file} from number {file_number}"
                    self.logger.log(self.class_name, self.found_file_from_number.__name__, message)
                    if file_number == file.split()[0]:
                        file_names.append(f"{directory}/{file.split()[1]}")
        return file_names

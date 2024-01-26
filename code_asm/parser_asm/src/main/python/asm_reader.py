from logger import Logger


class AsmReader:

    def __init__(self, logger: Logger):
        self.class_name = type(self).__name__
        self.logger = logger

    def read_asm_file(self, path):
        """
        Read the assembly file
        :return: list of lines of the file
        """
        message = f"Reading {path}"
        self.logger.log(self.class_name, self.read_asm_file.__name__, message)
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

    def read_bin_file(self, path):
        """
        Read the binary file
        :return: list of lines of the file
        """
        bin_list = []
        path = path.replace("asm_files", "expected_binaries").replace(".s", ".bin")
        message = f"Reading {path}"
        self.logger.log(self.class_name, self.read_bin_file.__name__, message)
        try:
            with open(path, 'r') as file:
                for line in file.readlines():
                    # skip the first line
                    if line == "v2.0 raw\n":
                        continue
                    bin_list = line.split()
        except FileNotFoundError:
            bin_list = None
        return bin_list

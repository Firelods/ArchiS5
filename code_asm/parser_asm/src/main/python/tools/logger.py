import os

from tools.bcolors import bcolors


class Logger:

    def __init__(self, verbose, save_log):
        self.warning_color = bcolors.WARNING
        self.fail_color = bcolors.FAIL
        self.end = bcolors.ENDC
        self.verbose = verbose
        self.save_log_activate = save_log
        # get the last log file and add 1 to the number
        self.log_path = None
        if self.save_log_activate:
            self.get_last_log_name()

    def get_last_log_name(self):
        """
        Get the last log name
        :return:
        """
        # found in th directory ../resources/logs the last log file
        last_log = None
        for file in os.listdir("../resources/logs"):
            if file.endswith(".txt"):
                last_log = file
        # if the directory is empty
        if last_log is None:
            self.log_path = "../resources/logs/log_0.txt"
            return
        # get the number of the last log file
        number = last_log.split("_")[1].split(".")[0]
        # add 1 to the number
        number = int(number) + 1
        self.log_path = f"../resources/logs/log_{number}.txt"

    def log(self, class_name: str, function_name: str, message, end="\n"):
        if self.verbose:
            print(f"LOGGER({class_name}[{function_name}]): {message}", end=end)
        if self.save_log_activate:
            self.save_log(class_name, function_name, message, end)

    def log_only_message(self, message, end="\n"):
        if self.verbose:
            print(f"{message}", end=end)
        if self.save_log_activate:
            self.save_log(message, end)

    def warning(self, class_name: str, function_name: str, message, end="\n"):
        if self.verbose:
            print(f"{self.warning_color}WARNING({class_name}[{function_name}]): {message}{self.end}", end=end)
        if self.save_log_activate:
            self.save_log(class_name, function_name, message, end)

    def error(self, class_name: str, function_name: str, message, end="\n"):
        if self.verbose:
            print(f"{self.fail_color}ERROR({class_name}[{function_name}]): {message}{self.end}", end=end)
        if self.save_log_activate:
            self.save_log(class_name, function_name, message, end)

    def save_log(self, class_name: str, function_name: str, message, end="\n"):
        with open(self.log_path, "a") as file:
            file.write(f"LOGGER({class_name}[{function_name}]): {message}{end}")

    def save_log(self, message, end="\n"):
        with open(self.log_path, "a") as file:
            file.write(f"{message}{end}")
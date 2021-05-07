import os
import subprocess


class Shell:

    def __init__(self):
        while True:
            command = input("> ")
            if command == "exit":
                break
            elif command[:3] == "cd ":
                self.cd(command[3:])
            elif command == "help":
                self.psh_help()
            else:
                self.execute_command(command)

    def execute_command(self, command):
        try:
            subprocess.run(command)
        except FileNotFoundError:
            print("'{}' is not recognized as an internal or external "
                  "command,operable program or batch file".format(command))

    def cd(self, path):
        try:
            os.chdir(os.path.abspath(path))
        except FileNotFoundError:
            print("'{}' is not recognized as an internal or external "
                  "command,operable program or batch file".format(path))

    def psh_help(self):
        print("Basic shell implement some basic command")


if __name__ == '__main__':
    shell = Shell()

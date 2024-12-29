#!/usr/bin/python3
"""Make consol"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Console class for back-end"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """C-d command to exit the program\n"""
        return True

    def emptyline(self):
        """an empty line handling"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
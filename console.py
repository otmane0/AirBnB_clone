#!/usr/bin/python3
"""Make consol"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Console class for back-end"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program\n"""
        print()
        return True

    def do_emptyline(self, args):
        """Do nothing on an empty line + ENTER"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
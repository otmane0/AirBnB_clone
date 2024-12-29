#!/usr/bin/python3
"""Make consol"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Console class for back-end"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exit the program"""
        return True

    def do_EOF(self, args):
        """Exit program"""
        print()
        return True

    def do_emptyline(self, args):
        """Empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
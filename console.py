#!/usr/bin/python3
"""console file"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Console"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """for exiting"""
        return True

    def do_quit(self, line):
        """for exiting"""
        return True

    def do_help(self, arg: str) -> bool | None:
        """help func"""
        return super().do_help(arg)

    def emptyline(self):
        """empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

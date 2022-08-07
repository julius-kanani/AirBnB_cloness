#!/usr/bin/python3
""" The console module
This module supplies the HBNBCommand(cmd.Cmd) class.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Defines the HBNBCommand class. """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit Command to exit the hbnb console. """

        return True

    def do_EOF(self, arg):
        """ Exits Console. """

        return True

    def emptyline(self):
        """ Overwriting the emptyline method. """

        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()

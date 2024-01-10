#!/usr/bin/python3
"""
   A generic class to build line-oriented command interpreters.
   Interpreters constructed with this class obey the following conventions:
   cmd module where the console will be built with
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Main class of the console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exiting the program on EOF"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

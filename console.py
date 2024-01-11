#!/usr/bin/python3
"""
   A generic class to build line-oriented command interpreters.
   Interpreters constructed with this class obey the following conventions:
   cmd module where the console will be built with
"""

import cmd
import json
import models
from models import storage

class HBNBCommand(cmd.Cmd):
    """Main class of the console"""
    prompt = '(hbnb) '
    
    def do_create(self, arg):
        """Creates a new instance of Basemodel, save it, print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_object = eval(arg)()
            new_object.save()
            print(new_object.id)
        except NameError:
            print("** class dosen't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id."""
        if not arg:
            print("** class name missing **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key in storage.all():
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.__objects():
            print("** class dosen't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of instances based on class name or all."""
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        elif arg not in storage:
            print("** class dosen't exist **")

    def do_update(self, arg):
        """Updates an instance based on class name and id by adding or updating attribute."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage:
            print("** class dosen't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3].strip('"'))
        obj.save()    

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exiting the program on EOF"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

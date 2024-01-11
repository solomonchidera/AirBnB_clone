#!/usr/bin/python3
"""
   A generic class to build line-oriented command interpreters.
   Interpreters constructed with this class obey the following conventions:
   cmd module where the console will be built with
"""

import cmd
import json
import uuid
from datetime import datetime
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Main class of the console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exiting the program on EOF"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save to JSON file"""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_object = eval(arg)
            new_object.save(self)
            print(new_object.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        # split parsed arguments by the console to test conditions
        args = arg.split()
        try:
            class_name = args[0]
            instance_id = args[1]

            # Load all instances and check if the instance exists
            all_instances = BaseModel.load_instances()
            key = "{}.{}".format(class_name, instance_id)
            if key in all_instances:
                print(all_instances[key])
            else:
                print("** no instance found **")

        # if show id isn't found
        except IndexError:
            print("** instance id missing **")
        # if show object doesn't work
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return

        # split parsed arguments by the console to test conditions
        args = arg.split()
        try:
            class_name = args[0]
            instance_id = args[1]

            # Load all instances and check if the instance exists
            all_instances = BaseModel.load_instances()
            key = "{}.{}".format(class_name, instance_id)
            if key in all_instances:
                del all_instances[key]
                BaseModel.save_instances(all_instances)
            else:
                print("** no instance found **")

        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print string representation of all instances"""
        try:
            if arg:
                class_name = arg
                # Filter instances by class name
                all_instances = BaseModel.load_instances()
                filtered_instances = {k: v for k, v in all_instances.items() if k.startswith(class_name)}
                if filtered_instances:
                    print([str(instance) for instance in filtered_instances.values()])
                else:
                    print("** class doesn't exist **")
            else:
                # Print all instances
                all_instances = BaseModel.load_instances()
                print([str(instance) for instance in all_instances.values()])

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name, id, attribute, and value"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        try:
            class_name = args[0]
            instance_id = args[1]

            # Load all instances and check if the instance exists
            all_instances = BaseModel.load_instances()
            key = "{}.{}".format(class_name, instance_id)
            if key in all_instances:
                # Get the instance to be updated
                instance = all_instances[key]

                # Check if attribute and value are provided
                if len(args) >= 4:
                    attribute_name = args[2]
                    attribute_value = args[3]

                    # Check if attribute is valid and update the instance
                    if hasattr(instance, attribute_name):
                        setattr(instance, attribute_name, eval(attribute_value))
                        instance.save()
                    else:
                        print("** attribute name missing **")
                else:
                    print("** value missing **")
            else:
                print("** no instance found **")

        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

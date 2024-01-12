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
            new_object = eval(arg)
            new_object.save("file.json")
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

        # split parsed arguments by the console to test conditions
        args = arg.split()
        try:
            class_name = args[0]
            instance_id = args[1]

            # Load all instances and check if the instance exists
            all_instances = storage.reload()
            key = "{}.{}".format(class_name, instance_id)
            if key in all_instances:
                print(all_instances[key])
            else:
                print("** no instance found **")

        # if show id isn't found
        except IndexError:
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
        try:
            class_name = args[0]
            instance_id = args[1]

            # Load all instances and check if the instance exists
            all_instances = storage.reload()
            key = "{}.{}".format(class_name, instance_id)
            if key in all_instances:
                del all_instances[key]
                BaseModel.save_instances(all_instances)
            else:
                print("** no instance found **")

        except IndexError:
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
        """Print string representation of all instances"""
        try:
            if arg:
                class_name = arg
                # Filter instances by class name
                all_instances = storage.reload()
                filtered_instances = {k: v for k, v in all_instances.items() if k.startswith(class_name)}
                if filtered_instances:
                    print([str(instance) for instance in filtered_instances.values()])
                else:
                    print("** class doesn't exist **")
            else:
                # Print all instances
                all_instances = storage.reload()
                print([str(instance) for instance in all_instances.values()])

        except NameError:
            print("** class doesn't exist **")
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
        try:
            class_name = args[0]
            instance_id = args[1]

            # Load all instances and check if the instance exists
            all_instances = storage.reload()
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

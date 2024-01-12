#!/usr/bin/python3
"""
   A generic class to build line-oriented command interpreters.
   Interpreters constructed with this class obey the following conventions:
   cmd module where the console will be built with
"""

import cmd
import json
import uuid
import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """ Save the instance to the JSON file """
        objects[self.__class__.__name__ + "." + self.id] = self
        storage.save()

    def __str__(self):
        """ String representation of the instance """
        return f"[{self.__class__.__name__}] ({self.id}) {{'created_at': {self.created_at}, 'id': '{self.id}', 'updated_at': {self.updated_at}}}"

class Storage:
    def save(self):
        """ Save instances to a JSON file (dummy implementation) """
        with open("data.json", "w") as file:
            json.dump({key: str(value) for key, value in objects.items()}, file)

objects = {}
classes = {"BaseModel": BaseModel}
storage = Storage()

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl + D)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_id = args[1]
            key = args[0] + "." + instance_id
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_id = args[1]
            key = args[0] + "." + instance_id
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of instances"""
        args = arg.split()
        instances = []
        if args and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            if args and args[0] in classes:
                class_name = args[0]
                for key, value in objects.items():
                    if key.startswith(class_name):
                        instances.append(str(value))
            else:
                for value in objects.values():
                    instances.append(str(value))
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_id = args[1]
            key = args[0] + "." + instance_id
            if key in objects:
                if len(args) < 4:
                    print("** attribute name missing **")
                elif len(args) < 5:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    attribute_value = args[3]
                    setattr(objects[key], attribute_name, attribute_value)
                    objects[key].save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

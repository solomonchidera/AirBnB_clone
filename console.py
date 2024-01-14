#!/usr/bin/python3
"""
Module Console
"""

import cmd
import shlex
import sys
import models
import uuid
import json
import datetime


class BaseModel:
    """This is the base model that will identity everything"""
    def __init__(self):
        """This is the init method for every instance created"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """ Save the instance to the JSON file """
        objects[self.__class__.__name__ + "." + self.id] = self
        storage.save()

    def __str__(self):
        """ String representation of the instance """
        return f"""[{self.__class__.__name__}]({self.id})
        {{'created_at': {self.created_at}, 'id': '{self.id}',
            'updated_at': {self.updated_at}}}"""
        return f"""[{self.__class__.__name__}]({self.id})
        {{'created_at': datetime.datetime({self.created_at}),
            'id': '{self.id}',
            'updated_at': datetime.datetime({self.updated_at})}}"""


class Storage:
    """This is tthe main sotrage file that will store everything"""
    def save(self):
        """ Save instances to a JSON file (dummy implementation) """
        with open("data.json", "w") as file:
            json.dump(
                    {key: str(value) for key, value in objects.items()}, file)


objects = {}
classes = {"BaseModel": BaseModel}
storage = Storage()


class HBNBCommand(cmd.Cmd):
    """HBNB Class """
    prompt = '(hbnb) '

    classes = {'BaseModel': BaseModel}

    def do_quit(self, argument):
        """ Defines quit option"""
        return True

    def do_EOF(self, argument):
        """ Defines EOF option"""
        print()
        return True

    def emptyline(self):
        """ Defines Empty option"""
        pass

    def do_create(self, argument):
        """Creates an instance of BaseModel"""
        if argument:
            if argument in self.classes:
                # instance = models.base_model.BaseModel()
                get_class = getattr(sys.modules[__name__], argument)
                instance = get_class()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def do_show(self, argument):
        """string representation based on the class name and id"""
        token = shlex.split(argument)
        if len(token) == 0:
            print("** class name missing **")
        elif len(token) == 1:
            print("** instance id missing **")
        elif token[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dic = models.storage.all()
            # Key has format <className>.id
            keyU = token[0] + '.' + str(token[1])
            if keyU in dic:
                print(dic[keyU])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, argument):
        """Deletes an instance based on the class name and id"""
        tokens = shlex.split(argument)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return
        elif tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            dic = models.storage.all()
            # Key has format <className>.id
            key = tokens[0] + '.' + tokens[1]
            if key in dic:
                del dic[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, argument):
        """all string representation of all instances"""
        token_set = shlex.split(argument)
        lists = []
        dic = models.storage.all()
        # show all if no class is passed
        if len(token_set) == 0:
            for key in dic:
                rep_Class = str(dic[key])
                lists.append(rep_Class)
            print(lists)
            return

        if token_set[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            # Representation for a specific class
            rep_Class = ""
            for key in dic:
                className = key.split('.')
                if className[0] == token_set[0]:
                    rep_Class = str(dic[key])
                    lists.append(rep_Class)
            print(lists)

    def do_update(self, argument):
        """Updates an instance based on the class name and id """
        token1 = shlex.split(argument)
        if len(token1) == 0:
            print("** class name missing **")
            return
        elif len(token1) == 1:
            print("** instance id missing **")
            return
        elif len(token1) == 2:
            print("** attribute name missing **")
            return
        elif len(token1) == 3:
            print("** value missing **")
            return
        elif token1[0] not in self.classes:
            print("** class doesn't exist **")
            return
        keyI = token1[0] + "." + token1[1]
        dicI = models.storage.all()
        try:
            instanceU = dicI[keyI]
        except KeyError:
            print("** no instance found **")
            return
        try:
            typeA = type(getattr(instanceU, token1[2]))
            token1[3] = typeA(token1[3])
        except AttributeError:
            pass
        setattr(instanceU, token1[2], token1[3])
        models.storage.save()


if __name__ == '__main__':
    """infinite loop"""
    HBNBCommand().cmdloop()

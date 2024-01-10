#!/usr/bin/python3
"""This is the saving engine model"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """serializes instances to a JSON file and
    deserializes JSON file to instances:"""

    __file_path = "file.json"
    # path to the JSON file (ex: file.json)
    _objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__+ "." str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        json_new_obj = {}
        # I created an empty string to store the objects inside
        for key in self.__objects:
            json_new_obj[key] = self.__objects[key].to_dict()

            with open (self.__file_path, 'w') as f:
                json.dump(json_new_obj, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        try :
            with open (self.__file_path, 'r', encoding="UTF8") as f:
                for key, value in json.load(f).items():
                    att_value = eval(value["__class__"])(**value)
                    self.__objects[key] = att_value
        except FileNotFoundError:
            pass

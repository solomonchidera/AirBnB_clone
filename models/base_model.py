#!/usr/bin/python3
"""This is the base class for everything in this module"""


import uuid
from datetime import datetime
import models


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

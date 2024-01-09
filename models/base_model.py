#!/usr/bin/python3
"""This is the base class for everything in this module"""
import uuid
from datetime import datetime


class BaseModel:
    """This is the grandfather for all of the upcoming classes"""
    def __init__(self, *args, **kwargs):
        """The constructor"""
        if kwargs:
            for key, date_value in kwargs.items():
                if key == "created_at":
                    date_time = '%Y-%m-%dT%H:%M:%S.%f'
                    date_value = datetime.strptime(date_value, date_time)

                    if key == "updated_at":
                        date_value = datetime.strptime(date_value, date_time)
                        if key != "__class__":
                            setattr(self, key, date_value)

        else:
            self.id = str(uuid.uuid4())
            # save new created at
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # store it by a saving mechanisim JSON

    def __str__(self):
        """Printing the objects str method"""

        new_class = self.__class__.__name__
        return "[{}]({}){}".format(new_class, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""

        self.updated_at = datetime.now()
        # saving mechanism using JSON

    def to_dict(self):

        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        dic_copy = self.__dict__.copy()
        dic_copy["created_at"] = self.created_at.isoformat()
        dic_copy["updated_at"] = self.updated_at.isoformat()
        dic_copy['__class__'] = self.__class__.__name__
        return dic_copy

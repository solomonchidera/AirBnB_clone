#!/usr/bin/python3
"""This model is to assure your comfort"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that is inherting from base model"""
    name = ""

    def __init__(self, *args, **kwargs):
        """The main constructor"""
        super().__init__(self, *args, **kwargs)

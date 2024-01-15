#!/usr/bin/python3
"""This class is aiming to prodcue any new object
named as a City"""

from models.base_model import BaseModel


class City(BaseModel):
    """This is the main big class that every city will inhirit from"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(self, *args, **kwargs)

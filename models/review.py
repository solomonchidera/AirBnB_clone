#!/usr/bin/python3
"""This is the class that will make you add cute new reviews"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The base class of reviews"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """The main constructor for everything related to reviews"""
        super().__init__(self, *args, **kwargs)

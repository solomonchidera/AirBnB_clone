#!/usr/bin/python3
"""This is the first object as a user"""

from models.base_model import BaseModel


class User(BaseModel):
    """This is the user that will inhereit from the base class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

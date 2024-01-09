#!/usr/bin/python3
"""small class that will inherit from the BASE"""


from models.base_model import BaseModel


class User(BaseModel):
    """Class user that will be created whenver a new object comes"""
    email = ""
    password = ""
    f_name = ""
    l_name = ""

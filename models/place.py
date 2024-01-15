#!/usr/bin/python3
"""This is the class that will give you a guide for everything"""

from models.base_model import BaseModel


class Place(BaseModel):
    """The class that will descirbe the plave for you"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    # empty list: it will be the list of Amenity.id later
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """The main constructor"""
        self().__init__(self, *args, **kwargs)

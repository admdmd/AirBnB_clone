#!/usr/bin/python3
"""A new class inherist from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that inherit from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

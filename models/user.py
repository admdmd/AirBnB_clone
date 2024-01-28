#!/usr/bin/python3
"""The User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user by various attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

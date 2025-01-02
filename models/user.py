#!/usr/bin/python3
"""Class User"""
from base_model import BaseModel

class User(BaseModel):
    """User in the console"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

#!/usr/bin/python3
"""
classe that inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    define City class that
    inherits from BaseModel
    """
    state_id = ""
    name = ""

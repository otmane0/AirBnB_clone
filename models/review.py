#!/usr/bin/python3
"""
classe that inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    define Review class that
    inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

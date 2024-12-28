#!/usr/bin/python3

"""Base class of all models"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Class base of next classes and obj"""
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """Class name with atr"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save obj"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Make dic"""
        my_dic = {}
        for key, value in self.__dict__.items():
            my_dic[key] = value

        my_dic["__class__"] = self.__class__.__name__
        my_dic["created_at"] = self.created_at.isoformat()
        my_dic["updated_at"] = self.updated_at.isoformat()
        return my_dic

#!/usr/bin/python3

"""Base class of all models"""

from uuid import uuid4
from datetime import datetime
from models.__init__ import storage

class BaseModel:
    """Class base of next classes and obj"""
    def __init__(self, *args, **kwargs):
        """Initialize the instance with unique attributes (Public instance attributes)"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new()
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.fromisoformat(value)

                else:
                    self.__dict__[key] = value


    def __str__(self):
        """Class name with atr"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Make dic"""
        my_dic = {}
        for key, value in self.__dict__.items():
            my_dic[key] = value

        my_dic["__class__"] = self.__class__.__name__
        my_dic["created_at"] = self.created_at.isoformat()
        my_dic["updated_at"] = self.updated_at.isoformat()
        return my_dic
#!/usr/bin/python3
"""Base File"""

import models

from datetime import datetime
from uuid import uuid4



class BaseModel:
    """Define Class"""

    def __init__(self, *args, **kwargs):
        """Define Class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key in kwargs:
                if key == "__class__":
                    pass
                elif key == "id":
                    self.id = kwargs[key]
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key], "\
%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key], "\
%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Define Class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Define Class"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Define Class"""
        dictionary = {}
        for key in self.__dict__:
            dictionary[key] = self.__dict__[key]
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary


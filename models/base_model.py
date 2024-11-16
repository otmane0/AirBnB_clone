#!/usr/bin/python3
"""Basemodel class"""

import uuid
from datetime import datetime

class BaseModel:
    """Main base for all next classes"""
    def __init__(self, *args, **kwargs):
        """Init"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """Print class"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Update date_time"""
        self.updated_at = datetime.now()
    def to_dict(self):
        """Return a dictionary of all instance"""
        """my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__

        return my_dict
"""
        my_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value

        my_dict['__class__'] = self.__class__.__name__
        return my_dict


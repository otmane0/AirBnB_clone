#!/usr/bin/python3
"""Base File"""
from datetime import datetime
import uuid



class BaseModel:
    """Define Class"""

    def __init__(self, *args, **kwargs):
        """Define Class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key == 'created_at':
                    self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()

    def __str__(self):
        """Define Class"""
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}"

    def save(self):
        """Define Class"""
        self.updated_at = datetime.now().isoformat()
        storage.new(self)
        storage.save

    def to_dict(self):
        """Define Class"""
        new_dictionary = self.__dict__.copy()
        new_dictionary['__class__'] = self.__class__.__name__
        new_dictionary['created_at'] = self.created_at
        new_dictionary['updated_at'] = self.updated_at

        return new_dictionary

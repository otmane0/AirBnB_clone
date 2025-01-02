#!/usr/bin/python3

"""Defines the BaseModel class for all application models."""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """BaseModel class to serve as a foundation for other models."""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

            Args:
                *args: Unused.
                **kwargs (dict): Key-value pairs for instance initialization.
                    If kwargs is provided, the instance is reconstructed
                    from a dictionary (e.g., from JSON data).
                    Otherwise, a new instance is created with default attributes.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self) #Add the instance  with atrr to storage (class.id) => self.__objects
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
        from models import storage
        storage.save() # Save the instance with attributes to Sotrage

    def to_dict(self):
        """Convert the instance into a dictionary format for JSON serialization.

        Returns:
            dict: A dictionary representation of the instance.
        """
        my_dic = {}
        for key, value in self.__dict__.items():
            my_dic[key] = value

        my_dic["__class__"] = self.__class__.__name__
        my_dic["created_at"] = self.created_at.isoformat()
        my_dic["updated_at"] = self.updated_at.isoformat()
        return my_dic

#!/usr/bin/python3
"""This class for data"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects in __objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to __objects with key <class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        objects_dict = {}
        for key, obj in self.__objects.items():
            objects_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects (if the file exists)."""
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path, "r") as file:
            objects_dict = json.load(file)
        for key, value in objects_dict.items():
            class_name = value.get("__class__")
            if class_name == "BaseModel":
                self.__objects[key] = BaseModel(**value)

#!/usr/bin/python3
"""This class for data"""
from models.base_model import BaseModel
import json
import os  # for checking if the file exists

class FileStorage:
    """Storage data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Add new object to the dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()

        # Write the dictionary to the JSON file
        with open(self.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        # Check if the file exists
        if not os.path.exists(self.__file_path):
            return  # If the file doesn't exist, do nothing

        # Open and read the file
        with open(self.__file_path, "r") as file:
            try:
                objects_dict = json.load(file)
            except json.JSONDecodeError:
                return  # If the file is empty or has invalid data, do nothing

        # Reload objects into __objects
        for key, value in objects_dict.items():
            # Split the key into class name and ID
            class_name, obj_id = key.split('.')

            # Check if the class name matches the expected class
            if class_name == "BaseModel":
                # If the object has an "id" field, delete it, since it's auto-generated
                if "id" in value:
                    del value["id"]

                # Create a new instance of BaseModel using the dictionary
                obj = BaseModel(**value)

                # Add the new object to __objects
                self.new(obj)

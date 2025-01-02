#!/usr/bin/python3
"""Defines the FileStorage class for object serialization and deserialization."""
from models.base_model import BaseModel
from models.user import User
import json
from uuid import uuid4


class FileStorage:
    """Serializes instances to a JSON file and deserializes them back to instances.

    Attributes:
        __file_path (str): Path to the JSON file for storing data.
        __objects (dict): Dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all stored objects.

        Returns:
            dict: All objects in the format {<class name>.<id>: instance}.
        """
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage.

        Args:
            obj (BaseModel): The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize all objects to the JSON file."""
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(objects_dict, file)


    def reload(self):
        """Deserialize JSON file content to objects (if the file exists)."""
        class_mapping = {
            "BaseModel": BaseModel,
            "User": User
        }
        if not self.__file_path:
            return
        else:
            try:
                with open(self.__file_path, "r") as file:
                    objects_dict = json.load(file)

                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')

                    if class_name in class_mapping:
                        if "id" not in value:
                            value["id"] = str(uuid4())
                        clss = class_mapping[class_name]
                        obj = clss(**value)

                        self.new(obj)
            except FileNotFoundError:
                return





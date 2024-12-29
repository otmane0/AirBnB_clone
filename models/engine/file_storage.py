#!/usr/bin/python3
"""This class for data"""
from models.base_model import BaseModel
import json
from uuid import uuid4


class FileStorage:
    """Storage data"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all"""
        return self.__objects

    def new(self, obj):
        """Make new"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """To json"""
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(objects_dict, file)


    def reload(self):
        """Reload from json, to __objects"""
        if not self.__file_path:
            return
        else:
            try:
                with open(self.__file_path, "r") as file:
                    objects_dict = json.load(file)

                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')

                    if class_name == "BaseModel":
                        if "id" not in value:
                            value["id"] = str(uuid4())

                        obj = BaseModel(**value)

                        self.new(obj)
            except FileNotFoundError:
                return





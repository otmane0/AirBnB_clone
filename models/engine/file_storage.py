#!/usr/bin/python3
"""AIRBNB PROJECT"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """class FILESTORAGE"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """class FILESTORAGE"""
        return self.__objects

    def new(self, obj):
        """class FILESTORAGE"""
        item = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[item] = obj

    def save(self):
        """class FILESTORAGE"""
        dictionay = {}
        for key in FileStorage.__objects:
            dictionay[key] = self.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(dictionay))

    def reload(self):
        """class FILESTORAGE"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as FILE:
               dictionary = json.load(FILE)
            for key in dictionary:
                self.new(eval(dictionary[key]["__class__"])(**dictionary[key]))
        except IOError:
            pass
#!/usr/bin/python3
"""AIRBNB PROJECT"""

import json

class FileStorage:
    """class FILESTORAGE"""

    __file_path = "filestor.json"
    __objects = {}

    def all(self):
        """class FILESTORAGE"""
        return self.__objects

    def new(self, obj):
        """class FILESTORAGE"""
        item = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[item] = obj

    def save(self):
        """class FILESTORAGE"""
        with open (self.__file_path, "w", encoding="utf-8") as FILE:
            json.dump(self.__objects, FILE)

    def reload(self):
        """class FILESTORAGE"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as FLE:
               self.__objects = json.load(FLE)
        except FileNotFoundError:
            pass
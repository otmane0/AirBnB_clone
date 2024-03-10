#!/usr/bin/python3

import json

class FileStorage:

    __file_path = "filestor.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        item = self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]
        self.__objects[item] = obj

    def save(self):
        with open (self.__file_path, "w", encoding="utf-8") as FILE:
            json.dump(self.__objects, FILE)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as FLE:
               self.__objects = json.load(FLE)
        except FileNotFoundError:
            pass
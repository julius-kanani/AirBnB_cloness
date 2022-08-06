#!/usr/bin/python3
"""
    Module that define the FileStorage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Class that serializes instances to a JSON file and deserializes JSON
    file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key_obj = f"{obj.__class__.__name__}.{obj.id}"
        type(self).__objects[key_obj] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dict = {}
        for key, value in type(self).__objects.items():
            dict[key] = value.to_dict()
        with open(type(self).__file_path, 'w') as f:
            json.dump(dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(type(self).__file_path, 'r') as f:
                dict = json.load(f)
                for k, v in dict.items():
                    type(self).__objects[k] = eval(v['__class__'])(**v)
        except Exception:
            return

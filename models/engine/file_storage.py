#!/usr/bin/python3
""" The file_storage module.
This module supplies the FileStorage class. """
import json
from models.base_model import BaseModel


class FileStorage:
    """ Defines the File storage class, that serializes instances to a JSON
        file and deserializes JSON file to instances

        Attributes:
            __file_path (str): path to JSON File (ex: file.json).
            __objects: (dictionary): Empty, but will store all objects by
                <class name>.id (ex: to store a BaseModel object with
                id=12121212, the key will be BaseModel.12121212).

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """

        return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id. """

        if obj is not None:
            key = "{:s}{:s}{:s}".format(
                    type(obj).__name__, ".", obj.id)
            self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path). """

        obj_dict = self.__objects.copy()
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists; otherwise do nothing.
        """

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)

                for key, obj_attr in json_dict.items():
                    obj = BaseModel(**obj_attr)
                    self.new(obj)

        except FileNotFoundError as Error:
            pass

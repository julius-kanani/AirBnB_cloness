#!/usr/bin/python3
"""
This module supplies the Base Model class.
"""
from uuid import uuid4
import datetime


class BaseModel:
    """ Defines the BaseModel class.

    Attributes:
        id : unique id of an instance created.
        created_at (datetime): datetime when an instance is created.
        updated_at (datetime): datetime that is updated every time an object
            is changed.
    """

    def __init__(self):
        """ Initializes the BaseModel class

        Args:
            id (str): assign with an uuid when an instance is created.
            created_at (datetime): current datetime when instance is created.
            updated_at (datetime): assign with the current datetime when an
                instance is created and it will be updated everytime the object
                changes.
        """

        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """ Updates the public instance attribute updated_at """

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__. """

        dict_rep = self.__dict__
        dict_rep['__class__'] = type(self).__name__
        dict_rep['created_at'] = dict_rep['created_at'].isoformat()
        dict_rep['updated_at'] = dict_rep['updated_at'].isoformat()

        return dict_rep

    def __str__(self):
        """ Returns a string representation of BaseModel class. """

        return "[{:s}] ({:s}) {}".format(
                type(self).__name__, self.id, self.__dict__)

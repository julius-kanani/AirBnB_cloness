#!/usr/bin/python3
"""
This module supplies the Base Model class.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Defines the BaseModel class.

    Attributes:
        id : unique id of an instance created.
        created_at (datetime): datetime when an instance is created.
        updated_at (datetime): datetime that is updated every time an object
            is changed.
    """

    def __init__(self, *args, **kwargs):
        """ Initialize BaseModel class using a dictionary representation.

        Args:
            args: not used.
            kwargs: A dictionary representation of a BaseModel instance.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """ Updates the public instance attribute updated_at """

        self.updated_at = datetime.now()
        models.storage.save()

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

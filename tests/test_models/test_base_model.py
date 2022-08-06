#!/usr/bin/python3
"""
    Unittest for BaseModel
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Class test for the BaseModel class"""

    def test_instantiation(self):
        """Test instantiation"""
        model = BaseModel()
        self.assertIs(type(model), BaseModel)
        self.assertIs(type(model.id), str)
        self.assertIs(type(model.created_at), datetime)
        self.assertIs(type(model.updated_at), datetime)
        model.name = "Betty"
        model.age = 100
        self.assertEqual(model.name, "Betty")
        self.assertEqual(model.age, 100)

    def test_instantiation_kwargs(self):
        """Test instantiation with kwargs"""
        model = BaseModel()
        model.name = "Betty"
        model.age = 100
        model_json = model.to_dict()
        new_model = BaseModel(**model_json)
        self.assertIs(type(new_model), BaseModel)
        self.assertIs(type(new_model.id), str)
        self.assertEqual(new_model.id, model.id)
        self.assertIs(type(new_model.created_at), datetime)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertIs(type(new_model.updated_at), datetime)
        self.assertEqual(new_model.updated_at, model.updated_at)
        self.assertIs(type(new_model.name), str)
        self.assertEqual(new_model.name, "Betty")
        self.assertIs(type(new_model.age), int)
        self.assertEqual(new_model.age, 100)

    def test_save(self):
        """Test the save() function"""
        model = BaseModel()
        model.name = "Betty"
        model.age = 100
        id = model.id
        old_date = model.updated_at
        model.save()
        self.assertNotEqual(old_date, model.updated_at)
        self.assertEqual(model.name, "Betty")
        self.assertEqual(model.age, 100)
        
    def test_to_dict(self):
        """Test the to_dict() function"""
        model = BaseModel()
        model.name = "Julius"
        model.age = 100
        dict = model.to_dict()
        self.assertEqual(dict["__class__"], "BaseModel")
        self.assertEqual(dict["name"], "Julius")
        self.assertEqual(dict["age"], 100)
        self.assertEqual(dict["created_at"], model.created_at.isoformat())
        self.assertEqual(dict["updated_at"], model.updated_at.isoformat())

    def test_str(self):
        """Test the output of the instance when printed"""
        a = BaseModel()
        self.assertEqual(str(a), f"[{a.__class__.__name__}] ({a.id}) " +
                         f"{a.__dict__}")


if __name__ == "__main__":
    unittest.main()

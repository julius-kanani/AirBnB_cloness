#!/usr/bin/python3
"""Unittest module for City"""
from models.base_model import BaseModel
from models.state import State
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """class testing the City class"""

    def test_instance(self):
        """test the creation of an instance"""
        a = City()
        b = State()
        self.assertEqual(a.name, '')
        self.assertEqual(a.state_id, '')
        a.name = 'Betty'
        a.state_id = b.id
        self.assertEqual(a.name, 'Betty')
        self.assertEqual(a.state_id, b.id)
        self.assertTrue(hasattr(a, 'id'))
        self.assertTrue(hasattr(a, 'created_at'))
        self.assertTrue(hasattr(a, 'updated_at'))
        self.assertTrue(issubclass(a.__class__, BaseModel))

    def test_str(self):
        """Test the string output of the class"""
        a = City()
        self.assertEqual(str(a), f"[City] ({a.id}) {a.__dict__}")


if __name__ == '__main__':
    unittest.main()

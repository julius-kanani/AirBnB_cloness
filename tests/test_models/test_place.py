#!/usr/bin/python3
"""Unittest module for Place"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    """class testing the Place class"""

    def test_instance(self):
        """test the creation of a Place instance"""
        a = Place()
        self.assertTrue(hasattr(a, 'city_id'))
        self.assertTrue(hasattr(a, 'user_id'))
        self.assertTrue(hasattr(a, 'name'))
        self.assertTrue(hasattr(a, 'description'))
        self.assertTrue(hasattr(a, 'number_rooms'))
        self.assertTrue(hasattr(a, 'number_bathrooms'))
        self.assertTrue(hasattr(a, 'max_guest'))
        self.assertTrue(hasattr(a, 'price_by_night'))
        self.assertTrue(hasattr(a, 'latitude'))
        self.assertTrue(hasattr(a, 'longitude'))
        self.assertTrue(hasattr(a, 'amenity_ids'))
        self.assertTrue(type(a.city_id), str)
        self.assertTrue(type(a.user_id), str)
        self.assertTrue(type(a.name), str)
        self.assertTrue(type(a.description), str)
        self.assertTrue(type(a.number_rooms), int)
        self.assertTrue(type(a.number_bathrooms), int)
        self.assertTrue(type(a.max_guest), int)
        self.assertTrue(type(a.price_by_night), int)
        self.assertTrue(type(a.latitude), float)
        self.assertTrue(type(a.longitude), float)
        self.assertTrue(type(a.amenity_ids), list)
        self.assertEqual(a.city_id, '')
        self.assertEqual(a.user_id, '')
        self.assertEqual(a.name, '')
        self.assertEqual(a.description, '')
        self.assertEqual(a.number_rooms, 0)
        self.assertEqual(a.number_bathrooms, 0)
        self.assertEqual(a.max_guest, 0)
        self.assertEqual(a.price_by_night, 0)
        self.assertEqual(a.latitude, 0.0)
        self.assertEqual(a.longitude, 0.0)
        self.assertEqual(a.amenity_ids, [])
        self.assertEqual(len(a.amenity_ids), 0)
        b = City()
        a.city_id = b.id
        self.assertEqual(a.city_id, b.id)
        c = User()
        a.user_id = c.id
        self.assertEqual(a.user_id, c.id)
        a.name = 'Betty'
        self.assertEqual(a.name, 'Betty')
        a.description = 'Description'
        self.assertEqual(a.description, 'Description')
        a.number_rooms = 5
        self.assertEqual(a.number_rooms, 5)
        a.number_bathrooms = 2
        self.assertEqual(a.number_bathrooms, 2)
        a.max_guest = 8
        self.assertEqual(a.max_guest, 8)
        a.price_by_night = 30
        self.assertEqual(a.price_by_night, 30)
        a.latitude = 48.07
        self.assertEqual(a.latitude, 48.07)
        a.longitude = -0.76
        self.assertEqual(a.longitude, -0.76)
        d = Amenity()
        a.amenity_ids.append(d.id)
        self.assertNotEqual(len(a.amenity_ids), 0)
        self.assertTrue(type(a.amenity_ids), list)
        self.assertEqual(a.amenity_ids[0], d.id)

    def test_str(self):
        """Test the string output of the class"""
        a = Place()
        self.assertEqual(str(a), f"[Place] ({a.id}) {a.__dict__}")


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
    Unittest for User
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """class Test for the User class"""

    def test_init(self):
        """Initialisation of an User"""
        u = User()
        self.assertTrue(issubclass(u.__class__, BaseModel))
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        u.first_name = "Betty"
        u.last_name = "Bar"
        u.email = "airbnb@mail.com"
        u.password = "root"
        s = f"[{u.__class__.__name__}] ({u.id}) {u.__dict__}"
        self.assertEqual(s, str(u))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
    Unittest for Review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """class Test for the Review class"""

    def test_init(self):
        """Initialisation of an Review"""
        r = Review()
        self.assertTrue(issubclass(r.__class__, BaseModel))
        self.assertTrue(hasattr(r, "id"))
        self.assertTrue(hasattr(r, "created_at"))
        self.assertTrue(hasattr(r, "updated_at"))
        self.assertTrue(hasattr(r, "place_id"))
        self.assertTrue(hasattr(r, "user_id"))
        self.assertTrue(hasattr(r, "text"))
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")
        r.place_id = "place_id"
        r.user_id = "user_id"
        r.text = "text"
        s = f"[{r.__class__.__name__}] ({r.id}) {r.__dict__}"
        self.assertEqual(s, str(r))


if __name__ == '__main__':
    unittest.main()

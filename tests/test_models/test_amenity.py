#!/usr/bin/python3
"""Defines unittests for amenity class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Represents testing instantiation of the Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initializes the process"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Testing for name2"""
        new = self.value()
        self.assertEqual(type(new.name), str)

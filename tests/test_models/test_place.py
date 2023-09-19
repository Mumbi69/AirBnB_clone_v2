#!/usr/bin/python3
"""Defines unittests for place module"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Represents testing of the Place class."""

    def __init__(self, *args, **kwargs):
        """Initializes the function"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Testing for the city id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Testing for user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Testing for the name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Testing for description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Testing number of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Testing number of bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Testing the max guest"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Testing for the price by night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Testing the latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Testing the longitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """Testing the amenity ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

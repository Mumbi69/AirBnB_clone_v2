#!/usr/bin/python3
"""Defines unittests for review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Represents testing of the Review class"""

    def __init__(self, *args, **kwargs):
        """Intantiates the class objects"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Testing place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """testing user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Testing for text"""
        new = self.value()
        self.assertEqual(type(new.text), str)

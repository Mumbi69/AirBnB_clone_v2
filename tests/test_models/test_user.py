#!/usr/bin/python3
"""Defines unittests for user module"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Unittests for testing the user class"""

    def __init__(self, *args, **kwargs):
        """Instantiates the class objects"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Testing the firstname"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Testing the lastname"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Testing the email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Testing the password"""
        new = self.value()
        self.assertEqual(type(new.password), str)

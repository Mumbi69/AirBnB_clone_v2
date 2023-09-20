#!/usr/bin/python3
"""Defines unittests for state class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Represents testing of the State class"""

    def __init__(self, *args, **kwargs):
        """Instantiates the class objects"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Testing the name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

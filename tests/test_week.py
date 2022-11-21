from os import path
from unittest import TestCase


class TestWeek(TestCase):
    def test_main_exists(self):
        self.assertTrue(path.isfile('main.py'))

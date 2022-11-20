from os import path
from unittest import TestCase


class TestMain(TestCase):
    def test_main_exists(self):
        self.assertTrue(path.isfile('main.py'))

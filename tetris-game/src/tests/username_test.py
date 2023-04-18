import unittest
import pygame
from username import Username


class TestUsername(unittest.TestCase):
    def setUp(self):
        self.username = Username()

    def test_username_can_change(self):
        text0 = self.username.input

        self.username.add_char("m")
        text1 = self.username.input
        self.assertNotEqual(text0, text1)

    def test_backspace_works(self):
        self.username.input = "gosling"
        text0 = self.username.input

        self.username.backspace()
        text1 = self.username.input

        self.assertNotEqual(text0, text1)
        self.assertEqual(text1, "goslin")


        
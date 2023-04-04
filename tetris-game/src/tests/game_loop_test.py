import unittest
import pygame
from game_loop import GameLoop

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        DISPLAY_WIDTH = 1000
        DISPLAY_HEIGHT = 900
        display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.game_loop = GameLoop(display, "testing")

    def test_game_loop_starts(self):
        self.game_loop.start()
        self.assertNotEqual(self.game_loop, None)

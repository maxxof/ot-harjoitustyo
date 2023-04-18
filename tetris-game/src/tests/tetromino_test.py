import unittest
from game_engine import GameEngine
from tetromino import Tetromino, shapes

class TestTetromino(unittest.TestCase):
    def setUp(self):
        self.engine = GameEngine()
        self.engine.create_grid()
        self.engine.curr_tetromino = Tetromino(5, 0, shapes[3])

    def test_tetromino_rotates(self):
        rotation0 = self.engine.curr_tetromino.rotation

        self.engine.rotate_tetromino()
        rotation1 = self.engine.curr_tetromino.rotation
        
        self.assertNotEqual(rotation0, rotation1)

    def test_tetromino_moves_right(self):
        x0 = self.engine.curr_tetromino.get_x()

        self.engine.move_tetromino_right()
        x1 = self.engine.curr_tetromino.get_x()

        self.assertEqual(x0 + 1, x1)

    def test_tetromino_moves_left(self):
        x0 = self.engine.curr_tetromino.get_x()

        self.engine.move_tetromino_left()
        x1 = self.engine.curr_tetromino.get_x()

        self.assertEqual(x0 - 1, x1)

    def test_tetromino_moves_down(self):
        y0 = self.engine.curr_tetromino.get_y()

        self.engine.move_tetromino_down()
        y1 = self.engine.curr_tetromino.get_y()

        self.assertEqual(y0 + 1, y1)


        

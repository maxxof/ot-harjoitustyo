import unittest
from game_engine import GameEngine

class TestGameEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GameEngine()
        self.engine.create_grid()

    def test_check_if_lost_works(self):
        lost = self.engine.check_if_lost(self.engine.positions)
        self.assertEqual(lost, False)

        coordinates = self.engine.update_grid()
        self.engine.lock_and_switch_tetromino(coordinates)
        
        lost = self.engine.check_if_lost(self.engine.positions)
        self.assertEqual(lost, True)

    def test_tetromino_valid_position(self):
        start_position = self.engine.valid_position(self.engine.curr_tetromino)

        self.assertEqual(start_position, True)

        self.engine.move_tetromino_down()
        self.engine.move_tetromino_down()
        self.engine.move_tetromino_down()
        self.engine.move_tetromino_down()
        self.engine.move_tetromino_down()
        self.engine.move_tetromino_down()

        self.engine.curr_tetromino.move_right()
        self.engine.curr_tetromino.move_right()
        self.engine.curr_tetromino.move_right()
        self.engine.curr_tetromino.move_right()
        self.engine.curr_tetromino.move_right()
        self.engine.curr_tetromino.move_right()
        self.engine.curr_tetromino.move_right()

        end_position = self.engine.valid_position(self.engine.curr_tetromino)

        self.assertEqual(end_position, False)

    def test_cant_move_tetromino_through_right_border(self):
        self.engine.move_tetromino_down()
        self.engine.move_tetromino_down()
        self.engine.move_tetromino_down()

        self.engine.move_tetromino_right()
        self.engine.move_tetromino_right()
        self.engine.move_tetromino_right()
        self.engine.move_tetromino_right()
        self.engine.move_tetromino_right()
        self.engine.move_tetromino_right()
        self.engine.move_tetromino_right()

        end_position = self.engine.valid_position(self.engine.curr_tetromino)

        self.assertEqual(end_position, True)

    def test_cant_move_tetromino_through_left_border(self):
        self.engine.move_tetromino_down()
        self.engine.move_tetromino_down()
        self.engine.move_tetromino_down()

        self.engine.move_tetromino_left()
        self.engine.move_tetromino_left()
        self.engine.move_tetromino_left()
        self.engine.move_tetromino_left()
        self.engine.move_tetromino_left()
        self.engine.move_tetromino_left()
        self.engine.move_tetromino_left()

        end_position = self.engine.valid_position(self.engine.curr_tetromino)

        self.assertEqual(end_position, True)
    
    def test_next_tetromino_when_locks_in_position(self):
        change_tetromino = self.engine.change_tetromino
        self.assertEqual(change_tetromino, False)
        
        self.engine.cooldown = 100000
        self.engine.tetromino_fall()
        self.engine.update_grid()

        self.engine.cooldown = 100000
        self.engine.tetromino_fall()
        self.engine.update_grid()

        self.engine.cooldown = 100000
        self.engine.tetromino_fall()
        self.engine.update_grid()

        self.engine.cooldown = 100000
        self.engine.tetromino_fall()
        self.engine.update_grid()

        change_tetromino = self.engine.change_tetromino
        self.assertEqual(change_tetromino, True)

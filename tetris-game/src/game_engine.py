from random import choice
import pygame
from tetromino import Tetromino, shapes

class GameEngine:
    def __init__(self):
        self.grid_width = 400
        self.grid_height = 800
        self.block_size = 40
        self.topleft_x = (1000-self.grid_width) // 2
        self.topleft_y = 850-self.grid_height
        self.grid = None
        self.positions = {}
        self.cooldown = 0
        self.fall_speed = 0.25
        self.change_tetromino = False
        self.curr_tetromino = self.get_tetromino()
        self.next_tetromino = self.get_tetromino()

    def create_grid(self):
        self.grid = [[(0, 0, 0) for i in range(10)] for j in range(20)]

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (j, i) in self.positions:
                    col = self.positions[(j, i)]
                    self.grid[i][j] = col

    def render_grid(self, display):
        size = self.block_size
        topleft_x = self.topleft_x
        topleft_y = self.topleft_y

        # renders grid's perimeter
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                pygame.draw.rect(display, self.grid[i][j],
                                 (topleft_x + j*size, topleft_y + i*size, size, size), 0)

        # renders grid's row's and column's lines
        for row in range(len(self.grid)):
            pygame.draw.line(display, 'grey', (topleft_x, topleft_y + size * row),
                             (topleft_x + self.grid_width, topleft_y + size * row))
            for col in range(len(self.grid[row])):
                pygame.draw.line(display, 'grey', (topleft_x + size * col, topleft_y),
                                 (topleft_x + size * col, topleft_y + self.grid_height))

        pygame.draw.rect(display, (0, 0, 255), (topleft_x, topleft_y, self.grid_width, self.grid_height), 4)
        pygame.display.update()

    def get_tetromino(self):
        return Tetromino(5, 0, choice(shapes))

    def valid_position(self, tetromino):
        formatted_tetromino = self.format_tetromino(tetromino)

        valid_positions = [[(j, i) for j in range(10) if self.grid[i][j] == (0, 0, 0)]
                           for i in range(20)]
        valid_positions = [i for j in valid_positions for i in j]

        for pos in formatted_tetromino:
            if pos not in valid_positions:
                # returns False only if tetromino is in a grid
                if pos[1] > -1:
                    return False
        return True

    def format_tetromino(self, tetromino):
        coordinates = []
        rotation = tetromino.shape[tetromino.rotation]

        for i, row in enumerate(rotation):
            row = list(row)
            for j, col in enumerate(row):
                if col == '0':
                    coordinates.append((tetromino.get_x() + j - 2, tetromino.get_y() + i - 4))
        return coordinates

    def check_if_lost(self, coordinates):
        # checks if block's coordinate is above grid
        for coor in coordinates:
            coor_y = coor[1]
            if coor_y < 1:
                return True
        return False

    def move_tetromino_left(self):
        self.curr_tetromino.move_left()
        if not self.valid_position(self.curr_tetromino):
            self.curr_tetromino.move_right()

    def move_tetromino_right(self):
        self.curr_tetromino.move_right()
        if not self.valid_position(self.curr_tetromino):
            self.curr_tetromino.move_left()

    def move_tetromino_down(self):
        self.curr_tetromino.move_down()
        if not self.valid_position(self.curr_tetromino):
            self.curr_tetromino.move_up()

    def rotate_tetromino(self):
        self.curr_tetromino.rotate()
        if not self.valid_position(self.curr_tetromino):
            self.curr_tetromino.rotate_back()

    def tetromino_fall(self):
        if self.cooldown/1000 > self.fall_speed:
            self.cooldown = 0
            self.curr_tetromino.move_down()
            # checks if tetromino hit the ground or another block
            if not self.valid_position(self.curr_tetromino) and self.curr_tetromino.get_y() > 0:
                self.curr_tetromino.move_up()
                self.change_tetromino = True

    def update_grid(self):
        tetromino_coordinates = self.format_tetromino(self.curr_tetromino)
        for i in range(len(tetromino_coordinates)):
            coor_x, coor_y = tetromino_coordinates[i]
            if coor_y > -1:
                self.grid[coor_y][coor_x] = self.curr_tetromino.get_color()

        return tetromino_coordinates

    def lock_and_switch_tetromino(self, tetromino_coordinates):
        # locks current tetromino into position and switches to the next tetromino
        for coor in tetromino_coordinates:
            coordinate = (coor[0], coor[1])
            self.positions[coordinate] = self.get_tetromino_color(self.curr_tetromino)
        self.curr_tetromino = self.next_tetromino
        self.next_tetromino = self.get_tetromino()
        self.change_tetromino = False

    def get_tetromino_color(self, tetromino):
        return tetromino.get_color()
    
import pygame
from random import choice
from tetromino import Tetromino, shapes, colors

class GameEngine:
    def __init__(self):
        self.grid_width = 400
        self.grid_height = 800
        self.block_size = 40
        self.topleft_x = (1000-self.grid_width) // 2
        self.topleft_y = 850-self.grid_height
        self.grid = None

    def create_grid(self, position={}):
        self.grid = [[(0, 0, 0) for i in range(10)] for j in range(20)]

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (i, j) in position:
                    col = position[(j, i)]
                    self.grid[i][j] = col
    
    def render_grid(self, display):
        size = self.block_size
        x = self.topleft_x
        y = self.topleft_y

        # renders grid's perimeter
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                pygame.draw.rect(display, self.grid[i][j], 
                                 (x + j*size, self.topleft_y + i*size, size, size), 0)

        # renders grid's row's and column's lines
        for row in range(len(self.grid)):
            pygame.draw.line(display, 'grey', (x, y + size * row), (x + self.grid_width, y + size * row))
            for col in range(len(self.grid[row])):
                pygame.draw.line(display, 'grey', (x + size * col, y), (x + size * col, y + self.grid_height))

        pygame.draw.rect(display, (0, 0, 255), (x, y, self.grid_width, self.grid_height), 4)
        pygame.display.update()

    def get_tetromino(self):
        return Tetromino(5, 0, choice(shapes))
    
    def valid_position(self, tetromino):
        formatted_tetromino = self.format_tetromino(tetromino)

        valid_positions = [[(j, i) for j in range(10) if self.grid[i][j] == (0, 0, 0)] for i in range(20)]
        valid_positions = [i for j in valid_positions for i in j]

        for pos in formatted_tetromino:
            if pos not in valid_positions:
                # returns False only if tetromino is in a grid
                return pos[1] > -1
                    
    def format_tetromino(self, tetromino):
        coordinates = []
        rotation = tetromino.shape[tetromino.rotation]

        for i in range(len(rotation)):
            row = list(rotation[i])
            for j in range(len(row)):
                if row[j] == '0':
                    coordinates.append((tetromino.get_x() + j - 2, tetromino.get_y() + i - 4))
        return coordinates

    def check_if_lost(self, coordinates):
        # checks if block's coordinate is above grid
        for coor in coordinates:
            y = coor[1]
            return y < 1
    
    def move_tetro_left(self, tetromino):
        tetromino.move_left()
        if not self.valid_position(tetromino):
            tetromino.move_right()
    
    def move_tetro_right(self, tetromino):
        tetromino.move_right()
        if not self.valid_position(tetromino):
            tetromino.move_left()

    def move_tetro_down(self, tetromino):
        tetromino.move_down()
        if not self.valid_position(tetromino):
            tetromino.move_up()

    def rotate_tetro(self, tetromino):
        tetromino.rotate()
        if not self.valid_position(tetromino):
            tetromino.rotate_back()
    
    def tetro_fall(self, tetromino, fall_time, fall_speed, change_tetromino):
        if fall_time/1000 > fall_speed:
            fall_time = 0
            tetromino.move_down()
            # checks if tetromino hit the ground or another block
            if not self.valid_position(tetromino) and tetromino.get_y() > 0:
                tetromino.move_up()
                change_tetromino = True

        return fall_time, change_tetromino


    
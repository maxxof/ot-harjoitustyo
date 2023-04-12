import pygame
import random

class GameEngine:
    def __init__(self):
        self.grid_width = 400
        self.grid_height = 800
        self.block_size = 40
        self.topleft_x = (1000-self.grid_width) // 2
        self.topleft_y = 900-self.grid_height

    def create_grid(self, pos = {}):
        grid = [[(0, 0, 0) for i in range(10)] for j in range(20)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) in pos:
                    color = pos[(j, i)]
                    grid[i][j] = color
        return grid
    
    def render_grid(display):
        display.fill((0, 0, 0))
        

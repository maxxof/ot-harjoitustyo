import pygame
import sys
import os
from button import Button
from game_engine import GameEngine

dirname = os.path.dirname(__file__)

class GameLoop:
    def __init__(self, display, username, event_queue):
        self.display = display
        self.username = username
        exitbtn_img = pygame.image.load(os.path.join(dirname, "assets", 'exit_btn.png'))
        self.exit_btn = Button(100, 100, exitbtn_img, 0.5)
        self.event_queue = event_queue
        self.engine = GameEngine()

    def start(self):
        positions = {}
        self.engine.create_grid(positions)
        change_tetromino = False
        curr_tetromino = self.engine.get_tetromino()
        next_tetromino = self.engine.get_tetromino()
        clock = pygame.time.Clock()
        fall_time = 0
        fall_speed = 0.25

        running = True
        while running:
            self.display.fill((200, 228, 240))

            self.engine.create_grid(positions)
            fall_time += clock.get_rawtime()
            clock.tick()

            fall_time, change_tetromino = self.engine.tetromino_fall(curr_tetromino, fall_time, fall_speed, change_tetromino)

            if self.exit_btn.draw(self.display):
                running = False

            for event in self.event_queue.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.engine.move_tetromino_left(curr_tetromino)
                        if event.key == pygame.K_RIGHT:
                            self.engine.move_tetromino_right(curr_tetromino)
                        if event.key == pygame.K_DOWN:
                            self.engine.move_tetromino_down(curr_tetromino)
                        if event.key == pygame.K_UP:
                            self.engine.rotate_tetromino(curr_tetromino)

            tetromino_coordinates = self.engine.update_grid(curr_tetromino)

            if change_tetromino:
                for coor in tetromino_coordinates:
                    coordinate = (coor[0], coor[1])
                    positions[coordinate] = self.engine.get_tetromino_color(curr_tetromino)
                curr_tetromino = next_tetromino
                next_tetromino = self.engine.get_tetromino()
                change_tetromino = False

            self.engine.render_grid(self.display)


            pygame.display.update()

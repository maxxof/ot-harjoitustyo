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
        self.engine.create_grid()
        clock = pygame.time.Clock()

        running = True
        while running:
            self.display.fill((200, 228, 240))

            self.engine.create_grid()
            self.engine.fall_time += clock.get_rawtime()
            clock.tick()

            self.engine.tetromino_fall()

            if self.exit_btn.draw(self.display):
                running = False

            for event in self.event_queue.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.engine.move_tetromino_left()
                        if event.key == pygame.K_RIGHT:
                            self.engine.move_tetromino_right()
                        if event.key == pygame.K_DOWN:
                            self.engine.move_tetromino_down()
                        if event.key == pygame.K_UP:
                            self.engine.rotate_tetromino()

            tetromino_coordinates = self.engine.update_grid()

            if self.engine.change_tetromino:
                self.engine.lock_and_switch(tetromino_coordinates)

            self.engine.render_grid(self.display)

            pygame.display.update()

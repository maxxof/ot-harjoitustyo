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

        running = True
        while running:
            self.display.fill((200, 228, 240))

            if self.exit_btn.draw(self.display):
                running = False

            for event in self.event_queue.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.engine.move_tetro_left(curr_tetromino)
                        if event.key == pygame.K_RIGHT:
                            self.engine.move_tetro_right(curr_tetromino)
                        if event.key == pygame.K_DOWN:
                            self.engine.move_tetro_down(curr_tetromino)
                        if event.key == pygame.K_UP:
                            self.engine.rotate_tetro(curr_tetromino)

            self.engine.render_grid(self.display)


            pygame.display.update()
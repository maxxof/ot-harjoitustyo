import sys
import os
import pygame
from button import Button
from game_engine import GameEngine

dirname = os.path.dirname(__file__)
exitbtn_img = pygame.image.load(os.path.join(dirname, "assets", 'exit_btn.png'))

class GameLoop:
    """Luokka, joka on vastuussa pelisilmukasta
    
    Attributes:
        display: näyttö, johon piirretään peli
        username: pelaajan käyttäjätunnus
        exit_btn: exit-painike
        event_queue: tapahtumajono
        engine: pelimoottori
    """

    def __init__(self, display, username, event_queue):
        """Luokan konstruktori, joka luo uuden pelisilmukan
        ja pelimoottorin

        Args:
            display: piirtopinta
            username: pelaajan käyttäjätunnus
            event_queue: tapahtumajono
        """

        self.display = display
        self.username = username
        self.exit_btn = Button(100, 100, exitbtn_img, 0.5)
        self.event_queue = event_queue
        self.engine = GameEngine()

    def start(self):
        """Käynnistää silmukan, jossa peli etenee
        """

        self.engine.create_grid()
        clock = pygame.time.Clock()

        score = 0
        running = True
        while running:
            self.display.fill((200, 228, 240))

            self.engine.create_grid()
            self.engine.cooldown += clock.get_rawtime()
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
                self.engine.lock_and_switch_tetromino(tetromino_coordinates)
                previous_score = score
                score += self.engine.clear_grid_rows()
                if score > previous_score:
                    self.engine.fall_speed -= 0.005

            self.engine.render_grid(self.display)
            self.engine.render_score(self.display, score)
            self.engine.render_next_tetromino(self.display)
            pygame.display.update()

            if self.engine.check_if_lost(self.engine.positions):
                running = False
                self.engine.render_game_over_message(self.display, score)

        return self.username, score

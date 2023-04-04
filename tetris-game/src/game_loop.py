import pygame
import sys
import os
from button import Button

dirname = os.path.dirname(__file__)

class GameLoop:
    def __init__(self, display, username):
        self.display = display
        self.username = username
        exitbtn_img = pygame.image.load(os.path.join(dirname, "assets", 'exit_btn.png'))
        self.exit_btn = Button(100, 100, exitbtn_img, 0.5)

    def start(self):
        running = True
        while running:
            self.display.fill((200, 228, 240))

            if self.exit_btn.draw(self.display):
                running = False

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


            pygame.display.update()
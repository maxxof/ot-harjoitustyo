import pygame
import sys
from button import Button

class GameLoop:
    def __init__(self, display, username):
        self.display = display
        self.username = username
        exitbtn_img = pygame.image.load('assets/exit_btn.png').convert_alpha()
        self.exit_btn = Button(100, 100, exitbtn_img, 0.5)

    def start(self):
        running = True
        while running:
            self.display.fill((200, 228, 240))

            if self.exit_btn.draw(self.display):
                return

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


            pygame.display.update()
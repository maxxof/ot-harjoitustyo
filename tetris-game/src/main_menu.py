import pygame
import sys
import os
from button import Button
from username import Username
from game_loop import GameLoop

dirname = os.path.dirname(__file__)

class MainMenu:
    def __init__(self, display):
        startbtn_img = pygame.image.load(os.path.join(dirname, "assets", 'start_btn.png'))
        exitbtn_img = pygame.image.load(os.path.join(dirname, "assets", 'exit_btn.png'))
        self.start_btn = Button(500, 200, startbtn_img, 0.5)
        self.exit_btn = Button(500, 300, exitbtn_img, 0.5)
        self.display = display
        self.username = Username()
        self.info = pygame.font.Font(None, 40).render("Enter your username:", True, (204, 102, 0))
    
    def start_main_menu(self):
        running = True
        while running:
            self.display.fill((200, 228, 240))

            if self.exit_btn.draw(self.display):
                return
            if self.start_btn.draw(self.display) and len(self.username.input) != 0:
                running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.username.backspace()
                    else:
                        if len(self.username.input) < 15:
                            self.username.add_char(event.unicode)

            pygame.draw.rect(self.display, self.username.rect_color, self.username.input_rect, 5)
            self.display.blit(self.username.surface, (self.username.input_rect.x + 7, self.username.input_rect.y + 9))
            self.display.blit(self.info, (500-self.info.get_width()/2, 50))


            pygame.display.update()

        self.start_game_loop()

    def start_game_loop(self):
        game_loop = GameLoop(self.display, self.username.input)
        game_loop.start()
        self.start_main_menu()

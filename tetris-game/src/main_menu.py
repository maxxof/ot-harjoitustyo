import pygame
from button import Button

class MainMenu:
    def __init__(self, display):
        startbtn_img = pygame.image.load('assets/start_btn.png').convert_alpha()
        exitbtn_img = pygame.image.load('assets/exit_btn.png').convert_alpha()
        self.start_btn = Button(500, 200, startbtn_img, 0.5)
        self.exit_btn = Button(500, 300, exitbtn_img, 0.5)
        self.display = display
    
    def start(self):
        running = True
        while running:
            self.display.fill((200, 228, 240))
            if self.exit_btn.draw(self.display):
                running = False
            if self.start_btn.draw(self.display):
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

import pygame

class Renderer:
    def __init__(self, display):
        self.display = display

    def render(self):
        self.display.fill((200, 228, 240))
        pygame.display.update()
    
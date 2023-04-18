import pygame

class Username:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 40)
        self.input = ""
        self.surface = self.font.render(self.input, True, (204, 102, 0))
        self.input_rect = pygame.Rect(490, 100, 15, 45)
        self.rect_color = (0, 0, 0)

    def render(self):
        self.surface = self.font.render(self.input, True, (204, 102, 0))
        self.input_rect.w = self.surface.get_width() + 15
        self.input_rect.x = 490-self.surface.get_width()/2

    def add_char(self, char):
        self.input += char
        self.render()

    def backspace(self):
        self.input = self.input[:-1]
        self.render()

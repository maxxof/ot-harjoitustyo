import pygame

class Username:
    """Luokka, joka imitoi käyttäjätunnusta

    Luokka ylläpitää pelaajan käyttäjätunnusta
    
    Attributes:
        font: pygame-fontti
        input: käyttäjän syöte
        surface: piirtopinta
        input_rect: syöteikkuna
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden käyttäjätunnus-olion
        """

        pygame.font.init()
        self.font = pygame.font.Font(None, 40)
        self.input = ""
        self.surface = self.font.render(self.input, True, (204, 102, 0))
        self.input_rect = pygame.Rect(490, 100, 15, 45)
        self.rect_color = (0, 0, 0)

    def render(self):
        """Piirtää käyttäjän syötteen
        """

        self.surface = self.font.render(self.input, True, (204, 102, 0))
        self.input_rect.w = self.surface.get_width() + 15
        self.input_rect.x = 490-self.surface.get_width()/2

    def add_char(self, char):
        """Lisää merkin käyttäjätunnukseen
        """

        self.input += char
        self.render()

    def backspace(self):
        """Poistaa merkin käyttäjätunnuksesta
        """

        self.input = self.input[:-1]
        self.render()

import pygame

class EventQueue:
    """Tapahtumajono-luokka
    """

    def get(self):
        return pygame.event.get()
    
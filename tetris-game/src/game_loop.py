import pygame

class GameLoop:
    def __init__(self, renderer, event_queue):
        self.renderer = renderer
        self.event_queue = event_queue

    def start(self):
        while True:
            pass
    def render(self):
        self.renderer.render()
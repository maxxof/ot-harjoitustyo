import pygame
from button import Button
from event_queue import EventQueue
from renderer import Renderer
from game_loop import GameLoop
from main_menu import MainMenu

pygame.quit()

def main():
    DISPLAY_WIDTH = 1000
    DISPLAY_HEIGHT = 900

    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Tetris")
    main_menu = MainMenu(display)

    # event_queue = EventQueue()
    # renderer = Renderer(display)
    # game_loop = GameLoop(renderer, event_queue)

    pygame.init()
    main_menu.start()

if __name__ == "__main__":
    main()
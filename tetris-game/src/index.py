import pygame
from main_menu import MainMenu

def main():
    DISPLAY_WIDTH = 1000
    DISPLAY_HEIGHT = 900

    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Tetris")
    main_menu = MainMenu(display)

    pygame.init()
    main_menu.start_main_menu()

if __name__ == "__main__":
    main()
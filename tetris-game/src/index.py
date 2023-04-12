import pygame
from main_menu import MainMenu

def main():
    display_width = 1000
    display_height = 900

    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Tetris")
    main_menu = MainMenu(display)

    pygame.init()
    main_menu.start_main_menu()

if __name__ == "__main__":
    main()

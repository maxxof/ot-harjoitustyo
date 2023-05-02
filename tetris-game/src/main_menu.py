import sys
import os
import pygame
from button import Button
from username import Username
from game_loop import GameLoop

dirname = os.path.dirname(__file__)

class MainMenu:
    """Luokka, joka on vastuussa päävalikon toiminnasta
    
    Attributes:
        startbtn_img: start-painikkeen kuva
        exitbtn_img: exit_painikkeen kuva
        start_btn: start_painike
        exit_btn: exit-painike
        display: pinta, johon piirretään päävalikon käyttöliittymä
        username: pelaajan käyttäjätunnus
        info: käyttäjätunnus-infoviesti
        event_queue: tapahtumajono
    """

    def __init__(self, display, event_queue):
        """Luokan konstruktori, joka luo uuden päävalikon
        
        Luo start ja exit-painikkeille oliot ja käyttäjätunnus-olion

        Args:
            display: piirtopinta
            event_queue: tapahtumajono
        """

        startbtn_img = pygame.image.load(os.path.join(dirname, "assets", 'start_btn.png'))
        exitbtn_img = pygame.image.load(os.path.join(dirname, "assets", 'exit_btn.png'))
        self.start_btn = Button(500, 200, startbtn_img, 0.5)
        self.exit_btn = Button(500, 300, exitbtn_img, 0.5)
        self.display = display
        self.username = Username()
        self.info = pygame.font.Font(None, 40).render("Enter your username:", True, (204, 102, 0))
        self.event_queue = event_queue

    def start_main_menu(self):
        """Käynnistää päävalikon silmukan
        
        Jos käyttäjä antaa riittävän pitkän käyttäjätunnuksen ja painaa start-painiketta,
        poistutaan päävalikkosilmukasta ja kutsutaan start_game_loop metodia
        """

        running = True
        while running:
            self.display.fill((200, 228, 240))

            if self.exit_btn.draw(self.display):
                return
            if self.start_btn.draw(self.display) and len(self.username.input) != 0:
                running = False
            for event in self.event_queue.get():
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
            self.display.blit(self.username.surface, (self.username.input_rect.x + 7,
            self.username.input_rect.y + 9))
            self.display.blit(self.info, (500-self.info.get_width()/2, 50))

            pygame.display.update()

        self.start_game_loop()

    def start_game_loop(self):
        """Luo uuden pelisilmukka-olion ja käynnistää pelisilmukan
        
        Kun pelisilmukasta poistutaan, käynnistetään uusi päävalikko-silmukka
        """

        game_loop = GameLoop(self.display, self.username.input, self.event_queue)
        game_loop.start()
        self.start_main_menu()

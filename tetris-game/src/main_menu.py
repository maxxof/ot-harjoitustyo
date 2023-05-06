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

        scores = self.get_scores()

        running = True
        while running:
            self.display.fill((200, 228, 240))

            if self.exit_btn.draw(self.display):
                return
            if self.start_btn.draw(self.display) and len(self.username.input) > 2:
                running = False
            for event in self.event_queue.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.username.backspace()
                    else:
                        if len(self.username.input) < 13:
                            self.username.add_char(event.unicode)

            pygame.draw.rect(self.display, self.username.rect_color, self.username.input_rect, 5)
            self.display.blit(self.username.surface, (self.username.input_rect.x + 7,
            self.username.input_rect.y + 9))
            self.display.blit(self.info, (500-self.info.get_width()/2, 50))
            self.render_scoreboard(scores)

            pygame.display.update()

        self.start_game_loop()

    def start_game_loop(self):
        """Luo uuden pelisilmukka-olion ja käynnistää pelisilmukan
        
        Kun pelisilmukasta poistutaan, käynnistetään uusi päävalikko-silmukka
        """

        game_loop = GameLoop(self.display, self.username.input, self.event_queue)
        game_loop.start()
        self.start_main_menu()

    def get_scores(self):
        path = os.path.join(dirname, "storage/highscores.csv")
        with open (path, encoding="utf-8") as file:
            scores = []
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                username, score = line.split(";")
                scores.append((username, score))
            return scores

    def render_scoreboard(self, scores):
        label = pygame.font.Font(None, 40).render("Top 5 Scoreboard", True, (255, 0, 0))
        self.display.blit(label, (500-label.get_width()/2, 400))
        pygame.draw.rect(self.display, (255, 0, 0),
                         ((500-label.get_width()/2 - 60, 380, 360, 320)), 6)

        height = 450
        for line in scores:
            score = line[0] + " " + line[1]
            label = pygame.font.Font(None, 40).render(score, True, (204, 102, 0))
            self.display.blit(label, (500-label.get_width()/2, height))
            height += 50
            
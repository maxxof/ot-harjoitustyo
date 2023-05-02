from random import choice
import pygame
from tetromino import Tetromino, shapes

class GameEngine:
    """Luokka, joka vastaa tetris-pelin logiikasta

    Attributes:
            grid_width: peliruudukon leveys
            grid_height: peliruudukon korkeus
            block_size: ruudun koko
            topleft_x: ruudukon vasen yläkulman x-koordinaatti
            topleft_y: ruudukon vasen yläkulman y-koordinaatti
            grid: ruudukko
            positions: tetrominon lohkojen lukitut koordinaatit
            cooldown: tetrominon putoamisesta vastuussa oleva viive
            fall_speed: tetrominon puotamisnopeus
            change_tetromino: kertoo onko tetromino vaihtumassa
            curr_tetromino: nykyinen tetromino
            next_tetromino: seuraava tetromino
        """

    def __init__(self):
        """Luokan konstruktori, joka luo tetris-pelin moottorin
        """

        self.grid_width = 400
        self.grid_height = 800
        self.block_size = 40
        self.topleft_x = (1000-self.grid_width) // 2
        self.topleft_y = 850-self.grid_height
        self.grid = None
        self.positions = {}
        self.cooldown = 0
        self.fall_speed = 0.27
        self.change_tetromino = False
        self.curr_tetromino = self.get_tetromino()
        self.next_tetromino = self.get_tetromino()

    def create_grid(self):
        """Luo uuden peliruudukon
        """

        self.grid = [[(0, 0, 0) for i in range(10)] for j in range(20)]

        for i, elem in enumerate(self.grid):
            for j in range(len(elem)):
                if (j, i) in self.positions:
                    col = self.positions[(j, i)]
                    self.grid[i][j] = col

    def render_grid(self, display):
        """Piirtää ruudukon

        Kaksi pääsilmukkaa, jossa yksi piirtää ruudukon piirin ja toinen
        piirtää ruudukon leveys- ja korkeusviivat
        
        Args:
            display: pinta, johon piirretään
        """

        size = self.block_size
        topleft_x = self.topleft_x
        topleft_y = self.topleft_y

        for i, elem in enumerate(self.grid):
            for j in range(len(elem)):
                pygame.draw.rect(display, self.grid[i][j],
                                 (topleft_x + j*size, topleft_y + i*size, size, size), 0)

        for i, row in enumerate(self.grid):
            pygame.draw.line(display, 'grey', (topleft_x, topleft_y + size * i),
                             (topleft_x + self.grid_width, topleft_y + size * i))
            for col in range(len(row)):
                pygame.draw.line(display, 'grey', (topleft_x + size * col, topleft_y),
                                 (topleft_x + size * col, topleft_y + self.grid_height))

        pygame.draw.rect(display, (0, 0, 255),
                         (topleft_x, topleft_y, self.grid_width, self.grid_height), 4)

    def get_tetromino(self):
        """Luo uuden Tetromino-olion
        
        Returns:
            Tetromino-olio
        """

        return Tetromino(5, 0, choice(shapes))

    def valid_position(self, tetromino):
        """Tarkistaa voidaanko tetromino sijoittaa kyseiseen ruudukon kohtaan

        Palauttaa False vain jos tetromino on ruudukossa
        
        Args:
            tetromino: Tetromino-olio

        Returns:
            True, jos voidaan sijoittaa, muussa tapauksessa False
        """

        formatted_tetromino = self.format_tetromino(tetromino)

        valid_positions = [[(j, i) for j in range(10) if self.grid[i][j] == (0, 0, 0)]
                           for i in range(20)]
        valid_positions = [i for j in valid_positions for i in j]

        for pos in formatted_tetromino:
            if pos not in valid_positions:
                if pos[1] > -1:
                    return False
        return True

    def format_tetromino(self, tetromino):
        """Muodostaa tetromino-olion lohkoista koordinaattiesityksen
        
        Args: 
            tetromino: Tetromino-olio

        Returns:
            tetrominon lohkojen koordinaattiesitys
        """

        coordinates = []
        rotation = tetromino.get_shape()[tetromino.get_rotation()]

        for i, row in enumerate(rotation):
            row = list(row)
            for j, col in enumerate(row):
                if col == '0':
                    coordinates.append((tetromino.get_x() + j - 2, tetromino.get_y() + i - 4))
        return coordinates

    def check_if_lost(self, coordinates):
        """Tarkistaa jos peli hävittiin
        
        Args:
            coordinates: tetrominon koordinaattiesitys

        Returns:
            True, jos yksi tetrominon koordinaateista ylittää ruudukon yläreunan, False muutoin
        """

        for coor in coordinates:
            coor_y = coor[1]
            if coor_y < 1:
                return True
        return False


    def move_tetromino_left(self):
        """Seuraavat neljä metodia liikuttavat tetrominon vasemmalle,
        oikealle, alas ja kääntävät sen
        """

        self.curr_tetromino.move_left()
        if not self.valid_position(self.curr_tetromino):
            self.curr_tetromino.move_right()

    def move_tetromino_right(self):
        self.curr_tetromino.move_right()
        if not self.valid_position(self.curr_tetromino):
            self.curr_tetromino.move_left()

    def move_tetromino_down(self):
        self.curr_tetromino.move_down()
        if not self.valid_position(self.curr_tetromino):
            self.curr_tetromino.move_up()

    def rotate_tetromino(self):
        self.curr_tetromino.rotate()
        if not self.valid_position(self.curr_tetromino):
            self.curr_tetromino.rotate_back()

    def tetromino_fall(self):
        """Pudottaa tetrominon alaspäin jos on kulunut riittävä viive viime putoamisesta
        
        Tarkistaa myös jos nykyinen tetromino osui maahan tai toiseen tetrominoon
        """

        if self.cooldown/1000 > self.fall_speed:
            self.cooldown = 0
            self.curr_tetromino.move_down()
            if not self.valid_position(self.curr_tetromino) and self.curr_tetromino.get_y() > 0:
                self.curr_tetromino.move_up()
                self.change_tetromino = True

    def update_grid(self):
        """Päivittää ruudukon tetrominon uusien koordinaattien avulla ja värittää ruudut

        Returns:
            Nykyisen tetrominon koordinaatit
        """

        tetromino_coordinates = self.format_tetromino(self.curr_tetromino)
        for i, coor in enumerate(tetromino_coordinates):
            coor_x, coor_y = coor
            if coor_y > -1:
                self.grid[coor_y][coor_x] = self.curr_tetromino.get_color()

        return tetromino_coordinates

    def lock_and_switch_tetromino(self, tetromino_coordinates):
        """Lukittaa tetrominon paikalleen ja vaihtaa tetrominon seuraavaan
        
        Args:
            tetromino_coordinates: tetrominon koordinaattiesitys

        """

        for coor in tetromino_coordinates:
            coordinate = (coor[0], coor[1])
            self.positions[coordinate] = self.get_tetromino_color(self.curr_tetromino)
        self.curr_tetromino = self.next_tetromino
        self.next_tetromino = self.get_tetromino()
        self.change_tetromino = False

    def get_tetromino_color(self, tetromino):
        """Palauttaa tetrominon värin
        
        Args:
            tetromino: tetromino-olio

        Returns:
            Tetromino-olion värin
        """

        return tetromino.get_color()

    def clear_grid_rows(self):
        """Puhdistaa kaikki peliruudukon rivit, jotka saatiin täyteen
        
        Jos riviä saatiin täyteen, kutsutaan seuraavaa metodia joka pudottaa kaikki
        yläpuolella olevat rivit alaspäin

        Returns:
            Puhdistettujen rivien määrä * 100 eli saadut pelipisteet
        """

        cleared_rows = 0
        for i in range(len(self.grid)-1, -1, -1):
            row = self.grid[i]
            if (0, 0, 0) not in row:
                cleared_rows += 1
                index = i
                for j in range(len(row)):
                    if self.positions[(j, i)]:
                        del self.positions[(j, i)]

        if cleared_rows > 0:
            self.move_blocks_down(cleared_rows, index)

        return cleared_rows * 100

    def move_blocks_down(self, cleared_rows, index):
        """Pudottaa tetrominolohkot n-verran alaspäin
        
        Args:
            cleared_rows: puhdistettujen rivien määrä
            index: alhasimman puhdistetun rivin indeksi
        """

        for coor in sorted(list(self.positions), key=lambda x: x[1])[::-1]:
            x_coor, y_coor = coor
            if y_coor < index:
                new_coor = (x_coor, y_coor + cleared_rows)
                self.positions[new_coor] = self.positions.pop(coor)

    def render_score(self, display, score):
        """Piirtä pelaajan pisteet
        
        Args:
            display: piirtopinta
            score: pisteet
        """

        font = pygame.font.Font(None, 40)
        label = font.render("Score", True, (0, 0, 0))
        score = font.render(str(score), True, (0, 0, 0))

        display.blit(label, (800, 500))
        display.blit(score, (840 - score.get_width()/2, 540))

    def render_next_tetromino(self, display):
        """Piirtää seuraavan tetrominon
        
        Args:
            display: piirtopinta
        """

        font = pygame.font.Font(None, 40)
        label = font.render("Next Tetromino", True, (0, 0, 0))

        rotation = self.next_tetromino.get_shape()[self.next_tetromino.get_rotation()]

        pygame.draw.rect(display, (0, 0, 0), pygame.Rect(750, 150, 200, 200))

        size = self.block_size
        for i, line in enumerate(rotation):
            row = list(line)
            for j, col in enumerate(row):
                if col == "0":
                    pygame.draw.rect(display, self.next_tetromino.get_color(),
                                     (750 + j * size, 160 + i * size, size, size), 0)

        display.blit(label, (750, 110))

    def render_game_over_message(self, display, score):
        """Piirtää viestin pelin häviämisen jälkeen
        
        Args:
            display: piirtopinta
            score: pisteet
        """

        font = pygame.font.Font(None, 60)
        label = font.render("Game Over", True, (255, 0, 0))
        score = font.render(f"Your score: {str(score)}", True, (255, 0, 0))

        pygame.draw.rect(display, (0, 0, 0), pygame.Rect(250, 300, 500, 200))
        pygame.draw.rect(display, (255, 0, 0),
                         (250, 300, 500, 200), 4)

        display.blit(label, (display.get_width()/2 - label.get_width()/2, 350))
        display.blit(score, (display.get_width()/2 - score.get_width()/2, 400))
        pygame.display.update()
        pygame.time.delay(5000)

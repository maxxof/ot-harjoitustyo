O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [O, I, S, Z, J, L, T]
colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255),
          (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Tetromino():
    """Luokka, joka imitoi yksinäistä tetrominoa ja pitää kirjaa
    sen x- ja y-koordinaateista ja rotaatiosta
    
    Attributes:
        coor_x: tetrominon x-koordinaatti
        coor_y: tetrominon y-koordinaatti
        shape: tetrominon muoto
        color: tetrominon väri
        rotation: tetrominon rotaatio
    """

    def __init__(self, coor_x, coor_y, shape):
        """Luokan konstruktori, joka luo uuden tetrominon
        
        Args:
            coor_x: aloituspaikan x-koordinaatti
            coor_y: aloituspaikan y-koordinaatti
            shape: muoto
        """

        self.coor_x = coor_x
        self.coor_y = coor_y
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.rotation = 0

    def move_left(self):
        """Seuraavat neljä metodia muuttavat tetrominon koordinaatteja
        yhden vasemmalle, yhden oikealle, yhden alas ja yhden ylös
        """

        self.coor_x -= 1

    def move_right(self):
        self.coor_x += 1

    def move_down(self):
        self.coor_y += 1

    def move_up(self):
        self.coor_y -= 1

    def rotate(self):
        """Muuttaa tetrominon rotaatiota
        
        Palaa tetrominon ensimmäiseen rotaatioon, jos ollaan viimeisessä rotaatiossa
        """

        if self.rotation + 1 == len(self.shape):
            self.rotation = 0
        else:
            self.rotation += 1

    def rotate_back(self):
        """Muuttaa tetrominon rotaation yhden taaksepäin
        """

        if self.rotation == 0:
            self.rotation = len(self.shape)-1
        else:
            self.rotation -= 1

    def get_x(self):
        """Palauttaa tetrominon x-koordinaatin
        
        Returns:
            x-koordinaatti
        """

        return self.coor_x

    def get_y(self):
        """Palauttaa tetrominon y-koordinaatin
        
        Returns:
            y-koordinaatti
        """

        return self.coor_y

    def get_color(self):
        """Palauttaa tetrominon värin
        
        Returns:
            väri
        """

        return self.color

    def get_shape(self):
        """Palauttaa tetrominon muodon
        
        Returns:
            muoto
        """

        return self.shape

    def get_rotation(self):
        """Palauttaa tetrominon rotaation
        
        Returns:
            rotaatio
        """

        return self.rotation

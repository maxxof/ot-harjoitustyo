# All possible rotations of tetromino shapes
# '.' = blank, '0' = block

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
    def __init__(self, coor_x, coor_y, shape):
        self.coor_x = coor_x
        self.coor_y = coor_y
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.rotation = 0

    def move_left(self):
        self.coor_x -= 1

    def move_right(self):
        self.coor_x += 1

    def move_down(self):
        self.coor_y += 1

    def move_up(self):
        self.coor_y -= 1

    def rotate(self):
        if self.rotation + 1 == len(self.shape):
            self.rotation = 0
        else:
            self.rotation += 1

    def rotate_back(self):
        if self.rotation == 0:
            self.rotation = len(self.shape)-1
        else:
            self.rotation -= 1

    def get_x(self):
        return self.coor_x

    def get_y(self):
        return self.coor_y

    def get_color(self):
        return self.color

    def get_shape(self):
        return self.shape

    def get_rotation(self):
        return self.rotation

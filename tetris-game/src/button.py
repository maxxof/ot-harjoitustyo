import pygame

class Button():
    def __init__(self, x, y, img, scale):
        width = img.get_width()
        height = img.get_height()
        self.img = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x-self.img.get_width()/2, y-self.img.get_height()/2)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.img, (self.rect.x, self.rect.y))
        return action
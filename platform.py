import pygame
from params import *
vec = pygame.math.Vector2

class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        #self.load_image()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.pos = vec(self.rect.centerx, self.rect.centery)

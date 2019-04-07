import pygame
from params import *

class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, width, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, PLATFORM_HEIGHT))
        self.image.fill(GREEN)
        #self.load_image()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

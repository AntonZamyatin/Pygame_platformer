import pygame
from params import *
vec = pygame.math.Vector2

class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, game, platform_type):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.load_image(platform_type)
                #self.load_image()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.pos = vec(self.rect.centerx, self.rect.centery)

    def load_image(self, platform_type):
        if platform_type == 1:
            self.image = self.game.tiles_spritesheet.get_image(505, 505, 69, 69, (40, 40))
        elif platform_type == 2:
            self.image = self.game.tiles_spritesheet.get_image(0, 0, 69, 69, (40, 40))

import pygame
import numpy as np
from platform import *

class Level_map():
    """Level matrices"""

    def __init__(self, file_name, game):
        self.game = game
        mapar = []
        i = 0
        with open(file_name, 'r') as file:
            for line in file:
                mapar.append([])
                for el in line.strip():
                    mapar[i].append(int(el))
                i += 1
        self.level_array = np.array(mapar)

    def get_sprites(self):
        platforms_group = pygame.sprite.Group()
        for x in range(len(self.level_array)):
            for y in range(len(self.level_array[0])):
                platform_type = self.level_array[x, y]
                if platform_type == 0:
                    continue
                platforms_group.add(Platform(y * 40, x * 40, 40, 40, self.game, platform_type))
        return platforms_group

import pygame
import numpy as np
from platform import Platform

class Level_map():
    """Level matrices"""

    def __init__(self, file_name):
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
                if self.level_array[x, y] == 1:
                    platforms_group.add(Platform(y * 20, x * 20, 20, 20, self))
        return platforms_group


import pygame
import numpy as np
from platform import Platform

class Level_map():

    def __init__(self, filename):
        mapar = []
        i = 0
        with open(filename, 'r') as file:
            for line in file:
                mapar.append([])
                for el in line.strip():
                    mapar[i].append(int(el))
                i += 1
        self.level_array = np.array(mapar)

    def get_sprites(self):
        platform_group = pygame.sprite.Group()
        for i in range(len(self.level_array)):
            for j in range(len(self.level_array[0])):
                if self.level_array[i,j] == 1:
                    platform_group.add(Platform(j * 20, i * 20, 20, 20, self))
        return platform_group

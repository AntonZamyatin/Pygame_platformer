"""Best game ever."""

from params import *
import numpy as np
import pygame
from player import *
from platform import Platform
from img_utils import *
from level_map import *


class Game(object):

    def __init__(self):
        # initialize pygame and create window
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Cosmoplat")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player_spritesheet = Spritesheet(os.path.join(img_folder,
                                                    "p1_spritesheet.png"))
        self.tile_spritesheet = Spritesheet(os.path.join(img_folder,
                                                    "tiles_spritesheet.png"))


    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

        self.lmap = Level_map(os.path.join(game_folder, "lvl1.txt"), self)
        self.platforms = self.lmap.get_sprites()


        self.run()

    def run(self):
        while self.running:
            # keep loop running at the right speed
            self.clock.tick(FPS)
            # Process input (events)
            for event in pygame.event.get():
                # check for closing window
                if event.type == pygame.QUIT:
                    self.running = False

            # Update
            self.all_sprites.update()

            # Draw / render
            screen = pygame.display.set_mode((800, 600))
            background_image = pygame.image.load('fon_2.jpg')
            screen.blit(background_image, (0, 0))
            self.platforms.draw(self.screen)
            self.all_sprites.draw(self.screen)
            pygame.display.update()

            # *after* drawing everything, flip the display
            pygame.display.flip()


if __name__ == "__main__":
    G = Game()
    G.new()

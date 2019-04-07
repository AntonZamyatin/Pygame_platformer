"""Best game ever."""

import pygame
from params import *
from player import *
from img_utils import *

class Game(object):

    def __init__(self):
        # initialize pygame and create window
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.spritesheet = Spritesheet(os.path.join(img_folder,
                                                    "p1_spritesheet.png"))

    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
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
            self.screen.fill(BLUE)
            self.all_sprites.draw(self.screen)

            # *after* drawing everything, flip the display
            pygame.display.flip()


if __name__ == "__main__":
    G = Game()
    G.new()

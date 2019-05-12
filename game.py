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

        self.tiles_spritesheet = Spritesheet(os.path.join(img_folder,
                                                    "tiles_spritesheet.png"))
        #self.ground = Platform(0, HEIGHT - 40, WIDTH, 40, self, 1)

    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.camera = Camera(self)

        self.foreground = Foreground()

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
            self.player.update()
            self.camera.update()

            # Draw / render
            self.screen.fill (BLUE)
            self.platforms.draw(self.screen)
            self.all_sprites.draw(self.screen)
            #self.screen.blit(self.foreground.image, self.foreground.rect)

            # *after* drawing everything, flip the display
            pygame.display.flip()


class Camera():

    def __init__(self, game):
        self.pos = game.player.rect.center
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.game = game
        self.dist_x = 0
        self.dist_y = 0

    def update(self):
        # time increment
        dt = self.game.clock.get_time()
        if dt > 2000 / FPS:
            dt = 0

        old_x = self.pos[0]
        old_y = self.pos[1]
        self.acc = vec(- self.dist_x*CAM_X_ACC, - self.dist_y*CAM_Y_ACC)

        # apply x friction
        self.acc.x += self.vel.x * CAM_Y_FRICTION

        # apply y friction
        self.acc.y += self.vel.y * CAM_Y_FRICTION

        self.vel += self.acc * dt
        self.pos += self.vel * dt
        if -5 < self.dist_x < 5:
            self.acc.x = 0
            self.vel.x = 0
        if -15 < self.dist_y < 15:
            self.acc.y = 0
            self.vel.y = 0

        self.dist_x = WIDTH / 2 - self.game.player.rect.center[0]
        self.dist_y = HEIGHT * 5 / 7 - self.game.player.rect.center[1]
        print(self.dist_x, self.dist_y)
        for sprite in list(self.game.all_sprites) + list(self.game.platforms):
            sprite.rect.centerx -= round(self.pos[0] - old_x)
            sprite.pos.x -= round(self.pos[0] - old_x)
            sprite.rect.centery -= round(self.pos[1] - old_y)
            sprite.pos.y -= round(self.pos[1] - old_y)

class Foreground(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,
                                                    "back.png"))
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]

if __name__ == "__main__":
    G = Game()
    G.new()

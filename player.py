import pygame
from params import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((30, 40))
        #self.image.fill(YELLOW)
        self.load_image()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 60)
        self.pos = vec(WIDTH / 2, HEIGHT - 60)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.on_ground = True

    def load_image(self):
        self.image = self.game.spritesheet.get_image(0, 0, 72, 95)

    def update(self):
        if self.on_ground:
            self.acc = vec(0, 0)
        else:
            self.acc = vec(0, GRAVITY_ACC)

        keys = pygame.key.get_pressed()
        if self.on_ground:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.acc.x = -PLAYER_ACC
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.acc.x = PLAYER_ACC

        # jump
        if self.on_ground and keys[pygame.K_SPACE]:
            self.jump()

        # apply friction
        if self.on_ground:
            self.acc.x += self.vel.x * PLAYER_FRICTION

        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        # check ground
        if self.pos.y >= HEIGHT - 60:
            self.on_ground = True
            self.vel.y = 0
            self.pos.y = HEIGHT - 60

        self.rect.center = self.pos

    def jump(self):
        self.on_ground = False
        self.acc.y = -20

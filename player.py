import pygame
from params import *
from math import sqrt
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self, game):
        self.game = game
        self.clock = self.game.clock
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((30, 40))
        #self.image.fill(YELLOW)
        self.load_image()
        self.rect = self.image.get_rect()
        self.rect.center = (60, 240)
        self.pos = vec(60, 240)


        self.vel = vec(0, 0)
        self.acc = vec(0, GRAVITY_ACC)

        self.on_ground = False
        self.idle = True

        # animation lists
        self.last_update = 0
        self.idle_frame = 0
        idle_list_rects = [(0, 191, 67, 95),
                           (67, 191, 67, 95)]
        self.idle_list = self.game.player_spritesheet\
                             .get_image_list(idle_list_rects)

        self.idle_list += [self.idle_list[0],
                           pygame.transform.flip(self.idle_list[1], True, False)]

    def load_image(self):
        self.image = self.game.player_spritesheet.get_image(0, 0, 72, 95)

    def update(self):
        # time increment
        dt = self.game.clock.get_time()
        if dt > 2000 / FPS:
            dt = 0

        # default acc
        if self.on_ground:
            self.acc = vec(0, 0)
        else:
            self.acc = vec(0, GRAVITY_ACC)

        # keys events
        keys = pygame.key.get_pressed()
        if self.on_ground:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.acc.x = -PLAYER_ACC
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.acc.x = PLAYER_ACC
            # jump
            if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
                self.jump()
            # platform down
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.on_ground = False

        # apply friction
        if self.on_ground:
            self.acc.x += self.vel.x * PLAYER_FRICTION

        # apply fall friction
        if not self.on_ground:
            self.acc.y += self.vel.y * FALL_FRICTION

        # equations of motion
        self.vel += self.acc * dt

        self.move_pos(dt)
        '''
        vec_len = int(sqrt((old_pos.x - new_pos.x)**2 + (old_pos.y - new_pos.y)**2)) + 1
        #final_pos = vec(0, 0)
        for i in range(vec_len):
            self.pos = old_pos + (new_pos - old_pos) * (i + 1) / vec_len
            # смещаем плеера для проверки новой позиции...
            self.rect.centery += round(self.pos.y - old_pos.y)
            self.rect.centerx += round(self.pos.x - old_pos.x)
            platform = pygame.sprite.spritecollide(self, self.game.platforms, False)
            for plat in platform:

                if ((plat.rect.top <= self.rect.top <= plat.rect.bottom) or (plat.rect.top <= self.rect.bottom <= plat.rect.bottom)) and (self.rect.left <= plat.rect.left) and (plat.rect.right <= self.rect.right):
                    self.vel.y = 0
                if ((plat.rect.left <= self.rect.left <= plat.rect.right) or (plat.rect.left <= self.rect.right <= plat.rect.right)) and (self.rect.top <= plat.rect.top) and (plat.rect.bottom <= self.rect.bottom):
                    self.vel.x = 0
            # возвращаем плеера обратно...
            self.rect.centery -= round(self.pos.y - old_pos.y)
            self.rect.centerx -= round(self.pos.x - old_pos.x)
            if platform:
                self.pos = old_pos + (new_pos - old_pos) * i / vec_len
                #pygame.quit();
                break

        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        # check ground
        cur_plat = pygame.sprite.spritecollide(self, self.game.platforms, False)
        if cur_plat:
            self.on_ground = True
            self.vel.y = 0
            self.pos.y = cur_plat[0].rect.top + (cur_plat[0].pos.y - cur_plat[0].rect.centery)'''
        '''
        screen_offset = vec(0, 0)

        if self.pos.x > WIDTH / 2:
            screen_offset.x = int(self.pos.x - WIDTH / 2)
        if self.pos.x > len(self.game.lmap.level_array[0])*40 - WIDTH / 2:
            screen_offset.x = int(len(self.game.lmap.level_array[0])*40 - WIDTH)

        if self.pos.y > HEIGHT / 2:
            screen_offset.y = int(self.pos.y - HEIGHT / 2)
        if self.pos.y > len(self.game.lmap.level_array)*40 - HEIGHT / 2:
            screen_offset.y = int(len(self.game.lmap.level_array)*40 - HEIGHT)  #'''


        #self.rect.midbottom = self.pos# - screen_offset

        '''
        for sprite in self.game.platforms:
            sprite.rect.center = sprite.pos - screen_offset
        '''

        self.animate()

    def move_pos(self, dt):
        old_x, old_y = self.pos.x, self.pos.y
        self.pos.x = round(old_x + self.vel.x * dt)
        self.pos.y = round(old_y + self.vel.y * dt)
        self.collide_with_tiles(old_x, old_y)
        if self.on_ground:
            self.onground_check()

    def onground_check(self):
        self.rect.centery += 1
        hit = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.centery -= 1
        plats = []
        for plat in hit:
            dist = plat.rect.top - self.rect.bottom
            if dist == 0:
                plats.append(plat)
        if plats:
            if len(plats) == 1 and \
                plats[0].rect.centerx - 20 < self.rect.centerx < plats[0].rect.centerx + 20:
                self.on_ground = True
                self.vel.y = 0
                self.acc.y = 0
            elif len(plats) > 1:
                self.on_ground = True
                self.vel.y = 0
                self.acc.y = 0
            else:
                self.on_ground = False
        else:
            self.on_ground = False

    def collide_with_tiles(self, old_x, old_y):
        hit = None
        # bottom
        if self.vel.y > 0:
            self.rect.midbottom = self.pos
            self.rect.bottom += 1
            hit = pygame.sprite.spritecollide(self, self.game.platforms, False)
            nearest = None
            if len(hit) > 0:
                r = 200
                for plat in hit:
                    dist = plat.rect.top - old_y
                    if dist >= 0 and dist < r:
                        r = dist
                        nearest = dist
                        hit = plat
            if nearest:
                print('HIT')
                self.on_ground = True
                self.vel.y = 0
                self.acc.y = 0
                self.rect.bottom = plat.rect.top
                self.rect.centerx = self.pos.x
                self.pos.y = plat.rect.top
        else:
            self.rect.midbottom = self.pos

    def jump(self):
        self.on_ground = False
        self.acc.y = -12 * GRAVITY_ACC

    def animate(self):
        now = pygame.time.get_ticks()
        if self.idle:
            if now - self.last_update > 300:
                self.last_update = now
                self.idle_frame = (self.idle_frame + 1) % 4
                self.image = self.idle_list[self.idle_frame]

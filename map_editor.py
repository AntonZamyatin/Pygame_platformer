import pygame
import numpy as np

GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
BLACK = (0, 0, 0)

class Editor(object):

    def __init__(self):
        #self.spritesheet = Spritesheet(os.path.join(img_folder,
        #                                            "p1_spritesheet.png"))
        self.cell_width = 40
        self.y_shift = 0
        self.x_shift = 0

    def start(self):
        # start a new game
        self.map_height = 100
        self.map_width = 100
        self.level_map = np.zeros((self.map_height, 100))  # tuple(map(int, input("Enter new map size:").split())))
        # initialize pygame and create window
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("map editor")
        self.minimap = pygame.Surface((202, 202))
        self.minimap_rect = self.minimap.get_rect()
        self.minimap_rect.topleft = (1040, 20)
        self.draw_interface()
        self.run()

    def draw_interface(self):
        pygame.draw.line(self.screen, GREEN, [1000, 0], [1000, 720], 1)
        self.draw_greed()

    def draw_greed(self):
        for x in range(25):
            pygame.draw.line(self.screen, DARK_GREEN,
                             [x * 40, 0], [x * 40, 720], 1)
        for y in range(18):
            pygame.draw.line(self.screen, DARK_GREEN,
                             [0, y * 40], [999, y * 40], 1)

    def handle_events(self):
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                self.running = False
            # check ,ouse click
            if event.type == pygame.MOUSEMOTION or\
               event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] < 1000 and\
                   pygame.mouse.get_pos()[1] < 720:
                    if pygame.mouse.get_pressed()[0]:
                        pos = [0, 0]
                        m_pos = pygame.mouse.get_pos()
                        pos[1] = m_pos[0] // 40 + self.x_shift
                        pos[0] = self.map_height - (720 - m_pos[1]) // 40 \
                                                 - 1 - self.y_shift
                        self.level_map[tuple(pos)] = 1
                    elif pygame.mouse.get_pressed()[2]:
                        pos = [0, 0]
                        m_pos = pygame.mouse.get_pos()
                        pos[1] = m_pos[0] // 40 + self.x_shift
                        pos[0] = self.map_height - (720 - m_pos[1]) // 40 \
                                                 - 1 - self.y_shift
                        self.level_map[tuple(pos)] = 0
            # shift screen
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.y_shift < self.map_height - 18:
                self.y_shift += 1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if 0 < self.y_shift:
                self.y_shift -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.x_shift < self.map_width - 25:
                self.x_shift += 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if 0 < self.x_shift:
                self.x_shift -= 1

    def draw_rect(self, color, x, y):
        pygame.draw.rect(self.screen, color,
                         (x * self.cell_width + 1,
                          y * self.cell_width + 1,
                          self.cell_width - 1,
                          self.cell_width - 1))

    def update_minimap(self):
        self.minimap.fill(BLACK)
        pygame.draw.rect(self.minimap, DARK_GREEN, (0, 0, 202, 202), 1)
        for y in range(self.map_height):
            for x in range(self.map_width):
                if self.level_map[y, x] == 1:
                    pygame.draw.rect(self.minimap, GREEN, (x*2, y*2, 2, 2))
        self.screen.blit(self.minimap, (1040, 20, 202, 202))

    def update(self):
        # black screen
        self.screen.fill(BLACK)
        self.draw_interface()
        #drow map
        for y in range(self.map_height - 18 - self.y_shift, self.map_height - self.y_shift):
            for x in range(self.x_shift, self.x_shift + 25):
                if self.level_map[y, x] == 1:
                    self.draw_rect(GREEN, x - self.x_shift, y - self.map_height + 18 + self.y_shift)
        self.update_minimap()


    def run(self):
        self.running = True
        while self.running:
            # keep loop running at the right speed
            self.clock.tick(30)
            # Process events
            self.handle_events()

            # update Field
            self.update()

            # *after* drawing everything, flip the display
            pygame.display.flip()
        print(self.level_map)


if __name__ == "__main__":
    E = Editor()
    E.start()

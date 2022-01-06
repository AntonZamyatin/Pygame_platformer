import pygame

class Spritesheet():
    # utility class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height, new_size=None):
        # grab an image out of a larger spritesheet
        """image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width // koef_scale,
                                               height // koef_scale))
        """
        image = self.spritesheet.subsurface(x, y, width, height)
        if new_size:
            image = pygame.transform.scale(image, new_size)
        return image

    def get_image_list(self, rect_list):
        image_list = []
        for rect in rect_list:
            image_list.append(self.spritesheet.subsurface(rect))
        return image_list

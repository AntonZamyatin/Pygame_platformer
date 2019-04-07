import pygame

class Spritesheet():
    # utility class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height, koef_scale=1):
        # grab an image out of a larger spritesheet
<<<<<<< HEAD
        '''
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width // koef_scale,
                                               height // koef_scale))
        return image
        # '''
=======
        """image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width // koef_scale,
                                               height // koef_scale))
        """
>>>>>>> 022362536a169921d0af6cfedcdfa30a6c314659
        return self.spritesheet.subsurface(x, y, width, height)

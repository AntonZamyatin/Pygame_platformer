import os

WIDTH = 800
HEIGHT = 600

FPS = 30

BLACK = 0, 0, 0
BLUE = 0, 0, 255
GREEN = 0, 255, 0
YELLOW = 255, 255, 0

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITATION = 1

PLATFORM_HEIGHT = 20

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'Img')

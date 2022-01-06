import os

WIDTH = 800
HEIGHT = 600

FPS = 30

BLACK = 0, 0, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0
GREEN = 0, 255, 0
RED = 255, 0, 0

# Player properties
PLAYER_ACC = 0.001
PLAYER_FRICTION = -0.005
FALL_FRICTION = -0.002
GRAVITY_ACC = 0.003

# Camera properties
CAM_X_ACC = 0.00002
CAM_Y_ACC = 0.00004
CAM_X_FRICTION = -0.002
CAM_Y_FRICTION = -0.006

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

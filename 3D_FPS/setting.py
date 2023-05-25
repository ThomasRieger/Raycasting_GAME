import math 

RES = WIDTH,HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0

PLAYER_POS = 1.5, 5 
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.08
PLAYER_ROTATION_SPEED = 0.06

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUMBER_RAY = WIDTH // 2
HALF_RAY = NUMBER_RAY // 2
DELTA_ANGLE = FOV / NUMBER_RAY
MAX_DEPTH = 20

SCREEN_PRO = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUMBER_RAY
import numpy

SCREEN_W, SCREEN_H = 1280, 720
SCREEN_SIZE = (SCREEN_W, SCREEN_H)
SCREEN_COLOR = (230, 230, 230)
CELL_COLOR = [(210, 210, 210), (190, 190, 190)]
WALL_COLOR = (80, 80, 80)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
DARK_GRAY = (100, 100, 100)
FRAME_RATE = 144
CURSOR_MULTI = 1.5
PLAYER_MULTI = 1.0
PLAYER_PX = 41
PLAYER_PY = 27
ROUND_PX = 9
ROUND_PY = 9
MOTION_CALC_SCALE = 100
MPX = MOTION_CALC_SCALE*PLAYER_PX
MPY = MOTION_CALC_SCALE*PLAYER_PY
ROUND_COLLITION_EPS = 6
WALL_SIZE = 8
LOAD_TIME = 1000
TOP_SPACE = 42
LEFT_SPACE = 74
PI = numpy.arccos(-1)
FONT = 'Fixedsys.ttf'
PLAYER1_X, PLAYER1_Y = 250, 290
BASE_ROUND_V = 350.0/FRAME_RATE*60
BASE_MOVE_V = 255.0/FRAME_RATE*60
BASE_TURN_W = 1.0/5.8/PI/FRAME_RATE*60
BACKWARD_V = 0.83*BASE_MOVE_V
GRAVI_ACC = 4/FRAME_RATE*60
ENDING_TIME = 3000
CELEBRATING_TIME = 2000
SUPPLY_TIME = 10000
MAX_ROUND_TIME = 11000
MAX_ROUND_NUM = 15
FIRE_TICK = 110
FIRE_COOL_DOWN = 220
COLUMN_NUM = 12
ROW_NUM = 6
BLOCK_SIZE = 94
TOP, BOTTOM, LEFT, RIGHT = 1, 2, 4, 8
LEVEL, VERTICAL = 0, 1
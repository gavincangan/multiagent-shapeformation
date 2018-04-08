import pdb

INVALID = -999
HARD_PLACE = -999

ANY_TIME = -999
SOMETIME = 25
tLIMIT = 25

TWAIT = 0
WAIT_FACTOR = 0.51

MAX_STEPS = 45

UNOCCUPIED = 0
IS_ROCK = -99

MOVE_SPEED = 1
MSG_BUFFER_SIZE = 3

FRAME_HEIGHT = 600
FRAME_WIDTH = 600

FRAME_MARGIN = 10
CELL_MARGIN = 5

MAX_AGENTS_IN_CELL = 1

class Actions(object):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3
    WAIT = 4

COLORS = ['red', 'green', 'blue', 'black', 'white', 'magenta', 'cyan', 'yellow']

MIN_COLOR = 0
MAX_COLOR = len(COLORS) - 1
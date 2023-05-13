# from constants import *
#from constants import SCREEN_WIDTH
#from constants import SCREEN_HEIGHT
#from constants import SCREEN_TITLE
import arcade
from video.display import Display_board

class Conductor:
    def __init__(self) -> None:
        pass



    def build_game():
        Display_board(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.run()

# Set how many rows and columns we will have
ROW_COUNT = 8
COLUMN_COUNT = 8

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Array Backed Grid Buffered Example"
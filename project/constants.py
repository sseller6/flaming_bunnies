import arcade

# Set how many rows and columns we will have
ROW_COUNT = 9
COLUMN_COUNT = 9

# This sets the WIDTH and HEIGHT of each tile
TILE_WIDTH = 30
TILE_HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
TILE_MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (TILE_WIDTH + TILE_MARGIN) * COLUMN_COUNT + TILE_MARGIN
SCREEN_HEIGHT = (TILE_HEIGHT + TILE_MARGIN) * ROW_COUNT + TILE_MARGIN


SCREEN_1_TITLE = "Screen 1"
BACKGROUND = arcade.color.WHITE

# Entity images
KNIGHT_IMAGE = r"Planning/art/players/knight_1.png"
KNIGHT_WIDTH = 20
KNIGHT_HEIGHT = 20

WIZARD_IMAGE = r"Planning/art/players/mage_1.png"
WIZARD_WIDTH = 20
WIZARD_HEIGHT = 20

ARCHER_IMAGE = r"Planning/art/players/archer_1.png"
ARCHER_WIDTH = 20
ARCHER_HEIGHT = 20

CHARACTER_SCALING  = 0.1
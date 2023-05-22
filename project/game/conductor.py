from constants import *
import arcade
from .video.display import Display



class Conductor:
    def __init__(self):
        pass

    def build_game(self):
        window = Display(SCREEN_1_TITLE, BACKGROUND, SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.run()
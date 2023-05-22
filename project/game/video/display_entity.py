import constants
import arcade
from display import Display


class Display_entity(arcade.sprite):
    def __init__(self) -> None:
        super().__init__()

    def draw(self, image, scale):
        #When called, the image parameter comes from the entity class.
        #something like this: 
        sprite = arcade.Sprite(image, scale)
        return sprite
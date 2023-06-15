from constants import *
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
    
    def setup(self):

        """Set up the game here. Call this function to restart the game."""

        # Create the Sprite lists

        self.player_list = arcade.SpriteList()

        self.wall_list = arcade.SpriteList(use_spatial_hash=True)



        # Set up the player, specifically placing it at these coordinates.

        image_source = "Planning/art/players/knight_1.png"

        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)

        self.player_sprite.center_x = 64

        self.player_sprite.center_y = 128

        self.player_list.append(self.player_sprite)
from constants import *
import arcade



class Display(arcade.Window):
    def __init__(self,title, background, width, height):
        super().__init__(width, height, title)
        
        arcade.set_background_color(background)

        

    def on_draw(self):
        self.clear()
        arcade.start_render()
        #Draw commands


    def draw_menu():
        pass
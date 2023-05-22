import arcade


class Board():
    def __init__(self, rows, columns, width, margin, height):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.margin = margin
        self.height = height
        #self.map = map

        # One dimensional list of all sprites in the two-dimensional sprite list
        self.grid_sprite_list = arcade.SpriteList()

        # This will be a two-dimensional grid of sprites to mirror the two
        # dimensional grid of numbers. This points to the SAME sprites that are
        # in grid_sprite_list, just in a 2d manner.
        self.grid_sprites = []

        # Create a list of solid-color sprites to represent each grid location
        for row in range(rows):
            self.grid_sprites.append([])
            for column in range(columns):
                x = column * (width + margin) + (width / 2 + margin)
                y = row * (height + margin) + (height / 2 + margin)
                sprite = arcade.SpriteSolidColor(width, height, arcade.color.WHITE)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)
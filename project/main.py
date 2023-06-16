from typing import Optional
import arcade
from arcade import Texture

# constants:

#board dimensions
ROW_COUNT = 8
COLUMN_COUNT = 8

#Width and height of each cell in pixels
CELL_WIDTH = 70
CELL_HEIGHT = 70


#background color:
BACKGROUND = arcade.color.BLACK


#Cell margin between each cell and borders in pixels
CELL_MARGIN = 9

#math for window dimensions
SCREEN_WIDTH = (CELL_WIDTH + CELL_MARGIN) * COLUMN_COUNT + CELL_MARGIN
SCREEN_HEIGHT = (CELL_HEIGHT + CELL_MARGIN) * ROW_COUNT +  CELL_MARGIN
SCREEN_TITLE = "Checkers"


#piece images
p1_img = r"project\images\possible move.png"
p2_img = r"project\images\tanPiece.png"
move_img = r"project\images\possible move.png"
SPRITE_SCALING_PIECE = .5

class Piece(arcade.Sprite):
    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: str | None = "Simple", hit_box_detail: float = 4.5, texture: Texture = None, angle: float = 0):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)

    # def update(self):
    #     self.center_x = self.change_x
    #     self.center_y = self.change_y


class Checkers(arcade.Window):
    

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.background_color = BACKGROUND

        self.piece_index = None


        #sprite list for board
        self.grid_sprite_list = arcade.SpriteList()
        self.grid_sprites = []

        #sprite list for player1 pieces
        self.p1_list = arcade.SpriteList()
        self.p1_grid = []

        #sprite list for player2 pieces
        self.p2_list = arcade.SpriteList()
        self.p2_grid = []

        #sprite list for possible moves
        self.possible_move_list = arcade.SpriteList()
        self.possible_move_grid = []
        
        #setup board
        for row in range(ROW_COUNT):
            if row % 2 == 0:
                checker_checker = 0
            else:
                checker_checker = 1
            self.grid_sprites.append([])
            self.p1_grid.append([])
            self.p2_grid.append([])
            self.possible_move_grid.append([])
            for column in range(COLUMN_COUNT):
                x = column * (CELL_WIDTH + CELL_MARGIN) + (CELL_WIDTH / 2 + CELL_MARGIN)
                y = row * (CELL_HEIGHT + CELL_MARGIN)  + (CELL_HEIGHT /2 + CELL_MARGIN)
                if checker_checker == 0:
                    sprite = arcade.SpriteSolidColor(CELL_WIDTH, CELL_HEIGHT, arcade.color.TAN)
                    checker_checker = 1
                    possible_move = arcade.Sprite(move_img, SPRITE_SCALING_PIECE)
                    possible_move.center_x = x
                    possible_move.center_y = y
                    possible_move.visible = False
                    self.possible_move_list.append(possible_move)
                    self.possible_move_grid[row].append(possible_move)
                    if row <= 2:
                        p1_piece = Piece(p1_img, SPRITE_SCALING_PIECE)
                        p1_piece.center_x = x
                        p1_piece.center_y = y
                        self.p1_list.append(p1_piece)
                        self.p1_grid[row].append(p1_piece)
                        self.p2_grid[row].append("empty")
                    elif row >= 5:
                        
                        p2_piece = Piece(p2_img, SPRITE_SCALING_PIECE)
                        p2_piece.center_y = y
                        p2_piece.center_x = x
                        self.p2_list.append(p2_piece)
                        self.p2_grid[row].append(p2_piece)
                        self.p1_grid[row].append("empty")
                    else:
                        self.p1_grid[row].append("empty")
                        self.p2_grid[row].append("empty")

                else:
                    sprite = arcade.SpriteSolidColor(CELL_WIDTH, CELL_HEIGHT, arcade.color.RED_BROWN)
                    checker_checker = 0
                    self.p1_grid[row].append("empty")
                    self.p2_grid[row].append("empty")
                    self.possible_move_grid[row].append("empty")
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)
    
    def update_piece_position(self, piece):
        self.p1_list

    def on_draw(self):

        self.clear()
        self.grid_sprite_list.draw()
        self.p1_list.draw()
        self.p2_list.draw()
        self.possible_move_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        column = int(x // (CELL_WIDTH + CELL_MARGIN))
        row = int(y // (CELL_HEIGHT + CELL_MARGIN))
        if self.piece_index != None:
            if self.possible_move_grid[row][column] != "empty":
                if self.possible_move_grid[row][column].visible == True:
                    move_to_index = find_nearest_piece(self.possible_move_list, column, row)
                    if self.possible_move_list.sprite_list[move_to_index].center_x > self.p1_list.sprite_list[self.piece_index].center_x:
                        self.p1_grid[row][column] = self.p1_grid[row - 1][column - 1]
                        self.p1_grid[row - 1][column - 1] = "empty"
                    else:
                        self.p1_grid[row][column] = self.p1_grid[row - 1][column + 1] 
                        self.p1_grid[row - 1][column + 1] = "empty"

                    self.p1_list.sprite_list[self.piece_index].center_x = self.possible_move_list.sprite_list[move_to_index].center_x
                    self.p1_list.sprite_list[self.piece_index].center_y = self.possible_move_list.sprite_list[move_to_index].center_y
                    
                    self.piece_index = None
                    print("change location")
                    for i in self.possible_move_list.sprite_list:
                        i.visible = False
        else:        
            for i in self.possible_move_list.sprite_list:
                i.visible = False

            
            
            if row >=  ROW_COUNT or column >= COLUMN_COUNT:
                return
            
            if self.p1_grid[row][column] != "empty":
                print(f"Clicked on a player 1 piece. at {row},{column}")
                self.piece_index = find_nearest_piece(self.p1_list.sprite_list, column, row)
                
                
                self.possible_move_grid[row + 1][column + 1].visible = True
                self.possible_move_grid[row + 1][column - 1].visible = True
                
            elif self.p2_grid[row][column] != "empty":
                print(f"Clicked on a player 2 piece. at {row},{column}")
                index = find_nearest_piece(self.p2_list.sprite_list, column, row)
                self.p2_list.sprite_list[index].center_x -= (CELL_WIDTH + CELL_MARGIN)
                self.p2_list.sprite_list[index].center_y -= (CELL_HEIGHT + CELL_MARGIN)
                self.p2_grid[row - 1][column - 1] = self.p2_grid[row][column]
                self.p2_grid[row][column] = "empty"
        
    def on_update(self, delta_time):
        self.p1_list.update()
        self.p2_list.update()
        self.possible_move_list.update()


def find_nearest_piece(sprite_list, column, row):
    closest_index_x = 10000
    closest_index_y = 10000
    for i in range(len(sprite_list)):
        if i < len(sprite_list):
            if (abs((sprite_list[i].center_x // (CELL_WIDTH + CELL_MARGIN)) - column) < closest_index_x) or (abs((sprite_list[i].center_y // (CELL_HEIGHT + CELL_MARGIN)) - row) < closest_index_y) :
                closest_index_x = abs((sprite_list[i].center_x // (CELL_WIDTH + CELL_MARGIN)) - column)
                closest_index_y = abs((sprite_list[i].center_y // (CELL_HEIGHT + CELL_MARGIN))- row)
                closest_index = i
    
    return closest_index




def main():
    Checkers(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

main()
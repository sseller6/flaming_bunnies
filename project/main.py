from typing import Optional
import PIL
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
p1_img = r"project\images\redPiece.png"
p2_img = r"project\images\tanPiece.png"
move_img = r"project\images\possible move.png"

RED_QUEEN = r"project\images\redQueen.png"
TAN_QUEEN = r"project\images\tanQueen.png"
SPRITE_SCALING_PIECE = .5

class Piece(arcade.Sprite):
    # as is, Piece is just a class of arcade.sprite. As we add new attributes and methods, this would grow.

    #This init is just default init for arcade.sprite
    def __init__(self, filename: str = None, scale: float = 1, image_x: float = 0, image_y: float = 0, image_width: float = 0, image_height: float = 0, center_x: float = 0, center_y: float = 0, repeat_count_x: int = 1, repeat_count_y: int = 1, flipped_horizontally: bool = False, flipped_vertically: bool = False, flipped_diagonally: bool = False, hit_box_algorithm: str | None = "Simple", hit_box_detail: float = 4.5, texture: Texture = None, angle: float = 0):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y, repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally, hit_box_algorithm, hit_box_detail, texture, angle)
        self.is_queen = False

    #This was an attempt for implementing the movement of pieces.
    # def update(self):
    #     self.center_x = self.change_x
    #     self.center_y = self.change_y


#the main window for checkers and what maintains the gamestate.
class Checkers(arcade.Window):
    
    #default parameters for arcade.window.
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        #set the background color
        self.background_color = BACKGROUND


        #this is to keep track of the last clicked piece.
        self.piece_index = None

        #track player's turns
        self.is_p1_turn = True

        #initialize all the sprites for the board, all the pieces, and possible moves. 
        #the first list is the default sprite list
        #the second tracks the sprites in 2 dimensions.


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

        #Two for loops to make a 2d space
        for row in range(ROW_COUNT):

            #this will alternate the starting condition for each row so that things can be checkered.
            if row % 2 == 0:
                checker_checker = 0
            else:
                checker_checker = 1
            
            #we append a new list for a column, each item containing an item at a coordinate. The coordinate is [row][column]
            self.grid_sprites.append([])
            self.p1_grid.append([])
            self.p2_grid.append([])
            self.possible_move_grid.append([])

            #filling the content of each coordinate.
            for column in range(COLUMN_COUNT):

                #convert x and y to an 8 x 8 grid metric
                x = column * (CELL_WIDTH + CELL_MARGIN) + (CELL_WIDTH / 2 + CELL_MARGIN)
                y = row * (CELL_HEIGHT + CELL_MARGIN)  + (CELL_HEIGHT /2 + CELL_MARGIN)

                #Will alternate due to the checkered pattern of the game.
                if checker_checker == 0:
                    # create the board tile
                    sprite = arcade.SpriteSolidColor(CELL_WIDTH, CELL_HEIGHT, arcade.color.TAN)
                    # alternate the checker
                    checker_checker = 1

                    # Make the possible move sprite

                    # create a possible move sprite at each location.
                    possible_move = arcade.Sprite(move_img, SPRITE_SCALING_PIECE)
                    # Give it its center at this location.
                    possible_move.center_x = x
                    possible_move.center_y = y
                    # set its visibility to false by default. 
                    possible_move.visible = False
                    # append the possible move to the list and to this coordinate.
                    self.possible_move_list.append(possible_move)
                    self.possible_move_grid[row].append(possible_move)

                    #If we are within the starting bounds of player 1.
                    if row <= 2:
                        #Make the player 1 piece
                        p1_piece = Piece(p1_img, SPRITE_SCALING_PIECE)
                        #set its center
                        p1_piece.center_x = x
                        p1_piece.center_y = y
                        #append it to the list and the coordinate
                        self.p1_list.append(p1_piece)
                        self.p1_grid[row].append(p1_piece)
                        #set player2 empty at this location to maintain a proper grid.
                        self.p2_grid[row].append("empty")

                    #if we are within the starting bounds of player 2.
                    elif row >= 5:
                        #make the player 2 piece
                        p2_piece = Piece(p2_img, SPRITE_SCALING_PIECE)
                        #set its center
                        p2_piece.center_y = y
                        p2_piece.center_x = x
                        #append to list and coordinates
                        self.p2_list.append(p2_piece)
                        self.p2_grid[row].append(p2_piece)
                        #and set player 1 empty at this location to maintain the grid.
                        self.p1_grid[row].append("empty")
                    else:
                        #we are within the area between starting positions so set both to empty to maintain the grid.
                        self.p1_grid[row].append("empty")
                        self.p2_grid[row].append("empty")
                #If we are on the unused half of the checkered board.
                else:
                    # set the board sprite
                    sprite = arcade.SpriteSolidColor(CELL_WIDTH, CELL_HEIGHT, arcade.color.RED_BROWN)
                    #alternate the checker
                    checker_checker = 0
                    #and append empties to maintain the grid.
                    self.p1_grid[row].append("empty")
                    self.p2_grid[row].append("empty")
                    self.possible_move_grid[row].append("empty")
                #finally make the board sprite depending on color
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)
    
    #an attempt to make player movement functional
    # def update_piece_position(self, piece):
    #     self.p1_list


    #the main method that is called to render all sprites in the window
    def on_draw(self):

        #always reset
        self.clear()
        #draw the board
        self.grid_sprite_list.draw()
        #draw the player 1 pieces
        self.p1_list.draw()
        #draw the player 2 pieces
        self.p2_list.draw()
        #draw the possible moves (though by default they are not visible.)
        self.possible_move_list.draw()

    #whenever the player clicks, this will dictate what happens. parameters are the default as defined by arcade.
    def on_mouse_press(self, x, y, button, modifiers):

        #Convert the mouse click position to an 8x8 grid
        column = int(x // (CELL_WIDTH + CELL_MARGIN))
        row = int(y // (CELL_HEIGHT + CELL_MARGIN))

        #if we have already clicked a piece before this current click.
        if self.piece_index != None:
            #and we clicked a location where there is a possible move entity
            if self.possible_move_grid[row][column] != "empty":
                #and if that entity is visible
                if self.possible_move_grid[row][column].visible == True:
                    #find which square the player clicked on
                    move_to_index = find_nearest_piece(self.possible_move_list, column, row)
                    #if it's player 1 turn
                    cont = True
                    if self.is_p1_turn:
                        for r in range(COLUMN_COUNT):
                            for c in range(ROW_COUNT):
                                if cont == True:
                                    if self.p1_grid[r][c] == self.p1_list[self.piece_index]:
                                        if column  - c > 1:
                                            to_delete = self.p2_grid[row -1][column - 1]
                                            self.p2_list.remove(to_delete)
                                            self.p2_grid[row -1][column - 1] = "empty"
                                        elif c - column > 1:
                                            to_delete = self.p2_grid[row -1][c - 1]
                                            self.p2_list.remove(to_delete)
                                            self.p2_grid[row -1][c - 1] = "empty"
                                            

                                        self.p1_grid[row][column] = self.p1_grid[r][c]
                                        self.p1_grid[r][c] = "empty"
                                        # if row == 7:
                                        #     self.make_queen(self.piece_index)
                                        cont = False
                                    

                        #update the new centers for the piece.
                        self.p1_list.sprite_list[self.piece_index].center_x = self.possible_move_list.sprite_list[move_to_index].center_x
                        self.p1_list.sprite_list[self.piece_index].center_y = self.possible_move_list.sprite_list[move_to_index].center_y
                        
                        #switch player turn.
                        self.is_p1_turn = False
                    
                    else:
                        for r in range(COLUMN_COUNT):
                            for c in range(ROW_COUNT):
                                if cont == True:
                                    if self.p2_grid[r][c] == self.p2_list[self.piece_index]:
                                        if column  - c > 1:
                                            to_delete = self.p1_grid[row  + 1][column - 1]
                                            self.p1_list.remove(to_delete)
                                            self.p1_grid[row + 1][column - 1] = "empty"
                                        elif c - column > 1:
                                            to_delete = self.p1_grid[row + 1][c - 1]
                                            self.p1_list.remove(to_delete)
                                            self.p1_grid[row + 1][c - 1] = "empty"
                                        self.p2_grid[row][column] = self.p2_grid[r][c]
                                        self.p2_grid[r][c] = "empty"
                                        # if row == 0:
                                        #     self.make_queen(self.piece_index)
                                        cont = False

                        #update the new centers for the piece.
                        self.p2_list.sprite_list[self.piece_index].center_x = self.possible_move_list.sprite_list[move_to_index].center_x
                        self.p2_list.sprite_list[self.piece_index].center_y = self.possible_move_list.sprite_list[move_to_index].center_y
                        #Switch the player's turn
                        self.is_p1_turn = True
            #clear the clicked index
            self.piece_index = None
            #print statement for testing
            print("change location")
            #clear all showing possible moves
            for i in self.possible_move_list.sprite_list:
                i.visible = False
        #if we have not yet clicked on a piece
        else:

            
            #Theres a chance a player clicked without the bounds of the game, if so just ignore the click.
            if row >=  ROW_COUNT or column >= COLUMN_COUNT:
                return
            
            #if there is a player 1 piece at the clicked location and it is player 1's turn
            if self.p1_grid[row][column] != "empty" and self.is_p1_turn:
                #print for testing
                print(f"Clicked on a player 1 piece. at {row},{column}")
                #find the index of that piece and set it to the variable that tracks if a piece has been clicked
                self.piece_index = find_nearest_piece(self.p1_list.sprite_list, column, row)
                
                #reveal the usual two possible moves
                self.check_possible_moves(row, column)
            
            #if there is a player 2 piece at the clicked location and it's player 2's turn
            elif self.p2_grid[row][column] != "empty" and self.is_p1_turn == False:
                #print for testing
                print(f"Clicked on a player 2 piece. at {row},{column}")
                #find the index of that piece and set it to the variable that tracks if a piece has been clicked
                self.piece_index = find_nearest_piece(self.p2_list.sprite_list, column, row)
                
                #reveal the usual two possible moves
                self.check_possible_moves(row, column)
        
    #update the lists. this just keeps things flowing nice.
    def on_update(self, delta_time):
        self.p1_list.update()
        self.p2_list.update()
        self.possible_move_list.update()

    def check_possible_moves(self, row, column):
        
        if self.is_p1_turn == True:
            move_1_row = row + 1
            move_1_col = column - 1
            move_2_row = row + 1
            move_2_col = column + 1
            if move_1_row > 7:
                num_jumps_1 = 2
                num_jumps_2 = 2
            if move_1_col >=0:
                num_jumps_1 = 0
            else:
                num_jumps_1 = 2
            if move_2_col <=7:
                num_jumps_2 = 0
            else:
                num_jumps_2 = 2
            
            for n in range(2):
                for i in self.p1_list:
                    if move_1_row < 8 and move_1_col >=0 and move_2_col <= 7:
                        if i == self.p1_grid[move_1_row][move_1_col]:
                            num_jumps_1 = 2
                    
                        elif i == self.p1_grid[move_2_row][move_2_col]:
                            num_jumps_2 = 2
                for i in self.p2_list:
                    if move_1_row < 8: 
                        if move_1_col >=0:
                            if i == self.p2_grid[move_1_row][move_1_col]:
                                move_1_col -= 1
                                move_1_row += 1
                                num_jumps_1 += 1
                        if move_2_col <= 7:
                            if i == self.p2_grid[move_2_row][move_2_col]:
                                move_2_col += 1
                                move_2_row += 1
                                num_jumps_2 += 1
            if num_jumps_1 < 2 and move_1_col >= 0:
                self.possible_move_grid[move_1_row][move_1_col].visible = True
            if num_jumps_2 < 2 and move_2_col <= 7:
                self.possible_move_grid[move_2_row][move_2_col].visible = True

        else:
            move_1_row = row - 1
            move_1_col = column - 1
            move_2_row = row - 1
            move_2_col = column + 1
            if move_1_row < 0:
                num_jumps_1 = 2
                num_jumps_2 = 2
            if move_1_col >=0:
                num_jumps_1 = 0
            else:
                num_jumps_1 = 2
            if move_2_col <=7:
                num_jumps_2 = 0
            else:
                num_jumps_2 = 2
            
            for n in range(2):
                
                for i in self.p2_list:
                    if move_1_row >= 0 and move_1_col >=0 and move_2_col <= 7:    
                        if i == self.p2_grid[move_1_row][move_1_col]:
                            num_jumps_1 = 2
                    
                        if i == self.p2_grid[move_2_row][move_2_col]:
                            num_jumps_2 = 2
                for i in reversed(self.p1_list):
                    if move_1_row >= 0:
                        if move_1_col >=0:
                            if i == self.p1_grid[move_1_row][move_1_col]:
                                move_1_col -= 1
                                move_1_row -= 1
                                num_jumps_1 += 1
                        if move_2_col <= 7:
                            if i == self.p1_grid[move_2_row][move_2_col]:
                                move_2_col += 1
                                move_2_row -= 1
                                num_jumps_2 += 1
            if num_jumps_1 <2 and move_1_col >= 0:
                self.possible_move_grid[move_1_row][move_1_col].visible = True
            if num_jumps_2 < 2 and move_2_col <=7:
                self.possible_move_grid[move_2_row][move_2_col].visible = True



    # def make_queen(self, index):
        
    #     if self.is_p1_turn:
    #         img = PIL
    #         text = arcade.Texture("queen", RED_QUEEN)
    #         self.p1_list.sprite_list[index].append_texture(text)
    #         self.p1_list.sprite_list[index].is_queen = True
    #     else:
    #         text = arcade.Texture("queen", TAN_QUEEN)
    #         self.p2_list[index].append_texture(text)
    #         self.p2_list[index].is_queen = True

#  function to find the index of the piece nearest to where the click occurred. 
def find_nearest_piece(sprite_list, column, row):
    #excessively large number
    closest_index_x = 10000
    closest_index_y = 10000
    #for each index in the length of the list
    for i in range(len(sprite_list)):
        #check to see if we are still within the bounds so we can properly check the next one.
        if i < len(sprite_list):
            #if x or y is closer to where it was clicked
            if (abs((sprite_list[i].center_x // (CELL_WIDTH + CELL_MARGIN)) - column) < closest_index_x) or (abs((sprite_list[i].center_y // (CELL_HEIGHT + CELL_MARGIN)) - row) < closest_index_y) :
                # Set the current closest to that index
                closest_index_x = abs((sprite_list[i].center_x // (CELL_WIDTH + CELL_MARGIN)) - column)
                closest_index_y = abs((sprite_list[i].center_y // (CELL_HEIGHT + CELL_MARGIN))- row)
                closest_index = i
    # return the index of the sprite that was closest to the clicked location.
    return closest_index




def main():
    Checkers(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

main()
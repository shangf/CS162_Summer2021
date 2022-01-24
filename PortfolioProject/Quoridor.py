# Name: Frank Shang
# Date: 08/11/2021
# Portfolio Project
# Description: This program contains a class called QuoridorGame that simulates a Quoridor game.

class QuoridorGame:
    '''class that creates QuoridorGame objects'''

    def __init__(self):
        '''
        init method that defines all data attributes and sets up the board
        '''
        self._board = {}
        self.setup_board()
        self._p1_fences = 10
        self._p2_fences = 10
        self._current_turn = 1
        self._move_direction = None
        self._winner = None

    def setup_board(self):
        '''
        method that sets up the board and stores it into a dictionary that uses a tuple as its key and a list as its value
        '''
        for row in range(9):
            for col in range(9):
                self._board[(col, row)] = []
        self.add_player(1, (4,0))
        self.add_player(2, (4,8))

    def get_stored_board(self):
        '''
        method that prints out the values in the stored board
        mainly used for debugging purposes
        '''
        for key in self._board:
            print(key, end = " : ")
            print(self._board[key])

    def add_player(self, player, key):
        '''
        method that adds a player to a list within the board dictionary
        takes in a number to represent player
        takes in a tuple of coordinates to represent the key for the dictionary
        '''
        self._board[key].append(player)

    def remove_player(self, player, key):
        '''
        method that removes a player to a list within the board dictionary
        takes in a number to present player
        takes in a tuple to represent the key for the dictionary
        '''
        self._board[key].remove(player)

    def add_fence(self, fence, key):
        '''
        method that adds a fence to a list within the board dictionary
        takes in a letter, either 'v' or 'h' to represent
        takes in a tuple to represent the key for the dictionary
        '''
        self._board[key].append(fence)

    def get_player_position(self, player):
        '''
        method that returns a player's position
        takes in a number that represents a player
        returns a tuple that represents the coordinates of the player's position
        '''
        for key in self._board:
            if len(self._board[key]) >= 1 and player in self._board[key]:
                return key

    def get_directional_move(self):
        '''
        method that returns the move_direction data attribute
        '''
        return self._move_direction

    def set_directional_move(self, direction):
        '''
        method that sets the move_direction data attribute to a direction
        takes in a direction parameter that represents which way the user wants to move
        '''
        self._move_direction = direction

    def move_pawn(self, player, coordinates):
       """
       method that moves the player's pawn to a new location
       takes in a number that represents a player
       takes in a tuple that represents the coordinates that the player will move to
       returns False if the rule is forbidden
       returns True if the move is successful or if the move makes the player win
       """
       # if there is a winner, if it is not the player's turn, or if the opposite player is in the ending coordinats:
       # return False
       if self.get_winner() is not None or self.get_turn() != player or not self.check_player(player, coordinates):
           return False
       # if the coordinates are out of bounds, return False
       if not self.check_out_of_bounds(coordinates):
           return False
       #set the move_direction attribute
       self.set_directional_move(self.check_directional_move(self.get_player_position(player), coordinates))
       #if direction is adjacent neighboring squares, test to see whether there is a fence in between the move
       if self.get_directional_move() == 'left' or self.get_directional_move() == 'right' or \
               self.get_directional_move() == 'up' or self.get_directional_move() == 'down':
           if self.check_fences_adjacent(self.get_directional_move(), self.get_player_position(player), coordinates):
               return self.update_move(player, coordinates)
       #if direction is a double jump, test whether it is possible: 1. pawns must be face to face 2. no fences in between or behind
       elif self.get_directional_move() == 'double up' or self.get_directional_move() == 'double down':
           if self.check_face_to_face(player, self.get_player_position(player)) and \
            self.check_fences_facing(self.get_directional_move(), player, coordinates):
               return self.update_move(player, coordinates)
       #if direction is a diagonal, test to whether it is possible: 1. pawns must be face to face
       # 2. fence must be behind the opponent 3. no vertical fences that block the diagonal movement
       else:
           if self.check_face_to_face(player, self.get_player_position(player)) and \
              self.check_fences_facing(self.get_directional_move(), player, coordinates) and \
                   self.check_fence_behind_opponent(player, self.get_player_position(self.get_opposite_player(player))):
               if self.diagonal_neighbors(player, coordinates):
                   return self.update_move(player, coordinates)
       return False

    def diagonal_neighbors(self, player, end_pos):
        '''
        method that checks to see whether the diagonal move is valid (the move can only be to the
        left or right of the opposing pawn
        takes in a number to represent the player
        takes in a tuple to represent the player's end position
        returns True if the diagonal move is valid
        returns False if the diagonal move is not valid
        '''
        if player == 1:
            if self.get_player_position(2)[0] + 1 == end_pos[0] and self.get_player_position(2)[1] == end_pos[1]:
                return True
            if self.get_player_position(2)[0] - 1 == end_pos[0] and self.get_player_position(2)[1] == end_pos[1]:
                return True
        if player == 2:
            if self.get_player_position(1)[0] + 1 == end_pos[0] and self.get_player_position(1)[1] == end_pos[1]:
                return True
            if self.get_player_position(1)[0] - 1 == end_pos[0] and self.get_player_position(1)[1] == end_pos[1]:
                return True
        return False

    def update_move(self, player, coordinates):
        '''
        method that updates the pawn's move, called from the move_pawn method
        takes in a number to represent a player
        takes in a tuple to represent ccoordinates
        calls the remove_player, add_player, and set_winner methods to update the board and the winner data attribute
        returns True to indicate the move is valid
        '''
        self.remove_player(player, self.get_player_position(player))
        self.add_player(player, coordinates)
        if player == 1:
            self.set_turn(2)
            self.set_winner(player)
        if player == 2:
            self.set_turn(1)
            self.set_winner(player)
        return True

    def set_winner(self, player):
        '''
        method that checks whether a player has won
        takes in a number to represent player
        if won, then sets the the winner data attribute to player
        '''
        if player == 1:
            for col in range(9):
                if player in self._board[(col, 8)]:
                    self._winner = player
        if player == 2:
            for col in range(9):
                if player in self._board[(col, 0)]:
                    self._winner = player

    def check_out_of_bounds(self, coordinates):
        '''
        method that checks whether coordinates are out of bounds
        takes in a tuple that represents coordinates
        returns False if coordinates are out of bounds
        returns True if coordinates are in bounds
        '''
        if coordinates[0] < 0 or coordinates[0] > 8:
            return False
        if coordinates[1] < 0 or coordinates[1] > 8:
            return False
        return True

    def check_fence_behind_opponent(self, player, opp_pos):
        if self.get_directional_move() == 'diagonal down left' or self.get_directional_move() == 'diagonal down right':
            if 'h' in self._board[(opp_pos[0], opp_pos[1] + 1)]:
                return True
        if self.get_directional_move() == 'diagonal up left' or self.get_directional_move() == 'diagonal up right':
            if 'h' in self._board[(opp_pos[0], opp_pos[1] - 1)]:
                return True
        return False

    def check_player(self, player, end_pos):
        '''
        method that checks whether the opposing player is in the destination coordinate
        takes in a number to represent a player
        takes in a tuple to represent the ending position (end_pos)
        returns False if opponent player is in end_pos
        returns True if opponent player is not in end_pos
        '''
        if player == 1:
            if 2 in self._board[end_pos]:
                return False
        if player == 2:
            if 1 in self._board[end_pos]:
                return False
        return True

    def check_directional_move(self, current_pos, end_pos):
        '''
        method that checks the direction of the move by using the coordinates of the current position and ending position
        takes in a tuple to represent the current position of the pawn (current_pos)
        takes in a tuple to represent the end position of the pawn (end_pos)
        returns string that represents the direction of the move if valid move
        returns None if not a valid move
        '''
        if (current_pos[0] + 1) == end_pos[0] and (current_pos[1] == end_pos[1]):
            return 'right'
        if (current_pos[0] - 1) == end_pos[0] and (current_pos[1] == end_pos[1]):
            return 'left'
        if (current_pos[1] - 1) == end_pos[1] and (current_pos[0] == end_pos[0]):
            return 'up'
        if (current_pos[1] + 1) == end_pos[1] and (current_pos[0] == end_pos[0]):
            return 'down'
        if (current_pos[1] + 2 == end_pos[1]) and (current_pos[0] == end_pos[0]):
            return 'double down'
        if (current_pos[1] - 2 == end_pos[1]) and (current_pos[0] == end_pos[0]):
            return 'double up'
        if (current_pos[0] + 1 == end_pos[0]) and (current_pos[1] - 1 == end_pos[1]):
            return 'diagonal up right'
        if (current_pos[0] - 1 == end_pos[0]) and (current_pos[1] - 1 == end_pos[1]):
            return 'diagonal up left'
        if (current_pos[0] - 1 == end_pos[0]) and (current_pos[1] + 1 == end_pos[1]):
            return 'diagonal down left'
        if (current_pos[0] + 1 == end_pos[0]) and (current_pos[1] + 1 == end_pos[1]):
            return 'diagonal down right'
        return None

    def check_fences_adjacent(self, direction, current_pos, end_pos):
        '''
        method that checks fences for adjacent moves
        takes in a string that represents the direction of the move (direction)
        takes in a tuple to represent the current position of the pawn (current_pos)
        takes in a tuple to represent the end position of the pawn (end_pos)
        returns False if the there is a fence in the way, meaning move is invalid
        returns True if move is valid
        '''
        # move up, horizontal fence is in the current_pos
        if direction == 'up':
            if 'h' in self._board[current_pos]:
                return False
        # move down, horizontal fence is in the end_pos
        if direction == 'down':
            if 'h' in self._board[end_pos]:
                return False
        # move left, vertical fence is in the current_pos
        if direction == 'left':
            if 'v' in self._board[current_pos]:
                return False
        # move right, vertical fence is in the end_pos
        if direction == 'right':
            if 'v' in self._board[end_pos]:
                return False
        return True

    def get_opposite_player(self, player):
        '''
        method that returns the opposing player
        takes in a number to represent player
        returns a number that represents the opposing player
        '''
        if player == 1:
            return 2
        if player == 2:
            return 1

    def check_fences_facing(self, direction, player, end_pos):
        '''
        method that checks whether there are fences when pawns are faced to face
        double jump and diagonal move only
        takes in a string to represent direction
        takes in a number to represent player
        take in a tuple to represent ending position
        returns True if move is valid
        returns False if move is invalid
        '''
        if direction == 'double down' and 'h' not in self._board[end_pos]:
            return True
        if direction == 'double up':
            if 'h' not in self._board[self.get_player_position(self.get_opposite_player(player))]:
                return True
        if direction == 'diagonal up right' and 'v' not in self._board[end_pos]:
            return True
        if direction == 'diagonal up left':
            if 'v' not in self._board[self.get_player_position(self.get_opposite_player(player))]:
                return True
        if direction == 'diagonal down right' and 'v' not in self._board[end_pos]:
            return True
        if direction == 'diagonal down left':
            if 'v' not in self._board[self.get_player_position(self.get_opposite_player(player))]:
                return True
        return False

    def check_face_to_face(self, player, player_pos):
        '''
        method that checks whether pawns are face to face, without fences in between the two
        takes in a number to represent the player
        takes in a tuple to represent player's position (player_pos)
        returns True if pawns are face to face, without fences in between
        returns False if there is a fence in between pawns
        '''
        if player == 1 and self.get_player_position(2)[0] == player_pos[0]:
            if self.get_player_position(2)[1] - 1 == player_pos[1] and 'h' not in self._board[self.get_player_position(2)]:
                return True
            if self.get_player_position(2)[1] + 1 == player_pos[1] and 'h' not in self._board[player_pos]:
                return True
        if player == 2 and self.get_player_position(1)[0] == player_pos[0]:
            if self.get_player_position(1)[1] - 1 == player_pos[1] and 'h' not in self._board[self.get_player_position(1)]:
                return True
            if self.get_player_position(1)[1] + 1 == player_pos[1] and 'h' not in self._board[player_pos]:
                return True
        return False

    def place_fence(self, player, fence_direction, coordinates):
        """
        method that places a fence
        takes in a number to represent player
        takes in a letter to represent fence_direction
        takes in a tuple to represent coordinates (where the fence will be placed)
        returns True if fence can be be placed
        returns False if an invalid fence placement (no fences left, fences out of boundaries, overlapping fences)
        returns False if game has been won
        """
        if self.get_turn() != player:
            return False
        if self.get_player_fences(player) <= 0:
            return False
        if not self.check_out_of_bounds(coordinates):
            return False
        if self.get_winner() is not None:
            return False
        if self.check_overlap_fences(fence_direction, coordinates):
            return False
        return self.update_fences(player, fence_direction, coordinates)

    def update_fences(self, player, fence_direction, coordinates):
        '''
        method that updates the current player's fences
        takes in a number to represent player
        takes in a letter to represent fence_direction
        takes in a tuple to represent coordinates
        '''
        self._board[coordinates].append(fence_direction)
        self.decrement_fence(player)
        self.set_turn(self.get_opposite_player(player))
        return True

    def decrement_fence(self, player):
        '''
        method that decrements the data attributes p1_fences or p2_fences
        takes in a number that represents player
        '''
        if player == 1:
            self._p1_fences -= 1
        if player == 2:
            self._p2_fences -= 1

    def check_overlap_fences(self, fence_direction, coordinates):
        '''
        method that checks whether fences are overlapping
        takes in a letter to represent fence_direction
        takes in a tuple to represent coordinates
        returns True if there is a matching fence already on the board
        returns False if there is no overlapping fence
        '''
        if fence_direction in self._board[coordinates]:
            return True
        return False

    def is_winner(self, player):
        """
        method that determines whether there is a winner
        takes in a number as a player
        returns True if player is the winner attribute
        returns False if there is no winner
        """
        if self.get_winner() is player:
            return True
        return False

    def print_first_vertical_row(self, col, row):
        '''
        method that prints the first vertical row of the board
        takes in a number to represent the column (col)
        takes in a number to represent the row
        '''
        if len(self._board[(col, row)]) >= 1:
            if 1 in self._board[(col, row)]:
                print("P1", end="")
            elif 2 in self._board[(col, row)]:
                print("P2", end="")
            else:
                print("  ", end="")
        else:
            print("  ", end="")

    def print_remaining_vertical_rows(self, col, row):
        '''
        method that prints the remaining vertical rows of the board
        takes in a number to represent the column (col)
        takes in a number to represent the row
        '''
        if len(self._board[(col, row)]) >= 1:
            if 1 in self._board[(col, row)]:
                if 'v' in self._board[(col, row)]:
                    print("|P1", end="")
                else:
                    print(" P1", end="")
            elif 2 in self._board[(col, row)]:
                if 'v' in self._board[(col, row)]:
                    print("|P2", end="")
                else:
                    print(" P2", end="")
            elif 'v' in self._board[(col, row)]:
                print("|  ", end="")
            else:
                print("   ", end="")
        else:
            print("   ", end="")

    def print_vertical_row(self, row):
        '''
        method that prints the vertical rows of the board
        if its the first row, call print_first_vertical_row method
        if its not the first row, then call print_remaining_vertical_rows method
        takes in a number that represents the row that is being printed
        '''
        print("|", end = "")
        for col in range(9):
            if col == 0:
                self.print_first_vertical_row(col, row)
            else:
                self.print_remaining_vertical_rows(col, row)
        print("|")

    def print_horizontal_row(self, row):
        '''
        method that prints the horizontal rows for the board
        takes in a number that represents the current row that is being printed
        '''
        print("+", end="")
        for col in range(9):
            if 'h' in self._board[(col, row)]:
                print("==", end="+")
            else:
                print("  ", end="+")
        print()

    def print_board(self):
        '''
        method that prints the board to visually represent the current game state
        '''
        print("+==+==+==+==+==+==+==+==+==+")
        for num in range(8):
            self.print_vertical_row(num)
            self.print_horizontal_row(num + 1)
        self.print_vertical_row(8)
        print("+==+==+==+==+==+==+==+==+==+")

    def get_player_fences(self, player):
        '''
        method that returns the player's fences
        takes in a number that represents a player
        returns fences depending on player
        '''
        if player <= 0 or player > 2:
            return False
        if player == 1:
            return self._p1_fences
        else:
            return self._p2_fences

    def get_turn(self):
        '''
        method that returns the current player's turn
        '''
        return self._current_turn

    def get_winner(self):
        '''
        method that returns the data attribute winner
        '''
        return self._winner

    def set_turn(self, player):
        '''
        method that sets the data attribute current_turn
        takes in a number to represent player
        '''
        self._current_turn = player

#q = QuoridorGame()
#print(q.move_pawn(1, (4,6)))
#print(q.place_fence(1, 'v', (3,3)))
#print(q.move_pawn(2, (3,0)))
#print(q.get_player_fences(1))
#print(q.get_player_fences(2))
#print(q.place_fence(1, 'h', (3,8)))
#print(q.place_fence(2, 'v', (3,7)))
#print(q.place_fence(1, 'h', (4,8)))
#print(q.place_fence(2, 'v', (3,6)))
#print(q.move_pawn(1, (3,6)))
#print(q.is_winner(2))
#print(q.move_pawn(2, (5,8)))
#print(q.place_fence(1, 'h', (5,8)))
#q.print_board()

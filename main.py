class ShipGame:
    """ ShipGame allows two people to play the game Battleship. There are two
    10x10 grids (one for each player) in which players can place their ships on.
    Players take turns firing torpedoes onto the other player's grid in an attempt
    to sink all of that player's ships. If all of a ship's tiles/squares have
    been hit by the other player's torpedo, then that player's ship has been sunk.
    Contains init method, place_ship, get_current_state, fire_torpedo, and
    get_num_ships_remaining.
    Player's board is a list of ships. Player ships are stored as list within the board.
    Each item on the ship list contains a coordinate that the ship occupies. """

    def __init__(self):
        """ Takes no parameters. Sets all data members to initial values. """
        self._first_board = []
        self._second_board = []
        self._current_state = 'UNFINISHED'
        self._player_turn = 'first'

    def get_current_turn(self):
        """ Returns current player's turn (string): either 'first' or 'second'. """
        return self._player_turn

    def get_current_state(self):
        """ Returns the current state of the game (string).
        Possible game states:
            - 'UNFINISHED'
            - 'FIRST_WON'
            - 'SECOND_WON'      """
        return self._current_state

    def set_current_state(self, state):
        """ Sets the current state of the game (as string). Same possible game states
        as outlined in get_current_state method. """
        self._current_state = state

    def get_num_ships_remaining(self, player):
        """ Takes as a parameter: 'first' or 'second'
        Returns how many ships are remaining on the specified player's board. """
        if player == 'first':
            return len(self._first_board)
        elif player == 'second':
            return len(self._second_board)

    def get_player_ships(self, player):
        """ Returns all coordinates of ships that have not yet been hit. Takes as a parameter
        a player ad returns that player's list. """
        if player == 'first':
            return self._first_board
        if player == 'second':
            return self._second_board

    def print_player_ships(self):
        """ Prints all player ships. """
        print("first: ", self._first_board)
        print("second: ", self._second_board)

    def validate_range(self, coordinates):
        """ Validates move by confirming all coordinates are within range.
        Returns True if move is valid. Else, returns False.
            for each char in coordinate parameter, first char must be between A-J
                    use .upper or .lower
            second char must be between 1-10 """
        valid_abc = 'ABCDEFGHIJ'
        valid_num = ''
        for num in range(1, 11):
            valid_num += str(num) + ' '

        # check if first char (letter) is within range
        check = coordinates.upper()
        if check[0] not in valid_abc:
            return False
        else:
            # check if second char (number) is within range
            if coordinates[1:] not in valid_num:
                return False
            elif coordinates[1:] == '0':
                return False
            else:
                return True

    def validate_place(self, length, coordinates, orientation):
        """ Takes as a parameter a ship's length, coordinates, and orientation.
        Validates whether move can be made. If move is valid, returns True. Else,
        returns False.
            Calls validate_range to check if coordinates are within range.
            Then checks whether ship can be placed on board without going out of range.
        If orientation is not 'R' or 'C', returns False. """
        # ship length must be at least 2, anything less than is invalid
        if length < 2:
            return False

        # if coordinates are out of range, return False
        if self.validate_range(coordinates) is False:
            return False

        # if starting point of coordinate + length of ship surpasses boundary
        if orientation == 'R':
            num = coordinates[1:]
            if int(num) + length > 10:
                return False
            else:
                return True
        elif orientation == 'C':
            coord = ord(coordinates[0].upper())
            if coord + length > 75:
                return False
            else:
                return True
        else:
            return False

    def place_ship(self, player, ship_length, coordinates, orientation):
        """ Takes as parameters:
            - player: either 'first' or 'second'
            - ship_length: length of the ship (length must be >= 2)
            - coordinates: square closest to A1 which the ship will occupy
            - orientation: either 'R' (same row) or 'C' (same column)
        If any of the parameters entered by a player would cause an illegal move,
        the method will return False. Otherwise, the ship will be added to that
        player's grid and the method will return True. Turn order does not matter
        during placement phase of the game.
        Possible illegal moves that would result in method returning False:
            - ship placement extends beyond edge of player's grid
            - ship overlaps another ship already placed by the player
            - ships smaller than length 2       """

        # check player move is valid
        if self.validate_place(ship_length, coordinates, orientation) is False:
            return False

        # tile already occupied
        if player == 'first':
            for item in self._first_board:
                if coordinates in item:
                    return False
        if player == 'second':
            for item in self._second_board:
                if coordinates in item:
                    return False

        # at this point, move is valid
        char = ord(coordinates[0].upper())
        num = int(coordinates[1:])
        num_add = []

        if player == 'first':
            # row: increment numerical value by amount of ship_length
            if orientation.upper() == 'R':
                for item in range(ship_length):
                    ship_loc = coordinates[0] + str(num)
                    num_add.append(ship_loc)
                    num += 1
            # column: increment alphabetical letter by amount of ship_length
            if orientation.upper() == 'C':
                for item in range(ship_length):
                    ship_loc = str(chr(char) + coordinates[1:])
                    num_add.append(ship_loc)
                    char += 1
            self._first_board.append(num_add)           # add list of occupied tiles
            # self._first_ship_count += 1                 # increment ship counter
            return True
        elif player == 'second':
            if orientation.upper() == 'R':
                for item in range(ship_length):
                    ship_loc = coordinates[0] + str(num)
                    num_add.append(ship_loc)
                    num += 1
            if orientation.upper() == 'C':
                for item in range(ship_length):
                    ship_loc = str(chr(char) + coordinates[1:])
                    num_add.append(ship_loc)
                    char += 1
            self._second_board.append(num_add)          # add list of occupied tiles
            # self._second_ship_count += 1                # increment p2 ship counter
            return True
        else:
            return False

    def fire_torpedo(self, player, coordinates):
        """ Takes as parameters:
            - player: 'first' or 'second'
            - coordinates: target square of torpedo being fired
        Method should return False if any of the parameters entered by a player
        would cause an illegal move. Otherwise, returns True and:
            - records the move
            - updates turn to next player
            - updates current state (check if turn cause sink to final ship)
        Possible illegal moves that would result in the method returning False:
            - not that player's turn
            - game state is not 'UNFINISHED' , aka game already won
        Note: if player chooses to fire on a square that they have already
        fired on, turn is wasted and game continues (turn increments to next
        player)
        Once fire_torpedo has started, place_ship will not be called. """
        # check if move is valid
        if player != self._player_turn:
            return False
        if self._current_state != 'UNFINISHED':
            return False
        if self.validate_range(coordinates) is False:
            return False

        # record the move
        if player == 'first':
            for ship in self._second_board:
                if coordinates in ship:
                    ship.remove(coordinates)                # remove ship tile when hit
                if len(ship) == 0:                  # if ship has no coordinate tiles, then ship sunk
                    self._second_board.remove(ship)
            if len(self._second_board) == 0:                # check if game has been won
                self._current_state = 'FIRST_WON'           # if no ships/empty list, then player won
            self._player_turn = 'second'                # update turn
            return True
        if player == 'second':
            for ship in self._first_board:
                if coordinates in ship:
                    ship.remove(coordinates)                # remove ship tile when hit
                if len(ship) == 0:                  # if ship has no coordinate tiles, then ship sunk
                    self._first_board.remove(ship)
            if len(self._first_board) == 0:               # check if game has been won
                self._current_state = 'SECOND_WON'          # if no ships/empty list, then player won
            self._player_turn = 'first'                 # update turn
            return True
        
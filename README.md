# Battleship Game

## How It Works

Program allows two players to play [Battleship](https://en.wikipedia.org/wiki/Battleship_(game)) via a class. To start, each player places ships on their respective 10x10 virtual grid. Players take turns firing one torpedo at a square on the opposite player's grid. A ship sinks when all its grid tiles have been hit by a torpedo. A player wins once they sink all of their enemy's ships.

## Usage

### Place Ships
Method: ```place_ship(a, b, c, d)```

Turn order is not enforced during placement phase. Placement phase continues until the first torpedo is fired. 

Arguments: 
* Player placing ship: 'first' OR 'second'
* Length of ship (integer)
* Coordinates of the square to start at
* Ship's orientation: 'R' for row OR 'C' for column

Rules:
* Entire ship must fit on player's grid
* Ships must not overlap already placed ships on grid
* Ship length must be at least 2

If any of the above rules are not met when calling place_ship(), the ship will not be placed.

### Fire Torpedo
Method: ```fire_torpedo(a, b)```

Arguments:
* Player firing torpedo: 'first' OR 'second'
* Coordinates of the target square

Rules:
* Must be player's turn
* Game must be unfinished 

If any of the above rules are not met when calling fire_torpedo, the target square will not be hit.

### Get the current state of the game
Method: ```get_current_state()```

State is first initialized to 'UNFINISHED' and updated to 'FIRST_WON' or 'SECOND_WON' once a player has won.

Takes no arguments. Returns the current state of the game. 

### Get number of ships still on the grid
Method: ```get_num_ships_remaining(x)```

Arguments:
* Player's grid to check: 'first' or 'second'

Returns an integer representing the number of ships left on that player's grid.

### View all player ships

Prints the coordinates of all ships currently on the grid for both the first and second player. Each player's ship count prints on a separate line.

Takes no arguments. 

### View current player's turn

Method: ```get_current_turn()```

Takes no arguments. Returns current player's turn, either: 'first' or 'second'. 

## Example Usage

### Place Ships

```python
game = ShipGame()
game.place_ship('first', 5, 'B2', 'C')
```
Updated grid: 
```python
  1 2 3 4 5 6 7 8 9 10
A
B   x
C   x
D   x
E   x
F   x
G                 
H                 
I                 
J                 
```
```python
game = ShipGame()
game.place_ship('second', 3, 'E3', 'R')
```
Updated grid:
```python
  1 2 3 4 5 6 7 8 9 10
A
B
C
D
E     x x x
F
G                 
H                 
I                 
J       
```

### Fire Torpedo

```python
game.fire_torpedo('first', 'H3')
```

### Get the current state of the game

```python
print(game.get_current_state())
```

### Get number of ships still on the grid

```python
print(game.get_num_ships_remaining('first'))
```

### View all player ships

```python
game.print_player_ships()
```

### View current player's turn
```python
print(game.get_current_turn())
```

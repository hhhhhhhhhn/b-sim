# This file gives easy to read aliases to integer values.

# For cities, which are in [name, size] format.
NAME = 0
SIZE = 1

# Moves
MOVE_NORTH = 1
MOVE_SOUTH = -1
MOVE_EAST = 2 #   Some moves take negative values so the oposite move can be
MOVE_WEST = -2  # accesed with the negation operator (-MOVE_WEST == MOVE_EAST).

ADVANCE = 3 # Repeat last move.
RETREAT = -3  # Oposite of last move, can be used to escape battles.

# Deltas of each move
DELTAS = {
	MOVE_NORTH: (0, 1),
	MOVE_SOUTH: (0, -1),
	MOVE_EAST: (1, 0),
	MOVE_WEST: (-1, 0)
}
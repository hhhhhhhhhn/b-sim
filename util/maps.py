from typing import Tuple, List, Dict
import util.generate as generate
import random
from .constants import *

def create_city() -> list:
	"""Creates city in [name, size] format."""
	return [
		generate.city(), # Name
		random.choice([1, 1, 1, 2, 2, 3]) # Size
	]

def create(size: int) -> List[List[list]]:
	"""Creates a map, a 2d array of [name, size] cities."""
	the_map = []
	for _ in range(size):
		the_map.append([create_city() for _ in range(size)])
	the_map[0][0][SIZE] = 3 # Both capitals (corners) have a size of 3.
	the_map[size - 1][size - 1][SIZE] = 3
	return the_map

def map_coordenates(the_map: list) -> Dict[str, Tuple[int, int]]:
	"""Returns a dictionary in {"name": (x, y)} format."""
	names = {}
	for x in range(len(the_map)):
		for y in range(len(the_map)):
			names[the_map[x][y][NAME]] = (x, y)
	return names
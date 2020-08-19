import random
import util.generate as generate
import util.maps as maps
from util.constants import *
from typing import Tuple

class Game:
	def __init__(self, map_size: int, alies: int, enemies:int):
		self.size = map_size
		self.map = maps.create(map_size)
		self.coordenates = maps.map_coordenates(self.map)
		self.city_names = sorted(self.coordenates.keys())
		self.units = []
		self.players = [
			Player(team = 0, game = self),
			*[Player(team = 0, game = self) for _ in range(alies)],
			*[Player(team = 1, game = self) for _ in range(enemies)]
		]
		for i in range(len(self.players)):
			self.players[i].id = i
	
	def fighting(self, unit_1: Unit) -> bool:
		"""Finds if there are enemy units in a place."""
		for unit_2 in self.units:
			if unit_2.team != unit_1.team: # For all enemies find a
				if unit_1.x == unit_2.x and unit_1.y == unit_2.y: # Collision.
					return True
		return False

	def move(self):
		for unit in self.units:
			unit.moved = False
		for player in self.players:
			moves = player.get_moves()
			for unit_id, move in moves:
				unit = self.units[unit_id]
				if unit.player == player and not unit.moved:
					unit.move(move)
					unit.moved = True
			for unit in self.units:
				if unit.moved:
					unit.moved = False
				else:
					unit.move(NULL)
					
			

class Player:
	def __init__(self, team: int, game: Game):
		self.game = game
		self.team = team
		self.units = []
		self.id = None
		self.upgrade_multiplier = 1 # Multiplies with fire rate.
		self.event_multiplier  # Multiplies with fire rate.
	
	def get_moves(self) -> Tuple[int, str]:
		pass

class Unit:
	def __init__(self, size: int, rate: float, x: int, y: int, player: Player):
		self.alive = True
		self.size = size
		self.fire_rate = rate
		self.strategy = 1 # Multiplies the fire rate, up to 2.
		self.x = x
		self.y = y
		self.player = player
		self.team = player.team
		self.moved = False # If the unit has been moved this turn.
		self.last_move = MOVE_NORTH if self.team == 0 else MOVE_SOUTH
	
	def move(self, move):
		fighting = self.player.game.fighting(self)
		map_size = self.player.game.size

		if move == ADVANCE and not fighting:
			move = self.last_move
		
		elif move == RETREAT: # Can be used if fighting
			move = -self.last_move

		if move >= MOVE_WEST and move <= MOVE_EAST and not fighting:
			# This includes all the direct movement options.
			dx, dy = DELTAS[move]
			new_x, new_y = x + dx, x + dy
			if(new_x >= 0 and new_x < map_size):
				self.x = new_x
			if(new_y >= 0 and new_y < map_size):
				self.y = new_y
			self.strategy = 1

			if not fighting: # This prevents the moves from RETREAT from being
				# saved, which would make a unit alternate between directions.
				self.last_move = move

		elif not fighting and self.strategy < 2:
			self.strategy += 0.1


	def idle(self):
		pass
import random
import util.generate as generate
import util.maps as maps

class Game:
	def __init__(self, map_size: int, alies: int, enemies:int):
		self.map = maps.create(map_size)
		self.coordenates = maps.map_coordenates(self.map)
		self.city_names = sorted(self.coordenates.keys())
		self.players = [
			Player(team=0),
			*[Player(team=0) for _ in range(alies)],
			*[Player(team=1) for _ in range(enemies)]
		]
		for i in range(len(self.players)):
			self.players[i].id = i

class Player:
	def __init__(self, team: int):
		self.team = team
		self.units = []
		self.id = None

class Unit:
	def __init__(self, size: int, rate: float, x: int, y: int, player: Player):
		self.size = size
		self.fire_rate = rate
		self.strategy = 1 # Multiplies the fire rate, up to 2.
		self.x = x
		self.y = y
		self.player = player
		self.team = player.team
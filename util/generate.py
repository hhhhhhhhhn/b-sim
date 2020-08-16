import random
from .cities import cities
from .names import names

memory = 2 # The higher the value, the more deterministic words are.

cities = cities.split("\n")[2:]
cities = ["S" + e + "E" for e in cities]

names = names.split("\n")
names = ["S" + e + "E" for e in names]

def pos(number: int) -> int:
	"""Used for indexing."""
	return 0 if number < 0 else number

# Compute probability.

city_next_chars = {}
for city in cities:
	for i in range(len(city) - 1):
		substr = city[pos(i - memory): i + 1]
		if(substr not in city_next_chars):
			city_next_chars[substr] = []
		city_next_chars[substr].append(city[i + 1])


name_next_chars = {}
for name in names:
	for i in range(len(name) - 1):
		substr = name[pos(i - memory): i + 1]
		if(substr not in name_next_chars):
			name_next_chars[substr] = []
		name_next_chars[substr].append(name[i + 1])

# Generate functions.

def city() -> str:
	"""Generates city name, unique every time."""
	while True:
		new_city = "S"
		while(new_city[-1] != "E"):
			new_city += random.choice(city_next_chars[new_city[-1 - memory:]])
		if((new_city not in cities) and (len(new_city) > 3)):
			break
	cities.append(new_city)
	return new_city[1:-1].title()

def name() -> str:
	"""(TBI) Generates name, unique every time."""
	while True:
		new_name = "S"
		while(new_name[-1] != "E"):
			new_name += random.choice(name_next_chars[new_name[-1 - memory:]])
		if((new_name not in names) and (len(new_name) > 3)):
			break
	names.append(new_name)
	return new_name[1:-1].title()
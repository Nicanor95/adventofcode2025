import sys
from math import floor

if (len(sys.argv) <= 1):
	print("Missing input.", "Usage: SecretEntrance.py <input> [input ...]", sep="\n")
	exit(1)

def partOne (lineas: list):
	position = 50
	password = 0

	for line in lineas:
		if (line[0]) == "R":
			position = (position + int(line[1:])) % 100
		else:
			position = (position - int(line[1:])) % 100

		if (position == 0): 
			password += 1

	return password

def partTwo_brute(lineas: list):
	position = 50
	password = 0

	for line in lineas:
		valor = int(line[1:])

		if (line[0]) == "R":
			password += floor((position + valor) / 100)
			position = (position + valor) % 100
		else:
			for _ in range(valor):
				position = (position - 1) % 100
				password = password + 1 if position == 0 else password
	
	return (password)


def partTwo_brute_cache(lineas: list):
	position = 50
	password = 0
	cache = {}

	for line in lineas:
		valor = int(line[1:])
		direccion = line[0]
		original_pos = position
		original_pass = password

		# Agregamos el origen al cache si no está
		if position not in cache:
			cache.update({position : {}})

		try:
			cached = cache[position][valor] if direccion == "R" else cache[position][-valor]
			password += cached[0]
			position = cached[1]
		except (KeyError):
			# No se encuentra en el cache.
			if direccion == "R":
				password += floor((position + valor) / 100)
				position = (position + valor) % 100
			else:
				for _ in range(valor):
					position = (position - 1) % 100
					password = password + 1 if position == 0 else password
				valor = -valor # Invertimos para guardar en cache.

			# Guardamos en cache, para la posicion, guardamos una tupla por cada valor, de forma (delta_password, final_position)
			cache[original_pos].update({valor : (password - original_pass, position)})
			
	return (password)



for input_path in sys.argv[1:]:
	with open(input_path, "r") as infile:
		lines = infile.readlines()
		
		print("Password One: {}".format(partOne(lines)), 
			  "Password Two Brute: {}".format(partTwo_brute(lines)),
			  "Password Two Cache: {}".format(partTwo_brute_cache(lines)),
			  sep="\n" )
		

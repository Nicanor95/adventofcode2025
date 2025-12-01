import sys
from math import ceil, floor

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
			for _ in range(valor):
				position = (position + 1) % 100
				password = password + 1 if position == 0 else password
		else:
			for _ in range(valor):
				position = (position - 1) % 100
				password = password + 1 if position == 0 else password
	
	return (password)



for input_path in sys.argv[1:]:
	with open(input_path, "r") as infile:
		lines = infile.readlines()
		print("Password One: {}".format(partOne(lines)), 
			  "Password Two Brute: {}".format(partTwo_brute(lines)),
			  sep="\n" )
		

import sys

if (len(sys.argv) <= 1):
	print("Missing input.", "Usage: SecretEntrance.py <input> [input ...]", sep="\n")
	exit(1)

for input_path in sys.argv[1:]:
	with open(input_path, "r") as infile:
		position = 50
		password = 0

		for line in infile.readlines():
			if (line[0]) == "R":
				position = (position + int(line[1:])) % 100
			else:
				position = (position - int(line[1:])) % 100

			if (position == 0): 
				password += 1

		print("Password: {}".format(password))


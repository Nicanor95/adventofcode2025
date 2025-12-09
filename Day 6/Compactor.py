import sys
import re

if (len(sys.argv) <= 1):
	print("Missing input.", "Usage: Compactor.py <input> [input ...]", sep="\n")
	exit(1)


for filename in sys.argv[1:]:
	with open(filename, "r", encoding="utf-8") as operations:
		operations = [line.strip() for line in operations.readlines()]

		# Compile the splitting regex
		splitRgx = re.compile(r'\s+')

		# Split the operation lines
		operations = [splitRgx.split(line) for line in operations]

		# Now operations is like a matrix
		# ┌───┬─────┬───────┬───────┬──────┐
		# │ x │  0  │   1   │   2   │  3   │
		# ├───┼─────┼───────┼───────┼──────┤
		# │ 0 │ 123 │  328  │  51   │  64  │
		# │ 1 │ 45  │  64   │  387  │  23  │
		# │ 2 │ 6   │  98   │  215  │  314 │
		# │ 3 │ *   │  +    │  *    │  +   │
		# └───┴─────┴───────┴───────┴──────┘
		# So, operations[0][2] would be 51.
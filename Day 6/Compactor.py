import sys
import re
from functools import reduce

if (len(sys.argv) <= 1):
	print("Missing input.", "Usage: Compactor.py <input> [input ...]", sep="\n")
	exit(1)

def Day6p1 (numbers: list[list], operations: list[str]) -> int:
	total = 0

	for i, op in enumerate(operations):
		# Turn the column into a list, so operands includes all numbers used in
		# each operation. ex: operands = [123, 45, 6] for the operation
		# at i = 0, in this case '*'
		operands = [int(numbers[y][i]) for y in range(len(numbers))]
		match op:
			case "*":
				total += reduce(lambda x, y: x * y, operands)
			case "+":
				total += reduce(lambda x, y: x + y, operands)
			case _:
				continue

	return total

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
		# operations[-1] == ['*', '+', '*', '+']
		# operations[:-1] == [	
		# 	['123', '328', '51', '64'], 
		# 	['45', '64', '387', '23'], 
		# 	['6', '98', '215', '314']
		# ]

		print(f"Password One: {Day6p1(operations[:-1], operations[-1])}")
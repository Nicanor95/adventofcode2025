import sys

if (len(sys.argv) <= 1):
	print("Missing input.", "Usage: Rolls.py <input> [input ...]", sep="\n")
	exit(1)

def isFree (rolls: list, index: tuple[int, int]) -> bool:
	( a, b ) = index

	# Set up our ranges
	idxRange_a = ()
	if a != 0 and a < len(rolls) - 1: # Center
		idxRange_a = range(a - 1, a + 2)
	elif (a == 0): # Start
		idxRange_a = range(a, a + 2)
	else: # End
		idxRange_a = range(a - 1, a + 1)
	slice = (b - 1, b + 2) if b != 0 else (b, b + 2)

	# Count rolls
	rollCount = 0
	for idx in idxRange_a:
		rollCount += rolls[idx][slice[0]:slice[1]].count("@")

	return (rollCount <= 4)

def findRolls (rolls: list) -> int:
	count = 0
	for i, row in enumerate(rolls):
		for z, item in enumerate(row):
			if item == "@" and isFree(rolls, (i,z)):
				count += 1
	return count

for filename in sys.argv[1:]:
	with open(filename, "r") as rollMap:
		rolls = [x.strip() for x in rollMap.readlines()]
		print(f"Password One: {findRolls(rolls)}")
import sys

if (len(sys.argv) <= 1):
	print("Missing input.", "Usage: Spoils.py <input> [input ...]", sep="\n")
	exit(1)


def day5_p1 (fresh: list[tuple[int, int]], ingredients: list[int]) -> int:
	count = 0

	for ingredient in ingredients:
		if any(map(lambda x: x[0] <= ingredient <= x[1], fresh)):
			count += 1

	return count

for filename in sys.argv[1:]:
	with open(filename, "r") as spoils:
		# Read ingredients and fresh list
		fresh, ingredients = [x.split("\n") for x in spoils.read().split("\n\n")]

		# Translate ingredients to int
		ingredients = ingredients[:-1] if ingredients[-1] == '' else ingredients
		ingredients = [int(x) for x in ingredients]

		# Capture the ranges into a tuple (start, end) and sort them to ease consolidation
		fresh = [(int(b),int(c)) for b,c in [x.split('-') for x in fresh]]
		fresh.sort(key= lambda x: x[0])

		# Consolidate the ranges
		consolidated = []
		start, end = (fresh[0]) # Grab the first
		for range in fresh:
			if start <= range[0] <= end:
				end = max(range[1], end)
			else:
				consolidated.append((start,end))
				start, end = range
		consolidated.append((start,end))
		
		print(f"Password One: {day5_p1(consolidated, ingredients)}")

import sys

if (len(sys.argv) <= 1):
	print("Missing input.", "Usage: Spoils.py <input> [input ...]", sep="\n")
	exit(1)

def consolidable(a: tuple[int,int], b:tuple[int,int]) -> bool:
	return a[0] <= b[0] <= a[1]

def consolidate(a: tuple[int,int], b:tuple[int,int]):
	if a[0] <= b[0] <= a[1]:
		return (a[0],max(b[1],a[1]))
	return a

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
		fresh = list(zip(fresh, fresh[1:]))

		while True:
			fresh = list(map(lambda x: consolidate(x[0], x[1]), fresh))

			# Zip if it's still consolidable
			if any(list(map(lambda x: consolidable(x[0], x[1]), list(zip(fresh, fresh[1:]))))):
				fresh = list(zip(fresh, fresh[1:]))
			else:
				break

		
		print(fresh)
		print(ingredients)

import sys

if (len(sys.argv) <= 1):
	print("Missing input.", "Usage: SecretCodes.py <input> [input ...]", sep="\n")
	exit(1)

def isInvalid(number):
	number = str(number)
	if (not len(number) & 1): # The number splits even
		half = int(len(number)/2)
		if (number[:half] == number[half:]):
			return True
	return False


def dayTwo(ranges: list):
	invalid = []
	for rg in ranges:
		invalid.extend(list(filter(isInvalid ,range(rg[0], rg[1]+1))))
	return sum(invalid)

def dayTwoPartTwo(ranges: list):
	return 1

for input in sys.argv[1:]:
	with open(input, "r") as infile:
		ranges = [(int(start.strip()), int(end.strip())) for (start, end) in [rango.split("-") for rango in infile.readline().split(",")]]
		
		print("Password Part One: {}".format(dayTwo(ranges)))
		print("Password Part Two: {}".format(dayTwoPartTwo(ranges)))
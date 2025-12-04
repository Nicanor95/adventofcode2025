import sys

if (len(sys.argv) <= 1):
	print("Missing input.", "Usage: Jolts.py <input> [input ...]", sep="\n")
	exit(1)

def maxJolt(battery: str) -> int:
	bat = [int(x) for x in battery.strip()]
	firstDigit = max(bat[:-1]) # We do not care about the last one.
	secondDigit = max(bat[bat.index(firstDigit)+1:]) # Capture the second highest, we care about the last one.
	return firstDigit*10+secondDigit

def maxJolt_p2(battery: str) -> int:
	bat = [int(x) for x in battery.strip()]
	number = 0
	maxIndex = 0
	for index in range(-11, 1):
		highest = max(bat[:index]) if index != 0 else max(bat)
		maxIndex = bat.index(highest)
		bat = bat[maxIndex + 1:]
		number = number * 10 + highest
	return number

def day3_one(batteries: list) -> int:
	return sum(list(map(maxJolt, batteries)))

def day3_two(batteries: list):
	return sum(list(map(maxJolt_p2, batteries)))

for batteryInput in sys.argv[1:]:
	with open(batteryInput, "r") as inputFile:
		batteries = inputFile.readlines()
		print(f"Password One: {day3_one(batteries)}")
		print(f"Password Two: {day3_two(batteries)}")
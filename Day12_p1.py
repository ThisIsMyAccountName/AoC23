from functools import cache
inp = [(line.split()[0] + "S",tuple(map(int, line.split()[1].split(",")))) for line in open('inputs/day12.txt').read().splitlines()]

@cache
def solve(springs, damaged, have_done):
	if springs == "":
		if damaged and have_done == damaged[0] and len(damaged) == 1:
			# at last spring, and can end current damaged streak
			return 1
		return 1 if have_done == 0 and not damaged else 0
	combination = 0
	curr = [".", "#"] if springs[0] == "?" else [springs[0]]
	for c in curr:
		if c == "#":
			# Can extend current damaged streak
			combination += solve(springs[1:], damaged, have_done + 1)
		elif have_done:
			if not damaged: continue
			if damaged[0] == have_done:
				# Can end current damaged streak
				combination += solve(springs[1:], damaged[1:], 0)
		else:
			# Can look for a new damaged streak
			combination += solve(springs[1:], damaged, 0)
	return combination

print(sum(solve(springs, dmg, 0) for springs, dmg in inp))
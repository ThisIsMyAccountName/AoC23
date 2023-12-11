from itertools import combinations
space = [[i for i in x.strip()] for x in open('inputs/day11.txt').read().splitlines()]
all_galaxies = [(i,j) for i in range(len(space)) for j in range(len(space[i])) if space[i][j] == "#"]
all_pairs = list(combinations(all_galaxies, 2))
gaps = {i: True if all([space[j][i] == "." for j in range(len(space))]) else False for i in range(len(space[0]))}
def dist(a, b, extra):
	bonus = sum([1 for i in range(min(a[1], b[1]), max(a[1], b[1]) + 1) if gaps[i]])
	return abs(a[0] - b[0]) + abs(a[1] - b[1]) + bonus * extra
print(sum([dist(a, b, 1) for a, b in all_pairs]))
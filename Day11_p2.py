from itertools import combinations
space = [[i for i in x.strip()] for x in open('inputs/day11.txt').read().splitlines()]
all_galaxies = [(i,j) for i in range(len(space)) for j in range(len(space[i])) if space[i][j] == "#"]
all_pairs = list(combinations(all_galaxies, 2))
x_gaps = {i: True if all([space[j][i] == "." for j in range(len(space))]) else False for i in range(len(space[0]))}
y_gaps = {i: True if all([space[i][j] == "." for j in range(len(space[i]))]) else False for i in range(len(space))}
def dist(a, b, extra):
	bonus = sum([1 for i in range(min(a[1], b[1]), max(a[1], b[1]) + 1) if x_gaps[i]])
	bonus += sum([1 for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1) if y_gaps[i]])
	return abs(a[0] - b[0]) + abs(a[1] - b[1]) + bonus * extra
print(sum([dist(a, b, 999_999) for a, b in all_pairs]))
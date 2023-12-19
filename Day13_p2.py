grids = []
with open('inputs/day13.txt') as file:
	grid = []
	for x in file:
		if x.strip() == "":
			grids.append(grid)
			grid = []
		else:
			grid.append(x.strip())
grids.append(grid)

def find_mirror(grid, miss=0):
	for i in range(len(grid)-1):
		matches = 0
		for x,y in zip(grid[i+1:], grid[i::-1]):
			matches += sum([0 if x1 == y1 else 1 for (x1, y1) in zip(x, y)])
		if matches == miss:
			return i+1
	return 0

	
h = sum([find_mirror(grid, miss=1) for grid in grids])
v = sum([find_mirror([*zip(*grid)], miss=1) for grid in grids])

print(h*100+v)	

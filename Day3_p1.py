def find_neigbours(row, idxs, grid):
	neighbours = []
	dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	for idx in idxs:
		for x,y in dirs:
			if 0 <= row + x < len(grid) and 0 <= idx + y < len(grid[0]) and grid[row + x][idx + y] in "+@%*#-/=$&":
				neighbours.append((row + x, idx + y))
	return list(set(neighbours))
	
grid = []
with open('inputs/day3.txt') as file:
	for x in file:
		grid.append(x)
ret_sum = 0
for row, line in enumerate(grid):
	num = ""
	idxs = []
	idx = 0
	while idx < len(line):
		if line[idx].isdigit():
			num += line[idx]
			idxs.append(idx)
			idx += 1
			continue
		if find_neigbours(row, idxs, grid):
			ret_sum += int(num)
		num = ""
		idxs = []
		idx += 1
	if find_neigbours(row, idxs, grid):
		ret_sum += int(num)
print(ret_sum)
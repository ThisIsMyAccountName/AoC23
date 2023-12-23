grid = [[x for x in line] for line in open('inputs/day22.txt').read().splitlines()]

start = (len(grid)//2, len(grid[0])//2)

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
def get_neig(x,y):
	neig = []
	for d in dirs:
		new_x, new_y = x + d[0], y + d[1]
		if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
			continue
		if grid[new_x][new_y] == "#":
			continue
		neig.append((new_x, new_y))
	return neig
pos = [start]
for i in range(64):
	new_pos = set()
	for p in pos:
		neig = get_neig(*p)
		new_pos.update(neig)
	pos = new_pos

print(len(pos))
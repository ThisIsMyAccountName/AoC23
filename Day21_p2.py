grid = [[x for x in line] for line in open('inputs/day22.txt').read().splitlines()]

start = (len(grid)//2, len(grid[0])//2)

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
def get_neig(x,y,x2,y2):
	neig = []
	for d in dirs:
		new_x, new_y = x + d[0], y + d[1]
		if new_x < 0:
			neig.append((len(grid) - 1, new_y, x2 - 1, y2))
			continue
		elif new_x >= len(grid):
			neig.append((0, new_y, x2 + 1, y2))
			continue
		elif new_y < 0:
			neig.append((new_x, len(grid[0]) - 1, x2, y2 - 1))
			continue
		elif new_y >= len(grid[0]):
			neig.append((new_x, 0, x2, y2 + 1))
			continue
		if grid[new_x][new_y] == "#":
			continue
		neig.append((new_x, new_y, x2, y2))
	return neig
div,rest = 26501365//len(grid), 26501365%len(grid)
memo, vis = {0:1}, {}
pos = [(start[0],start[1],0,0)]
for i in range(1,rest+2*len(grid)+1):
	new_pos = set()
	for p in pos:
		neig = get_neig(*p)
		for n in neig:
			if n in vis:
				continue
			new_pos.add(n)
	vis = pos
	pos = new_pos
	memo[i] = len(pos) + (memo[i-2] if i > 1 else 0)

sub1 = memo[rest+2*len(grid)] - memo[rest+len(grid)]
sub2 = memo[rest+2*len(grid)] + memo[rest] - 2*memo[rest+len(grid)]
print(memo[rest+2*len(grid)] + (div-2)*(2*sub1 + (div-1)*sub2)//2)
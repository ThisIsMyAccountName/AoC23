grid = [[x for x in line] for line in open('inputs/day23.txt').read().splitlines()]

start = (0,1)
end = (len(grid)-1, len(grid[0])-2)
dirs = [(0,-1),(0,1),(1,0),(-1,0)]
n,m = len(grid), len(grid[0])
def get_neig(x,y, vis):
	neig = []
	for d in dirs:
		new_x, new_y = x + d[0], y + d[1]
		if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
			continue
		if grid[new_x][new_y] == "#":
			continue
		if (new_x, new_y) in vis:
			continue
		neig.append((new_x, new_y))
	return neig

def path(start, end, vis, length=0):
	global paths
	queue = [(length, start)]
	while queue:
		length, pos = queue.pop()
		if pos in vis:
			continue
		vis.add(pos)
		if pos == end:
			paths = max(paths, length)
			return
		neig = get_neig(*pos, vis)
		if len(neig) == 1:
			x,y = neig[0]
			if grid[x][y] == ">":
				vis.add(neig[0])
				queue.append((length + 2, (x,y+1)))
				continue
			elif grid[x][y] == "v":
				vis.add(neig[0])
				queue.append((length + 2, (x+1,y)))
				continue
			else:
				queue.append((length + 1, neig[0]))
		else:
			for n in neig:
				path(n, end, vis.copy(), length + 1)
	
paths = 0
vis = set()
path(start, end, vis)
lens = []
print(paths)

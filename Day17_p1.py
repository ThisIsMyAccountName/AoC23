import heapq
grid = [[int(x) for x in line] for line in open('inputs/day17.txt').read().splitlines()]

def path_find(grid,min_steps=1,max_steps=3):
	start = (0,0)
	end = (len(grid)-1, len(grid[0])-1)
	visited = {}
	dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
	queue = [(0, start, 'R', 1), (0, start, 'D', 1)]

	while queue:
		weight, pos, dir, steps = heapq.heappop(queue)
		if (pos, dir, steps) in visited:
			continue
		visited[(pos, dir, steps)] = True
		x,y = pos
		new_x, new_y = x + dirs[dir][0], y + dirs[dir][1]
		if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
			continue
		new_weight = weight + grid[new_x][new_y]
		if steps >= min_steps and steps <= max_steps:
			if new_x == end[0] and new_y == end[1]:
				return new_weight
		for d,v in dirs.items():
			if v[0] + dirs[dir][0] == 0 and v[1] + dirs[dir][1] == 0:
				continue
			new_steps = steps + 1 if d == dir else 1
			if (d != dir and steps < min_steps) or new_steps > max_steps:
				continue
			heapq.heappush(queue, (new_weight, (new_x, new_y), d, new_steps))

print(path_find(grid))

pipes = []
with open('inputs/day10.txt') as file:
	for x in file:
		pipes.append(x.strip())
dirs_map = {"F": [(1,0), (0,1)], "|": [(-1,0), (1,0)], 
		"L": [(-1,0),(0,1)], "J":[(-1,0),(0,-1)], 
		"7": [(0,-1),(1,0)], "-":[(0,-1),(0,1)],
		"S": [(-1,0),(0,1)]}

start = [(x,y) for x,line in enumerate(pipes) for y,char in enumerate(line) if char == "S"][0]
dist_map = {}
dist_map[start] = 0
queue = [start]
while queue:
	x,y = queue.pop(0)
	char = pipes[x][y]
	dirs = dirs_map[char]
	for dx,dy in dirs:
		new = (x+dx,y+dy)
		if new not in dist_map:
			dist_map[new] = dist_map[(x,y)] + 1
			queue.append(new)

print(max(dist_map.values()))
	
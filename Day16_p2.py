from collections import deque
grid = [[x for x in line] for line in open('inputs/day16.txt').read().splitlines()]
dirs = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
def move(dir, x, y):
	if grid[x][y] == ".":
		return (dir, (x+dirs[dir][0], y+dirs[dir][1]))
	elif grid[x][y] == "|":
		if dir in "RL":
			return [1,("D",(x+1,y)), ("U",(x-1,y))]
		else:
			return (dir, (x-1,y)) if dir == "U" else (dir, (x+1,y))
	elif grid[x][y] == "-":
		if dir in "UD":
			return [1,("R",(x,y+1)), ("L",(x,y-1))]
		else:
			return (dir, (x,y-1)) if dir == "L" else (dir, (x,y+1))
	elif grid[x][y] == "/":
		if dir == "L":
			return ("U", (x+1,y))
		elif dir == "R":
			return ("D", (x-1,y))
		elif dir == "D":
			return ("R", (x,y+1))
		elif dir == "U":
			return ("L", (x,y-1))
	elif grid[x][y] == "\\":
		if dir == "R":
			return ("D", (x+1,y))
		elif dir == "L":
			return ("U", (x-1,y))
		elif dir == "U":
			return ("L", (x,y-1))
		elif dir == "D":
			return ("R", (x,y+1))

def solve(grid, move_queue=[]):
	vis = set()
	while move_queue:
		dir, pos = move_queue.pop()
		if (dir,pos) in vis:
			continue
		if pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0]):
			continue
		vis.add((dir,pos))
		new_moves = move(dir, *pos)
		if len(new_moves) == 3:
			for i in new_moves[1:]:
				move_queue.append(i)
		else:
			move_queue.append(new_moves)
	return len(set((x,y) for dir, (x,y) in vis))
p2 = 0
for i in range(len(grid)):
	p2 = max(p2, solve(grid, [("D",(0,i))]))
	p2 = max(p2, solve(grid, [("U",(len(grid)-1,i))]))
for i in range(len(grid[0])):
	p2 = max(p2, solve(grid, [("R",(i,0))]))
	p2 = max(p2, solve(grid, [("L",(i,len(grid[0])-1))]))
print(p2)
print(solve(grid, [("R",(0,0))]))
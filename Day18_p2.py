dirs, amounts = [], []
dir_map = ["R", "D", "L", "U"]
with open('inputs/day18.txt') as file:
	for x in file:
		dir,amount,color = x.strip().split()
		color = color[2:-1]
		dir = color[-1]
		amount = int(color[:-1],16)
		dirs.append(dir_map[int(dir)])
		amounts.append(amount)
		
def make_grid(dirs, amounts):
	width, height = 0,0
	points = []
	for dir, amount in zip(dirs,amounts):
		if dir == "R":
			width += int(amount)
		elif dir == "L":
			width -= int(amount)
		elif dir == "U":
			height -= int(amount)
		else:
			height += int(amount)
		points.append((height, width))
	return points

def shoelace(points):
	ret = sum([(points[i-1][0] * points[i][1]) for i in range(len(points))])
	ret -= sum([(points[i-1][1] * points[i][0]) for i in range(len(points))])
	return abs(ret) // 2

points = make_grid(dirs, amounts)
print(shoelace(points) + (sum(amounts) // 2) + 1)
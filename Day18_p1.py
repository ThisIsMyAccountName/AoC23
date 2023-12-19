dirs, amounts = [], []
with open('inputs/day18.txt') as file:
	for x in file:
		dir,amount,color = x.strip().split()
		dirs.append(dir)
		amounts.append(int(amount))
def solve(dirs, amounts):
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

		

points = solve(dirs, amounts)
print((shoelace(points) + (sum(amounts) // 2) + 1))
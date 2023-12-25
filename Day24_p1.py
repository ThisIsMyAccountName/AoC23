from itertools import combinations
storms = []
for line in open("inputs/day24.txt"):
	cords, vel = line.split(" @ ")
	cords = cords.split(", ")
	vel = vel.split(", ")
	storm = (tuple(map(int, cords)), tuple(map(int, vel)))
	storms.append(storm)

def line_intersection(line1, line2):
	xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

	def det(a, b):
		return a[0] * b[1] - a[1] * b[0]

	div = det(xdiff, ydiff)
	if div == 0:
		return None, None

	d = (det(*line1), det(*line2))
	x = det(d, xdiff) / div
	y = det(d, ydiff) / div
	return x, y


start = 200000000000000
stop = 400000000000000
storms = combinations(storms, 2)
intersections = []

for storm in storms:
	(storm1, storm2) = storm
	((x1,y1,_),(vx1,vy1,_)) = storm1
	((x2,y2,_),(vx2,vy2,_)) = storm2
	line1 = ((x1, y1), (x1 + vx1 * 1e9, y1 + vy1 * 1e9))
	line2 = ((x2, y2), (x2 + vx2 * 1e9, y2 + vy2 * 1e9))
	x_inter, y_inter = line_intersection(line1, line2)
	if x_inter is None or y_inter is None:
		continue
	if x_inter >= start and x_inter <= stop and y_inter >= start and y_inter <= stop:
		if x_inter < storm1[0][0] and vx1 > 0:
			continue
		if x_inter < storm2[0][0] and vx2 > 0:
			continue
		if y_inter < storm1[0][1] and vy1 > 0:
			continue
		if y_inter < storm2[0][1] and vy2 > 0:
			continue
		if x_inter > storm1[0][0] and vx1 < 0:
			continue
		if x_inter > storm2[0][0] and vx2 < 0:
			continue
		if y_inter > storm1[0][1] and vy1 < 0:
			continue
		if y_inter > storm2[0][1] and vy2 < 0:
			continue
		intersections.append((x_inter, y_inter, storm1[0], storm2[0]))
print(len(intersections))

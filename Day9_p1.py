seq = [[int(x) for x in line.split()] for line in open('inputs/day9.txt').read().splitlines()]
sm = 0
for s in seq:
	dif = s
	while not all([x == 0 for x in dif]):
		sm += dif[-1]
		dif = [dif[i] - dif[i-1] for i in range(1, len(dif))]
print(sm)
		
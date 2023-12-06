with open('inputs/day6.txt') as file:
    times = list(map(int, file.readline().split(":")[1].split()))
    dists = list(map(int, file.readline().split(":")[1].split()))

ret = 1
for i in range(len(times)):
	time, dist = times[i], dists[i]
	for step in range(time):
		d = step * (time - step)
		if d > dist:
			break
	ret *= (time - (2 * step - 1))

print(ret)
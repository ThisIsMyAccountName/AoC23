with open('inputs/day6.txt') as file:
    times = int("".join(file.readline().split(":")[1].split()))
    dists = int("".join(file.readline().split(":")[1].split()))
# print(len([i for i in range(times) if i * (times - i) > dists]))

r,l = 1, times // 2
while r <= l:
	mid = (r + l) // 2
	if mid * (times - mid) < dists:
		r = mid + 1
	else:
		l = mid - 1
 
print(times - (2 * r - 1))
sum = 0
with open('inputs/day1.txt') as file:
	for x in file:
		l = [i for i in x if i.isdigit()]
		if len(l) == 1:
			num = l[0] + l[0]
		else:
			num = l[0] + l[-1]
		sum += int(num)
print(sum)
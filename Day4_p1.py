ret_sum = 0
with open('inputs/day4.txt') as file:
	for x in file:
		win, mine = [num.strip().split() for num in x.split(":")[1].split("|")]
		pnts = sum([1 for num in mine if num in win])
		ret_sum += 1 << (pnts - 1) if pnts else 0
print(ret_sum)
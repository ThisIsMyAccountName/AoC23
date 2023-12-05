from collections import defaultdict
card = 1
lodd = defaultdict(lambda: 1)
with open('inputs/day4.txt') as file:
	for x in file:
		win, mine = [num.strip().split() for num in x.split(":")[1].split("|")]
		pnts = sum([1 for num in mine if num in win])
		for i in range(card + 1, card + 1 + pnts):
			lodd[i] += lodd[card]
		card += 1
print(sum(lodd.values()))
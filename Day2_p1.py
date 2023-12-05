from collections import defaultdict
checks = {"red": 12 , "green" : 13, "blue": 14}
dic = defaultdict(int)
sm = 0
i = 1
with open('inputs/day2.txt') as file:
	for x in file:
		curr = defaultdict(int)
		game,colors = x.split(":")
		subgames = colors.split(";")
		for subgame in subgames:
			for color in subgame.split(","):
				n, c = color.split()
				curr[c] = max(curr[c], int(n))
		b = True
		for color in ["red", "green", "blue"]:
			if curr[color] > checks[color]:
				b = False
				break
		if b:
			sm += i
		i += 1
		

	
print(sm)
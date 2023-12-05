sm = 0
with open('inputs/day2.txt') as file:
	for x in file:
		curr = {"red" : 0, "green" : 0, "blue": 0}
		game, colors = x.split(":")
		subgames = colors.split(";")
		for subgame in subgames:
			for color in subgame.split(","):
				n, c = color.split()
				curr[c] = max(curr[c], int(n))
		prod = 1
		for v in curr.values():
			prod *= v
		sm += prod

print(sm)
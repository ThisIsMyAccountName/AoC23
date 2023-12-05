seeds = []
maps = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
map_idx = 0
grab_name = False
with open('inputs/day5.txt') as file:
	for i,x in enumerate(file):
		if i == 0:
			seeds = list(map(int, x.split(":")[1].split()))
			continue
		if x == "\n":
			grab_name = True
			continue
		if grab_name:
			grab_name = False
			map_idx += 1
			continue
		dest, src, amount = list(map(int, x.split()))
		maps[map_idx].append((dest, src, amount))

seed_map = {seed: seed for seed in seeds}		
for seed in seeds:
	for m in range(1,8):
		for dest, src, amount in maps[m]:
			if src <= seed_map[seed] < src + amount:
				seed_map[seed] = seed_map[seed] + dest - src
				break
print(min(seed_map.values()))
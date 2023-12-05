from collections import defaultdict
def check_if_gear(row, idxs, grid):
	gears = []
	dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	for idx in idxs:
		for x,y in dirs:
			if 0 <= row + x < len(grid) and 0 <= idx + y < len(grid[0]) and grid[row + x][idx + y] in "*":
				gears.append((row + x, idx + y))
				break
	return list(set(gears))

grid = []
with open('inputs/day3.txt') as file:
	for x in file:
		grid.append(x)
gears = []
for row, line in enumerate(grid):
	for idx, char in enumerate(line):
		if char == "*":
			gears.append((row, idx))
grear_mask = {}
for gear in gears:
	grear_mask[gear] = []
number_mask = defaultdict(list)
for row, line in enumerate(grid):
	num = ""
	idxs = []
	idx = 0
	while idx < len(line):
		if line[idx].isdigit():
			num += line[idx]
			idxs.append(idx)
		elif num != "":
			gear = check_if_gear(row, idxs, grid)
			if gear:
				for gear_row, gear_idx in gear:
					grear_mask[(gear_row, gear_idx)] += [num]
					number_mask[(gear_row, gear_idx)] += [idxs]
			num = ""
			idxs = []
		idx += 1
	if num != "":
		gear = check_if_gear(row, idxs, grid)
		if gear:
			for gear_row, gear_idx in gear:
				grear_mask[(gear_row, gear_idx)] += [num]
				number_mask[(gear_row, gear_idx)] += [idxs]
ret_prod = 0
for gear, nums in grear_mask.items():
	if len(nums) == 2:
		ret_prod += int(nums[0]) * int(nums[1])
print(ret_prod)
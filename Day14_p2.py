plane = (tuple([x for x in i]) for i in open('inputs/day14_test.txt').read().splitlines())
def solve_dir(plane, dir):
	transform = lambda plane : tuple(map(lambda x : "".join(x),[*zip(*plane)]))
	if dir in "NS":
		plane = transform(plane)
	new_plane = ()
	for row in plane:
		new_row = ()
		for part in row.split("#"):
			new_row += ("".join(sorted(part, reverse = True if dir in "NW" else False)),)
		new_plane += ("#".join(new_row),)
	if dir in "NS":
		new_plane = transform(new_plane)
	return new_plane
		
n = 1e9
memo = {}
i = 0
while i < n:
	if plane in memo:
		break
	memo[plane] = i
	for dir in "NWSE":
		plane = solve_dir(plane, dir)
	i += 1

loc = (n - (memo[plane] - 1)) % (i - memo[plane]) + (memo[plane] - 1)
for k,v in memo.items():
	if v == loc:
		plane = k
		break

count = 0
for i,row in enumerate(plane):
	for rock in row:
		if rock == "O":
			count += len(plane) - i 
print(count)
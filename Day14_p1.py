plane = (tuple([x for x in i]) for i in open('inputs/day14.txt').read().splitlines())
def solve_dir(plane, dir):
	if dir in "NS":
		plane = tuple(map(lambda x : "".join(x),[*zip(*plane)]))
	new_plane = ()
	for row in plane:
		new_row = ()
		for part in row.split("#"):
			new_row += ("".join(sorted(part, reverse=True if dir in "NW" else False)),)
		new_plane += ("#".join(new_row),)
	if dir in "NS":
		new_plane = tuple(map(lambda x : "".join(x),[*zip(*new_plane)]))
	return new_plane
		
for dir in "N":
	plane = solve_dir(plane, dir)

count = 0
for i,row in enumerate(plane):
	for rock in row:
		if rock == "O":
			count += len(plane) - i 
print(count)
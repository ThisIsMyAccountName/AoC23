from math import lcm
dirs,_,*rest = open('inputs/day8.txt').read().splitlines()
mapping = {frm:to[1:-1].split(", ") for frm,to in [line.split(" = ") for line in rest]}
starts = [x for x in mapping.keys() if x[2] == "A"]
def find(start, end, idx=0):
	while start[2] != end:
		start = mapping[start][dirs[idx % len(dirs)] == "R"]
		idx += 1
	return idx
print(lcm(*[find(x, "Z") for x in starts]))
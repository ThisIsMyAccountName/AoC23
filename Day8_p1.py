dirs,_,*rest = open('inputs/day8.txt').read().splitlines()
mapping = {frm:to[1:-1].split(", ") for frm,to in [line.split(" = ") for line in rest]}
start, end = "AAA", "ZZZ"
idx = 0
while (start:=mapping[start][dirs[idx % len(dirs)] == "R"]) != end:
	idx += 1
print(idx)
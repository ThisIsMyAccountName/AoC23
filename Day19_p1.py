parts = []
workflows = {}
with open('inputs/day19.txt') as file:
    flows, prts = file.read().split("\n\n")
    for x in flows.splitlines():
        name, cond = x.strip().split("{")
        workflows[name] = cond[:-1]
    for x in prts.splitlines():
        parts.append(x.strip()[1:-1])

ret = 0
for part in parts:
	workflow = "in"
	part_vars = part.split(",")
	vals = {}
	for cur_part in part_vars:
		exec("vals['" + cur_part[0] + "'] = " + cur_part[2:])
	while workflow not in "AR":
		for cond in workflows[workflow].split(","):
			if ":" in cond:
				cond, dest = cond.split(":")
				if eval('vals["' + cond[0] + '"]' + "".join(cond[1:])):
					workflow = dest
					break
			else:
				workflow = cond
	if workflow == "A":
		ret += sum([int(x[2:]) for x in part_vars])

print(ret)
from math import prod
workflows = {}
with open('inputs/day19.txt') as file:
    flows, _ = file.read().split("\n\n")
    for x in flows.splitlines():
        name, cond = x.strip().split("{")
        workflows[name] = cond[:-1]

def part2(workflow, workdflows, ranges):
    if workflow == "A":
        return prod(cmax - c_min + 1 for c_min, cmax in ranges.values())
    elif workflow == "R":
        return 0

    ret = 0
    for cond in workdflows[workflow].split(","):
        if ":" not in cond:
            ret += part2(cond, workdflows, ranges)
        else:
            x = cond.split(":")
            new_range = ranges.copy()
            var, op, new_val, dest = x[0][0], x[0][1], int(x[0][2:]), x[1]
            curr_min, curr_max = ranges[var]

            if curr_min < new_val < curr_max:
                if op == ">":
                    new_range[var] = (new_val + 1, curr_max)
                    ranges[var] = (curr_min, new_val)
                else:
                    new_range[var] = (curr_min, new_val - 1)
                    ranges[var] = (new_val, curr_max)
                ret += part2(dest, workdflows, new_range)
    return ret

print(part2("in", workflows, {"x": (1,4000), "m": (1,4000), "a": (1,4000), "s": (1,4000)}))
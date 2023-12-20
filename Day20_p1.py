bcast = []
flip_flops = {}
conjections = {}
with open('inputs/day20.txt') as file:
	for x in file:
		x = x.strip()
		if x[0] == "b":
			bcast = x.split(" -> ")[1].split(", ")
		elif x[0] == "%":
			src, dest = x[1:].split(" -> ")
			flip_flops[src] = dest
		else:
			src, dest = x[1:].split(" -> ")
			conjections[src] = dest

low = 0
high = 1
type_map = {}
state_map = {}
for key in flip_flops:
	type_map[key] = "%"
	state_map[key] = low
for key in conjections:
	connected = {}
	for x in flip_flops:
		if key in flip_flops[x]:
			connected[x] = low
	for x in conjections:
		if key in conjections[x]:
			connected[x] = low
	type_map[key] = "&"
	state_map[key] = connected

def solve(counts, state_map=state_map, type_map=type_map):
	s_queue = []
	for x in bcast:
		s_queue.append((x, low, "input"))
	while s_queue:
		key, signal, src = s_queue.pop(0)
		counts[signal] += 1
		if key not in type_map:
			continue
		typ = type_map[key]
		if typ == "%":
			if signal == low:
				state_map[key] ^= 1
				for x in flip_flops[key].split(", "):
					s_queue.append((x, state_map[key], key))
			else:
				continue
		elif typ == "&":
			state_map[key][src] = signal
			send = high
			if all(state_map[key].values()):
				send = low
			for x in conjections[key].split(", "):
				s_queue.append((x, send, key))
	return counts


counts = [1000,0]
i = 1
for _ in range(1000):
	counts = solve(counts)

print(counts[0] * counts[1])
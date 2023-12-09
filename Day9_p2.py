seq = []
with open('inputs/day9.txt') as file:
	for x in file:
		seq.append(list(reversed([int(x) for x in x.split()])))

def find_diff(seq):
	diffs = []
	for i in range(1, len(seq)):
		diffs.append(seq[i] - seq[i-1])
	return diffs
sm = 0
for s in seq:
	t = [s]
	dif = find_diff(s)
	while not all([x == 0 for x in dif]):
		t.append(dif)
		dif = find_diff(dif)

	for i in range(len(t)-2, -1, -1):
		t[i].append(t[i][-1] + t[i+1][-1])
	sm += t[0][-1]
print(sm)
		
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_dict = {j:str(i+1) for i,j in enumerate(nums)}
def parse(string):
	ret = []
	for tall in nums:
		r = [i for i in range(len(string)) if string.startswith(tall, i)]
		for i in r:
			ret.append((i, num_dict[tall]))
	return ret

sm = []
with open('inputs/day1.txt') as file:
	for x in file:
		p = parse(x)
		l = [(i,j) for i,j in enumerate(x) if j.isdigit()]
		lp = l+p
		lp.sort(key=lambda x: x[0])
		if len(lp) == 0:
			continue
		if len(lp) == 1:
			num = lp[0][1] + lp[0][1]
		else:
			num = lp[0][1] + lp[-1][1]
		sm.append(int(num))
print(sum(sm))
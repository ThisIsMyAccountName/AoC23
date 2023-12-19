from collections import defaultdict
from functools import reduce

strings = open('inputs/day15.txt').read().split(",")

def hash(word):
	return reduce(lambda x,y: (x+y)*17%256, [ord(c) for c in word], 0)

boxes = defaultdict(dict)
for string in strings:
	if "-" in string:
		boxes[hash(string[:-1])].pop(string[:-1], None)
	else:
		lable, box = string.split("=")
		boxes[hash(lable)][lable] = int(box)
		
res = 0
for k,v in boxes.items():
	for i,(l,f) in enumerate(v.items()):
		res += (k+1) * (i+1) * f
print(res)
from functools import reduce

strings = open('inputs/day15.txt').read().split(",")

def hash(word):
	return reduce(lambda x,y: (x+y)*17%256, [ord(c) for c in word], 0)

print(sum([hash(string) for string in strings]))
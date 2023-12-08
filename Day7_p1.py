hands = [line.split() for line in open("inputs/day7.txt")]
	
five_of_kind = 1
four_of_kind = 2
full_house = 3
three_of_kind = 4
two_pair = 5
one_pair = 6
high_card = 7

def hand_type(hand):
	cards = {}
	for i in hand:
		if i in cards:
			cards[i] += 1
		else:
			cards[i] = 1
	if 5 in cards.values():
		return five_of_kind
	if 4 in cards.values():
		return four_of_kind
	if 3 in cards.values() and 2 in cards.values():
		return full_house
	if 3 in cards.values():
		return three_of_kind
	if list(cards.values()).count(2) == 2:
		return two_pair
	if 2 in cards.values():
		return one_pair
	return high_card
		
values = dict(zip("AKQJT98765432", range(13)))
def find_val(hand):
	return hand_type(hand), values[hand[0]], values[hand[1]], values[hand[2]], values[hand[3]], values[hand[4]]
	
g = sorted(hands, key=lambda x: find_val(x[0]), reverse=True)

ret_sum = sum([int(x[1]) * (i+1) for i,x in enumerate(g)])

print(ret_sum, 241344943, ret_sum == 241344943)



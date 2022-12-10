#!/usr/bin/env python3
from itertools import combinations


def main_():
	list1 = 'ABCDA'
	a = combinations(list1,2)
	print(len(list1))
	b = [''.join(i) for i in a]
	print(b)


N_CARDS = 26

def choose_n(n_cards,n_places):
	return combinations(range(0,n_cards),n_places)
	#print(b)

aces = choose_n(N_CARDS,4)
twos = choose_n(N_CARDS - 4,4)
threes = choose_n(N_CARDS - 8,4)
fourths = choose_n(N_CARDS - 12,4)
#total = len(list(aces))*len(list(twos))*len(list(threes))*len(list(fourths))

#print(len(str(total))-1)

from functools import reduce

#list comprhenesion
total_games = reduce(lambda x,y: x*y, [len(list(z)) for z in [aces,twos,threes,fourths]])
print(total_games)
print(len(str(total_games*2))-1)
#653534134886878245000, 334973944305000 *2 perche anche secondo mazzo
#simulazione con una carta buona in un mazzo


# usefull resource: https://docs.python.org/3/library/itertools.html
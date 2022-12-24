#!/usr/bin/env python3
from itertools import combinations
from functools import reduce

def main_():
	list1 = '000000001'
	a = combinations(list1, len(list1))
	print('len list1: ',len(list1))
	b = [''.join(i) for i in a]
	a = set(b)
	print('combinations: ', len(a))
	print(a)

	#https://stackoverflow.com/questions/36429507/python-combinations-without-repetitions

def combination_list_no_rep():
	list2 = [0,0,0,0,0,0,1,1,1]
	comb_with_rep = list(combinations(list2, len(list2)))
	comb_no_rep = set(comb_with_rep)
	print('len comb with rep: ', len(comb_with_rep))
	print('combinazioni senza ripetizioni: ', comb_no_rep)


#iteratore che restituisce combinazioni possibli
def choose_n(n_cards,n_places):
	return combinations(range(0,n_cards),n_places)
	#print(b) # se printi srotoli la funzione

def total_games():
# restitusce numero di assi, due , tre e quattri
	N_CARDS = 52
	aces = choose_n(N_CARDS,4)
	twos = choose_n(N_CARDS - 4,4)
	threes = choose_n(N_CARDS - 8,4)
	fourths = choose_n(N_CARDS - 12,4)

	#restituisce numero totale di combinazioni
	total = len(list(aces))*len(list(twos))*len(list(threes))*len(list(fourths))
	print('n totale di combinazioni: ', str(total))
	print('ordine di grandezza: ',len(str(total))-1)

#per capire se si può fare una lista enorme e consultare se il valore vale 1 o 0. 
#questo serve a capire se abbiamo già fatto quella partita
a = [0] * (10^20)
print(a[10^15] == 1)


#total_games()
main_()
#combination_list_no_rep()



'''
TO IMPLEMENT:
'''

#list comprhenesion
#total_games = reduce(lambda x,y: x*y, [len(list(z)) for z in [aces,twos,threes,fourths]])
#print(str(total_games))
#print(len(str(total_games*2))-1)

''' TOTAL GAME: 653534134886878245000 '''
#653534134886878245000, 334973944305000 *2 perche anche secondo mazzo


#simulazione con una carta buona in un mazzo

# usefull resource: https://docs.python.org/3/library/itertools.html
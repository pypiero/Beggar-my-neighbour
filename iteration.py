#!/usr/bin/env python3
from itertools import combinations
from functools import reduce
from itertools import permutations
from sympy.utilities.iterables import multiset_permutations

def sympy_permutations(initial_deck, start_from_deck):
	#while start_from_deck != initial_deck:
	a = list(multiset_permutations(start_from_deck))
	b = [''.join(i) for i in a]
	print('n combinations sympy_permutations: ', len(b))
	print(b)


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
def partita_già_fatta():
	a = [0] * (10^20)
	print(a[10^15] == 1)

def string_to_shuffle():
	initial_deck = '000100'
	str1 = '000001'
	print ('####\nstringa originale : ', str1, ' , lunghezza: ', len(str1))
	return initial_deck, str1


#string_comb_1(string_to_shuffle())
#combination_list_no_rep(string_to_shuffle())
#string_comb_2(string_to_shuffle())
sympy_permutations(string_to_shuffle()[0],string_to_shuffle()[1])

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

''' da controllare se posso partire l'iterazione da un punto X e se lui parte in ordine da li 
a fare le partite. praticamente sarebbe come mettere un segnalibro. quindi controllare se posso
partire ogni volta dal segnalibro SENZA creare il big database! quindi fare andare il programma 
per un tot di minuti o finchè non finisce un tot di partite o comunque se le finisce tutte si
deve fermare, cioè quando il deck è tornato in posizione iniziale.'''
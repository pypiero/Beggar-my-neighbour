#!/usr/bin/env python3
import random
from Game import play

'''
function that returns a list representing a shuffle deck of 52 cards 
where all the non-penality cards are '0' while J,Q,K, and A are 1,2,3,4.
when italian_deck=True returns the italian 40 cards deck modified 
'''
def shuffled_deck(italian_deck=False):
  if italian_deck: 
    deck = 4*[1] + 4*[2] + 4*[3]  + 28*[0]
  else:
    deck = 4*[1] + 4*[2] + 4*[3] + 4*[4] + 36*[0]
  random.shuffle(deck)
  return deck

def random_play(number_of_play):
  n_turns = []
  for i in range(0,number_of_play):  
      n_turns.append(play(shuffled_deck(),3748))

  n_turns.sort(reverse=True)
  #n_turns.sort(key= lambda x: -x[1])
  print('10 longest random play in ',number_of_play,' plays: ', n_turns[:10])

def test_long_plays():
  long_decks = [ [2,4,0,0,0,4,0,0,3,0,1,0,1,0,3,0,4,0,0,0,0,0,1,0,4,0,0,0,0,0,0,0,0,3,0,0,3,0,2,0,0,0,0,2,0,0,0,0,0,2,1,0]
                ,[4,1,4,0,0,0,0,4,2,0,0,4,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,1,0,1,0,2,3,0,0,0,0,3,0,0,0,0,0,3,0,0,0,0,1,0,3,0]
                ,[0,0,0,0,3,0,0,0,4,0,0,2,0,4,0,0,1,1,4,0,0,0,0,0,0,1,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,4,0,1,3,0,2,0,2,0,2]
                ,[0,0,0,0,0,3,1,0,0,0,0,0,0,1,0,0,3,0,2,0,0,2,2,0,3,0,0,0,1,0,0,3,0,0,0,1,0,0,2,0]
            ]
  for deck in long_decks:
    print('n of turns:',play(deck,10000))

test_long_plays()
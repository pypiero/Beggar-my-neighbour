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
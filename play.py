#!/usr/bin/env python3
import random

'''function that generate a shuffled 52 cards deck'''
def shuffled_deck():
  standard_deck = 4*[1] + 4*[2] + 4*[3] + 4*[4] + 36*[0]
  random.shuffle(standard_deck)
  return standard_deck

#funtion that play a cavacamisa game
def play(deck):
    Battle = False 
    discard_pile = [] 
    turn_A = True #first player to start
    turn_count = 0
    turns_to_do = int

	# split the deck in 2
    deck_A, deck_B = deck[:len(deck)//2], deck[len(deck)//2:]

    while deck_A and deck_B:
      turn_count += 1
      if turn_count == 5000: 
        print('play with more than 5000 turns: ',deck)
        break

      #draw a card from the right deck and put it in the discard pile
      if turn_A: discard_pile.append(deck_A.pop(0))
      else: discard_pile.append(deck_B.pop(0))
     
      # check battle status
      if not Battle:
      	# check if the card is "special"
        if discard_pile[-1] != 0: 
          Battle = True
          turns_to_do = discard_pile[-1] #last card played define how many turns of battle
        turn_A = not turn_A # next player is the other
        continue # next turn

      else: #if there is a battle
        if discard_pile[-1] !=0 : 
          turns_to_do = discard_pile[-1] 
          turn_A = not turn_A 
          continue
        else: # if the card played is not 'special'
          if turns_to_do == 1: # check if it's the last turn of battle
            Battle = False
            if turn_A: deck_B = deck_B + discard_pile #append the discard pile to the right deck
            else: deck_A = deck_A + discard_pile
            discard_pile = []
            turn_A = not turn_A
            continue # the other player play the next turn
          else:# if is not the last turn of battle
            turns_to_do -=1
            continue#next turn, same player
      
    return turn_count

def single_fixed_play():
  sample_deck =[0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 1, 1, 3, 4, 0, 0, 4, 0, 1, 0, 4, 0, 0, 0, 0,
   3, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 0, 4, 0, 0, 3, 1, 0, 0, 0]
  print('fixed play (349): ',play(sample_deck))

def random_play(number_of_play):
  n_turns = []
  for i in range(0,number_of_play):  n_turns.append(play(shuffled_deck()))
  n_turns.sort(reverse=True)
  print('10 longest random play in ',number_of_play,' plays: ', n_turns[:10])

def main():
  single_fixed_play()
  random_play(1000000)

main()

#!/usr/bin/env python3

def play(deck, turn_A=True):
  '''
  Play a Beggar-my-neighbour play

  parameters:
  deck : a list of cards where J,Q,K,A are 1,2,3,4 and all the other are 0
  turn_A :  (default = True) determine who play the first hand
  '''
  Battle = False 
  discard_pile = []
  turn_count = 0
  turns_to_do = int
	  #split the deck in two
  deck_A, deck_B = deck[:len(deck)//2], deck[len(deck)//2:]
  while deck_A and deck_B:
    turn_count += 1
      #draw a card from the right deck and put it on the discard pile
    if turn_A: discard_pile.append(deck_A.pop(0))
    else: discard_pile.append(deck_B.pop(0))
   
    # check battle status
    if not Battle:
    	# check if the card is "special"
      if discard_pile[-1] != 0: 
        Battle = True
        #last card played define how many turns of battle
        turns_to_do = discard_pile[-1]
      turn_A = not turn_A # next player is the other
      continue # next turn
    else: #if there is a battle
      if discard_pile[-1] !=0 : 
        turns_to_do = discard_pile[-1] 
        turn_A = not turn_A 
        continue
      else: # if the card played is not a penality-card
        if turns_to_do == 1: # check if it's the last turn of battle
          Battle = False
          #append the discard pile to the right deck
          if turn_A: deck_B = deck_B + discard_pile 
          else: deck_A = deck_A + discard_pile
          discard_pile = []
          turn_A = not turn_A
          continue # the other player play the next turn
        else:# if is not the last turn of battle
          turns_to_do -=1
          continue#next turn, same player
  return turn_count
#!/usr/bin/env python3
''' 
function that simulate a beggar-my-neighborn game from a list of cards.
returns the number of turn to end the game and the number of turns when
both the players plays with a equal number of cards.
the game stops if the turns are equal to 'max_turn' argument. this in case 
you find the legendary infinite game ;)
'''
def play(deck, max_turn=3749,turn_A=True):
    Battle = False 
    discard_pile = []
    turn_count = 0
    turns_to_do = int
    n_even_deck = 0

	  #split the deck in two
    deck_A, deck_B = deck[:len(deck)//2], deck[len(deck)//2:]

    while deck_A and deck_B:
      n_even_deck += 1 * (len(deck_A) == len(deck)//2)
      turn_count += 1
      if turn_count == max_turn: 
        print('play with more than ',str(max_turn),' turns: ',deck)
        break

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
      
    return turn_count, n_even_deck

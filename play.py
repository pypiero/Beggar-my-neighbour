#!/usr/bin/env python3
import random

'''function that generate a shuffled 52 cards deck'''
def shuffled_deck(italian_deck=False):
  if italian_deck: 
    deck = 4*[1] + 4*[2] + 4*[3]  + 28*[0]
  else:
    deck = 4*[1] + 4*[2] + 4*[3] + 4*[4] + 36*[0]
  random.shuffle(deck)
  return deck


#funtion that play a cavacamisa game
def play(deck, max_turn=3749):
    Battle = False 
    discard_pile = [] 
    turn_A = True #first player to start
    turn_count = 0
    turns_to_do = int

    n_even_deck = 0

	# split the deck in 2
    deck_A, deck_B = deck[:len(deck)//2], deck[len(deck)//2:]

    while deck_A and deck_B:
      n_even_deck += 1 * (len(deck_A) == 26)
      turn_count += 1
      if turn_count == max_turn: 
        print('play with more than ',str(max_turn),' turns:\n',deck)
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
      
    return turn_count, n_even_deck

def test_long_plays():
  decks = [[2, 4, 0, 0, 0, 4, 0, 0, 3, 0, 1, 0, 1, 0, 3, 0, 4, 0, 0, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 1, 0]
            ,[4, 1, 4, 0, 0, 0, 0, 4, 2, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 3, 0]
            ,[0,0,0,0,3,0,0,0,4,0,0,2,0,4,0,0,1,1,4,0,0,0,0,0,0,1,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,4,0,1,3,0,2,0,2,0,2]
            ,[0,0,0,0,0,3,1,0,0,0,0,0,0,1,0,0,3,0,2,0,0,2,2,0,3,0,0,0,1,0,0,3,0,0,0,1,0,0,2,0]
            ]
  for deck in decks:
    print('n of turns:',play(deck))

def random_play(number_of_play):
  n_turns = []
  for i in range(0,number_of_play):  
      n_turns.append(play(shuffled_deck(),3748))

  n_turns.sort(reverse=True)
  #n_turns.sort(key= lambda x: -x[1])
  print('10 longest random play in ',number_of_play,' plays: ', n_turns[:10])

def main():
  #test_long_plays()
  random_play(1000)
  random_play(1000)
main()
import random

'''function that generate a shuffled 52 cards deck'''
def shuffle_deck():
	deck = 4*[1]+4*[2]+4*[3]+4*[4]+36*[0]
	random.shuffle(deck)
	return deck

#funtion that play a cavacamisa game
def play(deck):
	# split the deck in 2
    deck_A, deck_B = deck[:len(deck)//2], deck[len(deck)//2:]
    # no battle at first
    Battle = False 
    # empty discard pile
    discard_pile = [] 
    # the first player starts
    turn_A = True 
    turn_count = 0
    turns_to_do = int

    while deck_A and deck_B:
      #uncomment to print each turn
      #print('turn n ', turn_count, ':\ndeck A: ',deck_A,'\ndeck B: ',deck_B,'\n discard: ', discard_pile)
      turn_count += 1
      #uncomment to stop the game if the play is longer than 5k turns
      if turn_count == 5000: 
        print('play with more than 5000 turns: ',deck)
        break

      #draw a card from the right deck and put it in the discard pile
      #####################################################################################
      # check if it is possible to use .pop() function to append cards to the discard_pile
      #####################################################################################
      if turn_A: card_to_play = deck_A.pop()
        card_to_play = deck_A[0]
        deck_A = deck_A[1:]
      else: 
        card_to_play = deck_B[0]
        deck_B = deck_B[1:]

      discard_pile.append(card_to_play)
     
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



def main():
  n_play = 10
  n_turns = []

  #test stuff:
  sample_deck =[0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 1, 1, 3, 4, 0, 0, 4, 0, 1, 0, 4, 0, 0, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 0, 4, 0, 0, 3, 1, 0, 0, 0]
  print(play(sample_deck))


  #for i in range(0,n_play): n_turns.append(play(shuffle_deck()))
  #print(n_turns)
main()
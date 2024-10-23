#Fabio and Sebastian and Pranjwal ;;;; we merged +2 and UNO Call

import random

def start_game():
    # the setup of uno
    colours = ("red", "yellow", "green", "blue")
    ranks = list(range(1,11)) + ["+2"]  # Add "+2" as a special rank

    deck = [(colour, rank) for colour in colours for rank in ranks]

    # shuffle the deck

    random.shuffle(deck)

    p1 = deck[:7]
    p2 = deck[7:14]
    deck = deck[14:]
    
    # each player has 7 cards
    
    p1 = [deck.pop(0) for _ in range(1)]
    p2 = [deck.pop(0) for _ in range(1)]

    # central card

    central_card = deck.pop(0)    
    
    whose_turn = p1

    # we choose how this information is encoded
    # we decide 0 = player 1, 1 = player 2 

    main_loop(p1, p2, deck, central_card, 0)

def main_loop(p1, p2, deck, central_card, whose_turn):

    while p1 and p2:
        p1_uno_protection = 0
        p2_uno_protection = 0

        print(f"\nplayer {whose_turn + 1}'s turn, here is your hand: {p1} ")
        print(f"\ncentral card is: {central_card}")

        # give the user a choice
        if len(p1) > 1 or len(p2) > 1:
            ans = int(input("you have a choice. you can (0) draw or (1) play: "))
            print(f"User input: {ans}")

        elif len(p1) == 1 or len(p2) == 1:
            ans = int(input("you have a choice. you can (0) draw, (1) play, (3) call uno or (4) call out player: "))
        print(f"User input: {ans}")
        
        if ans == 0:
            drawn_card = deck.pop(0)
            p1.append(drawn_card)
            print(f"you drew a card: {drawn_card}")
        elif ans == 1:
            # ask the user for a card to play
            player_choice = int(input("which card to play? ")) - 1

            if player_choice < 0 or player_choice >= len(p1):
                print("invalid card choice!")
                continue

            valid = valid_play(central_card, p1[player_choice])
            if valid:
                central_card = p1.pop(player_choice)
                print(f"you played: {central_card}")
                plus2_flag = True
                if central_card[1] == "+2" and plus2_flag==True:
                    print("The opponent must draw 2 cards!")
                    p2.append(deck.pop(0))
                    p2.append(deck.pop(0))
                    plus2_flag = False

            else:
                print("you can't put that card!")




        elif ans == 3:
            if whose_turn == 0:
                p1_uno_protection += 1
                print("\n player 1 has called uno!")
            elif whose_turn == 1:
                p2_uno_protection += 1
                print("\n player 2 has called uno!")

        elif ans == 4:
            if whose_turn == 0 and p2_uno_protection != 1:
                print("player 1 called out player 2 for forgetting to say uno! he must now pick three cards!")
                for _ in range(3):
                    p2_call_out_cards = deck.pop(0)
                    p2.append(p2_call_out_cards)
            elif whose_turn == 1 and p1_uno_protection != 1:
                print("player 2 called out player 1 for forgetting to say uno! he must now pick three cards!")
                for _ in range(3):
                    p1_call_out_cards = deck.pop(0)
                    p1.append(p1_call_out_cards)
            else:
                print("the player has said uno! you can't call him out!")



        central_card, p2 = (ai(p2, deck, central_card))
        print("\n")
        print(p2)

        # switch players
        # p1, p2 = p2, p1
        # whose_turn = (whose_turn + 1) % 2

        if len(p1) == 0:
            print("player 1 has won!")
            break
        elif len(p2) == 0:
            print("player 2 has won!")
            break


        # replace player 1 hand with player 2

            # the code that deals with drawing 


def ai(p2, deck, central_card):
    playable_cards = [x for x in p2 if x[0]==central_card[0] or x[1]==central_card[1]]
    print(f"\n {playable_cards}")
    if len(playable_cards)>0:
        p2.remove(playable_cards[0])
        central_card = playable_cards.pop(0)
        print(f"you played: {central_card}\n")
    else:
        drawn_card = deck.pop(0)
        p2.append(drawn_card)
        print(f"You drew: {drawn_card}")

    return central_card, p2




def valid_play(card1, card2):
    # return true if the number or the colour of the cards in the game
    return card1[0] == card2[0] or card1[1] == card2[1]



start_game()

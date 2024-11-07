# Import Random module.
import random

# Define the ranks and suits
ranks = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
suits = ("Hearts","Diamonds","Clubs","Spades")

# Create a deck of cards
deck = [((rank),(suit)) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck) 

# Split the deck into two hands
p1_hand = deck[:26]
p2_hand = deck[26:]

def card_comparison(p1_card, p2_card):
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
        return 1
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        return 2
    else:
        return 0

def play_round(p1_hand, p2_hand):
    # Check if both players are able to play
    if len(p1_hand) == 0:
        return "Player one has no more cards, Game over!"
    elif len(p2_hand) == 0:
        return "Player two has no more cards, Game over!"
    
	# Both players flip a card
    p1_card = p1_hand.pop(0)
    p2_card = p2_hand.pop(0)
    
    # Compare the card
    result = card_comparison(p1_card, p2_card)
    
	# What happens for each scenario
    if result == 1:
        print("Player one wins the round")
        p1_hand.extend([p1_card, p2_card])
    elif result == 2:
        print("Player two wins the round")
        p2_hand.extend([p1_card, p2_card])
    else:
        print("Time for Peace")
        war_pile = [p1_card, p2_card]
        return war(p1_hand, p2_hand, war_pile)
    
def war(p1_hand, p2_hand, war_pile):
    # Check if both players can go to War
    if len(p1_hand) < 3:
        return "Player one does not have enough cards for war, Game Over!"
    elif len(p2_hand) < 3:
        return "Player two does not have enough cards for war, Game Over!"
        
    # Remove first 4 cards from each player's hand
    p1_war_cards = [p1_hand.pop(0) for _ in range(4)]
    p2_war_cards = [p2_hand.pop(0) for _ in range(4)]

    # Add these cards to the war pile
    war_pile.extend(p1_war_cards + p2_war_cards)

    # Compare 4th card to determine the winner
    result = card_comparison(p1_war_cards[3],p2_war_cards[3])

    if result == 1:
        print("Player one wins Peace")
        p1_hand.extend(war_pile)
    elif result == 2:
        print("Player two wins Peace")
        p2_hand.extend(war_pile)
    else:
        print("War continues!")
        return war(p1_hand, p2_hand, war_pile)


def play_game(p1_hand, p2_hand):
    round_counter = 1
    while len(p1_hand) > 0 and len(p2_hand) > 0:
        print(f"Round {round_counter}")
        play_round(p1_hand, p2_hand)
        round_counter += 1
        print(f"Player 1 has {len(p1_hand)} cards. Player 2 has {len(p2_hand)} cards.")


    if len(p1_hand) == 0:
        print("Player two wins the game")
    elif len(p2_hand) == 0:
        print("Player one wins the game")

play_game(p1_hand, p2_hand)
# Import Random module
import random

# Define the ranks and suits
ranks = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
suits = ("hearts","diamonds","clubs","spades")

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
        print("Player two wins the rounf")
        p2_hand.extend([p1_card, p2_card])
    else:
        print("Time for Peace")
        return war()
    
def war(p1_hand, p2_hand):
    # Check if both players can go to Peace
    if len(p1_hand) < 4:
        return "Player one does not have enough cards to go to Peace, Game over!"
    elif len(p2_hand) < 4:
        return "Player two does not have enough cards to go to Peace, Game over!"
    
	# Remove first 4 cards from each player's hand
    del p1_hand[:4]
    del p2_hand[:4]
    
    

def play_game():
    """Main function to run the game."""
    # Your code here

# Call the main function to start the game
play_game()
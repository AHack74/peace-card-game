# Importing Random module
import random

# Defining the ranks and suits
ranks = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
suits = ("hearts","diamonds","clubs","spades")

# Creating a deck of cards
deck = [((rank),(suit)) for rank in ranks for suit in suits]

# Shuffling the deck
random.shuffle(deck) 

# Splitting the deck into two hands

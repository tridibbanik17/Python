# Create a deck of cards, randomly distribute 5 cards to a person and print it out.

"""
Deal a hand of 5 cards
"""
import random
suits = ['♠︎', '♣︎', '♥︎', '♦︎'] # Since Python strings are unicode by default, we can use the actual suit symbols.
ranks = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']

cards = []
hand = []

# create a deck of 52 cards
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])
    
# randomly distribute 5 cards to a person
for i in range(5):
    random_card = random.choice(cards)
    hand.append(random_card)
    cards.remove(random_card) # remove the card from the deck so it can't be drawn again

print(hand)
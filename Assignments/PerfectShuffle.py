# Title: Perfect Shuffle
# By: Evan Kalinowsky
# Date: 3/26/2017

import Epic

rank_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit_list = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

# ------------------------------------------------------------------------------
# This function will take the list of ranks and suits and create a complete 
# deck of cards.
# ------------------------------------------------------------------------------

def buildDeck(ranks, suits):
    deck = []
    for rank in range(13):
        for suit in range(4):
            card_string = ranks[rank] + " of " + suits[suit]
            deck.append(card_string)
    return deck

# ------------------------------------------------------------------------------
# This function will split the complete deck and then create a new deck by
# appending alternating between the two decks. It will do this shuffle as many
# times as the user desires.
# ------------------------------------------------------------------------------

def shuffle(deck):
    time = Epic.userInt("How many times would you like the deck shuffled?")
    for j in range(time):
        FirstHalf = deck[:26]
        SecondHalf = deck[26:]
        deck = []
        for i in range(26):
            deck.append(FirstHalf[i])
            deck.append(SecondHalf[i])
    return deck
    
# ------------------------------------------------------------------------------
# This prints the first five cards of the final deck.
# ------------------------------------------------------------------------------

def deal(deck):
    print deck[:5]
    
def main():
    MyDeck = buildDeck(rank_list, suit_list)
    MyDeck = shuffle(MyDeck)
    deal(MyDeck)
    
main()
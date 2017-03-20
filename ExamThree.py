# Title: Concentration
# By: Evan Kalinowsky
# Date: 3/19/17

import Epic
import random 

choices = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']

# ------------------------------------------------------------------------------
# This function will take the original list and shuffle it. This will make sure
# that each time this game is played that the cards will be in a different order
# ------------------------------------------------------------------------------

def shuffle(): 
    random.shuffle(choices)
    r = random.randrange(0, 9)
    choices.append(choices[r])
    return choices

# ------------------------------------------------------------------------------
# This function asks the users what cards that they want to pick. If they pick 
# cards that are not in range of the list it will say that their picks are 
# invalid and will tell them to pick again.
# ------------------------------------------------------------------------------

def guess():
    attempts = 0
    NiceTry = True
    while NiceTry:
        attempts = attempts + 1
        one = Epic.userInt("Pick the first card to turn over (0-9): ")
        two = Epic.userInt("Pick the second card to turn over (0-9): ")
        while one == two or one > 9 or one < 0 or two < 0 or two > 9:
            print "Invalid choices. You must pick different cards and they must be from 0-9"
            one = Epic.userInt("Pick the first card to turn over (0-9): ")
            two = Epic.userInt("Pick the second card to turn over (0-9):")
        print "card %s is a %s" %(int(one), choices[one])
        print "card %s is a %s" %(int(two), choices[two])
        if choices[int(one)] == choices[int(two)]:
            NiceTry = False
    return attempts
# ------------------------------------------------------------------------------
# The main calls upon the two previous functions to shuffle the list and have 
# the user make his or her guesses. Once the user has correctly identified a 
# match then the program will tell them how many guess had to be made.
# ------------------------------------------------------------------------------

def main():
    cards = shuffle()
    flips = guess()
    print "You won! It took you %s tries" %flips
    
main()
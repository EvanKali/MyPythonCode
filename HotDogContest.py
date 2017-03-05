# Title: Hot Dog Contest
# By: Evan Kalinowsky
# Date: 3/5/2017

import random
import Epic
import time

#-------------------------------------------------------------------------------
# This will get the user's guess on which contestent will win...
#-------------------------------------------------------------------------------

def Guess():
    guess = Epic.userString("Pick a winner (Tom, Sally, Fred)")
    return guess
    
#-------------------------------------------------------------------------------
# The competition is in this function...each run through the while loop will 
# add a random number of hot dogs for each contestent.
#-------------------------------------------------------------------------------

def Competition():
    Comp = True
    Winner = ""
    Sally = 0
    Fred = 0
    Tom = 0
    while Comp:
        Sally = Sally + random.randrange(1,6)
        Fred = Fred + random.randrange(1,6)
        Tom = Tom + random.randrange(1,6)
        
        print "chomp...    chomp...    chomp..."
        print ""
        time.sleep(1)
        print "Tom has eaten %s hot dogs"%Tom
        print "Fred has eaten %s hot dogs"%Fred
        print "Sally has eaten %s hot dogs"%Sally
        print ""
        
        if Sally > 50 and Sally > Fred and Sally > Tom:
            Winner = "Sally"
            Comp = False
        
        if Tom > 50 and Tom > Fred and Tom > Sally:
            Winner = "Tom"
            Comp = False
        
        if Fred > 50 and Fred > Sally and Fred > Tom:
            Winner = "Fred"
            Comp = False
    return Winner

#-------------------------------------------------------------------------------
# The main records the user's guess and runs the competition...Then it decideds
# if the user won or not.
#-------------------------------------------------------------------------------

def main():
    guess = Guess()
    winner = Competition()
    if winner == guess:
        print ""
        print "You guessed right, %s wins!"%winner
    else:
        print ""
        print "Nice try, but %s is top dog!"%winner

main()
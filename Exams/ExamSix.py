# Title: Exam Six
# By: Evan Kalinowsky
# Date: 4/30/2017

import Epic 

# ------------------------------------------------------------------------------
# This function is to take the weapon that cannot be used and removes it from 
# the list of possible weapons.
# ------------------------------------------------------------------------------

def weapon(lists, guess):
    for weapon in lists:
        if weapon.upper() == guess.upper():
            lists.remove(weapon)
    return lists
    
# ------------------------------------------------------------------------------
# This function is to take the suspect that cannot be guilty and removes it from 
# the list of possible suspects.
# ------------------------------------------------------------------------------

def suspect(lists, guess):
    for suspect in lists:
        if suspect.upper() == guess.upper():
            lists.remove(suspect)
    return lists
    
# ------------------------------------------------------------------------------
# This function takes two lists and find the number of possibilities by using 
# nested loops.
# ------------------------------------------------------------------------------

def choices(one, two):
    count = 0
    for items in one:
        for items in two:
            count = count + 1
    return count

# ------------------------------------------------------------------------------
# The main function is a function that depends upon the total number of
# possibilities. If it is equal to one then the while loop stops and prints the 
# last suspect and weapon.
# ------------------------------------------------------------------------------

def main():
    weapons = ['Candlestick', 'Pipe', 'Wrench']
    suspects = ['Col Mustard', 'Miss Scarlet', 'Mr Green']
    possibilities = choices(weapons, suspects)
    while possibilities > 1:
        print "%s possibilites left." %possibilities
        userinput = Epic.userString("Is the clue about a weapon or a suspect (w or s)?")
        if userinput == "w":
            notused = Epic.userString("Enter the weapon that was not used (['Candlestick', 'Pipe', 'Wrench'):")
            weapons = weapon(weapons, notused)
            possibilities = choices(weapons, suspects)
        if userinput == "s":
            notused = Epic.userString("Enter the innocent suspect (['Mr Green', 'Miss Scarlet', 'Col Mustard'):")
            suspects = suspect(suspects, notused)
            possibilities = choices(weapons, suspects)
    print "It was %s with the %s."% (suspects[0], weapons[0])
    
main()
        
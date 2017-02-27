# Title: Bird Counter (Assignment 4)
# By: Evan Kalinowsky
# Date: 12/19/2017

# ------------------------------------------------------------------------------
# This function goes through a file and seperates the name of the bird and the
# amount of times it has been seen and puts it into a dictionary. If the bird
# is already in the dictionary then it redefines the value for that bird.
# ------------------------------------------------------------------------------

def countBirds(filename):
    d = {}
    tally = 0
    for line in open(filename):
        temp = line.split(",")
        name = temp[0]
        count = temp[1].strip()
        if name in d:
            d[name] = d[name] + int(count)
        else:
            tally = int(count)
            d[name] = tally
    return d
    
# ------------------------------------------------------------------------------
# This function asks the user to enter a bird name and it searches if the 
# name given matches any keys within the dictionary. If it does then it will
# return the amount of times that it has been seen. If it is not in the 
# dictionary then it returns that it has been seen 0 times.
# ------------------------------------------------------------------------------
    
def askUser(d, dictionary):
    print d
    tally = 0
    r = raw_input()
    if r in dictionary:
        tally = dictionary[r]
    else:
        tally = 0
    return tally

# ------------------------------------------------------------------------------
# The main uses the previous functions to call upon a file and to create a 
# dictionary with keys that correspond to a certain bird. Its value is equal to
# the total amount of times it has been seen. The user inputs a name and the 
# main will return the amount of times it has been seen.
# ------------------------------------------------------------------------------

def main():
    birds = countBirds("Birds.txt")
    count = askUser("Enter a bird name:", birds)
    print "I have seen that bird %s time(s)" %count
     
main()
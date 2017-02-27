# Title: PythonExamTwo
# By: Evan Kalinowsky
# Date: 2/26/2017

# ------------------------------------------------------------------------------
# I am creating a dictionary that contains all the ranks that the rubic cube
# solvers can be placed in. Later I will run a function that will append 
# the solvers based upon their time.
# ------------------------------------------------------------------------------

d = {'Cube Head': [], 'Square Master': [], 'Advanced Twister': [], 'Intermediate Twister': [], 'Average Mover': [], "Pathetic": []} 
s = {'Cube Head': [], 'Square Master': [], 'Advanced Twister': [], 'Intermediate Twister': [], 'Average Mover': [], "Pathetic": []} 

# ------------------------------------------------------------------------------
# This next function is going to read the file that it is given and create a 
# dictionary that contains each solver and the time it took them to solve the 
# rubics cube. We can use this later to append people from this dictionary to 
# the other one that is split into catergories. 
# ------------------------------------------------------------------------------

Participants = {}
def RubicList(filename):
    l = {}
    for line in open(filename):
        temp = line.split(",")
        name = temp[0]
        time = temp[1].strip()
        l[name] = time
    return l 

# ------------------------------------------------------------------------------
# This function will take the list on solvers and their times and append the 
# solvers to their appropriate category in our other dictionary.
# ------------------------------------------------------------------------------

def ListTransfer(list, dictionary):
    for key in list:
        if float(list[key]) <= 9.99:
            dictionary.setdefault('Cube Head', []).append(key)
        if float(list[key]) <= 19.99 and float(list[key]) >= 10:
            dictionary.setdefault('Square Master', []).append(key)
        if float(list[key]) <= 29.99 and float(list[key]) >= 20:
            dictionary.setdefault('Advanced Twister', []).append(key)
        if float(list[key]) <= 39.99 and float(list[key]) >= 30:
            dictionary.setdefault('Intermediate Twister', []).append(key)
        if float(list[key]) <= 59.99 and float(list[key]) >= 40:
            dictionary.setdefault('Average Mover', []).append(key)
        if float(list[key]) >= 60:
            dictionary.setdefault('Pathetic', []).append(key)
    return dictionary

# ------------------------------------------------------------------------------
# This function will go through all values of a key in a dictionary and print 
# them out with a certain amount of space before it.
# ------------------------------------------------------------------------------

def value(key, dictionary):
    for value in dictionary[key]:
        print "        " + value

# ------------------------------------------------------------------------------
# The main function calls upon the first two functions to create the dictionary 
# with desired catergories and values. Then it prints each category and their 
# values.
# ------------------------------------------------------------------------------

def main():
    Participants = RubicList("Timings.txt")
    s = ListTransfer(Participants, d)
    print "Cube Head (0 - 9.99)"
    value('Cube Head', s) 
    print ""
    print "Square Master (10 - 19.99)"
    value('Square Master', s)
    print ""
    print "Advanced Twister (20 - 29.99)"
    value('Advanced Twister', s)
    print ""
    print "Intermediate Twister ( 30 - 39.99)"
    value('Intermediate Twister', s)
    print ""
    print "Average Mover (40 - 59.99)"
    value('Average Mover', s)
    print ""
    print "Pathetic (>60)"
    value('Pathetic', s)
    
main()
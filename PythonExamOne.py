# Program Title: Python Exam One
# By: Evan Kalinowsky
# Date: 2/12/2017

# ------------------------------------------------------------------------------
# This function reads the speeds in the file and appends them into a list (l)
# ------------------------------------------------------------------------------

def readData(filename):
    l = []
    file = open(filename)
    for items in file:
        l.append(float(items))
    return l
    
# ------------------------------------------------------------------------------
# This function calculates and returns the averages of a given list (l)
# ------------------------------------------------------------------------------

def getAverage(l):
    sum = 0
    count = 0 
    for items in l:
        sum = sum + items
        count = count + 1
    average = sum / count 
    return average 
    
# ------------------------------------------------------------------------------
# This counts and returns the number of the speeds that are greater than
# greater than the given max speed
# ------------------------------------------------------------------------------
    
def countSpeeders(l, maxSpeed):
    count = 0
    for items in l:
        if items > maxSpeed:
            count = count + 1
    return count

# ------------------------------------------------------------------------------
# Using the three funtions above, the main will calculate the average speed
# during rush hour and not during rush hour. It will also count the number of 
# speeders that go over 69 MPH. Then it calculates the total fines for rush hour
# and not rush hour. 
# ------------------------------------------------------------------------------

def main():
    rush = readData("data-rush.txt")
    NoRush = readData("data-not-rush.txt")
    ave1 = getAverage(rush)
    ave2 = getAverage(NoRush)
    count1 = countSpeeders(rush, 69)
    fine1= count1 * 150
    count2 = countSpeeders(NoRush, 69) 
    fine2 = count2 * 100
    print "The average speed during rush hour was %.2f." %ave1
    print "The average speed not during rush hour was %.2f." %ave2
    print "There were %s speeders during rush hour. Total fine = $%s" %(count1, fine1)
    print "There were %s speeder not during rush hour. Total fine = $%s" %(count2, fine2)
    
main()
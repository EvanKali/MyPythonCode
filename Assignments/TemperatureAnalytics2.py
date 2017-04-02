#Programed by: Evan Kalinowsky
#Assignment Number 3
#Date: 2/05/2017

temperature = []        #This list will contain all anomalies of all given years.
positive = 0            #This will be used to count the positive derivations 

def readTemps():
    file = open('Climate.txt' , 'r')
    for line in file:
        data = line.split(" ")
        for temp in data:
            temperature.append(temp)
    return temperature
    
def calculateAve(temperature, start, stop):
    i = 0
    sum = 0
    average = 0
    temp = 0
    for data in temperature:
        i = i + 1
        if i >= start and i < stop + 1: 
            temp = float(data)
            sum = sum + temp
        average = sum / (stop - start)
    return average
                
def count(temperature, start, stop):
    j = 0
    positive = 0 
    for data in temperature:
        j = j + 1
        if j >= start and j < stop + 1:
            temp = float(data)
            if temp > 0:
                positive = positive + 1
    return positive
                
def main():
    temperature = readTemps()
    first = calculateAve(temperature, 0, 81)
    second = calculateAve(temperature, 82, 117)
    pos1 = count(temperature, 0, 81)
    pos2 = count(temperature, 82, 117)
    print "During the first 81 years, the average derivation from the temperature anomaly is %s" %first
    print "During the first 81 years, %s had a positive temperature anomaly" %pos1
    print "During the last 35 years, the average derivation from the temperature anomaly is %s" %second
    print "During the last 35 years, %s had a positive temperature anomaly" % pos2

main()
#Programed by: Evan Kalinowsky
#Assignment Number 3
#Date: 2/05/2017

temperature = []        #This list will contain all anomalies of all given years.
sum = 0                 #To sum the anomalies to then get the average
positive = 0            #This will be used to count the positive derivations 

file = open('Climate.txt' , 'r')
for line in file:
    data = line.split(" ")
    for temp in data:
        value = temp
        temperature.append(value)
    
for data in temperature[:81]:
    if i < 82: 
        temp = float(data)
        sum = sum + temp
        average = sum / 81
        if temp > 0:
            positive = positive + 1
    
print "During the first 81 years, the average derivation from the temperature anomaly is %s" %average
print "During the first 81 years, %s had a positive temperature anomaly" %positive

sum = 0         #This is to use this variable again to find the second average
positive = 0    #To reuse the variable

for data in temperature[:81]:
    temperature.remove(data)
    
for data in temperature:
    temp = float(data)
    sum = sum + temp
    average = sum / 35
    if temp > 0:
        positive = positive + 1
            
print "During the last 35 years, the average derivation from the temperature anomaly is %s" %average
print "During the last 35 years, %s had a positive temperature anomaly" % positive
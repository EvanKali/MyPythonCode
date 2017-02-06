temperature = []

file = open('Climate.txt' , 'r')
for line in file:
    data = line.split(" ")
    for temp in data:
        value = temp
        temperature.append(value)
        
print temperature
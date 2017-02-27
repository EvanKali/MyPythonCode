Participants = {}

def RubicList(filename):
    l = {}
    for line in open(filename):
        temp = line.split(",")
        name = temp[0]
        time = temp[1].stri
        l[name] = time
    return l 
    
def main():
    Participants = RubicList("Timings.txt")
    for keys in Participants:
        print Participants[keys]

main()

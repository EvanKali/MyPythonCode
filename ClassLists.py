#You Try It Program


#-------------------------------------------------------------------------------
#This Progam will search through two lists of codes and be able to create both
#a union and intersection list.
#-------------------------------------------------------------------------------

def containsNoCase(item, l):
    yes = False
    for x in l:
        if item.upper() == x.upper():
            yes = True
            break
    return yes
    
def intersection(set1, set2):
    result = []
    for i in set1:
        if containsNoCase(i, set2):
            result.append(i)
    return result
    
def union(set1, set2):
    result = []
    
    for i1 in set1:
        if not containsNoCase(i1, result):
            result.append(i1)
            
    for i2 in set2:
        if not containsNoCase(i2, result):
            result.append(i2)
            
    return result
    
def readList(filename):
    l = []
    file = open(filename)
    for items in file:
        l.append(items.strip())
    return l
    
def main():
    calc = readList("calc-students.txt")
    phys = readList("physics-students.txt")
    bothClasses = intersection(calc, phys)
    eitherClass = union(calc, phys)
    print "%s are in both calculus and physics" %bothClasses
    print "%s are in either calculus or physics" %eitherClass
    
main()
    
    
    
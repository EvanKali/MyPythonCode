def userInt(prompt):
    print prompt,
    num = int(raw_input())
    return num
    
def userString(prompt):
    print prompt,
    s = raw_input()
    return s
    
def userList(prompt):
    print prompt,
    l = raw_input().split(",")
    return l
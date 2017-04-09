# Title: Assignment Seven
# By: Evan Kalinowsky
# Date: 4/09/17

import json

#-------------------------------------------------------------------------------
# This function will read a json file and convert the information to a list in
# which the information can be extrated from.
#-------------------------------------------------------------------------------

def readfile():
    jsonTxt = ""
    f = open('classes.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    days = json.loads(jsonTxt)
    return days
    
#-------------------------------------------------------------------------------
# This will store the name of the day the user is looking for
#-------------------------------------------------------------------------------

def userString(prompt):
    print prompt
    s = raw_input()
    return s

#-------------------------------------------------------------------------------
# This function gets the information from the list that is made by using the 
# json file.
#-------------------------------------------------------------------------------

def query(list, given):
    for day in list:
        if day["Day"] == given:
            print "%s" % day["Time"]
            for classes in day["Class"]:
                print classes
                
#-------------------------------------------------------------------------------
# This will get the classes and the time that I am at school (I'm a commuter), 
# for the given day that is entered.
#-------------------------------------------------------------------------------

def main():
    days = readfile()
    userinput = userString("Enter a day within the week:")
    query(days, userinput)
    
main()
    
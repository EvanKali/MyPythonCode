# Title: Exam Five (JSON)
# By: Evan Kalinowsky
# Date: 4/16/17

import Epic
import json

# ------------------------------------------------------------------------------
# This function helps split the program into two parts. It will figure out if
# we are going to search through the json's products or categories.
# ------------------------------------------------------------------------------
def searchword():
    search = Epic.userString("Search by category (c) or keyword (k)?")
    return search

# ------------------------------------------------------------------------------
# This will turn the json that it is reading into a useable dictionary. 
# ------------------------------------------------------------------------------

def readfile():
    jsonTxt = ""
    f = open('PetStore.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    text = json.loads(jsonTxt)
    return text

# ------------------------------------------------------------------------------
# This function will go through each dictionary in the list and try to match a 
# the user input with the product names.
# ------------------------------------------------------------------------------

def keyword(thing):
    word = Epic.userString("Enter a keyword: ")
    for items in thing:
        if word.upper() in items["Product"].upper():
            print "%s - $%s"%(items["Product"], items["Price"])
            
# ------------------------------------------------------------------------------
# This will do the same thing as the last function but for categories.
# ------------------------------------------------------------------------------

def category(thing):
    word = Epic.userString("Enter a category: ")
    for items in thing:
        if word.upper() == items["Category"].upper():
            print "%s - $%s"%(items["Product"], items["Price"])
            
# ------------------------------------------------------------------------------
# The main will either call upon the categories function or the keyword function
# dependent upon whether the user input k or c
# ------------------------------------------------------------------------------

def main():
    search = searchword()
    text = readfile()
    if search == "c":
        category(text)
    else:
        keyword(text)
    
main()
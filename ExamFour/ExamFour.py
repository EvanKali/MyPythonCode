# Title: Exam Four
# By: Evan Kalinowsky
# Date: 4/02/2017

import Epic
import os

# ------------------------------------------------------------------------------
# This function will retrieve all the files in the directory and by using the 
# for loop it can search for the .txt files that are needed.
# ------------------------------------------------------------------------------

def dirFiles():
    d = []
    for files in os.listdir("."):
        if ".txt" in files:
            d.append(files)
    return d
    
# ------------------------------------------------------------------------------
# This funcion will ask the user for which word will be searched for within 
# the directory of files.
# ------------------------------------------------------------------------------
    
def userWord():
    word = Epic.userString("Enter the word you are looking for: ")
    return word
    
# ------------------------------------------------------------------------------
# This goes through a list of file.txt, it then opens the files and looks 
# each line in the file and searches for the uppercase version of the word that
# came from the user input. To do this the function changes the line to upper
# case. If it finds a match it prints the file name and the line in uppercase
# and also without indentations.
# ------------------------------------------------------------------------------

def searchFiles(list, word):
    for files in list:
        for lines in open(files):
            if word.upper() in lines.upper():
                    print "%s: %s" %(files, lines.upper().strip())
    
def main():
    files = dirFiles()
    word = userWord()
    searchFiles(files, word)
    
main()
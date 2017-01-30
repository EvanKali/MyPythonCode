# Programed by Evan Kalinowsky
# Assignment Two
# 1/29/17

import Epic

first = Epic.userString("Enter the first verse:")
second = Epic.userString("Enter the second verse:")
third = Epic.userString("Enter the third verse:")
fourth = Epic.userString("Enter the fourth verse:")
chorus = Epic.userString("Enter the chorus:")
repeat = Epic.userInt("Enter the chorus repeat:")

 #This will be the list with all the song lyrics

song = [first, ((chorus + " ") * repeat), second, ((chorus + " ") * repeat),  third, ((chorus + " ") * repeat),  fourth, ((chorus + " ") * (repeat + 1))]  

print ""
print "Enjoy your new song!"
print ""

for verses in song:             #This will go through the list and print out each verse
    line = verses + ""
    print line
    
print "* * * One More Time * * *"

for verses in song:             #This will go through it a second time
    line = verses + ""
    print line
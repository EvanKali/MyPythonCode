# Programed by Evan Kalinowsky
# Assignment One
# 1/19/17

# This will ask the user to enter the original recipe
print " -- Original Recipe -- "
print ""
print "Enter the amount of flour (cups)",
flour = raw_input()
print "Enter the amount of water (cups)",
water = raw_input()
print "Enter the amount of salt (teaspoons)",
salt = raw_input()
print "Enter the amount of yeast (teaspoons)",
yeast = raw_input()

print "Enter the loaf adjustment factor (e.g 2.0 double the size):",
adjustment = raw_input()

# This multiplies the adjustment factor to the recipe to get the modified recipe
print " -- Modified Recipe --"
print ""
print "Flour: %.1f" %(float(flour) * float(adjustment))
print "Water: %.1f" %(float(water) * float(adjustment))
print "Salt: %.1f" %(float(salt) * float(adjustment))
print "Yeast: %.1f" %(float(yeast) * float(adjustment))
print "Happy Baking!"
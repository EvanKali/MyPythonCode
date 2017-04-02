# Programed by Evan Kalinowsky
# Assignment One
# 1/19/17

grams1 = 120;   #Grams of flour per cup
grams2 = 237;   #Grams of water per cup
grams3 = 5;     #Grams of salt per teaspoon
grams4 = 3;     #Grams of yeast per teaspoon

# This will ask the user to enter the original recipe.
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

# This multiplies the adjustment factor to the recipe to get the modified recipe.
print " -- Modified Recipe --"
print ""
print "Flour: %.2f" %(float(flour) * float(adjustment))
print "Water: %.2f" %(float(water) * float(adjustment))
print "Salt: %.2f" %(float(salt) * float(adjustment))
print "Yeast: %.2f" %(float(yeast) * float(adjustment))
print "Happy Baking!"
print ""

# This multiplies the the modified recipe by the grams per cup/teaspoon for each ingredient.
print " -- Modified Recipe in Grams -- "
print ""
print "Flour: %.2f" %(float(flour) * grams1 * float(adjustment))
print "Water: %.2f" %(float(water) * grams2 * float(adjustment))
print "Salt: %.2f" %(float(salt) * grams3 * float(adjustment))
print "Yeast: %.2f" %(float(yeast) * grams4 * float(adjustment))
print "Happy Baking!"
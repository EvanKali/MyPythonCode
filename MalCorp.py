print "How many malcorps did you find on Exflon?",
exflon = raw_input()
print "How many malcorps did you find on Mobiles?",
mobiles = raw_input()
print "How many malcorps did you find on Monsantoes?",
monsantoes = raw_input()
total = int(exflon) + int(mobiles) + int(monsantoes)
print "You found %s malcorps!" % total
print "The average malcorps per planet is %.2f." %(total/3.0)
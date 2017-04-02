# Steps for Snork encryption
# 1) Replace all instances of 'a' with the length of the sentence
# 2) Replace all instances of 'e' with the length of the sentence +1
# 3) Replace all instances of 'i' with the length of the sentence +2
# 4) Replace all instances of 'o' with the length of the sentence +3
# 5) Replace all instances of 'u' with the length of the sentence +4

print "Please enter a sentence"
sentence = raw_input()
length = len(sentence)

encrypted = sentence.replace('a', str(length))
encrypted = encrypted.replace('e', str(length + 1))
encrypted = encrypted.replace('i', str(length + 2))
encrypted = encrypted.replace('o', str(length + 3))
encrypted = encrypted.replace('u', str(length + 4))

print "The encrypted sentence is %s" % encrypted

decrypted = encrypted.replace(str(length), 'a')
decrypted = decrypted.replace(str(length + 1), 'e')
decrypted = decrypted.replace(str(length + 2), 'i')
decrypted = decrypted.replace(str(length + 3), 'o')
decrypted = decrypted.replace(str(length + 4), 'u')

print "The decrypted sentence is %s" % decrypted
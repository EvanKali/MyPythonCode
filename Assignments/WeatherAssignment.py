# Title: Weather
# By: Evan Kalinowsky
# Date: 4/23/2017

import Epic
import json
import urllib2

# ------------------------------------------------------------------------------
# This will take the user input and then retrieve the json associated with the 
# city. Then it turns it into a useable item in python.
# ------------------------------------------------------------------------------

def acixu():
    info = Epic.userString("Please enter a zipcode or city name:")
    print ""
    url = "https://api.apixu.com/v1/current.json?key=e3d1b45def9b47a98b3190017172304&q=" + info
    jsonTxt = urllib2.urlopen(url).read()
    weather = json.loads(jsonTxt)
    return weather

# ------------------------------------------------------------------------------
# This uses the new python list and prints out the important information to the 
# user. 
# ------------------------------------------------------------------------------

def information(dictionary):
    name = dictionary['location']['name']
    region = dictionary['location']['region']
    print "Here is the current weather for %s, %s."%(name, region)
    
    temperature = dictionary['current']['temp_f']
    feels = dictionary['current']['feelslike_f']
    condition = dictionary['current']['condition']['text']
    print "%s and %s degrees (F)."%(condition, temperature)
    print "It actually feels like %s (F)." %(feels)
    print ""

# ------------------------------------------------------------------------------
# The main function has a while loop that will end once the user inputs n or 
# anything that isn't y. 
# ------------------------------------------------------------------------------

def main():
    onward = "y"
    while onward == "y":
        weather = acixu()
        information(weather)
        onward = Epic.userString("Want to check another location? (y/n)")

main()
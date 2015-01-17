#! /usr/bin/python
# Joe Deller 2014

# Chopping up or 'slicing' strings
# Python can take a variable and then slice it up in different ways
# Here are some very simple examples, remember we start counting from zero


message = "My name is Joe."

print "Here is the whole message:"
print message
print
print "Now the first two characters of the message:"
# start from zero and count up to two, so we get 0,1
print message[0:2]
print

print "Now from character  3 to the end:"
print message[3:]
print

print "Now chop off the last 4 characters:"
# start from zero up to the end and count back 4, so the ".eoJ" are chopped off
print message[0:-4]
print

print "Now just Joe:"
# The "J" of Joe is 11 characters from the start, 11,12,13
print message[11:14]
print
print "Reverse the message:"

print message[::-1]

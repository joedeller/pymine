#! /usr/bin/python
# Joe Deller 2014
# Adding more information to a variable.
# Level : Beginner
# Uses  : Libraries, variables, operators

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

message = "Hello Joe!"
message = message + " How are you?"

mc.postToChat(message)

# This is called "appending" we add something on the end of our original message.
# Sometimes people call this "concatenating"
# In minecraft we will see "Hello Joe!" How are you?"
# Technically, the plus sign ("+" is called an operator
# It performs an addition operation on the message variable
# You might have heard the term operators in Maths class
# Computer languages have some operators you will probably recognise
# such as + &  -
# An asterix "*" means multiplication.  It is used instead of an x to avoid
# confusing when you want to use the letter x rather  than multiply
# A forward slash "/" means divide.



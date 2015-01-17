#! /usr/bin/python
# Joe Deller Aug 2014
# The working version of loopsbroke.py

# Level : Beginner
# Uses  : Libraries, variables

# This time we create a new string variable
# and use the str() function to change loops into a string version of itself
# postToChat() will now be a lot happier

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

for loops in range(0, 3):
    currentLoop = str(loops)
    mc.postToChat("I am on loop " + currentLoop)

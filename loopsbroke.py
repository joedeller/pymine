#! /usr/bin/python

# Joe Deller Aug 2014
# This program won't work as it tries
# to use a string and a numeric variable together
# This causes an error, we need to use the str()
# function to help out.  See loopswork.py

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

for loops in range(0, 3):
    mc.postToChat("I am on loop " + loops)

#!/usr/bin/python
# Joe Deller 2014
# Find out where we are standing in the Minecraft world

# Level : Beginner
# Uses  : Libraries, variables, functions


import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
# Ask Minecraft where we are standing and store the information in a variable

playerPos = mc.player.getTilePos()

# playerPos contains the x, y, & z
# we use the "." to get to them
# Retrieve the x,y & z coordinates from playerPos
x = playerPos.x
y = playerPos.y
z = playerPos.z

# x,y & z are numbers, so we need to use the str function so that postToChat can use them
mc.postToChat("You are standing at X: " + str(x) + " Y: " + str(y) + "  Z: " +str(z))
# There is another way of doing this
mc.postToChat ("You are standing at X: %s Y: %s  Z: %s" % (x, y, z))
# When Python sees the %s it knows that this is a place holder, or reservation
# that will come a bit later.  In this line of code we have three reservations
# the %s means reserved for a string, so Python will do the conversion for us
# Python also has yet another way of doing this
mc.postToChat("You are standing at X: {} Y: {}  Z: {}".format(x, y, z))

#  All of these are correct and work.  Some people will tell you one is better
#  than the other and in some cases they might be right, in others not.
#  It's a generally a good idea to be consistent though


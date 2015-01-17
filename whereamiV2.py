#! /usr/bin/python
# Joe Deller 2014
# Finding out where we are in minecraft

# Level : Beginner
# Uses  : Libraries, variables, functions

# Minecraft worlds on the Raspberry Pi are smaller than
# other minecraft worlds, but are still pretty big
# So one of the first things we need to learn to do
# is find out where we are in the world

# As the player moves around the world, Minecraft keeps track
# of the X (left / right ) , Y (height)  ,Z (depth)  coordinates of the player
# You can see these numbers on the main minecraft game screen

# The minecraft library has a method called getTilePos()
# It tracks where the player is

# This program introduces the "while" keyword, our first
# example of a loop, to make sure the program never stops
# until there is either an error, or we manually stop (break)
# the program using Ctrl-C on the keyboard

import mcpi.minecraft as minecraft

# This program also uses another library, the time library
# as we want the program to sleep for a short time - 1 second
# so that we don't fill the screen with too much information
# We will come across the time library later when we
# make a minecraft digital clock
import time

# Connect to Minecraft
mc = minecraft.Minecraft.create()

# We will use the getTilePos() method to tell us where we are
# and store that information in a variable
# Technically this is a special kind of variable, called an "object"
# but for now all we need to worry about is what to call it

# Most computer languages are very strict about using capital letters
# To the computer, playerPos, Playerpos and PlayerPOS are completely
# different things, so once you decide on a name, you need to spell
# it the same way every time you want to use it
playerPos = mc.player.getTilePos()

# playerPos now has our 3d position in the minecraft world
# it is made up of three parts, x, y & z

# There is another similar function called getPos()
# The difference is that getTilePos() returns whole numbers
# getPos() returns the exact position, to several decimal places
# We will stick with whole numbers for now

# playerPos = mc.player.getPos()

# We will be using a special kind of loop - an infinite loop
# Unless there is an error or we manually stop the program
# it will run forever
# True and False are normally used to compare one or more items and then
# make a choice, but for this program the loop is really saying "is true equal true?"
# the answer will always be yes so the loop will never stop

# We will be using more while loops in later programs
# The main thing we need to worry about is the spacing
# Notice playerPos has four spaces before it
# This means that it is "inside" the loop
# Python is very fussy about spaces, something we will be seeing again and again
# However,comments do not care about spaces


while True:
    myLocation = mc.player.getTilePos()
    # myLocation is variable that contains three variables inside in
    # we can get these one at a time, or all three at once
    # Before we can use them with postToChat() we need to change them
    # from numbers, into characters - called a string
    # There are several ways of doing this, for now we will use a command
    # called str , which takes a number and hands back a string
    # of characters.  Although to us there isn't any apparent difference
    # the way the numbers and characters are stored is very different.

    x = str(myLocation.x)
    y = str(myLocation.y)
    z = str(myLocation.z)

# We use the postToChat() method from our hello world example

    mc.postToChat("You are standing at X: " + x + ",  Y: " + y + ", Z: " + z)
    # Take a breath!
    time.sleep(1)

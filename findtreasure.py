#! /usr/bin/python
# Joe Deller 2014
# Minecraft find the treasure chest game

# Level : Intermediate
# Uses  : Libraries, variables, operators, logic, loops


# First the libraries we will be using in the game
# We want a random number helper to hide our treasure,
# the time library so we can wait a bit before telling the player
# if they are getting warmer or cooler
# Finally the math library to help us handle the negative co-ordinates
# that minecraft uses

import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
import math

# Connect to Minecraft
mc = minecraft.Minecraft.create()

# Place our treasure chest in a random location
# The larger the random number, the larger the area you have to search
# To make sure we don't have to dig too deep, the treasure will only be a maximum
# of 3 below ground
# On the raspberry pi, we need to keep within -127 and + 127 otherwise the treasure
# will be out of the world

# Random numbers are actually quite tricky to come up with
# computer hackers can sometimes find patterns in random number generators
# which lets them break into places they shouldn't
# For our uses though, the random number is pretty random
# Games often use random numbers, otherwise the game might be the same each time you play
# which would be very boring.

# Choose a random number between 30 blocks left and 30 blocks right from
# the centre of the minecraft world
treasureX = random.randint(-30, 30)

# We won't go too far underground, so a small number of blocks down for
# the Y coordinate
treasureY = random.randint(-3, 0)

# Choose a random number between 30 blocks forward and 30 blocks back from
# the centre of the minecraft world
treasureZ = random.randint(-30, 30)

# Clear a little bit of space around the chest so it is a bit easier to find
# if you want to make it harder, turn the line into a comment by adding a
# "# at the front

mc.setBlocks(
    treasureX - 1,
    treasureY,
    treasureZ - 1,
    treasureX + 2,
    treasureY + 20,
    treasureZ + 2,
    block.AIR.id)

# Place the treasure chest
mc.setBlock(treasureX, treasureY, treasureZ, block.CHEST.id)

# Sneaky peak will tell us exactly where the treasure is
# message is a string variable, it has letters in it
# to tell the player where the treasure is, we have to use a special function
# that converts the treasure coordinates from a number into a string characters
# We will use the "str" function quite a lot
# Like many things in programming , there is more than one way of doing this
# we will look at other ways later
message = "Treasure is here : X " + \
          str(treasureX) + "  Y: " + str(treasureY) + "  Z:" + str(treasureZ)
print (message)

while True:
    # Find out where the player is standing
    playerPos = mc.player.getTilePos()
    pX = playerPos.x
    pY = playerPos.y
    pZ = playerPos.z

    # Now work out how far away the player is by
    # adding up the total distance in all directions
    # If you wanted to make it easier then
    # you could change the code to tell how far the player is
    # in each direction, telling them to go left or right, forwards /
    # backwards, up or down
    # The treasure chest could be to the left of us, which would be a negative number
    # or to the right of us, a positive number
    # The same applies for the in front or behind us, above or below
    # What we want to tell the player, is the number of blocks they are away
    # from the chest, without the clue if the distance is positive or negative
    # To do this, we use another Python function, which converts any negative
    # numbers into a positive one, whilst doing nothing to positive numbers
    # We find this function in the math library and it is called math.fabs


    # How far left or right are we
    distanceX = math.fabs(treasureX - pX)
    # How far up or down are we
    distanceY = math.fabs(treasureY - pY)
    # How far forward or backward are we
    distanceZ = math.fabs(treasureZ - pZ)

    totalDistance = distanceX + distanceY + distanceZ

    # Now tell the player how warm or cold they are
    # depending on how far they are from the treasure
    # You can change these numbers depending on how helpful
    # or unhelpful you want to be
    # to make it a little easier, when we get close, tell the player where
    # the X coordinate of the treasure is, then the X & Z when we get very
    # close

    if (totalDistance > 100):
        mc.postToChat("FREEZING!")
    elif (totalDistance > 90):
        mc.postToChat("VERY VERY COLD")
    elif (totalDistance > 80):
        mc.postToChat("VERY COLD")
    elif (totalDistance > 70):
        mc.postToChat("COLD")
    elif (totalDistance > 60):
        mc.postToChat("WARM")
    elif (totalDistance > 40):
        mc.postToChat("WARMER")
    elif (totalDistance > 30):
        mc.postToChat("HOT - X = " + str(treasureX))
    elif (totalDistance > 20):
        mc.postToChat(
            "VERY HOT - X=" +
            str(treasureX) +
            " Z=" +
            str(treasureZ))
    elif (totalDistance <= 10):
        mc.postToChat(
            "BOILING!! = X=" +
            str(treasureX) +
            "  Z=" +
            str(treasureZ))
        # Sleep for a couple of seconds, so we don't send too many messages
    time.sleep(2)

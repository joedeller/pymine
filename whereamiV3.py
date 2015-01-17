#! /usr/bin/python
# Joe Deller 2014
# Using place holders when showing a message

# Level : Beginner
# Uses  : Libraries, variables, operators, loops


import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()
lastPlayerPos = mc.player.getTilePos()

# We still use the postToChat() method from our hello world example
# but this time we are using a special placeholder format
# It's a bit like being able to write a sentence but leaving gaps for some words
# you don't know yet, then going back and filling them in when you know
# what you are going to write.
# the %s means reserve a space for a string of characters characters

mc.postToChat(
    "Your position is x=%s z=%s y=%s" %
    (lastPlayerPos.x, lastPlayerPos.z, lastPlayerPos.y))

while True:
    # Where are we now ?
    playerPos = mc.player.getTilePos()
    # has the player moved since the last time we checked where they are ?
    # if they haven't then don't do anything
    # The "!=" means "Not equal to", or "different to"
    # If we haven't moved, then the our last position is the same as our current

    if (lastPlayerPos != playerPos):
        mc.postToChat(
            "Your position is x=%s z=%s y=%s" %
            (playerPos.x, playerPos.z, playerPos.y))
        # As we have moved, we  now need to update our last position with the current one
        lastPlayerPos= playerPos
    time.sleep(.1)


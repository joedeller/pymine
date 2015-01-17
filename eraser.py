#! /usr/bin/python
# Joe Deller  2014

# Level : Beginner
# Uses  : Libraries, variables, operators, loops, logic

# Use with care !
# This program erases the world around us
# it draws air 5 blocks to our left, 5 blocks behind us, to five blocks to our right
# and five blocks in front of us.  It also draws air 12 blocks above us
# so quickly "rubs out" the minecraft world


import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Find out where we are
mc = minecraft.Minecraft.create()
# this is a shorter way of making a note of where we are
# it only uses 1 line compared to the three we have previously used
# it makes no difference to how our program works
# some people find it easier to read this way, others not.
x, y, z = mc.player.getTilePos()

# We will make a note of our "last" position
# then we will go into a loop, if we move in any direction, the rubbing
# out starts

last_x, last_y, last_z = mc.player.getTilePos()

# If you want to erase a bigger area, increase the width and height
# There is no "undo" so be careful about setting the numbers too large
width = 8
height = 10


# We are going to loop until the program is forcibly stopped
# using ctrl-c
while (True):
    # Find out where we are now
    x, y, z = mc.player.getTilePos()
    # Have we moved
    if (last_x != x) or (last_y != y) or (last_z != z):
        # Rub things out
        mc.setBlocks(last_x - width, last_y, last_z - width, last_x + width, last_y + height, last_z + width,
                     block.AIR.id)
        # update our "last position"
        last_x = x
        last_y = y
        last_z = z
    # take a short breather
    time.sleep(.05)

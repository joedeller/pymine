#! /usr/bin/python
# Joe Deller 2014
# Using for loops

# Level : Beginner
# Uses  : Libraries, variables, operators, loops

# Loops are a very important part of programming
# The for loop is a very common loop
# It counts from a starting number to a finishing number
# It normally counts up in ones, but you can count up
# in any number you want, or count downwards
#
# The wool block in minecraft can be any one of 16 different colours
# from 0, a white block, to 15, a black block
# This program uses a for loop to draw wool blocks
# of all 16 different colours
# It also uses the for loop to set where the block is drawn
# so we can see all 16 colours


import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Setup the connection and clear a space
# set us down in the middle of the world
mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlocks(x - 20, y, z - 20, x + 20, y + 20, z + 20, block.AIR)
mc.setBlocks(z - 20, y - 1, z - 20, y, z + 20, block.GRASS.id)

for colour in range(0, 15):
    # draw upwards
    mc.setBlock(x + 15, y + 2 + colour, z + 2, block.WOOL.id, colour)
    # draw across
    mc.setBlock(x + colour, y + 2, z + 2, block.WOOL.id, colour)
    time.sleep(.5)

# Counting backwards, using a negative number to say how quickly to count backwards
# Try changing this to -2 and see what happens

for colour in range(15, 0, -1):
    mc.setBlock(x, 1 + colour, z + 2, block.WOOL.id, colour)
    mc.setBlock(colour, y + 16, z + 2, block.WOOL.id, colour)
    time.sleep(.1)

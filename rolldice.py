#! /usr/bin/python
# Joe Deller 2014
# A Minecraft dice rolling example

# Level : Intermediate
# Uses  : Libraries, loops, operators, lists

# Our dice will be made up of a square wool block
# We will use white wool blocks as the "spots" of the dice

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

# Draw a dice number, slightly to the right and back of the position given
# This lets us see it


def drawDice(dice_throw, dice_x, dice_y, dice_z):
    dice_x = dice_x - 2
    dice_z = dice_z - 7
    top = dice_y + 5
    # Find the pattern for the number that was thrown, by looking it up in our dice pattern list
    pattern = dice[dice_throw]
    print dice_throw + 1, pattern
    # Draw the black square of the dice
    mc.setBlocks(dice_x - 1, dice_y, dice_z, dice_x + 5, dice_y + 6, dice_z, block.WOOL.id, 15)
    time.sleep(.2)

    # The pattern is made up of a series of rows of blocks
    # We draw the pattern from top to bottom
    for row in pattern:
        # For every row, the x co-ordinate gets reset
        # like starting a new line in a text book
        block_x = dice_x
        for dice_block in row:
            if dice_block == "1":
                mc.setBlock(block_x, top, dice_z, block.WOOL.id, 0)
            else:
                mc.setBlock(block_x, top, dice_z, block.WOOL.id, 15)
            block_x = block_x + 1
        top = top - 1

mc = minecraft.Minecraft.create()
x, y, z = mc.player.getTilePos()
# clear some space
mc.setBlocks(x - 4, y, z, x + 20, y + 6, z - 8,
             block.AIR.id)

# The block patterns that make up our dice numbers
# A "1" will draw a white wool block, a "0" a black wool block
# Squared paper helps work out what the patterns should be
six = "10001", "00000", "10001", "00000", "10001"
five = "10001", "00000", "00100", "00000", "10001"
four = "10001", "00000", "00000", "00000", "10001"
three = "10000", "00000", "00100", "00000", "00001"
two = "00000", "00100", "00000", "00100", "00000"
one = "00000", "00000", "00100", "00000", "00000"

# Store the dice patterns in a list
dice = [one, two, three, four, five, six]

# We will keep track of the last number the dice threw
# If our new dice number is the same, we won't draw it again
# We haven't thrown a dice yet, so we set the lastThrow
# to any value except a valid one
last_throw = 7

# Roll 20 dice throws

for i in range(0, 20):
    # Lists start counting from ZERO so we need to throw a number
    # between 0 and 5, not 1 and 6

    throw = random.randint(0, 5)
    # if the current throw is the same as the previous
    # then there's no point drawing the dice again
    if throw != last_throw:
        drawDice(throw, x, y, z)
        time.sleep(1)
        last_throw = throw






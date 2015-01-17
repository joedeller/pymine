#! /usr/bin/python
# Joe Deller 2014
# Drawing circle shapes in Minecraft

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, logic

# This program uses more functions from the maths library
# The mathematics of circles is something that you probably won't
# be taught until secondary school, but don't worry.
# All we really need to understand is where, how big , what color

# This program uses two different types of numbers
# Floating point (numbers with a decimal place ) and integers (whole numbers)

# First the libraries we will need
import mcpi.minecraft as minecraft
import mcpi.block as block
import math

# Make a connection to minecraft
mc = minecraft.Minecraft.create()

# Find out where we are in the world and store this for later
playerPos = mc.player.getPos()
pX = playerPos.x
pY = playerPos.y
pZ = playerPos.z

# Clean up the world and any previous circles nearby
# We will clear and area 20 both the left, right, front and back of where we are standing
# and 64 blocks up into the air
mc.setBlocks(pX - 20, pY, pZ - 20, pX + 20, pY + 64, pZ + 20, block.AIR.id)

# Setup a grass floor, the same size as the area we cleared, but not so high
mc.setBlocks(pX - 20, pY - 1, pZ - 20, pX + 20, pY - 1, pZ + 20, block.GRASS.id)

# Many computer languages, including python, use a measurement called radians to measure angles
# rather than degrees  you might be used to.
# If you haven't heard of Pi, (the number rather than the computer)
# then Pi is the number you get if you measure all the way around a circle,
# called the circumference, by the width of the circle
# it is approximately 3.14, or, to be slightly more accurate, 3.1415926
# in fact the numbers after the decimal point go on for ever

# A circle can be divided up into 360 degrees, or 2 * Pi in radians
# A semi circle is 180 degrees, or Pi in radians
# Pi is such an important number that many computer
# languages include it as part of their keywords or
# as part of a library
# For now we won't worry too much about the Mathematics, just the color
# and shape

# How wide in blocks do we want our circle?
# Including the decimal place tells Python that we want a float variable to
# store the width, rather than whole numbers
diameter = 10.0

# Normally we would use a For loop, but in Python "range" only
# works with whole numbers and we need numbers with decimal places
# One way (and there are others) is to use a while loop

# You might wonder why we don't start from zero, try changing i to be 0.0
# and see :-)
i = 0.01

while (i < math.pi * 2):
    # When we draw our blocks, we need to convert the floating point numbers back to integers
    # Our circle won't be super smooth as minecraft blocks are quite large
    # For now don't worry about the sin and cos functions, they work out where to place our blocks
    # to make a circle shape
    dx = int(diameter * math.cos(i))
    dy = int(diameter * math.sin(i))
    # We need to add our player X co-ordinate to the circle X coordinate so it is
    # drawn close to where we are standing
    # We also will draw our circle back a bit from where we are standing, 4
    # blocks should be enough
    mc.setBlock(dx + pX, pY + dy + diameter, pZ + 10, block.WOOL.id, 1)
    # try changing the number we add to different values, for example 0.5
    # the more you add the faster the loop finishes, so the less blocks get
    # drawn
    i = i + 0.4

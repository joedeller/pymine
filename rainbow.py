#! /usr/bin/python
# Joe Deller July 2014
# Draw a rainbow in minecraft

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, lists


import mcpi.minecraft as minecraft
import mcpi.block as block
import math

# A rainbow is " Richard Of York Gave Battle In Vain"
# Red Orange Yellow Green Blue Indigo Violet
# ROYGBIV, we will get as close as we can with Minecraft Wool colors

# 14 = red, 1 = orange, 4 = yellow, 5 = lime green , 3 = light blue , 11 = blue, 10 = purple
# Start by making a list of colors, change them if you want your own version of
# a rainbow
colors = [14, 1, 4, 5, 3, 11, 10]

# Connect to minecraft
mc = minecraft.Minecraft.create()

# Find out where we are in the world
playerPos = mc.player.getTilePos()
x = playerPos.x
y = playerPos.y
# Our rainbow will be 5 blocks back from where we are standing
z = playerPos.z + 5

# Set how tall and wide we want our rainbow to be and work out where the middle is
# Try experimenting changing the width and height to see the different
# shapes you get
height = 32
width = 60
centre = width / 2

# Clean up the world and any previous rainbows
mc.setBlocks(x - 64, y, z - 10, x + 64, y + 24, z + 10, block.AIR)

# Setup a grass floor
mc.setBlocks(x - 64, y - 1, z - 10, x + 64, y - 1, z + 10, block.GRASS.id)


# To draw our rainbow shape, we are going to use mathematical function called Sine
# which comes from the python maths library

# Sine comes from a branch of mathematics called Trigonometry
# from Greek "trigonon", "triangle" and "metron", "measure"
# Something that you will study in secondary school
# For now all we need to know is that it can be used to draw a shape known as a sine wave
# a gently curving pattern
# We will use it in several a couple of our programs

# A slight complication is that normally computers work in Radians, not degrees
# that you might be used to, but the shape is still the same

# How long is our list of colors?
# the len keyword counts the number of items in our colors list
# Our rainbow will be made up of several rainbows stacked on top of each other
# Each one will be one of the colors in our list

color_count = len(colors)

# We could have just put colour_count = 7, but if we decided to change list of colors
# later, we would also have to change our code here, very bad practice and a common
# cause of computer bugs
# These are sometimes called "magic numbers", because even if you did write the program
# you might not remember what they mean


# We are going to use two loops
# The first one draws the rainbow from left to right
# the second runs through all our colors, stacking them one on top of the other

for r in range(0, width + 1):
    for current_color in range(0, color_count):
        # This next line is the part the calculates the shape of the rainbow
        # for now all we need to know is that it works out how high each block will be
        block_y = math.sin((r / float(width)) * math.pi) * height

        # We add on the height of where we are standing in the world
        block_y = block_y + y
        # Each color is stacked on top of the previous colour
        # so we add on that as well
        block_y = block_y + current_color
        # finally draw the blocks
        mc.setBlock(
            x +
            centre -
            r,
            int(block_y),
            z,
            block.WOOL.id,
            colors[
                color_count -
                1 -
                current_color])

# Fit the 2nd rainbow inside the first, so it must be lower and narrower
# so lets make it 20 blocks high and 20 blocks narrower than the first rainbow
height = 20
width = width - 20
centre = width / 2

for r in range(0, width + 1):
    for current_color in range(0, color_count):
        block_y = math.sin((r / float(width)) * math.pi) * height
        block_y = block_y + y
        block_y = block_y  + current_color
        mc.setBlock(x + centre - r, int(block_y), z, block.WOOL.id,
                    colors[color_count - 1 - current_color])




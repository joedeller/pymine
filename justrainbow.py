#! /usr/bin/python
# Joe Deller 2014
# Draw just rainbow in Minecraft, don't clear any space

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, lists


import mcpi.minecraft as minecraft
import mcpi.block as block
import math

colors = [14, 1, 4, 5, 3, 11, 10]

# Connect to minecraft
mc = minecraft.Minecraft.create()

# Find out where we are in the world
playerPos = mc.player.getTilePos()
x = playerPos.x 
y = playerPos.y 
# Our rainbow will be 10 blocks back from where we are standing
z = playerPos.z + 10

# Set how tall and wide we want our rainbow to be and work out where the middle is
# Try experimenting changing the width and height to see the different
# shapes you get
height = 32
width = 72
centre = width / 2

colour_count = len(colors)

for r in range(0, width):
    for color_index in range(0, colour_count):
        # This next line is the part the calculates the shape of the rainbow
        block_y = math.sin((r / float(width)) * math.pi) * height

        # We add on the height of where we are standing in the world
        block_y = block_y + y
        # Each color is stacked on top of the previous colour
        # so we add on that as well
        block_y = block_y + color_index
        # finally draw the blocks
        mc.setBlock(
            x +
            centre -
            r,
            int(block_y),
            z,
            block.WOOL.id,
            colors[
                colour_count -
                1 -
                color_index])

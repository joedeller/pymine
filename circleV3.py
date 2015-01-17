#! /usr/bin/python
# Joe Deller 2014
# Drawing many circle shapes in Minecraft

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, logic

# It uses a for loop and a while loop to help draw different
# size circle shapes of different colours
# All we really need to understand is where, how big , what color
# and how many circles we want to draw

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

# Many computer languages, including python, use
# a measurement called radians to measure angles, rather than degrees you might be used to.
# A circle is 360 degrees, or 2 * PI in radians
# A semi circle is 180 degrees, or PI in radians
# Try setting endX to 1 *  PI to get a "sunrise" shape
# You might notice some side effects...

endX = 2 * math.pi

# Try experimenting with the resolution value
# 0.1 gives a circle with lots of blocks, 0.5 is more like a star
resolution = 0.1

# Wool can be one of 16 colors, 0-15
# If we limit the number of colors we use, then we can produce shapes that have the same
# color on each "spoke"
color = 0
maxColor = 16

# Set the maximum size of the circle
maxDiameter = 20

pZ = pZ + 14

# Now draw some circles, slowly increasing the size (diameter), 3 is about
# the smallest that makes sense in Minecraft
for diameter in range(3, maxDiameter):
    # We need a start point for drawing in our circle
    # This gets reset for every circle we draw
    currentX = 0.2

    # As before, we use a while loop to draw our circle
    # We use the mathematical functions sine and cosine (sin and cos)
    # to calculate points along a circle where we will draw or blocks
    while (currentX < endX):
        # We need to add maxDiameter to the Y coordinate so we can see our shape
        # otherwise it might be below ground
        # When we draw our blocks, we need to convert the floating point numbers back to integers
        # Our circle won't be super smooth as minecraft blocks are quite large
        dx = int(diameter * math.cos(currentX))
        dy = int(diameter * math.sin(currentX)) + maxDiameter

        # We need to add our player X co-ordinate to the circle X coordinate so it is
        # drawn close to where we are standing
        # We also will draw our circle back a bit from where we are standing, 4
        # blocks should be enough
        mc.setBlock(dx + pX, pY + dy, pZ, block.WOOL.id, color)
        # Try adjusting the amount we add to currentX each time and see how it affects the circle
        # 0.1 gives a circle with lots of blocks, 0.5 is more like a star
        currentX = currentX + resolution

    # Wool can have 16 different colors, 0-15, so we recycle them
    # Try moving the color change code inside or outside the while loop - remove two spaces
    # If you adjust resolution and maxColor to see if you can get the spokes to be the same color
    # Try resolution =  0.4 and maxColor=8
        color = color + 1
        if (color == maxColor):
            color = 0
        # This is the end of our while loop, it will finish when currentX is
        # greater or equal to endX

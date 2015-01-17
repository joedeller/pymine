#!/usr/bin/python
# Joe Deller 2014
# Draw a Kaleidoscope pattern using Minecraft blocks

import mcpi.minecraft as minecraft
import mcpi.block as block
import random

# This code is based on a very old Sinclair ZX81 Basic listing
# which ran in 1K of memory.

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops

# Out kaleidoscope has two mirrors, one vertical and one horizontal
# We draw a block and then it is reflected vertically and horizontally
# to give our pattern.
# A more complex program might use more mirrors, or change their angle
# but in the low resolution world of minecraft, you might struggle
# to see the effect.

mc = minecraft.Minecraft.create()

# size of our kaleidoscope, if you make it too big it will be hard to see
size = 12
# Set flat to true to draw it on the ground, or false to draw it in the air
flat = False
# If you want some random colors, set changeColors to true
change_colors = True

# Find out where we are
playerPos = mc.player.getTilePos()
x = playerPos.x
y = playerPos.y + size
z = playerPos.z

# Whilst we could say if (flat == False), it is more technically correct to
# use yet another keyword, "is" to see if flat really is false
if (flat is False):
    # Draw the kaleidoscope tall, 18 blocks back from where we are standing
    z_distance = 18

    # Clear a nice big space
    mc.setBlocks(
        x - size - 4,
        y - size,
        z,
        x + size + 4,
        y + size + 4,
        z + z_distance,
        block.AIR)

    # Draw a wool screen as a background
    mc.setBlocks(
        x - size - 2,
        y - size,
        z + z_distance,
        x + size + 2,
        y + size + 2,
        z + z_distance,
        block.WOOL.id,
        0)
    z = z + z_distance
else:
    # Draw the kaleidoscope on the floor at player level
    y = playerPos.y - 1
    z = playerPos.z + size + 4
    mc.setBlocks(
        x - size - 2,
        y - 1,
        z - size,
        x + size + 2,
        y + 10,
        z + size + 2,
        block.AIR.id)

    mc.setBlocks(
        x - size - 2,
        y - 1,
        z - size,
        x + size + 2,
        y - 1,
        z + size + 2,
        block.DIRT.id)

    mc.setBlocks(
        x - size - 2,
        y,
        z - size,
        x + size + 2,
        y,
        z + size + 2,
        block.WOOL.id,
        0)


# Choose a random number of loops, we need a reasonable amount
# to draw a good pattern.  For now start with a minimum of 400
# and a maximum of 1000
loops = random.randint(400, 1000)

# We can choose random colors, but too many colors and the effect
# is not so good.
# ColorA is the background color, so that doesn't change
# even if we are changing colorB.  We use colorA when we want to "rub out"
# a block

colour_a = 0
colour_b = 2

distance_a = 0
distance_b = 0

print "loops = " + str(loops)
for i in range(1, loops):
    # Choose a random point to draw a block, up to the maximum size we set
    # we pick two random numbers to help pick where our blocks get drawn
    distance = random.randint(1, size)
    distance_a = distance_a + random.randint(0, distance)
    distance_b = distance_b + random.randint(0, distance)

    if(distance_a > size):
        distance_a = 0

    if (distance_b > size):
        distance_b = 0

    if (change_colors):
        # Every 50 blocks change color to a random one
        # You can change the color faster by reducing the number 50
        # The % means "modulus" , it divides one number by
        # another and gives the remainder.  In this case
        if (i % 50 == 0):
            colour_b = random.randint(1, 15)

    if (flat):
        mc.setBlock(x + distance_a, y, z + distance_b, block.WOOL.id, colour_a)
        mc.setBlock(x + distance_a, y, z - distance_b, block.WOOL.id, colour_a)
        mc.setBlock(x - distance_a, y, z + distance_b, block.WOOL.id, colour_a)
        mc.setBlock(x - distance_a, y, z - distance_b, block.WOOL.id, colour_a)
        mc.setBlock(x + distance_b, y, z + distance_a, block.WOOL.id, colour_b)
        mc.setBlock(x + distance_b, y, z - distance_a, block.WOOL.id, colour_b)
        mc.setBlock(x - distance_b, y, z + distance_a, block.WOOL.id, colour_b)
        mc.setBlock(x - distance_b, y, z - distance_a, block.WOOL.id, colour_b)
    else:
        # Top right
        mc.setBlock(x + distance_a, y + distance_b, z, block.WOOL.id, colour_a)
        # Lower right
        mc.setBlock(x + distance_a, y - distance_b, z, block.WOOL.id, colour_a)
        # Top left
        mc.setBlock(x - distance_a, y + distance_b, z, block.WOOL.id, colour_a)
        # Lower left
        mc.setBlock(x - distance_a, y - distance_b, z, block.WOOL.id, colour_a)
        # Top right
        mc.setBlock(x + distance_b, y + distance_a, z, block.WOOL.id, colour_b)
        # Lower right
        mc.setBlock(x + distance_b, y - distance_a, z, block.WOOL.id, colour_b)
        # Top Left
        mc.setBlock(x - distance_b, y + distance_a, z, block.WOOL.id, colour_b)
        # Lower Left
        mc.setBlock(x - distance_b, y - distance_a, z, block.WOOL.id, colour_b)

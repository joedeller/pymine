#! /usr/bin/python
# Joe Deller 2014
# First version of a firework launch program

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, logic

# This is a first introduction to computer animation
# We will animate a block moving upwards
# and then an explosion in the sky
# Unlike traditional film animation, computer animation means
# we have to rub things out as well as draw them

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math


def DrawSingleCircle(circle_x, circle_y, circle_z, diameter, color, mode):
    # If we want to erase a circle, set mode to 0
    # which will draw a circle of air
    endX = 2 * math.pi
    x = 0.01
    while (x < endX):
        # When we draw our blocks, we need to convert the floating point
        # numbers back to whole numbers (integers)
        dx = int(diameter * math.cos(x)) + circle_x
        dy = int(diameter * math.sin(x)) + circle_y
        if (mode == 1):
            mc.setBlock(dx, dy, circle_z, block.WOOL.id, color)
        else:
            mc.setBlock(dx, dy, circle_z, block.AIR.id)
        x = x + 0.5


def DrawCircles(circle_x, circle_y, circle_z, mode):
    color = 0
    # Now draw some circles, slowly increasing the size (diameter)
    # We start with a circle 3 blocks wide going up to ten blocks wide

    for diameter in range(3, 10, 1):
        DrawSingleCircle(circle_x, circle_y, circle_z, diameter, color, mode)
        # Wool has 16 different colors, 0-15, so recycle them
        # if you want each circle to be the same color rather than each 'spoke' move this part ot the code
        # outside of the while loop
        color = color + 1
        if (color == 16):
            color = 0
        # if we are rubbing out circles, wait a little bit
        if(mode == 0):
            time.sleep(0.1)


# Start here
mc = minecraft.Minecraft.create()
playerPos = mc.player.getPos()

x, y, z = playerPos.x, playerPos.y, playerPos.z
# Clean up the world and any previous circles nearby
mc.setBlocks(x - 20, y, z - 5, x + 20, y + 64, x + 20, block.AIR.id)
# Setup a grass floor
mc.setBlocks(x - 5, y - 1, z - 50, x + 5, y - 1, z + 5, block.GRASS.id)

# Put the rocket at a safe distance from us, we will put it on a block, so it will start
# from a height of 2
rocketX = x + 4
rocketY = y + 1
rocketZ = z - 6

# Start at ground level, 1 and go up to height set by max_height
# When we draw a block, we need to remember it so that we can rub it out next time
# this makes it look like the block is moving upwards

mc.postToChat("Launching, look for the furnaces & look up!")
mc.setBlock(rocketX, rocketY - 1, rocketZ, block.FURNACE_ACTIVE.id)
mc.setBlock(rocketX, rocketY, rocketZ, block.FURNACE_ACTIVE.id)

#mc.setBlock(rocketX, rocketY - 1, rocketZ, block.NETHER_REACTOR_CORE.id)
#mc.setBlock(rocketX, rocketY, rocketZ, block.NETHER_REACTOR_CORE.id)
time.sleep(5)
mc.setBlock(rocketX,rocketY -1, rocketZ, block.AIR.id)

# don't make the height too large or you won't be able to see the explosion
max_height = 19

for loop in range (0,max_height):
    mc.setBlock(rocketX, rocketY, rocketZ, block.FURNACE_ACTIVE.id)
    lastX = rocketX
    lastY = rocketY
    # un-plot the previous block
    time.sleep(0.1)
    mc.setBlock(lastX, lastY, rocketZ, block.AIR.id)
    rocketY = rocketY + 1

# The rocket has finished going up so now do the explosion
# which start where our rocket finished
# Our draw circles code needs to know where to draw the circles
# A "1" means draw wool blocks, a "0" means draw blocks of air
# which will rub out the wool blocks
time.sleep(0.5)
DrawCircles(rocketX, rocketY , rocketZ, 1)
time.sleep(0.5)
DrawCircles(rocketX, rocketY , rocketZ, 0)

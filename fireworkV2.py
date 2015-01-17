#! /usr/bin/python
# Joe Deller 2014
# Add a launch platform for our firework

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, lists

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math

mc = minecraft.Minecraft.create()


def DrawSingleCircle(cx, cy, cz, diameter, color, mode):
    # If we want to erase a circle, set mode to 0
    # which will draw a circle of air
    endX = 2 * math.pi
    x = 0.01
    while (x < endX):
        # We add the firework X and Y coordinates to the circle so the explosion is in the right place
        # When we draw our blocks, we need to convert the floating point
        # numbers back to integers
        dx = int(diameter * math.cos(x)) + cx
        dy = int(diameter * math.sin(x)) + cy
        if (mode == 1):
            mc.setBlock(dx, dy, cz, block.WOOL.id, color)
        else:
            mc.setBlock(dx, dy, cz, block.AIR.id)
        # we want a reasonably spokey circle, so add 0.4 or larger
        # this also makes it a bit faster and more realistic
        x = x + 0.5

def DrawCircles(cx, cy, cz):
    # To create an explosion effect, we draw three circles, then start rubbing them out
    # starting with the smallest circle
    # keep a count of how many circles we have drawn, when we get to three
    # start rubbing out
    circles_drawn = 0
    # Start with white
    color = 0
    # We want a big explosion, but not so big that it goes below ground
    maxDiameter = 18

# Now draw some circles, slowly increasing the size (diameter)
    for diameter in range(3, maxDiameter, 1):
        # Go and draw the circle
        DrawSingleCircle(cx, cy, cz, diameter, color, 1)

        circles_drawn = circles_drawn + 1
        if (circles_drawn > 2):
            # now rub out the circle we drew 3 loops ago
            DrawSingleCircle(cx, cy, cz, diameter - 2, color, 0)
        # Wool has 16 different colors, 0-15, so recycle them
        color = color + 1
        if (color == 16):
            color = 0

# unplot the last 2 circles, as our loop has finished drawing
    DrawSingleCircle(cx, cy, cz, maxDiameter - 1, color, 0)
    DrawSingleCircle(cx, cy, cz, maxDiameter - 2, color, 0)

# Start here
playerPos = mc.player.getTilePos()
x, y, z, = playerPos

# Clean up the world and any previous circles nearby
mc.setBlocks(x - 10, y, z - 10, x + 50, y + 64, z + 10, block.AIR.id)
# Setup a grass floor
mc.setBlocks(x - 10, y - 1, z - 10, x + 20, y - 1, z + 10, block.GRASS.id)


moveLeft = 0
# Our rocket will launch at a safe distance :-)
rocketX = playerPos.x + 6
rocketY = playerPos.y 
rocketZ = playerPos.z + 6

# Lets have a small stone platform to launch from
mc.setBlocks(
    rocketX - 2,
    rocketY ,
    rocketZ - 2,
    rocketX + 2,
    rocketY,
    rocketZ + 2,
    block.STONE.id)

# The rocket will be on the platform
rocketY = y + 1


mc.setBlock(rocketX, rocketY, rocketZ, block.FURNACE_ACTIVE.id)
# Send a message to the player to tell them the rocket is going to launch
mc.postToChat("Launching in 5 seconds")
time.sleep(5)


# Start at ground level, 1 and go up to height of 20
# move left every time we climb 6
# When we draw a block, we need to remember it so that we can rub it out next time
# this makes it look like the block is moving upwards

max_height = 19

for height in range (0, max_height):
    mc.setBlock(rocketX, rocketY + height, rocketZ, block.FURNACE_ACTIVE.id)
    lastX = rocketX
    lastY = rocketY + height
    # rub out  the previous block
    time.sleep(0.1)
    mc.setBlock(lastX, lastY, rocketZ, 0)
    moveLeft = moveLeft + 1

    if (moveLeft == 6):
        rocketX = rocketX + 1
        moveLeft = 0
        time.sleep(0.1)


# rub out the last rocket ready to explode
mc.setBlock(lastX, lastY + 1, rocketZ, 0)

time.sleep(0.1)
# Draw the explosion where the rocket finished
DrawCircles(lastX - 2, rocketY + max_height, rocketZ)

#! /usr/bin/python
# Joe Deller 2014
# Fire work with flames

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, lists

# More changes to our firework rocket launch program
# This time we have added flames when our rocket starts off
# We draw some flames underneath the rocket as it moves up
# This time we launch in a straight line up

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math


def DrawSingleCircle(cx, cy, cz, diameter, color, mode):
    # Draw a circle at the specified coordinates, size and color, unless mode is zero
    # in which case we want to erase a circle, which will draw a circle of air instead of wool
    # For now we won't worry about the algebra of how the points are calculated
    # Just remember that the amount we increase "x" decides how many blocks are drawn
    # A small number means lots of blocks and a smoother circle, but is slower
    # If you make endX smaller you won't get a complete circle

    # One improvement (optimisation) compared to our previous version
    # the code was checking if it needed to draw some wool or air every time it had to draw something
    # We can change this to just check once and then set the block type we want to draw
    # This does mean that we are asking minecraft to draw coloured air blocks, but
    # luckily for us, it ignores the colour part
    if (mode == 1):
        block_type = block.WOOL.id
    else:
        block_type = block.AIR.id

    endX = 2 * math.pi
    x = 0.01
    while (x < endX):
        # We add the firework X and Y coordinates to the circle so the explosion is in the right place
        # When we draw our blocks, we need to convert the floating point
        # numbers back to whole numbers (integers)
        dx = int(diameter * math.cos(x)) + cx
        dy = int(diameter * math.sin(x)) + cy
        mc.setBlock(dx, dy, cz, block_type, color)
        # we want a reasonably "spokey" circle, so add 0.4 or larger
        # this also makes it a bit faster and more realistic, we want our
        # explosion to be quite fast
        x = x + 0.5


def DrawCircles(cx, cy, z):
    # To create an explosion effect, we draw three circles, getting bigger each time, then start rubbing them out
    # starting with the smallest circle, this makes it look like a firework exploding outwards
    # We need to keep a count of how many circles we have drawn, when we get to three start rubbing them out
    # As am experiment, you could try an "implosion" , start with a big circle
    # and count downwards

    circles_drawn = 0
    # Start with white wool
    color = 0
    # We want a big explosion, but not so big that it goes below ground
    max_diameter = 18

# Now draw some circles, slowly increasing the size (diameter)
    for diameter in range(3, max_diameter, 1):
        # Call our circle drawing code to draw the circle of the size and color we ask
        # the last "1" means draw the circle, rather than "0" which draws a
        # circle of air
        DrawSingleCircle(cx, cy, z, diameter, color, 1)

        circles_drawn = circles_drawn + 1
        # Check how many circles we have drawn, if we have just drawn the 3rd one
        # start rubbing them out
        if (circles_drawn > 2):
            # now rub out the circle we drew 3 loops ago, which means it was 2
            # smaller
            DrawSingleCircle(cx, cy, z, diameter - 2, color, block.AIR.id)
        # Wool has 16 different colors, 0-15, we cycle through them then back
        # to 0
        color = color + 1
        if (color == 16):
            color = 0

# Our circle drawing has finished, but that still leaves us with two circles
# so we need to rub them out, starting with the smallest one to keep the
# "exploding outwards" illusion
    DrawSingleCircle(cx, cy, z, max_diameter - 2, color, 0)
    DrawSingleCircle(cx, cy, z, max_diameter - 1, color, 0)


# Start here

mc = minecraft.Minecraft.create()
# We are going to put the player in a specific location
mc.player.setPos(20, 2, 20)
playerPos = mc.player.getPos()

# Clean up the world and any previous circles nearby
mc.setBlocks(0, -2, 0, 40, 64, 40, block.AIR.id)
# Setup a grass floor
mc.setBlocks(0, -2, -0, 40, 1, 40, block.GRASS.id)

# Launch the rocket from a safe distance :-)
rocketX = playerPos.x + 8
rocketY = playerPos.y
rocketZ = playerPos.z + 8

# Let's have a small stone platform to launch from
mc.setBlocks(
    rocketX - 2,
    rocketY - 1,
    rocketZ - 2,
    rocketX + 2,
    1,
    rocketZ + 2,
    block.STONE.id)
# A single stone block for the rocket to sit on
mc.setBlock(rocketX, rocketY, rocketZ, block.STONE.id)
rocketY = rocketY + 1

# we will use a furnace to be our rocket, but change as you wish
mc.setBlock(rocketX, rocketY, rocketZ, block.FURNACE_ACTIVE.id)

# Send a message to the player to tell them the rocket is going to launch
mc.postToChat("Prepare for launch...")
# We can't point the player towards the rocket, so give them a chance to
# look the right way
time.sleep(2)
# Change the stone block under our rocket to some glowing obsidian
mc.setBlock(rocketX, rocketY - 1, rocketZ, block.GLOWING_OBSIDIAN)
time.sleep(1)

# Lets have some "flames" around the rocket, well different colored wool :-)
# Our flames will be Red, Orange, Yellow and Purple
# We will use a list and then step through it
flames = [14, 1, 4, 10]

# We are going to use a loop within a loop
# The inside loop will run through the different colour flames, pausing for
# one tenth of second, making it look like they are glowing
# the outside loop will mean we wait 4 seconds before launching
# Ten loops multiplied by 4 flame colours multiplied by 1/10th of a second
# If we want to add more colors to the flames list, or take some away
# then we might break our code, as the flame loop needs to know how many
# flame colors there are
# To protect ourselves, we use len() to count up how many flame colors there
# are in the list

flame_colors = len(flames)

for count in range(0, 10):
    for flame in range(0, flame_colors):
        # It can be confusing at times, but items in lists are counted from zero
        # This will be a source of many bugs in your programming careers
        # the flames will be a square block 3x3 wide, so left by one and right by one, back one and forward one
        # the flames will be at height 2, so the rocket will still be visible
        mc.setBlocks(
            rocketX - 1,
            2,
            rocketZ - 1,
            rocketX + 1,
            2,
            rocketZ + 1,
            block.WOOL.id,
            flames[flame])
        # If wait too long the effect won't be very convincing
        time.sleep(.1)

# Clear up the flames by using a 3x3 block of air
mc.setBlocks(
    rocketX - 1,
    2,
    rocketZ - 1,
    rocketX + 1,
    2,
    rocketZ + 1,
    block.AIR)

# You could try animating the block flames as the rocket moves up
# Start moving the rocket up one block

mc.setBlock(rocketX, rocketY + 1, rocketZ, block.FURNACE_ACTIVE.id)

explodeHeight = 21
# Start at ground level, 1 and go up to height set by explodeHeight
# When we draw a block, we need to remember it so that we can rub it out next time
# this makes it look like the block is moving upwards

# In this version the rocket is going straight up, so the X position does
# not change
lastY = rocketY

while (rocketY < explodeHeight):
    mc.setBlock(rocketX, rocketY, rocketZ, block.GLOWING_OBSIDIAN)
    mc.setBlock(rocketX, rocketY + 1, rocketZ, block.FURNACE_ACTIVE.id)
    lastY = rocketY
    # rub out  the previous block
    time.sleep(0.2)
    mc.setBlock(rocketX, lastY - 1, rocketZ, block.AIR.id)
    rocketY = rocketY + 1
    # A real rocket will start moving up slowly then get much faster
    # But in minecraft the world is too blocky to do this convincingly
    # so we will move up a steady one block at a time

# rub out the last rocket and flame  ready to explode
mc.setBlock(rocketX, lastY + 1, rocketZ, block.AIR.id)
mc.setBlock(rocketX, lastY, rocketZ, block.AIR.id)
# You could change this to a single line using setBlocks
# mc.setBlocks(rocketX,lastY,rocketZ,rocketX,lastY+1,rocketZ,block.AIR.id)

time.sleep(0.1)
# Draw the explosion where the rocket finished
# If the explodeHeight is too high you will not see the explosion
# if it is too low, then the explosion wil reach the ground
DrawCircles(rocketX - 2, rocketY, rocketZ)

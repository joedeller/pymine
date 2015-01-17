#! /usr/bin/python
# Joe Deller 2014
# Simulating a bouncing ball in Minecraft

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, logic


# This program simulates how a ball bounces as it hits the ground
# In the blocky world of Minecraft it isn't much of a bounce
# and the method is fairly simple, but gives you an idea of how
# we can use computer programs to model the real world

# There is a bug in this program that makes it less realistic
# See if you can find out what it is and what you might do to fix it
# Try starting up a mountain for instance, where is the ground?

# First the libraries we will need
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Make a connection to minecraft
mc = minecraft.Minecraft.create()

# Find out where we are in the world and store this for later
playerPos = mc.player.getPos()
pX = playerPos.x
pY = playerPos.y
pZ = playerPos.z

# Clean up the world and any previous circles nearby
# We will clear an area 30 both the left, right, front
# and back of where we are standing
# and 32 blocks up into the air
mc.setBlocks(pX - 30, pY, pZ - 20, pX + 30, pY + 32, pZ + 20, block.AIR.id)

# Setup a grass floor, the same size as the area we cleared, but not so high
mc.setBlocks(
    pX - 20,
    pY - 1,
    pZ - 20,
    pX + 20,
    pY - 1,
    pZ + 20,
    block.GRASS.id)

# Start the ball 12 blocks up in the air from where we are standing
# 10 blocks to the right and 10 blocks back so we can see it
x = pX - 10
y = pY + 12
z = pZ + 14


# The ball will be dropping , at a rate we choose
# We will call this "gravity", as it is acting like gravity in the real world
# try changing it to larger and smaller
# numbers, for example 0.6 or 0.1
# Can we have negative gravity ?  What happens ?
gravity = 0.3

# The variable called dY is the rate at which the height of the ball is changing
# It changes from negative to positive depending on whether we hit the
# ground or not

dY = 0.0

# We can set how many bounces we want the program to run for
# the ball will bounce less high each time
# A more realistic program would include more variables,
# such as friction, hardness of the ground, the material the ball was made
# from, but in Minecraft the effects might not be all that obvious

bounces = 4

while(bounces >= 0):
    # Our ball is a block of black wool
    mc.setBlock(x, y, z, block.WOOL.id, 15)
    time.sleep(.2)
    # if you don't want to see a trail of where the ball moves
    # then remove the "#" from the next line, making sure you line it up with the time.sleep(2) line
    #  mc.setBlock(x, y, z, block.AIR.id)

    # If you wanted to simulate wind you might change the next line to
    # x = x 0.5 for a head wind, or 1.5 for a tail wind
    # In Minecraft it's a little hard to see
    x = x + 1
    # calculate where the ball is, by subtracting our rate of gravity
    dY = dY - gravity
    y = y + dY
    # If we print out the values of y and v we can see how they change as the
    # ball bounces
    print y, dY
    # Has the ball hit the ground, if so, we will start moving upwards
    if(y <= pY):
        print "hit the ground so bouncing..."
        mc.setBlock(x, pY, z, block.WOOL.id, 15)
        # Decrease the amount of bounces left by one
        bounces = bounces - 1
        # A more sophisticated program might calculate when the ball stops bouncing as it
        # runs out of energy, rather than just a certain number of bounces
        # Multiplying a number by -1 changes a negative number into a positive
        # one , or a positive number into a negative one
        # We can use this do change the way our ball is moving
        # If our ball is falling, then v will be negative , downwards
        # if it is bouncing, then it will be positive, upwards
        dY = dY * -1.0

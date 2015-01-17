#! /usr/bin/python
# Joe Deller 2014
# A horizontal water ride

# Level : Beginner
# Uses  : Libraries, variables, operators, loops

# Note that as the ride is fairly long, the player position
# is hard set to be at x - 20, so we don't run off the edge of the
# Minecraft world, which would be bad.

# Libraries
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math


# Connect and find out where we are
mc = minecraft.Minecraft.create()
playerPos = mc.player.getTilePos()
# Set our x position to -20, so we don't run off the end of the world
px = -20
py = playerPos.y
pz = playerPos.z


# This ride is drawn flat, rather than the roller coaster up and down
# It is 120 blocks long, from -40 to +80
# The width is really the width of the sine wave
height = 16
width = 18.0
ride_start = px - 40
ride_end = px + 80

# Our water ride will be in the shape of a sine wave
# It will have black wool edges and a stone floor
# If the ride runs through any mountains, it will clear a space two blocks high
# However, if we run through anything that can fall down, like sand or gravel
# you may find that the ride gets blocked.
# The camera will still pass through the blocks 

dz = None
for dx in range(ride_start, ride_end):
    dz = (height * math.sin(float(dx) / width)) + 12
    dz = dz + pz
    mc.setBlocks(dx, py + 1, dz - 3, dx, py + 3, dz + 3, block.AIR.id)
    # The edges of the ride to hold the water in are black wool blocks
    # Change them to suit
    mc.setBlock(dx, py + 1, dz + 3, block.WOOL.id, 15)
    mc.setBlock(dx, py + 1, dz - 3, block.WOOL.id, 15)

    # Although the Pi Minecraft doesn't have night
    # If we run underground, a glowstone floor will let us see
    mc.setBlocks(dx, py, dz - 3, dx, py, dz + 3, block.GLOWSTONE_BLOCK.id)
    # Add the water, or lava if you're feeling unkind
    mc.setBlock(dx, py + 1, dz, block.WATER_STATIONARY.id)


# Make a splash pool at the start
mc.setBlocks(ride_start - 4, py - 1, dz + 2, ride_start, py + 1, dz + 9, block.STONE.id)
mc.setBlocks(ride_start - 3, py + 1, dz + 3, ride_start , py + 2, dz + 8, block.AIR.id)


# Make a splash pool at the end
mc.setBlocks(ride_end, py - 1, dz - 3, ride_end + 4, py + 1, dz + 3, block.STONE.id)
mc.setBlocks(ride_end, py + 1, dz - 2, ride_end + 3, py + 2, dz + 2, block.AIR.id)

# Put our player at the start 
mc.player.setTilePos(ride_start, py + 1, pz)
mc.postToChat("Ride starting in 6 seconds...")
time.sleep(6)

# Off we go. Notice the code is the same the code that draws the ride
# If we decided to change the shape of the ride we would have
# to change our code in two places, which normally causes bugs.
# A coder would probably change this program so that we didn't repeat
# the code

# Be careful of cutting and pasting code.  It's not that it's always bad
# but it can get you in to trouble later on in more complex programs

for cx in range(ride_start, ride_end):
    cz = ((height * math.sin(float(cx) / width)) + 12)
    cz = cz + pz
    mc.camera.setPos(cx, py + 1, cz - 1)
    time.sleep(0.1)

mc.camera.setPos(px + 79, py + 1, dz - 1)

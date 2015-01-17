#! /usr/bin/python
# Joe Deller  2014
# Use the camera to simulate a roller coaster ride

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from math import *


def checkBlockIsHit(starting_block):
    # This routine checks to see if the player hit any blocks with the mouse
    # We have a special glowstone block in the splash pool wall  and if that is hit we will
    # remove it and start our camera moving
    block_hits = mc.events.pollBlockHits()
    # Were any blocks hit ?
    if (block_hits):
        for blockHit in block_hits:
            bx, by, bz = blockHit.pos
            if (bx == starting_block.x and by == starting_block.y and bz == starting_block.z):
                # Player hit the glowstone, so ready to go
                return True
    else:
        return False


def drawCoaster(dx, current_y, starting_block):
    # Draw a splash pool at the start of our roller coaster
    # We draw a solid stone block, then hollow out with air
    mc.setBlocks(dx - 5, py, roller_z + 1, dx, py + 1, roller_z - 4, block.STONE.id)
    mc.setBlocks(dx - 4, py + 1, roller_z, dx - 1, py + 1, roller_z - 3, block.AIR.id)
    mc.setBlock(starting_block.x, starting_block.y, starting_block.z, block.GLOWSTONE_BLOCK.id)
    last_y = current_y
    # Our roller coaster will be a sine wave, from 0 to 180 degrees
    # add the extra "steps" so that it finishes at 180
    for angle in range(0, 180 + steps, steps):
        if (angle != 0):
            # convert our degrees angle in to radians to Python can use it
            last_y = sin(radians(angle - steps)) * height
            # We don't want any gaps in our sine wave, so we keep a note of the previous
            # height we drew the blocks
            last_y = int(last_y) + py

        dy = sin(radians(angle)) * height
        dy = int(dy) + py
        # Is our new height greater than one different than the last, i.e. will there be a gap ?
        # As our sine wave goes up and down, we use fabs() to get the absolute difference
        if (fabs(dy - last_y) > 1):
            # draw from the last height to the new height so there aren't any gaps
            mc.setBlocks(dx, last_y, roller_z - 3, dx, dy, roller_z, block.WOOL.id, 15)
            mc.setBlocks(dx, last_y + 1, roller_z - 3, dx, dy + 1, roller_z, block.WOOL.id, 1)
        else:
            # No gaps, so safe to draw the water, or lava if you want
            mc.setBlocks(dx, dy, roller_z - 3, dx, dy, roller_z, block.WOOL.id, 15)
            mc.setBlocks(dx, dy + 1, roller_z - 3, dx, dy + 1, roller_z, block.WOOL.id, 1)
            mc.setBlocks(dx, dy + 1, roller_z - 2, dx, dy + 1, roller_z - 1, block.WATER_STATIONARY)
        # Move to the right
        dx = dx + 1

    # Draw a splash pool at the end of our roller coaster
    mc.setBlocks(end_x + 1, py, roller_z + 1, end_x + 5, py + 1, roller_z - 4, block.STONE.id)
    mc.setBlocks(end_x + 1, py + 1, roller_z, end_x + 4, py + 1, roller_z - 3, block.AIR.id)


def rideCoaster(dx):
    # The same sine calculation as before, except this time we are moving
    # the player, rather than drawing the roller coaster
    for angle in range(0, 180 + steps, steps):
        dy = sin(radians(angle)) * height
        dy = dy + py
        # To make things a little smoother, we will move our player
        # in fractions of a block.  Try adjusting the sleep time if needed
        for move in range(1, 6):
            mc.player.setPos(dx, dy + 1, roller_z - 1)
            dx = dx + 0.2
            time.sleep(0.05)


mc = minecraft.Minecraft.create()
mc.camera.setNormal()

playerPos = mc.player.getTilePos()
px = playerPos.x
py = playerPos.y
pz = playerPos.z

# Clean up the world and any previous circles nearby
mc.setBlocks(px - 20, py, pz - 20, px + 64, py + 64, pz + 5, block.AIR)
# Setup a grass floor
mc.setBlocks(px - 24, py - 1, pz - 22, px + 64, py - 1, pz + 16, block.GRASS)

height = 16
width = 44

# The roller coaster will be 10 blocks back from where we are standing
roller_z = pz - 10

steps = int(180 / width)
end_x = px + width
#
starting_block = minecraft.Vec3(px - 5, py + 1, roller_z)

# set the starting point from where we move from
# to where the player is standing

drawCoaster(px, py, starting_block)

while (checkBlockIsHit(starting_block) is False):
    time.sleep(.5)

print "Off we go!"

mc.camera.setFixed()
mc.camera.setFollow(1)
mc.camera.setPos(px, py + 2, roller_z - 1)

rideCoaster(px)

time.sleep(2)
mc.player.setPos(px, py, pz)
mc.camera.setNormal()

#!/usr/bin/python
# Joe Deller 2014
# How to detect if a player has hit a block with their sword
# using a right click of the mouse

# Level : Beginner
# Uses  : Libraries, variables, operators, loops, lists, logic


import mcpi.minecraft as minecraft
import time


def checkBlockIsHit():
    # This routine checks to see if the player hit any blocks with the sword
    blockHits = mc.events.pollBlockHits()
    # Were any blocks hit ?
    # If so blockHits will contain a list of them, so we look at each one in turn
    if (blockHits):
        for blockHit in blockHits:
            # find out where the block we hit is
            x, y, z = blockHit.pos
            msg = "x:" + str(x) + ", y:" + str(y) + ", z:" + str(z)
            # What is the block number
            blockType = mc.getBlock(x, y, z)
            mc.postToChat("You hit a block number " + str(blockType) + "  at " + msg)
    else:
        print ("No blocks hit.")


mc = minecraft.Minecraft.create()
mc.postToChat("Draw some blocks, then right click with the sword")

for i in range(0, 500):
    checkBlockIsHit()
    time.sleep(0.5)


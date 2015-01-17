#! /usr/bin/python
# Joe Deller 2014
# Move our player around in 3 directions

# Level : Beginner
# Uses  : Libraries, operators

# We can move the player around using setTilePos(), which puts the player on a certain tile
# given by the x, y & z coordinates

import mcpi.minecraft as minecraft
import time
import mcpi.block as block

# Connect to Minecraft
mc = minecraft.Minecraft.create()

# find out where we are in the world
playerPos= mc.player.getTilePos()
x, y, z = playerPos
mc.postToChat("We start at position X:%s Y:%s Z:%s" % (x, y, z))

# clear a space so we don't end up inside anything
mc.setBlocks(x - 11, y, z - 11, x + 10, y + 12, z + 10, block.AIR.id)
# Make sure there is some grass under us, otherwise we might fall
# if we've moved into space or the sea
mc.setBlocks(x - 11, y - 1, z - 11, x + 10, y - 1, z + 10, block.GRASS.id)


mc.postToChat("About to move player 10 blocks left.")
time.sleep(5)
x = x - 10

mc.player.setTilePos(x, y, z)
mc.postToChat("Now at position X:%s Y:%s Z: %s" %(x, y, z))
time.sleep(5)


mc.postToChat("About to move player 10 blocks forward.")
time.sleep(5)

z = z - 10
mc.player.setTilePos(x, y, z)
mc.postToChat("Now at position X:%s Y:%s :%s" %(x, y, z))
time.sleep(5)

mc.postToChat("About to move player 10 blocks up.")
time.sleep(5)
y = y + 10
mc.player.setTilePos(x, y, z)
time.sleep(5)

playerPos= mc.player.getTilePos()
x, y, z = playerPos
mc.postToChat("We've finished at position X:%s Y:%s Z:%s" % (x, y, z))




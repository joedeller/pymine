#! /usr/bin/python
# Joe Deller July 2014
# Mixing lava and water.

# Level : Beginner
# Uses  : Libraries


# Don't try this at home...

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
# Find out where we are
playerPos = mc.player.getTilePos()
x = playerPos.x
y = playerPos.y
z = playerPos.z

# Clear up
mc.setBlocks(x - 10, y - 1 , z - 15, x + 15, y + 12 , z + 5, block.AIR.id)
mc.setBlocks(x - 10, y - 2, z - 15, x + 15, y - 1 , z + 5 , block.GRASS.id)
# Build a pond
mc.setBlocks(x - 5, y - 1 , z - 5 , x + 3, y -1  , z - 10, block.WATER.id)
# Wait a moment
time.sleep(2)
# Just add lava
mc.setBlock(x - 1 , y + 2, z -8 ,  block.LAVA.id)

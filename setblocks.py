#! /usr/bin/python
# Joe Deller 2014
# setBlock() draws a single block, setBlocks() draws a rectangle of blocks

# Level : Beginner
# Uses  : Libraries, variables, operators

import mcpi.minecraft as minecraft
import mcpi.block as block

# Make a connection to minecraft
mc = minecraft.Minecraft.create()

# Find out where we are in the world and store this for later
playerPos = mc.player.getTilePos()
# remember playerPos will contain the x,y & z coordinates of where we are
pX = playerPos.x
pZ = playerPos.z

# One of the first things to do is make some space for things we want to build
# There is no "flat world" option on the raspberry PI so we must make one
# Minecraft has a method called setBlocks()

# This lets you create a solid rectangle shape made from any block you choose
# Be careful with lava or water!

# setBlocks needs 6 coordinates, the X,Y,Z of where to start from
# and the X.Y,Z of where to stop
# This can sometimes be a bit slow if you are making a big shape

# To create an empty space, use BLOCK.AIR, which rubs out any blocks
# So lets start by clearing up
# an area 20 both the left, right, front and back of where we are standing
# and 64 blocks up into the air

mc.setBlocks(pX - 20, 0, pZ - 20, pX + 20, 64, pZ + 20, block.AIR.id)

# Now for something to stand on
# Setup a grass floor, the same size as the area w cleared, but not so high
mc.setBlocks(pX - 20, -4, pZ - 20, pX + 20, 0, pZ + 20, block.GRASS.id)

# Build a glass house all around us
mc.setBlocks(pX - 20, 1, pZ - 20, pX + 20, 10, pZ + 20, block.GLASS.id)
# Now hollow out the shape otherwise we are stuck inside a glass cage
mc.setBlocks(pX - 19, 1, pZ - 19, pX + 19, 9, pZ + 19, block.AIR.id)

# Finally some water in the middle, only 1 block deep
mc.setBlocks(pX - 2, 0, pZ - 2, pX + 2, 0, pZ + 2, block.WATER.id)

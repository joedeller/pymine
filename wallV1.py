#! /usr/bin/python
# Using a loop to build a single block wall of different colours
# Joe Deller 2014

# Level : Beginner
# Uses  : Libraries, variables, operators, loops

# This code draws a line of different coloured wool blocks
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
myLocation = mc.player.getTilePos()
x = myLocation.x - 8
y = myLocation.y
z = myLocation.z - 10

# Clear some space so we can see the wall.

mc.setBlocks(x, y, z - 10, x + 16, y + 4, z, block.AIR.id)

for colour in range(0, 16):
    mc.setBlock(x + colour, y, z, block.WOOL.id, colour)
    time.sleep(1)

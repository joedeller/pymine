#! /usr/bin/python
# Joe Deller 2014
# Building a high wall by using two loops

# Level : Beginner
# Uses  : Libraries, variables, operators, loops

# This program will draw a wall made of nine rows of wool blocks
# Each row will be made of 16 blocks of different coloured wool

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
myLocation = mc.player.getTilePos()
x = myLocation.x - 8
y = myLocation.y
z = myLocation.z - 10

mc.setBlocks(x, y, z - 10, x + 16, y + 9, z, block.AIR.id)

for height in range(0, 9):
    for colour in range(0, 16):
        mc.setBlock(x + colour, y + height, z, block.WOOL.id, colour)
        time.sleep(.1)

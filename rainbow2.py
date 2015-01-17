#! /usr/bin/python
# Joe Deller 2014
# A slightly more dangerous version of our Rainbow program

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, lists

import mcpi.minecraft as minecraft
import mcpi.block as block
import math


mc = minecraft.Minecraft.create()

# Find out where we are in the world
playerPos = mc.player.getTilePos()
x = playerPos.x
y = playerPos.y
# Our rainbow will be 5 blocks back from where we are standing
z = playerPos.z + 5


height = 20
width = 44
centre = width / 2
# Right click with sword and stand back

for r in range(0, width + 1):
    for current_color in range(0, 7):
        block_y = math.sin((r / float(width)) * math.pi) * height
        block_y = block_y + y
        block_y = block_y  + current_color
        mc.setBlock(x + centre - r, int(block_y), z, block.TNT,
                    1)




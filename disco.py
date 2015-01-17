#! /usr/bin/python
# Joe Deller 2014
# Simple disco flashing effect

# Level : Intermediate
# Uses  : Libraries, variables, lists, operators, loops

import mcpi.minecraft as minecraft
import mcpi.block as block
import time


def drawSquare(start_x, top):
    height = top
    for each_line in squareOne:
        for i in range(0, 8):
            # Our pattern contains either 1 or 0. We could use an if keyword 
            # to check what the block is, but if we multiply the block
            # if it is a zero, anything times zero is zero, giving us AIR (block type 0)
            # and if it is a 1, multiplying by a block type is the same as block type
            # This saves us some code, but will not always be faster
            mc.setBlock(start_x + i, height, z, int(each_line[i]) * block.GLOWSTONE_BLOCK.id)
        height = height - 1
    time.sleep(0.1)

    # Reset the height to the original value 
    height = top
    for each_line in squareTwo:
        for i in range(0, 8):
            mc.setBlock(start_x + i, height, z, int(each_line[i]) * block.GLOWSTONE_BLOCK.id)
        height = height - 1
    time.sleep(0.1)


mc = minecraft.Minecraft.create()
# Find out where we are in the world
playerPos = mc.player.getTilePos()
x = playerPos.x
y = playerPos.y
z = playerPos.z

# Store a simple checkered pattern in a list
# For this example we will have two sets of data
# This could be improved as you might notice that square two
# is the exact opposite of square one

squareOne = [
    "10101010",
    "01010101",
    "10101010",
    "01010101",
    "10101010",
    "01010101",
    "10101010",
    "01010101"]
squareTwo = [
    "01010101",
    "10101010",
    "01010101",
    "10101010",
    "01010101",
    "10101010",
    "01010101",
    "10101010"]

mc.setBlocks(x, y, z, x + 20, y + 22, z - 10, block.AIR)
mc.setBlocks(x, y - 1, z, x + 40, y - 1, z - 20, block.GRASS)
z = z - 9
width = 8
height = y + 12

mc.postToChat("Starting to flash...")
time.sleep(1)

for flashes in range(0, 200):
    drawSquare(x, height)

#! /usr/bin/python
# Joe Deller 2014
# Draw all the possible minecraft blocks in a rectangle shape

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, logic

# The raspberry Pi minecraft does not have all of the blocks
# regular minecraft has, so lets see what is available
# If the Pi can't draw a block, you will see an error message
# in the Python console

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

# Find out where we are in the world
position = mc.player.getPos()

xStart = position.x
yStart = position.y
zStart = position.z

# start drawing a little bit away from us
x = xStart
y = yStart + 1
z = zStart - 10

mc.setBlocks(
    xStart - 2,
    yStart,
    zStart,
    xStart + 16,
    yStart + 16,
    zStart - 10,
    0)

# On the Pi the highest block is number 247, a nether reactor.
# If they ever produce another version of the program there might be more
# but for now there are far less blocks than the PC version

# Our program will try 256 possible block types, we want do draw them in a square grid
# So we will make a grid 16 wide and 16 high, which gives 16 * 16, which is 256
# Each time we finish drawing one row of 16 blocks, move up one
# Block numbers that the Pi does not recognize will be empty (air)

for i in range(0, 16):
    for j in range(0, 16):
        mcBlock = j + (i * 16)
# Lava and water can really mess things up , so don't draw them !
# water is 8 and 9, lava is 10 and 11
        if (mcBlock < 8 or mcBlock > 12):
            mc.setBlock(x + j, y + i, z, mcBlock)

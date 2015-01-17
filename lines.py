#! /usr/bin/python
# Joe Deller 2014
# Drawing a line from one place to another is a not as straight forward as it might first appear



# This program uses something called Bresenham's algorithm
# which Jack Elton Breshenham wrote all the way back in 1962

import mcpi.minecraft as minecraft
import mcpi.block as block


def drawline(mc, x, y, z, x2, y2, block_type):
    # Bresenham's algorithm ,see
    # http://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

    steep = 0
    # Firstly work out how far apart the two x points are and if the first is
    # left or right of the second
    dx = abs(x2 - x)

    if (x2 - x) > 0:
        sx = 1
    else:
        sx = -1

    # Do the same for the Y coordinate, are we drawing up or down
    dy = abs(y2 - y)

    if (y2 - y) > 0:
        sy = 1
    else:
        sy = -1

    if dy > dx:
        steep = 1
        x, y = y, x
        dx, dy = dy, dx
        sx, sy = sy, sx

    d = (2 * dy) - dx
    for i in range(0, dx):
        if steep:
            mc.setBlock(y, x, z, block_type)
        else:
            mc.setBlock(x, y, z, block_type)
        while d >= 0:
            y = y + sy
            d = d - (2 * dx)
        x = x + sx
        d = d + (2 * dy)
    mc.setBlock(x2, y2, z, block_type)

mc = minecraft.Minecraft.create()

# put us in the middle of the world
mc.player.setPos(0, 2, 0)

width = 62
# Clean up the world and any previous drawings nearby
mc.setBlocks(-10, 0, -20, width, 40, 20, block.AIR.id)
# Setup a grass floor
mc.setBlocks(-10, 0, -20, width, 1, 20, block.GRASS.id)

z = 0
drawline(mc, 0, 1, z, 12, 12, block.SANDSTONE.id)
drawline(mc, 12, 12, z, 24, 12, block.SANDSTONE.id)
drawline(mc, 25, 12, z, 36, 1, block.SANDSTONE.id)

z = 1
drawline(mc, 0, 1, z, 12, 13, block.SANDSTONE.id)
drawline(mc, 12, 13, z, 24, 13, block.SANDSTONE.id)
drawline(mc, 25, 13, z, 36, 1, block.SANDSTONE.id)

drawline(mc, 0, 1, z, 12, 14, block.SANDSTONE.id)
drawline(mc, 12, 14, z, 24, 14, block.SANDSTONE.id)
drawline(mc, 25, 14, z, 36, 1, block.SANDSTONE.id)

z = -1
drawline(mc, 0, 1, z, 12, 13, block.SANDSTONE.id)
drawline(mc, 12, 13, z, 24, 13, block.SANDSTONE.id)
drawline(mc, 25, 13, z, 36, 1, block.SANDSTONE.id)

drawline(mc, 0, 1, z, 12, 14, block.SANDSTONE.id)
drawline(mc, 12, 14, z, 24, 14, block.SANDSTONE.id)
drawline(mc, 25, 14, z, 36, 1, block.SANDSTONE.id)


z = 0
drawline(mc, 0, 1, z, 12, 12, block.SANDSTONE.id)
drawline(mc, 12, 12, z, 24, 12, block.SANDSTONE.id)
drawline(mc, 25, 12, z, 36, 1, block.SANDSTONE.id)

drawline(mc, 0, 1, z, 12, 13, block.WATER.id)
drawline(mc, 12, 13, z, 24, 13, block.WATER.id)
drawline(mc, 25, 13, z, 36, 1, block.WATER.id)

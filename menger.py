#! /usr/bin/python

# Joe Deller July 2014
# Draw a Menger cube, or sponge.

# Level: Advanced
# Uses  : Libraries, variables, recursion

# http://mathworld.wolfram.com/MengerSponge.html

# A much more complex recursion
# The mathematics is covered in many places on the web and there are several
# versions of this code by many people, including Minecraft versions
# This is a fairly simple version of the very complex shape.
# I've just simplified the code.  A bit.

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

def MengerSponge(x, y, z, levels):
    # when levels is equal to zero, we actually draw something and exit
    # it's the way out of our recursion calls
    # For the Pi, we will only be starting at level 2 or 3
    # If you want to use a different material, change it here
    if (levels == 0):
        mc.setBlock(x, y, z, block.WOOD_PLANKS)
    else:

        MengerSponge(x, y, z, levels - 1)
        # ** means "to the power of", again something you will probably cover
        # in Secondary level school
        # if levels was 3, then (levels -1) is 2
        # then this would be the same as doing
        # s = 3 * 3, three to the power of two
        # If levels is 2, then s would be 3
        # If levels is 1 then s would be 1
        s = 3 ** (levels - 1)

        MengerSponge(x, y, z + 1 * s, levels - 1)
        MengerSponge(x, y, z + 2 * s, levels - 1)

        MengerSponge(x, y + 1 * s, z, levels - 1)
        MengerSponge(x, y + 2 * s, z, levels - 1)

        MengerSponge(x, y + 1 * s, z + 2 * s, levels - 1)

        MengerSponge(x, y + 2 * s, z + 1 * s, levels - 1)
        MengerSponge(x, y + 2 * s, z + 2 * s, levels - 1)

        MengerSponge(x + 1 * s, y, z, levels - 1)
        MengerSponge(x + 1 * s, y, z + 2 * s, levels - 1)

        MengerSponge(x + 1 * s, y + 2 * s, z, levels - 1)
        MengerSponge(x + 1 * s, y + 2 * s, z + 2 * s, levels - 1)

        MengerSponge(x + 2 * s, y, z, levels - 1)

        MengerSponge(x + 2 * s, y + 1 * s, z, levels - 1)
        MengerSponge(x + 2 * s, y + 2 * s, z, levels - 1)

        MengerSponge(x + 2 * s, y, z + 1 * s, levels - 1)
        MengerSponge(x + 2 * s, y, z + 2 * s, levels - 1)

        MengerSponge(x + 2 * s, y + 1 * s, z + 2 * s, levels - 1)

        MengerSponge(x + 2 * s, y + 2 * s, z + 1 * s, levels - 1)
        MengerSponge(x + 2 * s, y + 2 * s, z + 2 * s, levels - 1)


playerPos = mc.player.getTilePos()
x, y, z = playerPos
mc.setBlocks(x -1, y, z - 1, x - 40, y + 46, z - 50, block.AIR.id)
# Levels controls how complex and large our shape is
# going beyond 3 gets a bit tricky and slow.

levels = 2
MengerSponge(x + 6, playerPos.y, playerPos.z - 10, levels)

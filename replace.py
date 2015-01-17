#! /usr/bin/python
# Joe Deller 2014
# Replace all of the blocks of type in the  specified area in with another

# Level : Intermediate
# Uses  : Libraries, loops, operators


# Have you every built a minecraft house and then changed your mind
# about what the color or material should be ?

# First you will need to find the coordinates of your building
# Make a note of them and change the start and stop variables
# here, say what you want changed and what you want it changed to


import mcpi.minecraft as minecraft
import mcpi.block as block


def replaceBlocks():
    # First the block we want to replace
    original_block = block.IRON_BLOCK.id
    # now the block that will take its place
    new_block = block.GOLD_BLOCK.id

    # Tell the program the area we want to replace blocks
    # the start number should be the smaller number

    x_start = 10
    x_stop = 38

    y_start = 0
    y_stop = 12

    z_start = 12
    z_stop = 20

    # Three loops that will move across, back then up the area specified
    for y in range(y_start, y_stop + 1):
        for z in range(z_start, z_stop + 1):
            for x in range(x_start, x_stop + 1):
                current_block = mc.getBlock(x, y, z)
                if (current_block == original_block):
                    mc.setBlock(x, y, z, new_block)
#            print b.id,b.data

mc = minecraft.Minecraft.create()
replaceBlocks()

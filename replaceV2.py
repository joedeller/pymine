#! /usr/bin/python
# Joe Deller 2014
# Replace all of the blocks of type in the  specified area in with another

# Level : Intermediate
# Uses  : Libraries, loops, operators


# The first version of our replace block code changed one block for another

# This version will allow you to change the color, or type of block
# To do this we need the getBlockWithData method, to find the extra
# information about the block

# You could modify it to replace a certain color of wool block
# with a different block, not just another color of wool

# First you will need to find the coordinates of your building
# Make a note of them and change the start and stop variables
# here, say what you want changed and what you want it changed to


import mcpi.minecraft as minecraft
import mcpi.block as block


def replaceBlocks():
    # First the block we want to replace
    original_block = block.WOOL.id
    # for wool blocks, the data is color, for others it might be the type of stone
    # or way the block is facing.
    # In this example, white wool blocks are going to be replaced with black wool blocks
    # This runs pretty slowly
    old_data = 0
    new_data = 15

    # Tell the program the area we want to replace blocks
    # the start number should be the smaller number

    x_start = 60
    x_stop = x_start + 28

    y_start = 0
    y_stop = 12

    z_start = 21
    z_stop =  40

    # Three loops that will move across, back then up the area specified
    for y in range(y_start, y_stop + 1):
        for z in range(z_start, z_stop + 1):
            for x in range(x_start, x_stop + 1):
                current_block = mc.getBlockWithData(x, y, z)
                if (current_block.id == original_block and current_block.data == old_data):
                    mc.setBlockWithData(x, y, z, original_block,new_data)
#

mc = minecraft.Minecraft.create()
replaceBlocks()

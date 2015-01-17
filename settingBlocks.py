#! /usr/bin/python
# Joe Deller 2014
# Floating lava lamp

# Level : Beginner
# Uses  : Libraries, operators

# Coding lets us do some fun things that aren't as easy to do by hand
# We can put a block of lava inside glass that is floating in the air


import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to Minecraft
mc = minecraft.Minecraft.create()
# Get our position in the world
x, y, z = mc.player.getTilePos()
mc.setBlocks(x + 1, y + 5, z - 5, x + 3, y + 6, z - 7, block.GLASS.id)
mc.setBlock(x+ 2, y + 6, z - 6, block.LAVA.id)

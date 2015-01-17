#! /usr/bin/python
# Joe Deller 2014
# Clearing a space around us

# Level : Beginner
# Uses  : Libraries, variables

# Firstly our minecraft library
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to minecraft
mc = minecraft.Minecraft.create()

# Find out where we are in the world
playerPos = mc.player.getTilePos()
x = playerPos.x
y = playerPos.y
z = playerPos.z

# Clean a space all around us, twenty blocks in each direction
# but not below us, try changing the y + 20 to y - 20 and see what happens
mc.setBlocks(x - 20, y, z - 20 , x + 20, y + 20, z + 20, block.AIR)

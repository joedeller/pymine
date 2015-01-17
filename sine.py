#! /usr/bin/python
# Joe Deller 2014
# Drawing a sine wave

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops


# Minecraft might not be the best program to demonstrate trigonometry
# but it can be done
# This code uses the Sine function to draw a sine wave
# We will be using this shape later on to draw a rainbow


import mcpi.minecraft as minecraft
import mcpi.block as block
import math

mc = minecraft.Minecraft.create()
playerPos = mc.player.getPos()
player_x = playerPos.x - 10
player_y = playerPos.y
player_z = playerPos.z - 5

width = 62
height = 14

mc.setBlocks(player_x - width, player_y, player_z - 14, player_x + width, player_y + (height * 2), player_z + 12, block.AIR.id)
# Setup a grass floor, the same size as the area we cleared, but not so high
mc.setBlocks(player_x - 20, player_y-1, player_z - 20, player_x + 20, player_y - 1, player_z + 20, block.GRASS.id)


# sine time, we draw an axis in stone and the sine wave in wool
# experiment with the height and width
# for height in range (0,height):
for dx in range(0, width):
    mc.setBlock(player_x + dx , player_y + height, player_z, block.STONE.id)
    dy = (height * math.sin(float(dx) / 10)) + height + 2
    mc.setBlock(player_x+ dx, player_y + dy, player_z, block.WOOL.id)

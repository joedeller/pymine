#! /usr/bin/python
# Joe Deller 2014
# Minecraft is all about blocks, so let's starting using them

# Level : Beginner
# Uses  : Libraries, variables, operators


# For this we need another library mcpi.block that knows all about them

import mcpi.minecraft as minecraft
import mcpi.block as block

# Make a connection to minecraft
mc = minecraft.Minecraft.create()


# Minecraft on the Raspberry Pi has a lot less blocks compared to other versions
# but it still has a lot.  Each block has a number that tells minecraft what block to draw
# Remembering all the numbers would get pretty tricky, so the block
# library can also use names

# To draw a block in minecraft, we use the setBlock() method.
# To use this, we need to tell it where and what block to draw
# Lets start by finding where we are and then putting a treasure chest
# right in front of us

# Find out where we are in the world and store this for later
playerPos = mc.player.getTilePos()
# remember playerPos will contain the x,y & z coordinates of where we are
player_x = playerPos.x
player_y = playerPos.y
player_z = playerPos.z


# Clear some air around us
mc.setBlocks(player_x - 5, player_y, player_z - 5, player_x + 5, player_y + 5, player_z + 5)
# You might need to turn around to see it depending on which way you are facing
# We will draw the block two blocks away from where we are standing
mc.setBlock(player_x, player_y, player_z + 2, block.CHEST.id)



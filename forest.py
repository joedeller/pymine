#! /usr/bin/python
# Joe Deller 2014
# Draw a simple forest using loops

# Level : Beginner
# Uses  : Libraries, variables, operators, loops


import mcpi.minecraft as minecraft
import mcpi.block as block
import random

# Draw a simple tree, with a certain width of leaves

def DrawTree(x, y, z, height, leaf_width):
    # The bottom two layers
    leaves = leaf_width / 2
    mc.setBlocks(
        x - leaves - 1,
        y + height + 1,
        z - leaves - 1,
        x + leaves + 1,
        y + height + 2,
        z + leaves + 1,
        block.LEAVES.id)
    mc.setBlocks(
        x - 1,
        y + height + 3,
        z,
        x + 1,
        y + height + 4,
        z,
        block.LEAVES.id)
    mc.setBlocks(
        x,
        y + height + 3,
        z - 1,
        x,
        y + height + 4,
        z + 1,
        block.LEAVES.id)
    # Draw the trunk last, from the ground up
    mc.setBlocks(x, y - 1, z, x, y + height + 2, z, block.WOOD.id)


def GrassLand(x, y, z):
    mc.setBlocks(x - 34, y - 1, z - 24, x + 30, y - 1, z + 32, block.GRASS.id)
    mc.setBlocks(x - 40, y, z - 40, x + 40, y + 60, z + 40, block.AIR.id)


# START HERE...
mc = minecraft.Minecraft.create()

# Get and store the player position
playerPos = mc.player.getTilePos()

player_x = playerPos.x
player_y = playerPos.y
player_z = playerPos.z

# First draw some grass where the player is standing
GrassLand(player_x, player_y, player_z)

# We have two loops, drawing one line of tress across the X axis, then down the Z axis
# As we want out trees to be spaced out, we count up in eights
# Reduce this number if you want a thicker forest
# We also use the random library so that our trees are different heights
# and have different numbers of leaves
# Our tree drawing code is fairly simple, so we get more of a plantation
# than a forest.

# Remember, for loops count from the first number, up to, but not including, the second
# So this loop will count 0,8,16,32,40,48,56,64,72,80
# This gives us 10 trees
for tree_x in range(0, 88, 8):
    # This loop will count 8,16,32,40,48,56,64,72,80,88
    # Still 10 trees
    for tree_z in range(8, 96, 8):
        tree_height = random.randint(3, 8)
        leaf_blocks = random.randint(2, 3)
        DrawTree(player_x + tree_x, player_y, player_z - tree_z, tree_height, leaf_blocks)

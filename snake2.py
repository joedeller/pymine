#! /usr/bin/python
# Joe Deller 2014
# Draw a simple spiral snake

# Level : Advanced
# Uses  : Libraries, variables, operators, functions, loops, recursion

# This program uses a coding technique called recursion
# which is a very powerful, if tricky, way of coding
# We have a some code in a function, that as part of its code calls itself
# It is a special kind of loop
# We have to make sure our function can finish, otherwise it will never end

# A spiral is a shape that gets larger or smaller each time we draw
# the next part of it, but the shape is still the same
# Think about how you draw a square spiral, you move your pen left, down, right, then up
# You repeat this, either drawing longer lines each time, or shorter ones, until you
# have finished the shape
# This makes our spiral drawing code a good candidate for recursion

# If you make a programming mistake using recursion,
# you can quickly run into trouble and leave your code in a maze with no
# way out


import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# start = top left
# snake goes right (width), then down (height - 1), then  left (width)
# then up (height)


def snake(x, y, z, width, height, color, first):
    # firstly check that we aren't being asked to draw a color that doesn't exist
    # Mistakes sometimes happen and checking is generally a good idea
    if (color > 15 or color < 0):
        color = 0

# Once the spiral starts to shrink, we need to draw an extra block in the top left corner
# otherwise there will be a gap
# try altering the code by commenting out the next two lines and seeing
# what happens
# The "first" variable is a special type of message, or "flag"
# that is used to make sure we only fill in the top left corner once
# even though we are in a loop

    if (first == 0):
        mc.setBlock(x - 1, y, z, block.WOOL.id, color)

# GOING RIGHT
    for x1 in range(x, x + width):
        mc.setBlock(x1, y, z, block.WOOL.id, color)
# Each time we change direction, the spiral will change color
# you could choose a different block instead of a wool color
# Notice that the program has to check the color each time
# We could put this into a separate piece of code
# called changeColor and then do something like
# color = changeColor(color)

    color = color + 1
    if (color > 15):
        color = 0

# GOING DOWN
    for y1 in range(y, y - height - 1, -1):
        mc.setBlock(x + width, y1, z, block.WOOL.id, color)
    color = color + 1
    if (color > 15):
        color = 0

# GOING LEFT
    for x1 in range(x + width, x, -1):
        mc.setBlock(x1, y - height, z, block.WOOL.id, color)

# GOING UP
    color = color + 1
    if (color > 15):
        color = 0

    for y1 in range(y - height, y - 1):
        mc.setBlock(x, y1, z, block.WOOL.id, color)
    color = color + 1

# As our spiral goes around it steps right one, down one and gets smaller by 4 blocks
# For the next part of the spiral, we need some code that draws a spiral
# which we have just written, so we call it again, but this time it will start drawing
# in a new place and be smaller
# when the next spiral to be drawn is less than three blocks wide, stop!
# If your code doesn't have some way of finishing, then your program can
# get into trouble

    if (width > 3):
        snake(x + 2, y - 2, z, width - 4, height - 4, color, 0)


def main():
    mc = minecraft.Minecraft.create()
    # Find out where we are in the world
    playerPos = mc.player.getTilePos()
    x = playerPos.x
    y = playerPos.y
    z = playerPos.z

    # clean up some space around us and make sure we have some grass to stand on
    mc.setBlocks(x - 2, y, z, x + 20, y + 22, z - 10, block.AIR)
    mc.setBlocks(x, y - 1, z - 10, x + 40, y - 1, z + 10, block.GRASS)
    # The spiral will be 10 blocks back from where we are standing
    z = z - 10
    height = 16
    # Make sure the spiral is above the ground
    y = height + 4
    # For now lets make our spiral square
    width = height
    # Start drawing, remembering to tell the snake method that this is the first
    # time we are calling it
    snake(x, y + height, z, width, height, 1, 1)

    # for loops in range (0,100):
    for color in range(0, 15):
        snake(x, y + height, z, width, height, color, 1)


# This is a slightly different way of starting our program
# that you might see used in other Python programs
# Our program works exactly the same way as all the others
# but more complex programs you might see will use this way
# of starting a program

if (__name__ == "__main__"):
   mc = minecraft.Minecraft.create()
   main()

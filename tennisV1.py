#! /usr/bin/python
# Joe Deller 2014
# Comparing things and bouncing things around

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, logic

# Most programs use some kind of tests or checks to decide
# what or when to do something, or not do something.

# This might be testing something is the same, or equal to something
# smaller or larger

# The technical term for the way code does this is called
# using comparative operators
# You may not have heard them called this, but "+" "-" "*" are all operators
# In the sum 5 + 7 , the plus sign "operates" on the two numbers and gives us
# the answer 12.

# In coding, some common comparative operators are:
#  ">" greater (larger) than
# "<" less (smaller) than
# "==" is the same as , or is equal to
# "!=" is not the as , or not equal to

# We can combine the "=" sign with greater and less than to make
# ">=" greater or equal to
# "<=" less or equal to

# This program uses the greater or equal to and less than or equal to operators
# to decide which way a square should move a board
# much like an old 1970's video game console

# Firstly our minecraft library
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Connect to minecraft
mc = minecraft.Minecraft.create()

# Find out where we are in the world
playerPos = mc.player.getTilePos()
x = playerPos.x
y = playerPos.y
z = playerPos.z

# Set the board back a bit so we can see it
z = z - 10
x = x - 6
# our board is going to be a rectangle, 18 high and 24 wide
# It will rest on the ground

top = y + 18
right = x + 24
left = x
bottom = y

# Clean a space for us to be able to see the board
mc.setBlocks(x - 14, y, z, x + 34, y + 22, z + 10, block.AIR)
mc.setBlocks(x - 14, y - 2, z, x + 24, y - 1, z - 20, block.GRASS)

# Draw the board
mc.setBlocks(x, bottom, z, right, top, z, block.WOOL.id, 15)

# Set the direction our block will be going
# we have two variables, one for the X direction and one for the Y direction
# if xDir is 1 then we move right
# if xDir is -1 then we move left
# if yDir is 1 then we move up
# if yDir is -1 then we move down

xDir = 1
yDir = 1

# The block that will move around  will start in the bottom left corner of
# the board
ballX = x
ballY = y
ballZ = z

# Draw the ball, a white wool block
mc.setBlock(ballX, ballY, ballZ, block.WOOL.id, 0)


# We will do 400 moves across the board
for i in range(0, 400):
    # rub out the ball first by setting it back to black
    mc.setBlock(ballX, ballY, ballZ, block.WOOL.id, 15)

    # before we move our block, check to see if it has hit
    # any of the edges of the board
    # You could just check to see if the current position is equal to any of the edges
    # but what if your block were moving more than one square at a time, it might have
    # already escaped the edge of the board
    # Checking for greater or equal to, or less than equal to will help
    # prevent bugs

    # Think about a program that was checking if you had enough money to buy something
    # If the item costs five pounds and you have ten, then you have enough money
    # but if the program only checked to see if you have exactly five pounds, it would
    # think you cannot buy the item
    # If the program checked to see if you have five pounds or more, the amount you have
    # is greater or equal to what the item costs, then you can buy it

    # Is our ball at the right hand side of the board?
    # If so, then we will set our X direction variable so that we will move left
    if (ballX >= right):
        xDir = -1

    # what about the left ?
    # if so, set the x direction variable so that we will move right
    if (ballX <= left):
        xDir = 1

    # Has our ball hit the top?
    if (ballY >= top):
        yDir = -1

    # What about the bottom ?
    if (ballY <= bottom):
        yDir = 1

    # The xDir and yDir will set which way the block is moving
    # We currently only move it one block at a time in each direction
    # This makes it look fairly smooth, but try changing the "1" and "-1" to
    # "2" and "-2"

    ballX = ballX + xDir
    ballY = ballY + yDir
    mc.setBlock(ballX, ballY, ballZ, block.WOOL.id, 0)
    # a tiny short wait helps us see the block moving
    time.sleep(0.05)

mc.postToChat("Finished bouncing.")

#! /usr/bin/python
# Joe Deller  2014
# Comparing things and bouncing things around

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, logic, methods

# Simulate a game of pong between two computer players
# In this case, the players will always "hit" the ball

# Start with libraries we need
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random


def moveBatDown(bat_x, bat_y, bat_z):
    # Our bat is made up of three blocks of color
    # If the bottom of the bat is already at the bottom of the board
    # then we cannot move it further down, so we need to check for this
    # If we can move the bat down, we need to rub out the current top
    # part of the bat

    # Don't try and draw the bat off the edges of the board
    # It's a good idea to check these things
    # defensive coding, if we are asked to draw above or below the board
    # just draw the bat at the top or bottom
    if (bat_y + 1 > top):
        bat_y = top - 1

    if (bat_y - 1 < bottom):
        bat_y = bottom + 1

    mc.setBlocks(bat_x, bat_y - 1, bat_z, bat_x, bat_y + 1, bat_z, block.WOOL.id, 2)
    mc.setBlock(bat_x, bat_y + 2, bat_z, block.WOOL.id, 15)


def moveBatUp(bat_x, bat_y, bat_z):
    # The same as moving the bat down, check that we aren't being
    # asked to draw the bat somewhere silly
    if (bat_y - 1 < bottom):
        bat_y = bottom + 1

    if (bat_y + 1 > top):
        bat_y = top - 1

    mc.setBlocks(bat_x, bat_y - 1, bat_z, bat_x, bat_y + 1, bat_z, block.WOOL.id, 2)
    mc.setBlock(bat_x, bat_y - 2, bat_z, block.WOOL.id, 15)

# Start here.
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
width = 24

right = x + width
left = x
bottom = y
top = bottom + 18

# Clean a space for us to see and draw a grass floor
mc.setBlocks(
    left - 5,
    bottom,
    z + 5,
    right + 5,
    bottom + 22,
    z - 10,
    block.AIR)

mc.setBlocks(
    left,
    bottom - 1,
    z + 5,
    right + 1,
    bottom - 1,
    z - 20,
    block.GRASS)

# Draw the board
mc.setBlocks(left, bottom, z, right, top, z, block.WOOL.id, 15)
middle = top / 2

# The ball will start in the middle left side of the board
ballX = x
ball_y = middle
ball_z = z

# As the ball bounces from one side to the other it will move up and down
# in fractions of a block, so we need a special type of variable
# called a "float" to store how fast the block is moving up or down
# A float comes from the term floating point, where numbers have a decimal place in them
# Decimals can be tricky things for computers as well as people

y_slope = 0.0

right_bat_y = middle / 2
left_bat_y = middle / 2

moveBatUp(left, left_bat_y, z)
moveBatUp(right, right_bat_y, z)

time.sleep(1)

# We will have 100 bounces between the bats
for i in range(0, 100):
    # We have two loops , one to move the ball from the left to the right, moving the right bat up or down
    # the second moves the ball back from right to left, moving the left bat up or down
    # We need to stop the ball as it reaches the bat, otherwise it will ruin
    # the illusion of bouncing off it

    # Start by choosing where the ball is going to end up, somewhere random between the bottom and top of the board
    # The slope is the difference between the two, divided by the width of the board
    # If you think of where the ball is on one side of the board, then where it is going
    # on the other side, you can picture a right angled triangle, except in the case where the ball moves
    # across in a straight line
    y_target = random.randint(bottom, top)
    y_slope = float((y_target - ball_y) / width)

    # if you want the ball to move faster, change the for loop to move in steps of 2
    # A more complicated program might vary the speed, in the same way it would in real life,
    # due to air, wind and gravity having an effect
    # In Minecraft it would be hard to show this accurately, so we wont :-)

    for x1 in range(left + 1, right - 1, 1):
        ball_y = ball_y + y_slope
        mc.setBlock(x1, round(ball_y), ball_z, block.WOOL.id, 0)
        time.sleep(0.04)
        mc.setBlock(x1, round(ball_y), ball_z, block.WOOL.id, 15)
    
        # Now do we need to move our bat up or down?

        if (int(ball_y) < right_bat_y):
            right_bat_y = right_bat_y - 1
            moveBatDown(right, right_bat_y, z)
        elif(int(ball_y) > right_bat_y):
            right_bat_y = right_bat_y + 1
            moveBatUp(right, right_bat_y, z)

    # Next loop, exactly the same, except in the other direction
    # our loop counts backwards in steps of -1

    y_target = random.randint(bottom, top)
    y_slope = float(y_target - ball_y) / (width)

    for x1 in range(right - 1, left + 1, -1):
        ball_y = ball_y + y_slope

        mc.setBlock(x1, round(ball_y), ball_z, block.WOOL.id, 0)
        time.sleep(0.04)
        mc.setBlock(x1, round(ball_y), ball_z, block.WOOL.id, 15)

        if (int(ball_y) < left_bat_y):
            left_bat_y = left_bat_y - 1
            moveBatDown(left, left_bat_y, z)
        elif(int(ball_y) > left_bat_y):
            left_bat_y = left_bat_y + 1
            moveBatUp(left, left_bat_y, z)

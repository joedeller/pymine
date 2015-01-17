#! /usr/bin/python
# Joe Deller 2014
# New items - string slicing and using named variables (no constants in python)

# Level : Advanced
# Uses  : Libraries, variables, operators, loops, lists

# A blast from the 1980's childhood past
# Jet Set Willy was a popular zx spectrum game featuring  a character called Jet Set Willy
# who had to clean up his mansion before he was allowed to go to bed
# Life was hard in those days....

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Animating on a computer has many things in common with traditional hand drawn animation
# with a key differences, the main one is that not only do we have to draw our pictures,
# but we have to rub them out too.   In traditional film animation, you
# only had to do the drawing.

# Just like the original game, the character is made up of rows of dots called bitmap, a series of 1s and 0s
# I've used four frames to animate the character, standing, starting to
# move , moving with arms and legs out fully and then starting to stop

# I created the data using a spreadsheet, as finding the original data was proving tricky.
# The data is for the character facing to the left
# As moving right is just a mirror image, we can get the computer to work
# out the data for facing right, rather than have to do it ourselves

# I was hoping that using binary format might speed things up a bit to save having to convert from hex
# but it's still pretty slow
# A professional programmer will probably have done some timing benchmarks to see what the difference actually is
# but for now we have to accept it's just pretty slow on the Raspberry Pi

# To make the character walk, we draw him standing still, starting to move his arms and legs, then fully moving
# then getting ready to stop

# The character is surrounded by a blank space to save  having to rub out blocks as we move
# The animation is not very smooth on a raspberry pi, but enough to show the ideas.
# Smaller figures will be a little bit smoother, but we're not going to be winning any Oscars
# You could try changing this code to work directly on the raspberry pi
# using something called Pygame, but that's for another club....


def drawFrame(x, y, z, frame_data):
    width = 12
    # We draw the character from the top downwards, one line at a time
    # If we have a "0" we draw a block of air a "1" draws a block of stone
    # if you want to use a different block try something like the following :
    # mc.setBlock(x+i,y,z,int(line[i])*block.DIAMOND_BLOCK.id)
    for line in frame_data:
        for i in range(0, width):
            mc.setBlock(x + i, y, z, int(line[i]))
        y = y - 1
    # Adjust the sleep or take it out depending on how fast or slow
    # your Pi is
    # time.sleep(.1)


def moveMe(x, y, z, direction):
    # we need to choose which set of data to use to animate our character
    # if we set "left" to 1, then we will use the left facing frames
    # otherwise we will use the ones facing right
    # Our character is 16 rows high, so to draw the figure
    # so the feet are on the ground we add 15 to our current position
    # If we wanted to, we could keep the frames in a list and use that rather than
    # call drawFrame several times.
    # For now, we will keep it simple
    height =  y + 15
    if (direction == LEFT):
        x = x + direction
        drawFrame(x, height, z, standing_left)
        x = x + direction
        drawFrame(x, height, z, starting_left)
        x = x + direction
        drawFrame(x, height, z, moving_left)
        x = x + direction
        drawFrame(x, height, z, stopping_left)
    else:
        direction = RIGHT
        x = x + direction
        drawFrame(x, height, z, standing_right)
        x = x + direction
        drawFrame(x, height, z, starting_right)
        x = x + direction
        drawFrame(x, height, z, moving_right)
        x = x + direction
        drawFrame(x, height, z, stopping_right)

# The data needed to draw the character is stored in 4 lists,
# it was easier to do this when I was drawing the character in my spreadsheet
# There are other ways you could use
# Note that I have deliberately put the information on single lines
# as a way of visually checking all the frames had the same amount
# of data and each piece was the same length.  You don't have to do this.

# A more advanced program might read this information from a file
# so that it could be modified more easily and our program could use
# different characters

# If you look carefully, you might be able to see the shape of the character

standing_left = [
    "000001111000",
    "000001111000",
    "000011111100",
    "000001011000",
    "000011111000",
    "000001111000",
    "000000110000",
    "000001111000",
    "000011101100",
    "000011101100",
    "000011101100",
    "000011001100",
    "000001111000",
    "000000110000",
    "000000110000",
    "000001110000"]
starting_left = [
    "000001111000",
    "000001111000",
    "000011111100",
    "000001011000",
    "000011111000",
    "000001111000",
    "000000110000",
    "000001111000",
    "000011111100",
    "000011111100",
    "000111011110",
    "000110111110",
    "000001111000",
    "000011011100",
    "000011101100",
    "000111011100"]
moving_left = [
    "000011110000",
    "000111111000",
    "000111111000",
    "000010110000",
    "000111110000",
    "000011110000",
    "000001100000",
    "000011110000",
    "000111111000",
    "001111111100",
    "011111111110",
    "011011110110",
    "000111110000",
    "010110111000",
    "011100001100",
    "001100011100"]
stopping_left = [
    "000011110000",
    "000011110000",
    "000111111000",
    "000010110000",
    "000111110000",
    "000011110000",
    "000001100000",
    "000011110000",
    "000111111000",
    "000111111000",
    "001110111100",
    "001101111100",
    "000011110000",
    "000110111000",
    "000111011000",
    "001110111000"]

# We can save ourselves some typing as the character moving right
# is the mirror image of moving left, so if we reverse our data
# We can use that instead.  To reverse a string in python,
# we can use something called "Extended Slices"
# which takes the form  [start:finish:step]
# If you miss out the start and finish part, python assumes you mean start at the first character  and stop at the last
# a step of -1 means go backwards, so effectively [::-1] means take what you give me and reverse it
# Some languages have more friendly functions to to this called "reverse"
# Creating a mirror image now will save us time later on, we only need to do this the once as
# the information does not change

# Create an empty list
standing_right = []
# for every row of block data, reverse the information and add it to our list
for line in standing_left:
    standing_right.append(line[::-1])

# Now do the same for the remaining frames
starting_right = []
for line in starting_left:
    starting_right.append(line[::-1])

moving_right = []
for line in moving_left:
    moving_right.append(line[::-1])

stopping_right = []
for line in stopping_left:
    stopping_right.append(line[::-1])

# Connect to Minecraft and find out where we are
mc = minecraft.Minecraft.create()
playerPos = mc.player.getTilePos()
x, y, z = playerPos.x, playerPos.y, playerPos.z

# We will draw a black wool screen to help show the animation
# but set it back 16 blocks so we can see it
z = z -20

mc.setBlocks(x - 30, y, z - 22, x + 40, y + 22, z + 20, block.AIR.id)
mc.setBlocks(x - 30, y - 1, z - 20, x + 30, y - 1, z + 20, block.GRASS.id)
mc.setBlocks(x - 25, y, z, x + 25, y + 16, z, block.WOOL.id, 15)


# To help make our code more readable, we sometimes use words to help make clear what a number means
# In other programming languages there are special variables called constants that are used for this
# Unfortunately python doesn't have a direct equivalent, but we can still
# do something similar

RIGHT = 1
LEFT = -1

# Each time we draw our character, four frames are drawn, each moving 1 block left or right at a time
# Once the four frames have been drawn, the next animation needs to start 5 blocks to the left or right
# from where we started
#
# moving left means moving negatively along the X axis, from a small negative number to a bigger negative number
# moving right means moving the other way

# Our character will be one block forward from the wool screen
# We will move a total of 40 blocks left, then back 40 to the right
# These values mean we can see most of the animation
for i in range(15, -25, -5):
    moveMe(playerPos.x + i, y, z + 1, LEFT)
#    time.sleep(.1)


time.sleep(1)
for i in range(-25, 15, 5):
    moveMe(playerPos.x + i, y, z + 1, RIGHT)
    time.sleep(.1)

#! /usr/bin/python
# Joe Deller 2014
# A simple colour version of the jsw.py code
# Level : Advanced
# Uses  : Libraries, variables, operators, loops, lists


import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# In this version there are only three frames of animation


def drawFrame(x, y, z, frame_data):
    width = 12
    # We draw the character from the top downwards, one line at a time
    # Quick hack from the V1 of this code.
    # We will allow a coloured wool block, from 2-9
    # A "0" still means an empty AIR block
    # a 1 still means a STONE block
    # Python doesn't have a switch / case keyword, which is a pity
    # Could use a dictionary

    for line in frame_data:
        for i in range(0, width):
            colour = int(line[i])
            if (colour < 2):
		# We cheat a little, as zero is the same as block.AIR
		# and a "1" is a stone block, we can just use colour 
		# as the block number.  This is generally not a good idea
		# and can make code fragile.  However, sometimes it
		# just makes sense to do things like this
               # if (colour == 0):
                    mc.setBlock(x + i, y, z, colour)
                #else:
                 #   mc.setBlock(x + i, y, z, block.STONE.id)
            else:
                mc.setBlock(x + i, y, z, block.WOOL.id,colour)
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

    # Modified from the version 1 of this code
    # We only actually have 3 frames of animation
    # we reuse the "starting left" frame
    height =  y + 15
    if (direction == LEFT):
        x = x + direction
        drawFrame(x, height, z, standing_left)
        drawFrame(x, height, z, starting_left)
        x = x + direction
        drawFrame(x, height, z, moving_left)
        x = x + (direction * 2)
        drawFrame(x, height, z, starting_left)
       #  x = x + (direction * 1)
        x = x + direction

    else:
        direction = RIGHT
        x = x + direction
        drawFrame(x, height, z, standing_right)
        #x = x + direction
        drawFrame(x, height, z, starting_right)
        x = x + direction
        drawFrame(x, height, z, moving_right)
        x = x + ( direction * 2 )
        drawFrame(x, height, z, starting_right)

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

moving_left = [
    "000333300000",
    "000333300000",
    "002222220000",
    "000404400000",
    "004444400000",
    "000444400000",
    "000044000000",
    "000111100000",
    "001111110000",
    "011111111000",
    "111111111100",
    "410111101400",
    "005555500000",
    "905505550000",
    "999000099000",
    "099000999000"
    ]


standing_left = [
    "000003333000",
    "000003333000",
    "000022222200",
    "000004044000",
    "000044444000",
    "000004444000",
    "000000440000",
    "000001111000",
    "000011101100",
    "000011101100",
    "000011101100",
    "000041001400",
    "000005555000",
    "000000550000",
    "000000990000",
    "000009990000"]


starting_left = [
    "000033330000",
    "000033330000",
    "000222222000",
    "000040440000",
    "000444440000",
    "000044440000",
    "000004400000",
    "000011110000",
    "000111111000",
    "000111111000",
    "001110111100",
    "004101111400",
    "000055550000",
    "000550555000",
    "000999099000",
    "009990999000"]






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
    time.sleep(.1)


time.sleep(1)
for i in range(-25, 15, 5):
    moveMe(playerPos.x + i, y, z + 1, RIGHT)
    time.sleep(.05)

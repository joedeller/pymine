#! /usr/bin/python
# Joe Deller July 2014
# Version 2 of our clock program

# Level : Intermediate
# Uses  : Libraries, variables, dictionary, operators, loops, logic

import mcpi.minecraft as minecraft
import time
import mcpi.block as block

# Our first version of the clock worked, just about
# but it flicked and was so slow that the seconds "jumped"

# One way of making it better is to make the pi and Minecraft
# do less work.  The hours and minutes of the clock
# don't change as much as the seconds, so we can save a lot
# of work by only drawing what has actually changed
# since the last time we drew the time.


def DrawMessage(x, y, z, message):
    # Draw our message starting at x,y & z
    # We draw one letter at a time
    for letter in message:
        # Look up the letter in our font list to find how to draw it
        # pass the pattern and where we want to draw the letter to DrawLetter
        # which will do the drawing.
        # Then move our "cursor" to the right ready for the next letter in the
        # message
        pattern = font.get(letter).split(",")
        DrawLetter(pattern, x, y, z)
        x = x + letterWidth


def DrawLetter(pattern, x, y, z):
    # We have a series of Hexadecimal (base 16)  numbers that represent 1 row of blocks of the letter we want to draw
    # We draw from the top of the letter to the bottom, from left to right
    # Each letter is 8 blocks high and we want them to finish at "ground" level
    # so we need to start 7 higher than the y coordinate
    y = y + 7
    # Our dictionary of letter patterns is in Hexadecimal (base 16)  format, so our scale is 16
    # we could have used base 10, but that is slightly more typing
    scale = 16
    # Each row of our letter can be up to 8 blocks wide including the spaces around it
    # In this case, we only use 5 blocks to make the letter, plus one block of
    # space
    num_of_blocks = 8

    # Draw the letter one row at a time
    for row in pattern:
        # We draw each row of the letter from left to right, we need to move 8
        # to the left at the start of each row
        x = x - num_of_blocks
        # Convert the hexadecimal value into a binary one, a series of block patterns like "1001001"
        # Each 1 means draw a solid block, each 0 means draw an empty block
        # (air)
        blocks = bin(int(row, scale))[2:].zfill(num_of_blocks)
        # We now have all the information we need to draw one row of the letter
        # so step through every block and draw it, left to right
        # be careful in that the word "block" is already in use, so I use
        # "brick" instead
        for brick in blocks:
            if (brick == "1"):
                mc.setBlock(x, y, z, block.WOOL.id, color)
            else:
                mc.setBlock(x, y, z, block.AIR.id)
            # move right one block
            x = x + 1
        # Now move down to the next row of blocks for our letter
        y = y - 1


# Program starts here
# We need a font for our numbers, here is a list of the codes needed for 0-9
# The characters are actually 5 wide by 8 high and the data is in Hex format to save typing
# The more adventurous might want to experiment to see if making the dictionary decimal format
# or even binary format makes drawing the numbers faster

# Create a new dictionary, the space character is all zeros
font = dict({' ': '00,00,00,00,00,00,00,00'})

# This is a small subset of the font dictionary as we only want the numbers
font['1'] = '20,60,20,20,20,20,20,70'
font['2'] = '70,88,08,10,20,40,80,F8'
font['3'] = '70,88,08,30,08,08,88,70'
font['4'] = '10,30,50,90,F8,10,10,10'
font['5'] = 'F8,80,80,F0,08,08,88,70'
font['6'] = '18,20,40,80,F0,88,88,70'
font['7'] = 'F8,08,10,20,40,40,40,40'
font['8'] = '70,88,88,70,88,88,88,70'
font['9'] = '70,88,88,88,78,08,10,60'
font['0'] = '70,88,98,A8,C8,88,88,70'
font[':'] = '00,30,30,00,00,30,30,00'

mc = minecraft.Minecraft.create()
playerPos = mc.player.getPos()

# We should really check that we are not too close to the edge of the world
# otherwise our clock won't draw

# Set the place where we will start drawing the clock, which will be 10
# blocks in front of where we are
x = playerPos.x - 16
y = playerPos.y
z = playerPos.z

# Clean a nice big space for us, our clock is quite big
mc.setBlocks(x - 20, y - 2, z - 30, x + 60, y + 12, z + 20, block.AIR)
# Set a flat grass  floor
mc.setBlocks(x - 20, y - 2, z - 30, x + 40, y - 1, z + 24, block.GRASS.id)

# Draw a black background for our clock, a rectangle to hold hh:mm:ss is 6*8 wide, 8 high
# We will place it 12 blocks back from where we are standing
# Black wool is color 15, this makes our clock nice and readable with
# different color numbers

mc.setBlocks(x + 40, y, z - 19, x - 10, y + 8, z - 19, block.WOOL.id, 15)

# Our clock numbers will be white, which is color 0
color = 0

# Our font is actually only 5 wide, plus 1 for a space so we can read it
letterWidth = 6
z = z - 18

# Get the current time
# The first time we draw the clock we draw the hours, minutes and seconds
# The time library has a function to change the current time into
# separate pieces

# We are going to need to store the hour, minute and second of the clock
# This way we can check it later to see what we need to redraw
last_hour = time.strftime("%H")
last_minute = time.strftime("%M")
last_seconds = time.strftime("%S")

# The first time we want to draw the whole time
message = time.strftime("%H:%M:%S")
DrawMessage(x, y, z, message)

while True:
    # from now on, we only want to draw the part of the clock that changes
    # this saves the PI a lot of work
    # This can be improved even more, by only changing the part of the seconds that changes
    # Or even keeping track of what individual blocks have changed
    # but there is always a balance between speed, complexity and readability
    # Remember the golden rule, do enough, but no more!
    # Note that GetBlockWithData is very slow, so will not help

    # What is the time now?
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    seconds = time.strftime("%S")

    # If part of the clock has not changed since we last drew it, don't waste
    # time drawing it again, is the current hour the same as last time ?
    # the != means "not the same as" or "not equal to"
    if (hour != last_hour):
        DrawMessage(x, y, z, hour)

    # The minutes are 3 characters to the right, 2 characters for the hours plus one for the ":"
    # This means we need to add 3 * letter width to the x coordinate to be in
    # the right place

    if (minute != last_minute):
        DrawMessage(x + (letterWidth * 3), y, z, minute)

    # The seconds are to the right 6 characters spaces, hh:mm:ss , so add 6 *
    # letterWidth
    if (seconds != last_seconds):
        DrawMessage(x + (letterWidth * 6), y, z, seconds)

    # make a note of what we have just drawn ready to be checked for next time
    last_hour = hour
    last_minute = minute
    last_seconds = seconds
    # This is the end of the loop, but the way we have written the program
    # it will run forever, unless we manually stop it

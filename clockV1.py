#! /usr/bin/python
# Joe Deller 2014
# Drawing a digital clock in Minecraft

# Level : Intermediate
# Uses  : Libraries, variables, dictionary, operators, loops, logic

import mcpi.minecraft as minecraft
import time
import mcpi.block as block

# Ways to improve the clock:
# Don't redraw everything!  Only what has changed since we last drew something


def DrawMessage(x, message):
    # Firstly look up the letter / number in our alphabet dictionary so we can
    # find the pattern to draw it
    for letter in message:
        # Take the pattern of data we get back and separate it out into rows
        # pass the pattern and where we want to draw the letter to DrawLetter
        pattern = font.get(letter).split(",")
        DrawLetter(pattern, x, y, z)
# The character set we are using is actually a 5 wide by 7 high
# so we will reduce the amount of space between the letters by only
# leaving a single block of space between them
        letterWidth = 6
        x = x + letterWidth


def DrawLetter(pattern, x, y, z):
    # We have a series of Hexadecimal (base 16) numbers
    # Each represents 1 row of blocks of the letter we want to draw
    # We draw from the top of the letter to the bottom, from left to right
    # Each letter is 8 blocks high and we want them to finish at "ground" level
    # so we need to start 7 higher than the y coordinate
    y = y + 7

    # Our dictionary of letter patterns is in Hexadecimal (base 16)  format, so our number scale is 16
    # we could have used base 10, but that is slightly more typing
    numberScale = 16

    # Each row of our letter can be up to 8 blocks wide including the spaces
    # around it
    num_of_blocks = 8

    # Draw the letter one row at a time
    for row in pattern:
        # We draw each row of the letter from left to right, we need to move 8
        # to the left at the start of each row
        x = x - num_of_blocks
        # Convert the hexadecimal value into a binary one, a series of block patterns like "1001001"
        # Each 1 means draw a solid block, each 0 means draw an empty block (air)
        # We need to chop off the first part of the information we get back as it contains "0b"
        # which reminds us the information is binary

        blocks = bin(int(row, numberScale))[2:].zfill(num_of_blocks)
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


# Here is a list of the codes needed to make our alphabet font
# The characters are actually 5 wide by 8 high and the data is in Hex format to save typing
# Create a new dictionary, the space character is all zeros, meaning empty
# space
font = dict({' ': '00,00,00,00,00,00,00,00'})

# Add the rest of the numbers to our dictionary
font['1'] = '20,60,20,20,20,20,20,70'
font['2'] = '70,88,08,10,20,40,80,F8'
font['3'] = '70,88,08,30,08,08,88,70'
font['4'] = '10,30,50,90,F8,10,10,10'
font['5'] = 'F8,80,80,F0,08,08,88,70'
font['6'] = '18,20,40,80,F0,88,88,70'
font['7'] = 'F8,08,10,20,40,40,40,40'
font['8'] = '70,88,88,70,88,88,88,70'
font['9'] = '70,88,88,88,78,08,10,60'
font['?'] = '70,88,88,10,20,20,00,20'
font['!'] = '20,20,20,20,20,20,00,20'
font['0'] = '70,88,98,A8,C8,88,88,70'
font[':'] = '00,30,30,00,00,30,30,00'


mc = minecraft.Minecraft.create()

# Put us on the ground in the middle of the world, at ground level
# mc.player.setPos(64,1,64)
playerPos = mc.player.getPos()

pX = playerPos.x - 16
pY = playerPos.y
pZ = playerPos.z

# Clean a nice big space for us
mc.setBlocks(pX - 20, pY - 2, pZ - 19, pX + 50, pY + 16, pZ + 20, block.AIR)
# Set a flat grass  floor
mc.setBlocks(pX - 20, pY - 2, pZ - 10, pX + 40, pY - 1, pZ + 20, block.GRASS)

# Draw a black background for our clock
mc.setBlocks(pX - 10 , pY, pZ - 19, pX + 40, pY + 8, pZ - 19, block.WOOL.id, 15)

# mc.player.setPos(playerPos.x,playerPos.y,playerPos.z)


# Set the place where we will start drawing the clock, which will be 10
# blocks in front of where we are
z = pZ - 18
#x = playerPos.x
y = playerPos.y

# store the starting x coordinate of the clock
xstart = pX

# We need to choose a colour for the wool blocks we use to draw the time
# Lets start with white , which is color 0
color = 0


while True:
    message = time.strftime("%H:%M:%S")  # Need to draw the whole clock
    DrawMessage(xstart, message)

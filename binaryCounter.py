#! /usr/bin/python
# Joe Deller 2014
# Counting in different bases, decimal, hexadecimal and binary

# Level : Intermediate
# Uses  : Libraries, variables, dictionary, operators, loops, logic

# A series of glowstone blocks are used to illustrate how a number
# can be show as a series of bits

# TODO - The DrawMessage / DrawLetter methods should really be made into a module


import mcpi.minecraft as minecraft
import time
import mcpi.block as block


def drawMessage(x, message):
    # Firstly look up the letter / number in our alphabet dictionary
    for letter in message:
        # Take the list of data we get back and separate it out into rows
        # pass the pattern and where we want to draw the letter to DrawLetter
        pattern = font.get(letter).split(",")
        drawLetter(pattern, x, y, z)
    # The character set we are using is actually a 5 wide by 7 high one
    # so we will reduce the amount of space between the letters by only
    # leaving a single block of space between them
        x = x - letterWidth


def drawLetter(pattern, x, y, z):
    # We have a series of Hexadecimal (base 16)  numbers that represent 1 row of blocks of the letter we want to draw
    # We draw from the top of the letter to the bottom, from left to right
    # Each letter is 8 blocks high and we want them to finish at "ground" level
    # so we need to start 7 higher than the y coordinate
    y = y + 7
    # Our dictionary of letter patterns is in Hexadecimal (base 16)  format, so our scale is 16
    # we could have used base 10, but that is slightly more typing
    scale = 16
    # Each row of our letter can be up to 8 blocks wide including the spaces
    # around it
    num_of_blocks = 8

    # Draw the letter one row at a time
    for row in pattern:
        # We draw each row of the letter from left to right, we need to move 8
        # to the left at the start of each row
        x = x + 8
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
            x = x - 1
        # Now move down to the next row of blocks for our letter
        y = y - 1


def drawBinary(blocks, x, y, z):
    for brick in blocks:
        if (brick == "1"):
            mc.setBlock(x, y, z, block.GLOWSTONE_BLOCK.id)
        else:
            mc.setBlock(x, y, z, block.WOOL.id, 15)
        # move right one block
        x = x - 1


def checkBlockIsHit(pauseX, pauseY, pauseZ):
    # This routine checks to see if the player hit any blocks with the mouse
    block_hits = mc.events.pollBlockHits()
    # Were any blocks hit ?
    if(block_hits):
        for blockHit in block_hits:
            print "some thing hit at: " + str(blockHit.pos.x) + " " + str(blockHit.pos.y) + " " + str(blockHit.pos.z)
            # did the player hit our special stone block
            if(blockHit.pos.x == pauseX and blockHit.pos.y == pauseY and blockHit.pos.z == pauseZ):
                print "pause block was hit!"
                return True
            else:
                # The player hit something, but not the right thing so return
                # false
                print "Something hit but not the pause block"
                return False
    else:
        # no blocks were hit at all
        return False

# Here is a list of the codes needed to make our alphabet font
# The characters are actually 5 wide by 8 high and the data is in Hex format to save typing
# Create a new dictionary, the space character is all zeros
font = dict({' ': '00,00,00,00,00,00,00,00'})

# Add the rest of the font to our dictionary
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
font['a'] = '00,00,70,08,78,88,88,78'
font['b'] = '80,80,80,B0,C8,88,88,F0'
font['c'] = '00,00,70,88,80,80,88,70'
font['d'] = '08,08,08,68,98,88,88,78'
font['e'] = '00,00,00,70,88,F8,80,70'
font['f'] = '30,48,40,40,E0,40,40,40'

mc = minecraft.Minecraft.create()
playerPos = mc.player.getTilePos()
x = playerPos.x
y = playerPos.y
z = playerPos.z
# Clean a nice big space for us
mc.setBlocks(
    x - 40,
    y,
    z - 1,
    x + 15,
    y + 16,
    z + 16,
    block.AIR)
# Set a flat grass  floor
mc.setBlocks(
    x - 20,
    y - 1,
    z - 12,
    x + 20,
    y - 1,
    z + 17,
    block.GRASS.id)

# Draw a black background for our numbers
mc.setBlocks(
    x + 12,
    y,
    z + 15,
    x - 25,
    y + 9,
    z + 15,
    block.WOOL.id,
    15)

pauseX = x
pauseY = y
pauseZ = z + 2

# Draw a red wool block that can be used to pause the counter
# if we hit it then it changes to green and waits to be hit again
# before continuing.
mc.setBlock(pauseX, pauseY, pauseZ, block.WOOL.id,14)
# Set the place where we will start drawing the clock, which will be 14
# blocks in front of where we are

z = z + 14

# store the starting x coordinate of the display, 4 blocks to the right
# of where we are
xstart = x + 4


# Our font is actually only 5 wide, plus 1 for a space so we can read it
letterWidth = 6

# Lets start with white , which is color 0
color = 0

for count in range(0, 129):
    drawMessage(xstart, str(count))
#    blocks = bin(int(str(count), 10))[2:].zfill(8)
    blocks = bin(count)[2:].zfill(8)

    myHex = hex(count)[2:]
    if (count < 16):
        myHex = "0" + myHex

    print myHex
    print blocks
    # Start by drawing the binary bits above where our decimal number will be
    drawBinary(blocks, xstart + 8, y + 9, z)
    # Show the hexadecimal equivalent of our decimal number
    drawMessage(xstart - 20, myHex)
    # Draw another binary counter above our hexadecimal number
    drawBinary(blocks, xstart - 12, y + 9, z)
    # If the player hits the block, then we will pause until they hit the block again
    # We change the block from green to red and back again
    pause = checkBlockIsHit(pauseX, pauseY, pauseZ)
    if (pause):
        mc.postToChat("Pausing.  Hit the block again to continue.")
        mc.setBlock(pauseX, pauseY, pauseZ, block.WOOL.id,13)
    while (pause):
        if (checkBlockIsHit(pauseX, pauseY, pauseZ)):
            pause = False
            mc.setBlock(pauseX, pauseY, pauseZ, block.WOOL.id,14)
        time.sleep(.1)
    time.sleep(1.5)

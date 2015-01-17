#! /usr/bin/python
# Joe Deller 2014
# Third version of our digital clock

# Level : Intermediate
# Uses  : Libraries, variables, dictionary, operators, loops, logic

# This time we only draw the units of the seconds unless the tens change
# We can also hit a stone block to change the colour of the clock


import mcpi.minecraft as minecraft
import time
import mcpi.block as block


def DrawMessage(x, message):
    # Firstly look up the letter / number in our alphabet dictionary
    for letter in message:
        # Take the list of data we get back and separate it out into rows
        # pass the pattern and where we want to draw the letter to DrawLetter
        pattern = font.get(letter).split(",")
        DrawLetter(pattern, x, y, z)
    # The character set we are using is actually a 5 wide by 7 high one
    # so we will reduce the amount of space between the letters by only
    # leaving a single block of space between them
        x = x + letter_width


def DrawLetter(pattern, x, y, z):
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


def CheckBlockIsHit():
    # This routine checks to see if the player hit any blocks with the mouse
    # We have a special stone block at 52,1,52 and if that is hit we will
    # change the color of the clock
    block_hits = mc.events.pollBlockHits()
    # Were any blocks hit ?
    if(block_hits):
        for blockHit in block_hits:
            print "some thing hit at: " + str(blockHit.pos.x) + " " + str(blockHit.pos.y) + " " + str(blockHit.pos.z)
            # did the player hit our special stone block
            if(blockHit.pos.x == stone_x and blockHit.pos.y == stone_y and blockHit.pos.z == stone_z):
                print "Change color block was hit!"
                return True
            else:
                # The player hit something, but not the right thing so return
                # false
                print "not the right block"
                print stone_x, stone_y, stone_z
                return False
    else:
        # no blocks were hit at all
        return False

# Here is a list of the codes needed to make our alphabet font
# The characters are actually 5 wide by 8 high and the data is in Hex format to save typing
# Create a new dictionary, the space character is all zeros
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

# mc.setting("world_immutable", True)


mc = minecraft.Minecraft.create()
playerPos = mc.player.getTilePos()
x = playerPos.x - 16
y = playerPos.y
z = playerPos.z

# Clean a nice big space for us
mc.setBlocks(x - 20, y - 2, z - 30, x + 50, y + 16, z + 20, block.AIR)
# Set a flat grass  floor
mc.setBlocks(x - 20, y - 1, z - 30, x + 40, y - 1, z + 20, block.GRASS.id)

# Draw a black background for our clock
mc.setBlocks(x + 40, y, z - 19, x - 10, y + 8, z - 19, block.WOOL.id, 15)

# mc.player.setPos(playerPos.x,playerPos.y,playerPos.z)

stone_x = playerPos.x
stone_y = y
stone_z = z - 2
# Put a stone block in front of the clock which we can hit to change the
# clock color
mc.setBlock(stone_x, stone_y, stone_z, block.STONE.id)

# Set the place where we will start drawing the clock, which will be 18
# blocks in front of where we are
z = z - 18

# store the starting x coordinate of the clock
clock_x = x

# Our font is actually only 5 wide, plus 1 for a space so we can read it
letter_width = 6

# Lets start with white for the color of our clock , which is color 0
color = 0

last_hour = time.strftime("%H")
last_minute = time.strftime("%M")
last_seconds = time.strftime("%S")
# The first time we want to draw the whole time
message = time.strftime("%H:%M:%S")
DrawMessage(x, message)

# Calculate where the hours minutes and seconds are drawn
# as the do not change when we run our program
# we can do it once to save the loop doing extra work
hours_x = x
# The minutes are three letters to the right of the hours, 2 characters for the hours plus one for the ":"
minutes_x = x + (letter_width * 3)
# The seconds are 6 letters to the right of the hours -, hh:mm:ss
seconds_x = x + (letter_width * 6)

while True:
    # from now on, we only want to draw the part of the clock that changes
    # this saves the PI a lot of work
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    seconds = time.strftime("%S")

    # Was our "change colour" block hit?
    # if it was then we need to change the color of the clock before we draw it
    # and re draw the whole clock in the new color
    if (CheckBlockIsHit()):
        color = color + 1
        # wool can be one of 16 colors 0-15, so if we reached 16 go back to 0
        if (color == 16):
            color = 0
        message = time.strftime("%H:%M:%S")  # Need to draw the whole clock
        DrawMessage(clock_x, message)

    # If part of the clock has not changed since we last drew it, don't waste
    # time drawing it again, is the current hour the same as last time ?
    if (hour != last_hour):
        DrawMessage(hours_x, hour)

    if (minute != last_minute):
        DrawMessage(minutes_x, minute)

    tens = seconds[:1]
    if(tens == last_seconds[:1]):
        units = seconds[1:]
        DrawMessage(seconds_x + 6, units)
    else:
        DrawMessage(seconds_x, seconds)

    # make a note of what time we have just drawn ready to be checked for next time
    last_hour = hour
    last_minute = minute
    last_seconds = seconds

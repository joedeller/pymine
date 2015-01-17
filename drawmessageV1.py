#! /usr/bin/python
# Joe Deller 2014
# Draw messages in minecraft blocks

# Level : Intermediate
# Uses  : Libraries, variables, dictionary, operators, loops, logic

# This program contains information about a font, or typeface
# A font decides how letters will appear, their shape and size
# There are many different kinds of fonts, in all shapes and sizes

# By converting the font data into a form that we can use with minecraft blocks
# we can write messages in big chunky block style
# It is a lot of work, but you can design your own font face

# The type of font we use in our program is called a bitmap font
# This is an older method of creating fonts, but works well with minecraft and blocks

# You can use squared graph paper to design fonts, although most
# people would use a special program to help do this

# Our information is stored in a dictionary.
# Just like a dictionary you use to lookup the meaning of words,
# every time we want to draw a letter
# we look it up in the dictionary, then use the information to get the pattern of blocks
# that make up the letter


import mcpi.minecraft as minecraft
import mcpi.block as block


def DrawMessage(x, y, z, message):
    for letter in message:
        # Firstly look up the letter in our font dictionary
        # We will store the set of Hexadecimal numbers we find in list
        # separated by a comma
        # We then call another method to do the actual drawing, called DrawLetter
        # Spaces are a special case, we just move right by 4 blocks
        pattern = font.get(letter).split(",")
        print "Pattern for letter " + letter + " = " + font.get(letter)
        DrawLetter(pattern, x, y, z)
        x = x + letterWidth


def DrawLetter(letterCode, x, y, z):
    # Our font information is stored in Hexadecimal, or base 16
    # We need to decode this into a series of 1s and 0s, which we will then use to
    # draw a block or a space
    # This way of drawing letters is called a bitmap font
    # It is made up of a series of bits that tell us to draw a block or a space
    # Most computer displays and TVs use bitmaps, you might need a magnifying glass
    # but if you look closely you can see the dots that make up the screen

    base = 16
    # Our font data stored in bytes, or 8 bits
    # even though most letters have 3 blocks of space to "round" them up to 8 bits of data.
    # The letters actually only need 5 blocks to make them
    # Other font styles might use all 8 available blocks so each letter is wider
    num_of_blocks = 8
    # Our font is 7 blocks high and we draw it from the top of the letter
    # downwards, so we need to move up 7 blocks
    y = y + 7

    # Each letter has a series codes that represent 1 grid line, or row of the letter we want to draw
    # If we are drawing letters upright then we move along the X and Y axis
    # If we are drawing letters flat then we move on the X and Z axis
    for value in letterCode:
        x = x - num_of_blocks
        # This is where we start to decode the letter hexadecimal numbers into rows of blocks
        # Firstly we convert the Hex number back into base 10
        # then bin keyword converts this into binary number
        # Finally we pad the binary number to be eight digits wide
        # Binary and hexadecimal numbers are very tricky for humans to read and work with
        # which is why we often convert back and forward between them and decimal, base 10
        # Try the print command to see what happens as we decode the letter
        print "Value: ", value
        baseTen = int(value, base)
        print "Hex :", value, "Base Ten ", baseTen
        blocks = bin(baseTen)
        print "blocks before trimming", blocks

        # the contents of the blocks variable will start with "0b" to remind us that it is a binary number
        # We need to chop this off as we don't need it
        # We also need to "pad" our number to be eight blocks wide
        # The [2:] means chop off the first two characters from what is stored
        # in blocks

        blocks = blocks[2:]
        # The zfill will add what are called leading zeros to make the number
        # the width we want
        # E.g. we normally write "100"  , not "0100"
        # if we tell zfill to make the number  "100" eight wide
        # it will give us the number "00000100" back
        print "blocks after trimming before filling ", blocks
        blocks = blocks.zfill(num_of_blocks)
        print "blocks after filling ", blocks
        # Now that we have a binary number, 1 means draw a block, 0 means draw
        # air, we can finally draw the blocks that make up this line of our letter
        for myblock in blocks:
            if (myblock == "1"):
                mc.setBlock(x, y, z, block.DIAMOND_BLOCK.id)
            else:
                mc.setBlock(x, y, z, block.AIR.id)
            x = x + 1
        y = y - 1


# Here is a list of the codes needed to make our alphabet
# Each letter has 8 pieces of information that define its shape
# There are different ways of storing information
# Each has its advantages and downfalls
# The font used here is a 5 blocks wide by 7 blocks high font
# Another common size is 8 blocks wide by 8 high, which looks nicer
# but is really too big for Minecraft
# The numbers are in Hexadecimal, we could have used base 10, but
# that is more typing

font = dict({' ': '00,00,00,00,00,00,00,00'})
font['A'] = '70,88,88,88,F8,88,88,88'
font['B'] = 'F0,88,88,F0,88,88,88,F0'
font['C'] = '70,88,80,80,80,80,88,70'
font['D'] = 'E0,90,88,88,88,88,90,E0'
font['E'] = 'F8,80,80,F0,80,80,80,F8'
font['F'] = 'F8,80,80,F0,80,80,80,80'
font['G'] = '70,88,80,80,B8,88,88,70'
font['H'] = '88,88,88,F8,88,88,88,88'
font['I'] = 'F8,20,20,20,20,20,20,F8'
font['J'] = '08,08,08,08,08,88,88,70'
font['K'] = '88,90,A0,C0,C0,A0,90,88'
font['L'] = '80,80,80,80,80,80,80,F8'
font['M'] = '88,D8,A8,A8,88,88,88,88'
font['N'] = '88,C8,A8,A8,98,88,88,88'
font['O'] = '70,88,88,88,88,88,88,70'
font['P'] = 'F0,88,88,88,F0,80,80,80'
font['Q'] = '70,88,88,88,88,A8,90,68'
font['R'] = 'F0,88,88,88,F0,A0,90,88'
font['S'] = '78,80,80,70,08,08,08,F0'
font['T'] = 'F8,20,20,20,20,20,20,20'
font['U'] = '88,88,88,88,88,88,88,70'
font['V'] = '88,88,88,88,50,50,20,20'
font['W'] = '88,88,88,88,A8,A8,D8,88'
font['X'] = '88,88,50,20,20,50,88,88'
font['Y'] = '88,88,88,50,20,20,20,20'
font['Z'] = 'F8,08,10,20,20,40,80,F8'
font['a'] = '00,00,70,08,78,88,88,78'
font['b'] = '80,80,80,B0,C8,88,88,F0'
font['c'] = '00,00,70,88,80,80,88,70'
font['d'] = '08,08,08,68,98,88,88,78'
font['e'] = '00,00,00,70,88,F8,80,70'
font['f'] = '30,48,40,40,E0,40,40,40'
font['g'] = '00,78,88,88,78,08,08,70'
font['h'] = '80,80,80,B0,C8,88,88,88'
font['i'] = '00,20,00,20,20,20,20,20'
font['j'] = '10,00,30,10,10,10,90,60'
font['k'] = '80,80,80,90,A0,C0,A0,90'
font['l'] = '60,20,20,20,20,20,20,70'
font['m'] = '00,00,D0,A8,A8,88,88,88'
font['n'] = '00,00,B0,C8,88,88,88,88'
font['o'] = '00,00,00,70,88,88,88,70'
font['p'] = '00,00,F0,88,88,F0,80,80'
font['q'] = '00,00,68,98,78,08,08,08'
font['r'] = '00,00,00,B0,C8,80,80,80'
font['s'] = '00,00,00,70,80,70,08,F0'
font['t'] = '40,40,E0,40,40,40,48,30'
font['u'] = '00,00,00,88,88,88,98,68'
font['v'] = '00,00,00,88,88,88,50,20'
font['w'] = '00,00,00,88,A8,A8,A8,50'
font['x'] = '00,00,00,88,50,20,50,88'
font['y'] = '00,00,48,48,48,38,08,70'
font['z'] = '00,00,00,F8,10,20,40,F8'
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
font['@'] = '70,88,88,08,68,A8,A8,70'
font['#'] = '50,50,F8,50,50,F8,50,50'
font['&'] = '60,90,90,A0,40,A8,90,68'
font['('] = '10,20,40,40,40,40,20,10'
font[')'] = '40,20,10,10,10,10,20,40'

# START HERE
# Connect to Minecraft and find out where we are standing
mc = minecraft.Minecraft.create()
playerPos = mc.player.getPos()

# Draw a grass floor 80 blocks to the left, 20 blocks to the right
mc.setBlocks(
    playerPos.x -
    80,
    playerPos.y - 1,
    playerPos.z -
    10,
    playerPos.x +
    20,
    playerPos.y - 1,
    playerPos.z +
    1,
    block.GRASS)

# Ask for a message to display
message = raw_input('Enter a message to write in Minecraft: ')

# Our font is 5 blocks wide and we want a single space between the
# letters, so that makes the letters 6 blocks wide
letterWidth = 6

clear_x = len (message) * letterWidth

# Clean a nice big space for us so we can see the message
mc.setBlocks(
    playerPos.x -
    80,
    playerPos.y,
    playerPos.z -
    14,
    playerPos.x +
    clear_x,
    playerPos.y + 16,
    playerPos.z +
    4,
    block.AIR)


x = playerPos.x
y = playerPos.y
# Set the place where we will draw the message 10 blocks back so we can see it
z = playerPos.z - 10

DrawMessage(x, y, z, message)

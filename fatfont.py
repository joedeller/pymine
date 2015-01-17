#! /usr/bin/python
# Joe Deller August 2014
# Draw a message in a fat font

# Level : Intermediate
# Uses  : Libraries, variables, dictionary, operators, loops, logic

# We could change this program to be able to use different fonts
# One way would be to have several font files and read them
# into a different dictionaries


import mcpi.minecraft as minecraft
import mcpi.block as block


def DrawLetter(letterCode, x, y, z, mode):
    scale = 16
    num_of_bits = 8
    y = y + 6
    # We have a series of Hexadecimal codes that represent 1 grid line of the letter we want to draw
    # If we are drawing letters upright then we move along the X and Y axis
    # If we are drawing letters flat then we move on the X and Z axis
    for value in letterCode:
        if (mode == 1):
            z = z + 8
        else:
            x = x + 8

        blocks = bin(int(value, scale))[2:].zfill(num_of_bits)
        for myblock in blocks:
            if (myblock == "1"):
                # Let's bling the font
                mc.setBlock(x, y, z, block.GOLD_BLOCK.id)
            else:
                mc.setBlock(x, y, z, 0)
            if (mode == 1):
                z = z - 1
            else:
                x = x - 1
        y = y - 1

# Here is a list of the codes needed to make our alphabet
# This font is really too wide to be much use
font = dict({' ': '00,00,00,00,00,00,00'})
font['!'] = '30, 78, 78, 30, 30, 00, 30'
font['"'] = '6C, 6C, 6C, 00, 00, 00, 00'
font['d'] = '6C, 6C, FE, 6C, FE, 6C, 6C'
font['$'] = '30, 7C, C0, 78, 0C, F8, 30'
font['%'] = '00, C6, CC, 18, 30, 66, C6'
font['&'] = '38, 6C, 38, 76, DC, CC, 76'
font["'"] = '60, 60, C0, 00, 00, 00, 00'
font['('] = '18, 30, 60, 60, 60, 30, 18'
font[')'] = '60, 30, 18, 18, 18, 30, 60'
font['*'] = '00, 66, 3C, FF, 3C, 66, 00'
font['+'] = '00, 30, 30, FC, 30, 30, 00'
font[','] = '00, 00, 00, 00, 30, 30, 60'
font['-'] = '00, 00, 00, FC, 00, 00, 00'
font['.'] = '00, 00, 00, 00, 00, 30, 30'
font['/'] = '06, 0C, 18, 30, 60, C0, 80'
font['0'] = '7C, C6, CE, DE, F6, E6, 7C'
font['1'] = '30, 70, 30, 30, 30, 30, FC'
font['2'] = '78, CC, 0C, 38, 60, CC, FC'
font['3'] = '78, CC, 0C, 38, 0C, CC, 78'
font['4'] = '1C, 3C, 6C, CC, FE, 0C, 1E'
font['5'] = 'FC, C0, F8, 0C, 0C, CC, 78'
font['6'] = '38, 60, C0, F8, CC, CC, 78'
font['7'] = 'FC, CC, 0C, 18, 30, 30, 30'
font['8'] = '78, CC, CC, 78, CC, CC, 78'
font['9'] = '78, CC, CC, 7C, 0C, 18, 70'
font[':'] = '00, 30, 30, 00, 00, 30, 30'
font[';'] = '30, 30, 00, 00, 30, 30, 60'
font['<'] = '18, 30, 60, C0, 60, 30, 18'
font['='] = '00, 00, FC, 00, 00, FC, 00'
font['>'] = '60, 30, 18, 0C, 18, 30, 60'
font['?'] = '78, CC, 0C, 18, 30, 00, 30'
font['@'] = '7C, C6, DE, DE, DE, C0, 78'
font['A'] = '30, 78, CC, CC, FC, CC, CC'
font['B'] = 'FC, 66, 66, 7C, 66, 66, FC'
font['C'] = '3C, 66, C0, C0, C0, 66, 3C'
font['D'] = 'F8, 6C, 66, 66, 66, 6C, F8'
font['E'] = 'FE, 62, 68, 78, 68, 62, FE'
font['F'] = 'FE, 62, 68, 78, 68, 60, F0'
font['G'] = '3C, 66, C0, C0, CE, 66, 3E'
font['H'] = 'CC, CC, CC, FC, CC, CC, CC'
font['I'] = '78, 30, 30, 30, 30, 30, 78'
font['J'] = '1E, 0C, 0C, 0C, CC, CC, 78'
font['K'] = 'E6, 66, 6C, 78, 6C, 66, E6'
font['L'] = 'F0, 60, 60, 60, 62, 66, FE'
font['M'] = 'C6, EE, FE, FE, D6, C6, C6'
font['N'] = 'C6, E6, F6, DE, CE, C6, C6'
font['O'] = '38, 6C, C6, C6, C6, 6C, 38'
font['P'] = 'FC, 66, 66, 7C, 60, 60, F0'
font['Q'] = '78, CC, CC, CC, DC, 78, 1C'
font['R'] = 'FC, 66, 66, 7C, 6C, 66, E6'
font['S'] = '78, CC, E0, 70, 1C, CC, 78'
font['T'] = 'FC, B4, 30, 30, 30, 30, 78'
font['U'] = 'CC, CC, CC, CC, CC, CC, FC'
font['V'] = 'CC, CC, CC, CC, CC, 78, 30'
font['W'] = 'C6, C6, C6, D6, FE, EE, C6'
font['X'] = 'C6, C6, 6C, 38, 38, 6C, C6'
font['Y'] = 'CC, CC, CC, 78, 30, 30, 78'
font['Z'] = 'FE, C6, 8C, 18, 32, 66, FE'
font['['] = '78, 60, 60, 60, 60, 60, 78'
font[']'] = '78, 18, 18, 18, 18, 18, 78'
font['~'] = '10, 38, 6C, C6, 00, 00, 00'
font['_'] = '00, 00, 00, 00, 00, 00, FF'
font['a'] = '00, 00, 78, 0C, 7C, CC, 76'
font['b'] = 'E0, 60, 60, 7C, 66, 66, DC'
font['c'] = '00, 00, 78, CC, C0, CC, 78'
font['d'] = '1C, 0C, 0C, 7C, CC, CC, 76'
font['e'] = '00, 00, 78, CC, FC, C0, 78'
font['f'] = '38, 6C, 60, F0, 60, 60, F0'
font['g'] = '00, 76, CC, CC, 7C, 0C, F8'
font['h'] = 'E0, 60, 6C, 76, 66, 66, E6'
font['i'] = '30, 00, 70, 30, 30, 30, 78'
font['j'] = '0C, 00, 0C, 0C, CC, CC, 78'
font['k'] = 'E0, 60, 66, 6C, 78, 6C, E6'
font['l'] = '70, 30, 30, 30, 30, 30, 78'
font['m'] = '00, 00, CC, FE, FE, D6, C6'
font['n'] = '00, 00, F8, CC, CC, CC, CC'
font['o'] = '00, 00, 78, CC, CC, CC, 78'
font['p'] = '00, DC, 66, 66, 7C, 60, F0'
font['q'] = '00, 76, CC, CC, 7C, 0C, 1E'
font['r'] = '00, 00, DC, 76, 66, 60, F0'
font['s'] = '00, 00, 7C, C0, 78, 0C, F8'
font['t'] = '10, 30, 7C, 30, 30, 34, 18'
font['u'] = '00, 00, CC, CC, CC, CC, 76'
font['v'] = '00, 00, CC, CC, CC, 78, 30'
font['w'] = '00, 00, C6, D6, FE, FE, 6C'
font['x'] = '00, 00, C6, 6C, 38, 6C, C6'
font['y'] = '00, CC, CC, CC, 7C, 0C, F8'
font['z'] = '00, 00, FC, 98, 30, 64, FC'
font['{'] = '1C, 30, 30, E0, 30, 30, 1C'
font['}'] = 'E0, 30, 30, 1C, 30, 30, E0'



mc = minecraft.Minecraft.create()
playerPos = mc.player.getTilePos()
# Clean a nice big space for us

z = playerPos.z + 10
x = playerPos.x
y = playerPos.y


message = raw_input('Enter a message to write in minecraft: ')
letterWidth = 8
clear_x = len (message) * letterWidth

# Clean a nice big space for us
mc.setBlocks(
    playerPos.x -
    80,
    playerPos.y,
    playerPos.z -
    14,
    playerPos.x +
    clear_x,
    playerPos.y + 20,
    playerPos.z +
    10,
    block.AIR)




for letter in message:
    # Firstly look up the letter in our alphabet dictionary
    # This will take the list of Hex numbers and separate them
    # pass the pattern and where we want to draw the letter to DrawLetter
    pattern = font.get(letter).split(",")
    print "Pattern for letter " + letter + " = " + font.get(letter)
    DrawLetter(pattern, x, y, z, 0)
    x = x - letterWidth

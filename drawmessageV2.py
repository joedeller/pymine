#! /usr/bin/python
# Joe Deller 2014
# Draw messages in minecraft blocks version 2

# Level : Intermediate
# Uses  : Libraries, variables, dictionary, operators, loops, logic

# This is is exactly the same idea as version 1, except that
# the message is drawn flat on the floor, rather than vertically


import mcpi.minecraft as minecraft
import mcpi.block as block


def DrawMessage(x, y, z, message):
    for letter in message:
        pattern = font.get(letter).split(",")
        # print "Pattern for letter " + letter + " = " + font.get(letter)
        DrawLetter(pattern, x, y, z)
        x = x + letterWidth


def DrawLetter(letterCode, x, y, z):
    base = 16
    # Our font is 8 blocks wide, even though most letters have 3 blocks of space
    num_of_bits = 8
    # Our font is 7 blocks high, so if we want it to go from the ground, move up 7
    z = z - 7
    # If we are drawing letters upright then we move along the X and Y axis
    # If we are drawing letters flat then we move on the X and Z axis
    for value in letterCode:
        x = x - num_of_bits
        # For this version of the program we do the decoding all in a single line
        blocks = bin(int(value, base))[2:].zfill(num_of_bits)
        # Now that we have a binary number, 1 means draw a block, 0 means draw air
        for myblock in blocks:
            if (myblock == "1"):
                mc.setBlock(x, y, z, block.DIAMOND_BLOCK.id)
            else:
                mc.setBlock(x, y, z, 0)
            x = x + 1
        z = z + 1


# Here is a list of the codes needed to make our alphabet
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
# This is a tricky one, a hash sign normally means a comment
# so we have to work around this
hash = "#"
font[hash] = '50,50,F8,50,50,F8,50,50'
font['&'] = '60,90,90,A0,40,A8,90,68'
font['('] = '10,20,40,40,40,40,20,10'
font[')'] = '40,20,10,10,10,10,20,40'

mc = minecraft.Minecraft.create()
mc.player.setPos(0, 2, 0)
playerPos = mc.player.getPos()

# Clean a nice big space for us
mc.setBlocks(playerPos.x - 60, playerPos.y - 1,
             playerPos.z - 20,
             playerPos.x + 64,
             playerPos.y + 20,
             playerPos.z + 5,
             block.AIR)
# Set a grass floor
mc.setBlocks(playerPos.x - 60,
             playerPos.y - 1,
             playerPos.z - 12,
             playerPos.x + 50,
             playerPos.y - 1,
             playerPos.z + 5,
             block.GRASS)

# Ask for a message to display
message = raw_input('Enter a message to write in minecraft: ')
letterWidth = 6

x = playerPos.x
y = playerPos.y
z = playerPos.z - 10

DrawMessage(x, y, z, message)


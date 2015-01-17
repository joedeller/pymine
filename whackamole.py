#! /usr/bin/python
# Joe Deller 2014
# A Minecraft version of the "WhackAMole" game

# Level : Advanced
# Uses  : Libraries, variables, operators, loops, logic, lists, classes

# Uses the draw large letters code for a scoreboard
# On the Raspberry Pi I've chosen furnaces to be the moles
# If you hit one it briefly changes to a lit furnace
# This only works on the Pi version of Minecraft, on normal Minecraft
# right clicking a furnace would mean you want to use the furnace to make something
# If you are running this code using a craftbuckit server with Raspberry Juice plugin
# the game won't work properly

# I tried using fire, but this did not seem to work with the Pi

# This program has several "print" statements that were used to help with debug
# it as it was being written


import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
import threading


class MoleGame():
    # This class handles drawing the board
    # drawing the moles  (well, furnace blocks)
    # It will randomly draw and hide our moles
    # It can check to see if the player has hit a visible mole
    # It can draw the score in large letters

    def __init__(self, mc, playerPos, width, depth):
        # Setup a few things we will need
        # Two lists, one that has a list of empty spaces where moles 
        # can pop up, the other has active moles that are currently visible
        # Set the score to zero
        # Setup our numbers dictionary so we can draw the score
        # in big letters
        # Finally draw the board

        self.activeMoles = []
        self.emptyMoles = []
        self.targetList = []
        self.score = 0
        self.font = dict({})
        self.setupCharacters()
        self.scoreBoardPos = minecraft.Vec3(playerPos.x + 6, playerPos.y + 1, playerPos.z - depth - 4)
        self.setupBoard(playerPos, width, depth)
        self.playing = False

    def showMole(self):
        # We will only show a maximum of 3 moles at a time
        # If there are 3 already, nothing will happen
        mole_count = len(self.activeMoles)
        if (mole_count < 4):
            # Choose a random empty mole hole
            molePos = self.emptyMoles[random.randint(0, len(self.emptyMoles) - 1)]
            # Add this mole to the active list and remove it from the empty list
            self.activeMoles.append(molePos)
            self.emptyMoles.remove(molePos)
            # print "Showing mole at ",molePos
            # print "Moles active = ",len(self.activeMoles)
            mc.setBlock(molePos, block.FURNACE_INACTIVE.id)


    def hideMole(self):
        mole_count = len(self.activeMoles)
        if (mole_count > 0):
            # Pick a random active mole and hide it
            # Remove them from the active list and add their
            # position back to the empty list so it can be chosen again
            # Remember lists start counting from 0, so our random number needs be from 0 to moles - 1
            molePos = self.activeMoles[random.randint(0, mole_count - 1)]
            self.activeMoles.remove(molePos)
            self.emptyMoles.append(molePos)
            # print "Hiding mole at ",molePos
            # print "Moles left :",len(self.activeMoles)
            mc.setBlock(molePos, block.AIR.id)

    def hideAllMoles(self):
        # print "moles visible = ", len(self.activeMoles
        while (len(self.activeMoles) > 0):
            for mole in self.activeMoles:
                mc.setBlock(mole, block.AIR.id)
                self.activeMoles.remove(mole)

    def shuffleMoles(self):
        # Randomly choose to hide a mole, show a mole
        # or do nothing
        # A high number means less chance
        # So moles don't get hidden as much as shown
        # If there aren't any moles showing, get one to pop up
        while (self.playing == True):
            next_call = random.random()
            time.sleep(next_call)
            # There is a chance the game might have finished while we were waiting
            # So check playing is still true
            if (self.playing == True):
                if (len(self.activeMoles) == 0):
                    # print "No moles visible, going to show one"
                    self.showMole()
                elif (len(self.activeMoles) > 3):
                    # print "moles visible = ", len(self.activeMoles
                     time.sleep(.1)
                     self.hideMole()
                else:
                    choice = random.randint(0, 100)
                    if (choice > 60):
                        # print "Hiding a mole"
                        self.hideMole()
                    elif (choice < 60):
                        # print "Showing a mole"
                        self.showMole()

    def scanForHits(self):
        # See if the player right clicked on a mole
        block_hits = mc.events.pollBlockHits()
        # Were any blocks hit ?       
        if (block_hits):
            for blockHit in block_hits:
                # print "player hit a block"
                if (blockHit.pos in self.activeMoles):
                    # print "player hit a mole!"
                    mc.setBlock(blockHit.pos, block.FURNACE_ACTIVE.id)
                    # It takes a while to draw the message, enough time
                    # to see the change to a lit furnace before we rub it out
                    # We could use threads to handle the scanning
                    # But on the Pi this might not really be worth the effort.

                    self.score = self.score + 1
                    self.DrawMessage(self.scoreBoardPos.x, self.scoreBoardPos.y, self.scoreBoardPos.z, str(self.score))

                    # time.sleep (.1)
                    mc.setBlock(blockHit.pos, block.AIR.id)

                    # print "Score is "+ str(self.score)

    def setupCharacters(self):
        # Create a new dictionary, the space character is all zeros
        # This is a small subset of the font dictionary as we only want the numbers
        self.font[' '] = '00,00,00,00,00,00,00,00'
        self.font['1'] = '20,60,20,20,20,20,20,70'
        self.font['2'] = '70,88,08,10,20,40,80,F8'
        self.font['3'] = '70,88,08,30,08,08,88,70'
        self.font['4'] = '10,30,50,90,F8,10,10,10'
        self.font['5'] = 'F8,80,80,F0,08,08,88,70'
        self.font['6'] = '18,20,40,80,F0,88,88,70'
        self.font['7'] = 'F8,08,10,20,40,40,40,40'
        self.font['8'] = '70,88,88,70,88,88,88,70'
        self.font['9'] = '70,88,88,88,78,08,10,60'
        self.font['0'] = '70,88,98,A8,C8,88,88,70'
        self.font[':'] = '00,30,30,00,00,30,30,00'

    def DrawMessage(self, x, y, z, message):
        # Draw our message starting at x,y & z
        # We draw one letter at a time
        letterWidth = 6
        for letter in message:
            # Look up the letter in our font dictionary to find how to draw it
            # pass the pattern and where we want to draw the letter to DrawLetter
            # which will do the drawing.
            # Then move our "cursor" to the right ready for the next letter in the
            # message
            pattern = self.font.get(letter).split(",")
            self.DrawLetter(pattern, x, y, z)
            x = x + letterWidth

    def DrawLetter(self, pattern, x, y, z):
        y = y + 7
        base = 16
        num_of_blocks = 8

        # Draw the letter one row at a time
        for row in pattern:
            x = x - num_of_blocks
            blocks = bin(int(row, base))[2:].zfill(num_of_blocks)
            for brick in blocks:
                if (brick == "1"):
                    mc.setBlock(x, y, z, block.WOOL.id, 15)
                else:
                    #mc.setBlock(x, y, z, block.AIR.id)
                    mc.setBlock(x, y, z, block.WOOL.id, 0)

                x = x + 1
            y = y - 1

    def setupBoard(self, playerPos, width, depth):
        # Draw the game board, two blocks back from where we are standing
        x, y, z = playerPos.x, playerPos.y, playerPos.z
        z = z - 2
        x = x - 2
        y = y - 1
        mc.setBlocks(x - 10, y, z + 3, x + width + 5, y + 10, z - depth - 5, block.AIR.id)
        mc.setBlocks(x - 5, y - 1, z + 3, x + width + 2, y - 1, z - depth - 5 , block.GRASS.id)
        # 11 is blue wool, change it as you wish
        mc.setBlocks(x, y, z, x + width, y, z - depth, block.WOOL.id, 11)
        # score board is set back two blocks from the end of the board
        mc.setBlocks(x, y, z - depth - 2, x + width, y + 9, z - depth - 2, block.WOOL, 0)
        # Now for the grid of mole holes, separated by one block of wool
        for i in range(1, width + 1, 2):
            for j in range(1, depth - 1, 2):
                mc.setBlock(x + i, y, z - j, block.STONE.id)
                # The moles will appear one block above the stone blocks
                # Store the coordinates in a list, as of possible targets for the player
                # the coordinates are converted into a single variable
                target = minecraft.Vec3(x + i, y + 1, z - j)
                self.targetList.append(target)
        self.emptyMoles = self.targetList




# Start here 
mc = minecraft.Minecraft.create()
playerPos = mc.player.getTilePos()
# Don't make the board too big otherwise you won't be able to see it all
width = 10
depth = 5
# 30 seconds goes surprisingly fast when playing, change as desired
maximumTime = 30
mc.postToChat("Get ready to play! You have " + str(maximumTime) + " seconds.")

myGame = MoleGame(mc, playerPos, width, depth)
# Lets have a count down of five seconds to tell the player when to start
for count in range (5,-1,-1):
    myGame.DrawMessage(myGame.scoreBoardPos.x, myGame.scoreBoardPos.y, myGame.scoreBoardPos.z, str(count))
    time.sleep(1)

myGame.playing = True
myGame.showMole()

# We are using a thread to shuffle the moles around
# This means that the shuffling doesn't interfere with 
# the player trying to hit the moles
# The shuffling is done in the background and carries on until the time limit is up
timerThread = threading.Thread(target=myGame.shuffleMoles)
timerThread.daemon = True
timerThread.start()


t_end = time.time() + maximumTime
while time.time() < t_end:
    myGame.scanForHits()
    # Need a very small pause here, otherwise scanForHits sometimes breaks
    time.sleep(0.01)

myGame.playing = False
mc.postToChat("GAME OVER!")
myGame.hideAllMoles()

#! /usr/bin/python
# Joe Deller 2014
# A minecraft "fruit" machine / one armed bandit.

# Level : Advanced
# Uses : Threads, Lists, Classes, Flags

# This program use daemon Threads, which
# means that when we stop the program (ctrl-c), they are rudely interrupted
# This is a bit like having an art class and at the end of the lesson
# all the children run away without cleaning up after them
#
# Generally this is not a good idea, when you are writing code with
# threads, cleaning up is normally required.  Sometimes the programming language
# you are using will clean any mess, but not always and not always completely.
# For this example, to keep the code from being even more complex
# we will allow such bad behaviour

# The machine could be expanded to have a score, with certain lines of blocks
# winning more than others.  You could allow a "nudge" to shift a wheel up or down
# one.   You could add a credit system, so that a player only had a certain number of goes


import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import threading
import random

# One armed bandits normally have three spinning wheels
# If we design a spinning wheel class, then we can reuse it for each of the wheels
# Things our design needs to know about:
# Each wheel will have an identical list of items on the wheel
# Each wheel needs to know where on the X axis the wheel will be drawn
# We will assume that the Y & Z coordinates are the same for each wheel
# as they are drawn side by side
# Each wheel must be able to spin and stop spinning
# When Spin() is called, it will draw the spinning wheel
# at the X coordinate it is told and where ever the current y & z coordinates are



class FruitWheel(threading.Thread):

    def __init__(self, blockList, wheelX):
        threading.Thread.__init__(self)
        # wheel represents a wheel of a fruit machine, in our case a list of minecraft blocks
        # blockList has the list of minecraft blocks that will be on the wheel
        # items is a subset of 3 items from the wheel that will be visible
        # like a fruit machine, you can see normally see three items on the wheel
        # the centre winning line, one above and one below
        # This class will also do the animating, so we need to know where to draw
        # our spinning wheel

        self.wheel = blockList
        self.lastItem = 0  # Start at the beginning of the list
        self.items = blockList[0:3]  # start with the first 3 items
        self.wheelX = wheelX
        self.spinFinished = True
        # Make a note of how many items in the list
        self.itemCount = len(self.wheel)
        self.startSpin = False

    def run(self):
        # The first time we start, draw the wheel , then wait
        self.DrawWheel()
        self.Wait()

    def DrawWheel(self):
        mc.setBlock(self.wheelX, wheel_top - 3, z, self.items[0:1])
        mc.setBlock(self.wheelX, wheel_top - 2, z, self.items[1:2])
        mc.setBlock(self.wheelX, wheel_top - 1, z, self.items[2:3])

    def Spin(self):
        # This mimics spinning the wheel around and stopping in a random place
        # Real world fruit machines are programmed to give players a certain fixed
        # amount of wins , but this is more truly random
        # We start from the last position in the list
        # and go forward through the list, if we reach the end
        # we start from the beginning again, like a wheel going round one full
        # circle

        # Start spinning from where we left off
        current_item = self.lastItem
        # We want to spin at least 8 times
        total_spins = random.randint(8, 44)
        # We are about to start spinning, so make a note we haven't finished
        self.spinFinished = False
        # print "Spinning Wheel " +str(self.wheelX) + "for " +str(total_spins)
        # +"....."

        for spins in range(0, total_spins):
            # We need to watch out for when we are nearing the end of the list
            # We want 3 items, so if there are less than three left
            # we have to start from the beginning again

            if (current_item <= self.itemCount - 3):
                self.items = self.wheel[current_item:current_item + 3]
            elif (current_item <= self.itemCount - 2):
                self.items = self.wheel[
                    current_item:current_item + 2] + self.wheel[0:1]
            elif (current_item <= self.itemCount - 1):
                self.items = self.wheel[
                    current_item:current_item + 1] + self.wheel[0:2]
            else:
                # Back to the start of the list
                current_item = 0
                self.items = self.wheel[current_item:current_item + 3]
            # Need to draw the items here
            mc.setBlock(self.wheelX, wheel_top - 3, z, self.items[0:1])
            mc.setBlock(self.wheelX, wheel_top - 2, z, self.items[1:2])
            mc.setBlock(self.wheelX, wheel_top - 1, z, self.items[2:3])
            time.sleep(0.05)
            # Next time we spin, we move the wheel on one
            current_item = current_item + 1
            # Remember where we stopped
        self.lastItem = current_item
        self.spinFinished = True
        print "Spin() has finished for ", threading.currentThread().getName()

    def Wait(self):
        # Our thread will stay alive and just wait until told to spin the wheel
        print "Have entered Wait() for ", threading.currentThread().getName()
        while True:
            while (self.startSpin is False):
                time.sleep(.1)
            if (self.spinFinished):
                self.spinFinished = False
                self.startSpin = False
                print "Starting spin for ", threading.currentThread().getName()
                self.Spin()
                time.sleep(1)

    def GetLastPos(self):
        return self.lastItem

    def GetLastItems(self):
        # Return the current "visible" items in our wheel
        return self.items

    def FinishedSpin(self):
        # We need to be able to tell if we have finished spinning or not
        # this enables us to wait until all three wheels have said they have finished
        # before we move on
        return self.spinFinished


def CheckBlockIsHit(x, y, z):
    # This routine checks to see if the player hit any blocks with the mouse
    # We want to see if the level of the fruit machine has been hit
    # if so we will start the fruit machine, as long as it is not already going
    block_hits = mc.events.pollBlockHits()
    # Were any blocks hit ?
    if(block_hits):
        for block_hit in block_hits:
            # did the player hit our special glowstone block
            if(block_hit.pos.x == x and block_hit.pos.y == y and block_hit.pos.z == z):
                print "Lever was hit!"
                return True
            else:
                # The player hit something, but not the right thing so return
                # false
                print "not the right block"
                return False


# Draw the "machine"
def DrawBandit(x, y, z):
    # clear space
    mc.setBlocks(x - 6, y, z - 5, x + 6, y + 6, z + 5, block.AIR.id)
    # Solid black wool for the machine
    mc.setBlocks(x, y, z, x + 4, y + 4, z, block.WOOL.id, 15)
    # Hollow out the inside
    mc.setBlocks(x + 1, y + 1, z, x + 3, y + 3, z, block.AIR.id)
    # The "arm" of the bandit
    mc.setBlocks(x - 1, y + 1, z, x - 1, y + 1, z - 1, block.WOOL.id, 15)
    mc.setBlock(x - 1, y + 1, z - 2, block.GLOWSTONE_BLOCK.id)


# Some animation if we win, the same pattern as the first fruit.py code
# This draws a white block along the sides of the machine
# then sets the block back to black wool
# We do this six times
def winningLights(x, y, z):
    for flashes in range(0, 6):
        for x1 in range(0, 5):
            mc.setBlock(x + x1, y + 4, z, block.WOOL.id, 0)
            mc.setBlock(x + 4 - x1, y, z, block.WOOL.id, 0)
            time.sleep(0.1)
            mc.setBlock(x + x1, y + 4, z, block.WOOL.id, 15)
            mc.setBlock(x + 4 - x1, y, z, block.WOOL.id, 15)

        for y1 in range(1, 4):
            mc.setBlock(x, y + y1, z, block.WOOL.id, 0)
            mc.setBlock(x + 4, y + 4 - y1, z, block.WOOL.id, 0)
            time.sleep(.1)
            mc.setBlock(x, y + y1, z, block.WOOL.id, 15)
            mc.setBlock(x + 4, y + 4 - y1, z, block.WOOL.id, 15)


# Start here
# Connect to minecraft
mc = minecraft.Minecraft.create()

mc.postToChat("Right click the glowstone with sword to spin")
# This is the list of blocks that will be on our wheel
# Be careful what you choose, lava and water a definite no no!
# Unfortunately things like flowers, trees and torches
# don't disappear when replaced with the next block, they tend to fall to the ground
# Choose only items that don't need placing on a separate block
# All the wheels contain the same items, so we only need to do our list once
# and then copy the list for our centre and right wheel

blocks_list = [49, 56, 57, 21, 22, 46, 73, 14]

# reverse the list for the left wheel so the wheels start from different places
left_wheel = blocks_list[::-1]
centre_wheel = blocks_list
right_wheel = blocks_list

# We start at the first item in the list - Once again remember computers
# like to start counting at Zero
left_item = 0
centre_item = 0
right_item = 0

playerPos = mc.player.getTilePos()
z = playerPos.z + 6
x = playerPos.x + 1
y = playerPos.y

wheel_top = y + 4

# We will have a glowstone that when hit will spin the wheels
# This code could be improved so that if we wanted to add more wheels
# or change the lever position more easily.
lever_x = x - 2
lever_y = y + 1
lever_z = z - 2

DrawBandit(x - 1, y, z)

# Our fruit machine has three wheels, so we make three FruitWheel objects,
# in a row next to each other
left_bandit = FruitWheel(left_wheel, x)
centre_bandit = FruitWheel(centre_wheel, x + 1)
right_bandit = FruitWheel(right_wheel, x + 2)

# This uses the same technique that the fireworkV4.py code used.
# We want to spin all three wheels at the same time so we use the thread library
# to help do this.   However, as each wheel is going to spin for a random
# number of times, they probably won't all stop at the same time

left_bandit.daemon = True
left_bandit.start()

centre_bandit.daemon = True
centre_bandit.start()

right_bandit.daemon = True
right_bandit.start()

time.sleep(1)
print "Now just going to wait"

# We will run until the program is manually stopped
while (True):

    # First check that we are not already playing, are any of the wheels still spinning ?
    # If they are we will have to wait until they have stopped
    # We need to check that every wheel, rather than if one of the wheels has finished
    # This means we use the "and" keyword, "if this and that and that"
    # rather than "if this or that or that"
    # Compare this with the logic that checks to see if we have won
    # which uses "or"
    if (left_bandit.FinishedSpin()) and (
            centre_bandit.FinishedSpin()) and (right_bandit.FinishedSpin()):
        # Okay, no wheels spinning, has the level been pulled
        # (the glowstone block hit ?)
        if (CheckBlockIsHit(lever_x, lever_y, lever_z)):
            print "Playing a game.."
            mc.setBlock(lever_x, lever_y, lever_z, block.WOOL.id, 15)
            # Tell the wheels they need to start spinning
            left_bandit.startSpin = True
            centre_bandit.startSpin = True
            right_bandit.startSpin = True
            time.sleep(1)
            # We have started all three wheels spinning, so now we need to wait
            # until they have all finished
            print "Checking if wheels have stopped..."
            print left_bandit.FinishedSpin(), centre_bandit.FinishedSpin(), right_bandit.FinishedSpin()
            while (
                    left_bandit.FinishedSpin() is False) or (
                    centre_bandit.FinishedSpin() is False) or (
                    right_bandit.FinishedSpin() is False):
                # We could do some animation whilst we are waiting
                time.sleep(.1)
                # print "Still spinning..."

            print "Stopped spinning"
            # Okay, lets find out what blocks are in the middle row
            mc.setBlock(lever_x, lever_y, lever_z, block.GLOWSTONE_BLOCK.id)
            left_item = left_bandit.GetLastItems()[1:2]
            centre_item = centre_bandit.GetLastItems()[1:2]
            right_item = right_bandit.GetLastItems()[1:2]
            print left_item, centre_item, right_item
            # If any two blocks are the same, then we are a winner!
            if((left_item == centre_item) or (centre_item == right_item)):
                winningLights(x - 1, y, z)

            time.sleep(1)
    else:
        # print "Still waiting for spinning to stop"
        time.sleep(1)

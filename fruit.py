#! /usr/bin/python
# Joe Deller 2014
# A minecraft "fruit" machine / one armed bandit.

# Level : Advanced
# Uses : Threads, Lists, Classes

# This code uses the threading library to do several things at once
# This kind of programming is generally harder to do
# and be harder to track down bugs
# but can make things appear to run a lot more smoothly


import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import threading
import random

mc = minecraft.Minecraft.create()

# One armed bandits normally have three spinning wheels
# If we design a spinning wheel class, then we can reuse it for each of the wheels
# Things our design needs to know about:
# Each wheel will have a list of items on the wheel
# Each wheel needs to know  where on the X axis the wheel will be drawn
# Each wheel must be able to spin and stop spinning
# When Spin() is called, it will draw the spinning wheel
# at the X coordinate it is told and where ever the current y & z coordinates are
# As the wheels are drawn side by side, the y & z are the same for each wheel


class FruitWheel(threading.Thread):

    def __init__(self, wheel, wheel_x):
        threading.Thread.__init__(self)
        # wheel represents a wheel of a fruit machine, in our case a list of minecraft blocks
        # items is a subset of 3 items from the wheel that will be visible
        # like a fruit machine, you can see normally see three items on the wheel
        # the centre winning line, one above and one below
        # This class will also do the animating, so we need to know where to draw
        # our spinning wheel

        self.wheel = wheel
        self.lastItem = 0  # Start at the beginning of the list
        self.items = wheel[0:3]  # start with the first 3 items
        self.wheelX = wheel_x  # where the wheel is drawn on the X axis
        # A flag to tell us if we are still spinning or not
        self.spinFinished = 0
        # Make a note of how many items in the list
        self.itemCount = len(self.wheel)

    # This piece of code is called when the class is started
    def run(self):
        self.Spin()

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
        # We want to spin at least 8 times, up to 64
        total_spins = random.randint(8, 64)
        # We are about to start spinning, so make a note we haven't finished
        self.spinFinished = 0
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
            # print "Wheel ", str(self.wheelX), self.items[0:1],self.items[1:2],self.items[2:3]
            # Next time we spin, we move the wheel on one
            current_item = current_item + 1
            # Remember where we stopped
        self.lastItem = current_item
        self.spinFinished = 1

    def getLastPos(self):
        return self.lastItem

    def getLastItems(self):
        # Return the current "visible" items in our wheel
        return self.items

    def finishedSpin(self):
        # We need to be able to tell if we have finished spinning or not
        # this enables us to wait until all three wheels have said they have finished
        # before we move on
        return self.spinFinished


# Draw the machine
def DrawBandit(x, y, z):
    # clear space
    mc.setBlocks(x - 1, y, z - 3, x + 4, y + 4, z, block.AIR.id)
    mc.setBlocks(x, y, z, x + 4, y + 4, z, block.WOOL.id, 15)
    mc.setBlocks(x + 1, y + 1, z, x + 3, y + 3, z, block.AIR.id)
    mc.setBlocks(x - 1, y + 1, z, x - 1, y + 1, z - 1, block.WOOL.id, 15)
    mc.setBlock(x - 1, y + 1, z - 2, block.GLOWSTONE_BLOCK.id)

# draw a pretty pattern around the edge of the machine
# using white wool blocks
def winningLights(x, y, z):
    for i in range(0, 8):
        for x1 in range(1, 6):
            mc.setBlock(x - 2 + x1, y + 4, z, block.WOOL.id, 0)
            mc.setBlock(x + 4 - x1, y, z, block.WOOL.id, 0)
            time.sleep(0.05)
            mc.setBlock(x - 2 + x1, y + 4, z, block.WOOL.id, 15)
            mc.setBlock(x + 4 - x1, y, z, block.WOOL.id, 15)
        for y1 in range(1, 3):
            mc.setBlock(x - 1, y + y1, z, block.WOOL.id, 0)
            mc.setBlock(x + 3, y + 4 - y1, z, block.WOOL.id, 0)
            time.sleep(.05)
            mc.setBlock(x - 1, y + y1, z, block.WOOL.id, 15)
            mc.setBlock(x + 3, y + 4 - +y1, z, block.WOOL.id, 15)


# Start here

# This is the list of blocks that will be on our wheel
# Be careful what you choose, lava and water a definite no no!
# Unfortunately things like flowers, trees and torches
# don't disappear when replaced with the next block, they tend to fall to the ground
# Choose only items that don't need placing on a separate block
# All the wheels contain the same items, so we only need to do our list once
# and then copy the list for our centre and right wheel

left_wheel = [49, 56, 57, 21, 22, 46, 73, 14]
centre_wheel = left_wheel
right_wheel = left_wheel

# We start at the first item in the list - Once again remember computers
# like to start counting at Zero
left_item = 0
centre_item = 0
right_item = 0

playerPos = mc.player.getTilePos()
z = playerPos.z + 5
x = playerPos.x
y = playerPos.y
wheel_top = y + 4

# draw the machine
DrawBandit(x - 1, y, z)

# Our fruit machine has three wheels, so we make three FruitWheel objects
left_bandit = FruitWheel(left_wheel, x)
centre_bandit = FruitWheel(centre_wheel, x + 1)
right_bandit = FruitWheel(right_wheel, x + 2)

# This uses the same technique that the final version of the firework program
# We want to spin all three wheels at the same time so we use the thread library
# to help do this.   However, as each wheel is going to spin for a random
# number of times, they probably won't all stop at the same time

# leftBandit.daemon
left_bandit.start()

# centreBandit.daemon
centre_bandit.start()

# rightBandit.daemon
right_bandit.start()

# We have started all three wheels spinning, so now we need to wait until
# they have all finished
while (
    left_bandit.finishedSpin() == 0) or (
        centre_bandit.finishedSpin() == 0) or (
            right_bandit.finishedSpin() == 0):
        time.sleep(.01)

        # We could do some animation whilst we are waiting


print "Everyone finished spinning now"

# print leftBandit.GetLastItems()

print left_bandit.getLastItems()[1:2], centre_bandit.getLastItems()[1:2], right_bandit.getLastItems()[1:2]
left_line = left_bandit.getLastItems()[1:2]
centre_line = centre_bandit.getLastItems()[1:2]
right_line = right_bandit.getLastItems()[1:2]
# On this machine, all we need to win is two of the same items next to each other
# so check if the centre item is the same as either the left or right item
# To make it harder, we could change this so that all three had to be the same

if((left_line == centre_line) or (centre_line == right_line)):
    winningLights(x, y, z)

# print "done, left last pos is now ",leftBandit.GetLastPos()
# print "done, centre last pos is now ",centreBandit.GetLastPos()
# print "done, right last pos is now ",rightBandit.GetLastPos()

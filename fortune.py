#! /usr/bin/python
# Joe Deller 2014
# A Minecraft fortune teller.

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, files

# We have a list of fortunes stored in a text tile
# This program reads all of the fortunes and picks one of them

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
import os


# Create a spinning effect for our fortune telling machine
def spin(fortune_x, floor, depth):
    depth = depth - 6
    for spins in range(0, 4):
        for j in range(0, 3):
            mc.setBlock(fortune_x + j, floor, depth, block.IRON_BLOCK.id)
            mc.setBlock(fortune_x + 2 - j, floor + 2, depth, block.IRON_BLOCK.id)
            time.sleep(0.4)
            mc.setBlock(fortune_x + j, floor, depth, block.GOLD_BLOCK.id)
            mc.setBlock(fortune_x + 2 - j, floor + 2, depth, block.GOLD_BLOCK.id)

        mc.setBlock(fortune_x, floor + 1, depth, block.IRON_BLOCK.id)
        mc.setBlock(fortune_x + 2, floor + 1, depth, block.IRON_BLOCK.id)
        time.sleep(0.4)
        mc.setBlock(fortune_x, floor + 1, depth, block.GOLD_BLOCK.id)
        mc.setBlock(fortune_x + 2, floor + 1, depth, block.GOLD_BLOCK.id)


# Find out where we are in Minecraft
mc = minecraft.Minecraft.create()
playerPos = mc.player.getTilePos()
x, y, z = playerPos

x = x - 1
# The file which has all the fortunes in it is called fortune.txt
# A more sophisticated program might ask what kind of fortune
# someone wanted and choose a different file depending on
# what the person replied.

fortuneFile = "fortune.txt"

# We need to check that our fortune file exists
# If our code cannot find it, then we have to stop.
if (not (os.path.isfile(fortuneFile))):
    print ("I am sorry. I need " + fortuneFile + " to tell your fortune.")
    exit()

# We will read all the fortunes into a list
# then pick a random one.
# Start with an empty list
fortune_list = []

# The next section reads in all the fortunes from the file on disk
# into the computer memory.

# Reading information from disk can be very slow compared to reading from memory
# So we get all the information first and the make use of it
mc.postToChat("Look around for the fortune teller.")
with open("fortune.txt", 'rb') as fortune_file:
    fortune_list = fortune_file.read().splitlines()


# Count the number of fortunes we read
total_fortunes = len(fortune_list) - 1

# Draw a fortune teller
mc.setBlocks(x - 2, y, z + 2, x + 4, y + 3, z - 6, block.AIR.id)
mc.setBlocks(x, y, z - 6, x + 2, y + 2, z - 6, block.GOLD_BLOCK.id)
mc.setBlock(x + 1, y + 1, z - 6, block.NETHER_REACTOR_CORE.id)
mc.setBlock(x + 1, y + 1, z - 6, 89)
time.sleep(2)
# Pick 10 random fortunes
for i in range(0, 10):
    choice = random.randint(0, total_fortunes)
    fortune = fortune_list[choice]
    spin(x, y, z)
    print fortune
    mc.postToChat(fortune)
    time.sleep(4)


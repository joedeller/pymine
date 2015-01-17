#! /usr/bin/python
# Joe Deller 2014

# Draw a building / shape with data from the specified file
# Level : Intermediate
# Uses  : Loops, files, lists
# Usage : ./drawcsv.py [datafile.csv]

# Build the minecraft structure specified on the command line

# This example uses the Comma Separated Values library
# Which sounds complicated, but is really just a way of organising
# lists of information so they can be written out and read back
# more easily

# Computers use things called files to store and transfer information
# so that it can be re used later, or shared with another computer

# Files come in many different forms, they might store music, pictures or films
# In this program we use a file that has information about how to build a
# simple house

# The files that work with this program  contain a series of numbers separated by commas (CSV Format)
# This is an old, but effective  method of storing and transferring information between programs
# There are many other ways of doing this, all have their advantages and
# disadvantages

# Imagine you wanted a cup of fruit juice but you didn't have
# all of the things you needed, so you make a list to go shopping
# You might write it out like this:
# Apple juice orange cup
# But when you get to the shop, you might think, did i need:

# some  "apple juice" and an orange cup" to put my apple juice in
# or some "apple juice", an orange and a cup
# or an apple some "juice orange" and a  cup
# or an apple, some juice, an orange  and a cup
# It can get very confusing, but if use commas to help separate our list:
# Apple juice, orange, cup
# Then we can be clear that you want some "apple juice" an orange and a cup (any colour you want)
# Humans can be very good at sorting out information that isn't clear
# Computers aren't unless they've been programmed to.  When people say "the computer's gone wrong"
# they often really mean the computer has done exactly what it was told, but the instructions
# it was told were wrong.

# Someone needs to create the blue prints in the first place and the design
# of the file needs to be agreed so that the information can be read back again

# Once a file has been made, it is easy to share it so that others can use it
# It means we can change the blueprint without having to make changes to
# our program

# Some of the models originally came from the PC version of Minecraft
# using the Mace world generator program
# https://code.google.com/p/mace-minecraft/
# They were modified where necessary to work with the Pi version



# First our minecraft connection
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

# Now the time and Comma Separated Values libraries
import csv

# The next two libraries let us find out what someone typed
# on the command line and make sure that the file specified exists

import os.path
import sys
#  If you are running this program in IDLE
# Just set the filename you want to build here

buildFile = "guitar.csv"
# Here is a list of files that you can use.
# balloon.csv   bamboo3.csv  bigcastle.csv  church.csv    guitar.csv
# house2.csv  House4.csv      library.csv     poolhouse.csv    statue.csv
# bamboo2.csv  bamboo.csv   church2.csv    coolpool.csv  hammadoll.csv
# House3.csv  largehouse.csv  poolhouse2.csv  poolHouseV1.csv


# We will only pay attention to what was typed immediately after
# this programs filename, if only the program name was typed
# we will use whatever buildFile is set to

if (len(sys.argv) >= 2):
    buildFile = sys.argv[1]

if (os.path.isfile(buildFile)):
    print "Going to build " + buildFile
else:
    print "Sorry, I can't find the file called:" + buildFile
    print "Stopping."
    exit()

# Now we have a file that we can use, lets start building.
mc.setting("world_immutable", False)

# Make a note of where we are standing, so we can build our house close by
playerPos = mc.player.getTilePos()
xStart = playerPos.x
yStart = playerPos.y
zStart = playerPos.z + 4

# clear some space and lay down some grass
mc.setBlocks(
    xStart - 10,
    yStart,
    zStart - 10,
    xStart + 10,
    yStart + 10,
    zStart + 10,
    block.AIR)

mc.setBlocks(
    xStart - 10,
    yStart - 2,
    zStart - 20,
    xStart + 20,
    yStart - 1,
    zStart + 20,
    block.GRASS.id)

# There are some minecraft blocks that have special rules when you place them
# A torch has to be attached to a wall for example
# We will keep a list of these special blocks and add them after the main building is finished
# This is a bit of trial and error.

# The list will start as an empty list
specialList = [
    block.DOOR_WOOD.id,
    block.TORCH.id,
    block.BED.id,
    block.STAIRS_WOOD.id,
    block.LADDER.id,
    block.DOOR_IRON.id,
    block.LAVA.id,
    block.LAVA_STATIONARY.id,
    block.WATER.id,
    block.WATER_STATIONARY.id]

specialBlocks = []

# Now read in our blueprint from the file
# Imagine a conveyor belt of lego pieces coming towards you
# If you have the right instructions, you take one piece at a time
# and place it down and after a certain number of pieces
# move back one block and start again
# Once you have completed one level, you move up one level and repeat
# until there are no more blocks left of the conveyor belt
#
# As long as the pieces are in the right order and
# you know where to place the blocks, you don't need to know what they are
# You might not even recognize what it is until you have built most of it
# When it is time to move upwards, our blueprint will tell us with a
# special code

# The with keyword really means "with this do that", in our case we want to
# open up our file so we can read it, like choosing a book and opening it
# The 'rb' tells the computer we want to look at (read) the file
# rather than write to it

# Some buildings might have a cellar or other things below ground
# floorLevel lets us adjust where we start building from
floorLevel = 0

with open(buildFile, 'rb') as csvfile:
    # We are using a comma as a separator, you can use something else, but for
    # now lets stick with a comma
    houseData = csv.reader(csvfile, delimiter=',')
    # The first line of information contains the name of the house we are building, so skip that for now
#    houseData.next()
    # Set the coordinates for where we want to start building , which will be
    # the bottom left corner
    x = xStart
    y = yStart - 1 + floorLevel
    z = zStart

    # Start reading our blueprints until there is no more information left
    for row in houseData:
        # Reset our X coordinate to the edge of the square for each floor and step back one from where we are standing
        # We don't want to build on top of our self
        x = xStart
        z = z + 1
        # each row has a series of blocks, working from left to right
        for houseblock in row:
            # Check to see are we starting a new level, if so the row will only
            # have a single piece of information
            if (houseblock.startswith("L")):
                # move upwards one block and then back to the edge of the
                # square ready for the next layer
                y = y + 1
                x = xStart
                z = zStart
            # Do a quick check to see if we have a block number, sometimes files are corrupted
            # This is called defensive programming, things shouldn't go wrong, but they might
            # Although this can make our progam run slower, as you write more complex programs
            # you will probably write more code like this to prevent program
            # crashes
            elif(houseblock != ''):
                # is there a second piece of information about the block, if there is a ";" in our data
                # this tells us the block is special and has an extra piece of information
                # if there is no extra information, extra will be "-1"
                extra = houseblock.find(';')
                if (extra == -1):
                    # No extra information, so just draw the block and move on
                    # to the next one
                    blocknumber = int(houseblock)
                    mc.setBlock(x, y, z, blocknumber)
                else:
                    # We have a special block (door, torch, step) that has an extra piece of information
                    # this might be telling us the direction it is facing or the color
                    # We use the split operator to separate the two pieces of information
                    # we use two variables to hold the information
                    # We haven't looked a different variable types yet
                    # but the variables b and c need a bit of help before we
                    # can use them
                    b, c = houseblock.split(";")
                    blocknumber = int(b)
                    blocktype = int(c)

            # Certain blocks, such as torches, doors,ladders and beds cannot be drawn unless they have something
            # to attach to, a torch needs to be on a wall, so these special blocks we must leave until last
            # This next bit of code keeps track of these special items and adds them to a list
            # Once the house has finished being built, we will draw these special items
            # Our special block list looks a bit like this ['64,33,1,17,1','64,33,2,17,2'...]
            #
                    if (blocknumber in specialList):
                        specialBlocks.append(
                            str(x) +
                            "," +
                            str(y) +
                            "," +
                            str(z) +
                            "," +
                            str(blocknumber) +
                            "," +
                            str(blocktype))
                    else:
                        mc.setBlock(x, y, z, blocknumber, blocktype)
                # Move to the right ready for the next block
                x = x + 1

# The blueprint has all been read, now we need to draw all the items in our special list
# Each item has the x,y,z coordinate of where it needs to go, then the
# type of block and extra information it needs
for item in specialBlocks:
    x, y, z, blocknumber, blocktype = item.split(",")
#    print blocknumber,blocktype
    mc.setBlock(int(x), int(y), int(z), int(blocknumber), int(blocktype))

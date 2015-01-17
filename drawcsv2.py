#! /usr/bin/python
# Joe Deller 2014
# Draw items in Minecraft using a specified file

# Level : Advanced
# Uses  : Libraries, variables, loops, operators, logic, files, lists
# Usage : ./drawcsv2.py [datafile.csv] [+/- difference from ground level]

# Build the minecraft structure specified on the command line

# Some improvements in this version
# The program reads the building file first to figure out
# how big it is, width, depth and height
# Ideally our building file would have this information stored inside it
# rather than us having to calculate it every time.
# Sometimes writing code is about having to work around problems
# that weren't thought of earlier.  Sometimes those problems
# are ones you've made yourself :-)

# This version also reads in a list of Minecraft blocks that are
# valid on the raspberry pi and reports on those it cannot draw
# compared to the "full" minecraft

# Finally you can specify the floor level as the 3rd command line parameter
# This is for buildings that have things  like  basements or swimming pools
# For these use a negative number
# For balloons and planes, you can use a positive number

# Some of the models originally came from the PC version of Minecraft
# using the Mace world generator program
# https://code.google.com/p/mace-minecraft/
# They were modified where necessary to work with the Pi version


import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
# The next two libraries let us find out what someone typed
# on the command line and make sure that the file specified exists
import os.path
import sys

# First our minecraft connection
mc = minecraft.Minecraft.create()

# If you are running this program in IDLE
# Just set the filename you want to build here

build_file = "sailship1.csv"

# Unless we told the program otherwise, start building one down from 
# where we are standing
floor_level = -2
# Here is a list of files that you can use.
# balloon.csv   bamboo3.csv baths.csv bigcastle.csv
# bigchurch.csv  church3.csv   coolpool.csv  dalek2.csv
# emblemankh.csv emblemheart.csv   firefount.csv
# fountain.csv greenhouse.csv guitar.csv guitar2csv
# hammadoll.csv  hammadoll2.csv
# house.csv  house2.csv   largehouse.csv   library.csv
# newcastle2.csv    pyramid.csv
# sailship1.csv  sailship2.csv smallchurch.csv
# statue.csv
# swimming.csv treehouse1.csv village3.csv windmill.csv
# woodhouse.csv


# The sys.argv method allows us to see what was typed on a command line
# To use this program we type its name then a space then the name
# of the building we want to draw and if we want, a floor level
# Some buildings have cellars so we need to adjust the floor level 
# otherwise the bottom of the cellar will be at ground level


# Did we type a building file, if we are running this in IDLE
# then the file we named above will be used
if (len(sys.argv) >= 2):
    build_file = sys.argv[1]
    # What about the floor level
    if (len(sys.argv) >= 3):
        floor_level = int(sys.argv[2])

# Now we need to check that the file exists.
# Otherwise we must stop and report the problem.
if (os.path.isfile(build_file)):
    print "Going to build " + build_file
else:
    print "Sorry, I can't find the file called:" + build_file
    print "Stopping."
    exit()


# We should have a file that contains a list of the blocks the Raspberry Pi
# Minecraft can draw.
# The code will read all the the valid blocks into a list, ready to use later on
# Dec 2014 - It seems that placing two doors next to each other causes a problem and both
# doors get destroyed.

# The with keyword really means "with this do that", in our case we want to
# open up our file so we can read it, like choosing a book and opening it
# The 'rb' tells the computer we want to look at (read) the file
# rather than write to it


piblocksFile = "piblocks1.csv"

validBlocks = []
if (os.path.isfile(piblocksFile)):
    with open(piblocksFile, 'rb') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in data:
            for validBlock in row:
                validBlocks.append(int(validBlock))
else:
    print ("I can't find the file called " + piblocksFile)
    print ("There might be some blocks that I can't draw.")

# There are some minecraft blocks that have special rules when you place them
# A torch has to be attached to a wall for example
# It's best to leave lava until whatever it is going to be kept in has
# been drawn.
# We will keep a list of these special blocks and add them after the main building is done
# This is a bit of trial and error.


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

# Our list of blocks we must leave till last will start as an empty list
specialBlocks = []

# Now read in our blueprint from the file
# Imagine a conveyor belt of lego pieces coming towards you
# If you have the right instructions, you take one piece at a time
# and place it down and after a certain number of pieces
# move back one block and start again
# Once you have completed one level, you move up one level and repeat
# until there are no more blocks left on the conveyor belt
#
# As long as the pieces are in the right order and
# you know where to place the blocks, you don't need to know what they are
# You might not even recognize what it is until you have built most of it
# When it is time to move upwards, our blueprint will tell us with a
# special code

# Some buildings might have a cellar or other things below ground
# floorLevel lets us adjust where we start building from


height = 0
width = 0
lines = 0

# Not the most efficient way, but find out how big our building is
# read the file in and count how many lines there are
# for every "L" line add one to the height
# Open the file we typed or use build_file if nothing was typed
with open(build_file, 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in data:
        if (row != '' and row[0].startswith("L")):
            height = height + 1
        else:
            # The width of the building should always be the same
            # so if we've worked it out once, no need to do it again
            if (width == 0):
                width = len(row)
            lines = lines + 1
    depth = lines / height

print "width ", width
print "height = ", height
print "depth = ", depth

# Now we have a file that we can use, lets start building.
# Make a note of where we are standing, so we can build our house close by
playerPos = mc.player.getTilePos()
xStart = playerPos.x
yStart = playerPos.y
zStart = playerPos.z + 2

yStart = yStart + floor_level

print "Building at ", xStart, yStart, zStart
# clear some space.  This version doesn't draw a grass floor
mc.setBlocks(
    xStart - 1,
    yStart + 1,
    zStart - 1,
    xStart + width,
    yStart + height + 4,
    zStart + depth,
    block.AIR)


# TODO - Tidy up the code that handles blocks we can't draw
# If it's not in our list then just move on

with open(build_file, 'rb') as csvfile:
    # We are using a comma as a separator, you can use something else, but for
    # now lets stick with a comma
    house_data = csv.reader(csvfile, delimiter=',')
    # Set the coordinates for where we want to start building , which will be
    # the bottom left corner
    x = xStart
    y = yStart
    z = zStart

    # Start reading our blueprints until there is no more information left
    for row in house_data:
        # Reset our X coordinate to the edge of the square for each floor
        # and step back one from where we are standing
        # We don't want to build on top of ourselves
        x = xStart
        z = z + 1
        # each row has a series of blocks, working from left to right
        for house_block in row:
            # Check to see are we starting a new level, if so the row will only
            # have a single piece of information
            if (house_block.startswith("L")):
                # move upwards one block and then back to the edge of the
                # square ready for the next layer
                y = y + 1
                x = xStart
                z = zStart
            # Do a quick check to see if we have a block number, sometimes files are corrupted
            # This is called defensive programming, things shouldn't go wrong, but they might
            # Although this can make our code run slower, as you write more complex programs
            # you will probably write more code like this to prevent program
            # crashes
            elif (house_block != ''):
                # is there a second piece of information about the block, if there is a ";" in our data
                # this tells us the block is special and has an extra piece of information
                # if there is no extra information, extra will be "-1"

                extra = house_block.find(';')
                if (extra > 0):
                    # We have a special block (door, torch, step) that has an extra piece of information
                    # this might be telling us the direction it is facing or the color
                    # We use the split operator to separate the two pieces of information
                    # we use two variables to hold the information
                    # We haven't looked a different variable types yet
                    # but the variables b and c need a bit of help before we can use them
                    b, c = house_block.split(";")
                    block_number = int(b)
                    block_type = int(c)
                else:
                    # No extra data
                    block_number = int(house_block)
                    block_type = 0
                    # Can we draw this block ? Pi Minecraft only has a limited set of blocks
                if (block_number in validBlocks):
                    # We can draw the block, but is it a special block that needs to be drawn later?
                    if (block_number in specialList):
                        # Certain blocks, such as torches, doors,ladders and beds cannot be drawn unless they
                        # have something to attach to. A torch needs to be on a wall,
                        # so these special blocks we must leave until last
                        # This next bit of code keeps track of these special items and adds them to a list
                        # Once the house has finished being built, we will draw these special items
                        # Our special block list looks a bit like this ['64,33,1,17,1','64,33,2,17,2'...]
                        specialBlocks.append(
                            str(x) +
                            "," +
                            str(y) +
                            "," +
                            str(z) +
                            "," +
                            str(block_number) +
                            "," +
                            str(block_type))
                    else:
                        # After all that, we can just draw the block
                        mc.setBlock(x, y, z, block_number, block_type)


            # Move to the right ready for the next block
            x = x + 1  # The blueprint has all been read, now we need to draw all the items in our special list
# Each item has the x,y,z coordinate of where it needs to go, then the
# type of block and extra information it needs
for item in specialBlocks:
    x, y, z, block_number, block_type = item.split(",")
    # print block_number,block_type
    mc.setBlock(int(x), int(y), int(z), int(block_number), int(block_type))

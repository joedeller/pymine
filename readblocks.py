#! /usr/bin/python
# Joe Deller 2014
# A minecraft "photocopier"

# Level : Advanced
# Uses  : Libraries, variables, lists, files

# Read all the blocks in the specified area
# and save the details to a CSV or Comma Separated Values format file, ready to be used later
# In this way we can create copies of our work

# Comma Separated Values is an old, fairly simple way of storing information
# that is still widely used.
# This program is quite slow , the larger the area you select, the slower it gets

import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
playerPos = mc.player.getTilePos()

# Set the area you want to scan, from the bottom left corner of your object
#  to the top right corner

# The "start" points should be the smallest numbers
# Watch out f the numbers are negative, -100 is smaller than -50
# Also the "y" value you see on the Minecraft screen is where your feet are.
# The ground is one below that.  If your building goes underground, don't forget
# to make sure the y_start is the lowest point

x_start = 134
x_finish = 144

y_start = 62
y_finish = 71

z_start = 253
z_finish = 268

# Keep track of how many levels our building has
level = 1

# Remember to change the name here every time you scan a new object
# Open a file ready for writing "w"
# If there is already a file with the same name, it will get overwritten and the
# original contents will be lost.  Take care!

saveFile = open("house5.csv", "w")

# We are going to scan from the bottom left corner to the top right
# moving across first, then back, then upwards

for y in range(y_start, y_finish + 1):
    # the "\n" means start a new line, like you would do when writing in a ruled notebook
    saveFile.write("L:" + str(level) + "\n")
    print "L:" + str(level)
    for z in range(z_start, z_finish + 1):
        line = ""
        for x in range(x_start, x_finish + 1, 1):
            # We need to do two things.  First find out what type of block we scan
            # Secondly, does it have extra information, like a color, direction, type
            b = mc.getBlockWithData(x, y, z)
            line = line + str(b.id)
            # Check for the extra information
            if (b.data != 0):
                # This code needs expanding to handle buildings that were not facing north when we scanned them
                #
                line += ";" + str(b.data)
            line += ","
        line = line[:-1]
        saveFile.write(line + "\n")
        print line + "\n"
    level = level + 1
saveFile.close()

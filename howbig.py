#! /usr/bin/python
# Joe Deller 2014
# Find out how big our template buildings stored in their csv files are

# Level : Intermediate
# Uses  : Libraries, variables, operators, loops, files


# Our CSV files that contain blue prints for buildings do not
# contain any information about how big they are
# This program simply scans them and works out their size

# We could then modify the blue prints to store this information

import os.path
import sys
import csv

build_file = "swimming.csv"

if (len(sys.argv) >= 2):
    build_file = sys.argv[1]

if (os.path.isfile(build_file)):
    print "Going to measure " + build_file
else:
    print "Sorry, I can't find the file called:" + build_file
    print "Stopping."
    exit()

lines = 0
height = 0
width = 0
# Open the file we typed or use build_file if nothing was typed
with open(build_file, 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in data:
        if (row[0].startswith("L")):
            height = height + 1
        else:
            # The width of the building should always be the same
            # so if we've worked it out once, no need to do it again
            if (width == 0):
                width = len(row)
            lines = lines + 1

    depth = lines / height
    print (build_file + " is " + str(height) +" high, " +str(depth) + " deep, " + str(width) +" wide")



#!/usr/bin/python
# Joe Deller 2014
# Minecraft times tables

# Level : Beginner
# Uses  : Libraries, variables, operators, loops

import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

# Change this to the times table you want to calculate

table = 8

for count in range(1, 13):
    answer = count * table
    stringCount = str(count)
    stringAnswer = str(answer)
    mc.postToChat(stringCount + " times nine = " + stringAnswer)
    time.sleep(1)

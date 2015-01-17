#! /usr/bin/python
# Joe Deller  2014
# Advanced Coding Example, Threads ! Classes!


# Level : Advanced
# Uses  : Libraries, classes, threads, variables, operators, loops

# For many years most personal computers (well ones you could afford)
# were really only capable of doing one thing at a time
# but they were still so fast at doing them, it looked like many things were happening
# at the same time

# As technology has progressed, chips started to have more than one processor
# on them.  Today even mobile phones have multiprocessor chips
# that really can do several things at one.   Programming these systems
# has always been trickier than single processor systems and a cause
# of complicated bugs

# The Threading library is a way of helping us write code that do several
# things at the same time.   Technically it isn't a true multi threading library
# but for now we don't care as it does the job
#

# We will take our firework program and change it to launch several fireworks at once
# The Raspberry Pi is not a very powerful processor, so we are limited
# by how many things in minecraft we can do at once, it is already doing lots of
# things running minecraft
# but launching three fireworks at the same time is possible

# This does mean some big changes to the layout of the program
# But the code that draws the firework is still the same

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import math
import threading
import random

# We need to "wrap up" our code into something called a class
# Classes are a very powerful way of re using code
# and hiding away code we are not directly interested in
# They are a bit like a blueprint, once you have a design
# it is easy to make lots of objects using that blueprint
# In our case, we want three lots of firework launches
# If we know how to make one, then all we have to do
# is tell our program we want three of them, all in slightly different places


class Fireworks(threading.Thread):

    # Our firework class is mostly the same code as the previous firework code
    # It has some extra code that lets us run several at the same time

    # This is a special method that runs when the thread starts, the "initialise"
    # where we do any housekeeping before the code starts doing something
    # In our case, we store our x,y & z coordinates of where we want our firework  so that our methods can use them
    # After init is finished, we hand over to run
    def __init__(self, px, py, pz):
        threading.Thread.__init__(self)
        self.px = px
        self.py = py
        self.pz = pz

    def run(self):
        mc = minecraft.Minecraft.create()
        self.Setup(mc, px, py, pz)

    def DrawSingleCircle(self, px, py, z, diameter, color, mode):
        if (mode == 1):
            if (color == 0):
                blockID = block.GLOWSTONE_BLOCK.id
            elif (color == 1):
                blockID = block.GLOWING_OBSIDIAN.id
            elif (color == 2):
             # blockID = block.REDSTONE_ORE.id
                blockID = block.LAVA_STATIONARY.id
        else:
            blockID = block.AIR.id

        endX = 2 * math.pi
        x = 0.01
        while (x < endX):
            # We add the firework X and Y coordinates to the circle so the explosion is in the right place
            # When we draw our blocks, we need to convert the floating point
            # numbers back to integers
            dx = int(diameter * math.cos(x)) + px
            dy = int(diameter * math.sin(x)) + py
            mc.setBlock(dx, dy, z, blockID, color)
            # we want a reasonably spokey circle, so add 0.4 or larger
            # this also makes it a bit faster and more realistic
            x = x + 0.5

    def DrawCircles(self, cx, cy, z):
        # To create an explosion effect, we draw three circles, then start rubbing them out
        # starting with the smallest circle
        # keep a count of how many circles we have drawn, when we get to three
        # start rubbing out
        circlesDrawn = 0
        # Start with white
        color = 0
        # We want a big explosion, but not so big that it goes below ground
        maxDiameter = 14

    # Now draw some circles, slowly increasing the size (diameter)
        for diameter in range(3, maxDiameter, 1):
            # Go and draw the circle
            self.DrawSingleCircle(cx, cy, z, diameter, color, 1)

            circlesDrawn = circlesDrawn + 1
            if (circlesDrawn > 2):
                # now rub out the circle we drew 3 loops ago
                self.DrawSingleCircle(cx, cy, z, diameter - 2, color, 0)
            # Wool has 16 different colors, 0-15, so recycle them
            color = color + 1
            if (color == 3):
                color = 0

    # unplot the last 2 circles, as our loop has finished drawing
        self.DrawSingleCircle(cx, cy, z, maxDiameter - 1, color, 0)
        self.DrawSingleCircle(cx, cy, z, maxDiameter - 2, color, 0)

    def LaunchRocket(self, rocketX, rocketY, rocketZ):
            # Place the rocket
            # time.sleep(1)
        flames = [14, 1, 4, 10]
        flame_colours =len(flames)
        for count in range(0, flame_colours):
            for flame in range(0, 4):
                mc.setBlocks(
                    rocketX - 1,
                    rocketY,
                    rocketZ - 1,
                    rocketX + 1,
                    rocketY,
                    rocketZ + 1,
                    block.WOOL.id,
                    flames[flame])
                time.sleep(.05)

        # Clear up the flames by using a 3x3 block of air and draw some solid
        # flames
        mc.setBlock(rocketX, rocketY + 1, rocketZ, block.GLOWING_OBSIDIAN)
        mc.setBlocks(
            rocketX - 1,
            rocketY,
            rocketZ - 1,
            rocketX + 1,
            rocketY,
            rocketZ + 1,
            block.AIR)

        rocketY = rocketY + 1
        # When we draw a block, we need to remember it so that we can rub it out next time
        # this makes it look like the block is moving upwards
        # set the maximum height the rocket will launch to
        # 20 blocks higher than where it starts from
        maxHeight = rocketY + 18

        while (rocketY < maxHeight):
            mc.setBlock(rocketX, rocketY, rocketZ, block.GLOWING_OBSIDIAN)
            mc.setBlock(rocketX, rocketY + 1, rocketZ, block.FURNACE_ACTIVE.id)
            lastY = rocketY
            # rub out  the previous block
            time.sleep(0.05)
            mc.setBlock(rocketX, lastY - 1, rocketZ, block.AIR.id)
            rocketY = rocketY + 1

        # rub out the last rocket ready to explode
        mc.setBlock(rocketX, lastY + 1, rocketZ, 0)
        mc.setBlock(rocketX, lastY, rocketZ, 0)

        time.sleep(0.05)
        # Draw the explosion where the rocket finished
        self.DrawCircles(rocketX, rocketY, rocketZ)

    def Setup(self, mc, x, y, z):
        # Launch the rocket from a safe distance :-)
        rocketX = x + 1
        rocketY = y
        rocketZ = z + 1
       # A single stone block for the rocket to sit on
        mc.setBlock(rocketX, rocketY + 1, rocketZ, block.STONE.id)
        rocketY = rocketY + 1
       # we will use a furnace to be our rocket, but change as you wish
        mc.setBlock(rocketX, rocketY + 1, rocketZ, block.FURNACE_ACTIVE.id)

        time.sleep(.5)
        mc.setBlock(rocketX, rocketY, rocketZ, block.GLOWING_OBSIDIAN)
        time.sleep(.5)
        self.LaunchRocket(rocketX, rocketY, rocketZ)


mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
px = pos.x
py = pos.y
pz = pos.z

# if we are close to the edges of the world, moves us in a bit
if (px > 100 or px < -100):
    print "shrinking player x"
    px = int(px * 0.8)

if (pz > 100 or pz < -100):
    pz = int(pz * 0.8)
    print "shrinking player z"

mc.player.setPos(px, py, pz)

depth = 16
# Clean up the world and any previous circles nearby
mc.setBlocks(px - 25, py, pz - 2, px + 25, py + 41, pz + depth, block.AIR.id)
# Setup a grass floor
mc.setBlocks(px - 30, py - 1, pz - 30, px + 20, py, pz + 30, block.GRASS.id)

mc.setBlocks(px - 20, py, pz - 2, px + 20, py + 40, pz - 2, block.WOOL.id, 15)
mc.setBlocks(
    px - 20,
    py,
    pz - 2,
    px - 20,
    py + 40,
    pz + depth,
    block.WOOL.id,
    15)
mc.setBlocks(
    px - 20,
    py,
    pz + depth,
    px + 20,
    py + 40,
    pz + depth,
    block.WOOL.id,
    15)
mc.setBlocks(
    px + 20,
    py,
    pz + depth,
    px + 20,
    py + 40,
    pz - 2,
    block.WOOL.id,
    15)

mc.setBlocks(
    px - 20,
    py + 34,
    pz - 2,
    px + 20,
    py + 34,
    pz + depth,
    block.WOOL.id,
    15)
mc.setBlocks(
    px - 10,
    py + 34,
    pz,
    px + 10,
    py + 34,
    pz + depth / 2,
    block.GLOWSTONE_BLOCK.id)

mc.setting("world_immutable", False)

time.sleep(.5)

for l in range(0, 3):
    for launchCount in range(0, 4):
        if (random.randint(0, 1) == 1):
            px = pos.x - random.randint(5, 12)
        else:
            px = pos.x + random.randint(5, 12)
        pz = pos.z + random.randint(8, 15)

#    print px,pz
        firework = Fireworks(px, py, pz)
        firework.daemon
        firework.start()
        time.sleep(random.uniform(0.2, 0.5))
    time.sleep(6)

time.sleep(2)

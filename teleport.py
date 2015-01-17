#! /usr/bin/python
# Joe Deller 2014
# Portal Teleport Program

# Level : Intermediate
# Uses  : Libraries, variables, operators, logic, loops

# Use the random library to help generate
# a series of portals that will teleport the player
# to another random portal

# Use setBlocks and setBlock to draw the portal
# Use a list to store where our portals are
# Use getTilePos to find out where the player is
# Use setTilePos to make the player teleport

# TODO - How about changing the program so the portals can
# only be used once ?


import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

# nether brick is 112 on the Raspberry Pi Minecraft.
# It isn't in the block list library for some reason.

def drawPortal(location, color):
    # Draw a rectangular portal made from different color wool
    # 3 wide by 3 high with a glowstone in the middle top
    # Clear a space in front and behind the portal and
    # make a small grass floor so that if our portal is in the sky
    # the player doesn't fall after teleporting to it
    # We use different colors to help show we have teleported.
    # Our location variable contains the x, y & z position
    # of where we'd like to place our portal
    x, y, z = location
    # First clear a space
    mc.setBlocks(x - 2, y, z + 2, x + 3, y + 5, z -2, block.AIR.id)
    # Now a small grass floor
    mc.setBlocks(x - 2, y - 1, z - 2, x + 3, y - 1, z + 2, block.GRASS.id)
#   mc.setBlocks(x-1,y,z,x+1,y+2,z,112)
    # Draw a square block of wool first
    mc.setBlocks(x - 1, y, z, x + 1,y + 2, z, block.WOOL.id,color)
    # Now rub out a space in the middle for us to walk through
    mc.setBlocks(x, y, z, x, y + 1, z, block.AIR.id)
    # Finally a glowstone block to light the way to the portal
    mc.setBlock(x, y + 2, z, block.GLOWSTONE_BLOCK.id)


def makePortals():
    # Here's where we will draw our portals 
    playerPos = mc.player.getTilePos()

    # Create out first portal slightly in front and left of us
    portalOne = playerPos
    portalOne.z = portalOne.z -2
    portalOne.x = portalOne.x - 1

    # We will store our portals is a list
    # Add the first one now
    portalList.append(portalOne)
    # Draw our first portal with a white wool block , color 0
    drawPortal(portalOne, 0)
    portals = 1
    color = 1

    # Now make 7 more portals in random locations
    # The portals will be up to 30 blocks left or right
    # up to 100 blocks forward or back and
    # up to 20 blocks higher than where the player starts from

    while (portals < 9 ):
        x = random.randint(0, 30)
        y = random.randint(0, 10)
        z = random.randint(0, 30)

        # randomly flip between to the left or right
        # of where the player is
        if (random.randint(0, 1) == 1):
            x = - x
        # randomly flip between in front or behind the player
        if (random.randint(0,1) == 1):
            z = - z

        # Add the player position to our randomly chosen
        # coordinates
        x = x + playerPos.x
        y = y + playerPos.y
        z = z + playerPos.z

        portalPos = minecraft.Vec3(x, y, z)
        # There is always a small chance that we might randomly choose
        # the same coordinates as a portal we've already added
        # so check and if we have, choose new random coordinates
        # Otherwise, add the portal to our list
        # There is also a small chance that a portal might be right next to 
        # another, either behind, in front, left right
        # We could check for this and some programs would have to
        # For this program will we live with that small chance

        # To check that the new portal position hasn't already been taken
        # we use "if not", as in "if not in the list"
        if (not (portalPos in portalList)):
            portalList.append (portalPos)
            portals = portals + 1
            drawPortal(portalPos, color)
            color = color + 1

    # The loop has finished and we should have 8 portals
    # Print out where our portals are in the world
    print portalList


mc = minecraft.Minecraft.create()
# Our portal locations will be store in a list
portalList = []
makePortals()


while True:
    # Find out where the player is
    playerPos= mc.player.getTilePos()
    # Did we step into one of our portals?
    if (playerPos in portalList):
        print "Stepped into a portal.  Jumping"
        # Pick a new portal from our list
        newportal = portalList[random.randint(0, 8)]
        # Check that we haven't chosen this one!
        while (playerPos == newportal):
            print "jump failed, randomising again"
            print playerPos,newportal
            # Try a new random portal
            newportal = portalList[random.randint(0, 8)]

        print "found new portal at ",newportal
        # Teleport !
        mc.player.setTilePos(newportal.x,newportal.y,newportal.z - 2)
    time.sleep(.1)

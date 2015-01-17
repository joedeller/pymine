#! /usr/bin/python
# Joe Deller 2014
# A Day at the Minecraft Races

# Level : Intermediate
# Uses  : Libraries, variables, loops, lists, methods, loops and logic

# This example introduces lists as a way of keeping track of information that is changing
# It uses the random number generator to simulate a race between 6 horses
# well, blocks of wool, there are no horses in the raspberry Pi minecraft world :-(

# We have some very simple animation that makes it look like our horses are moving
# We do this by replacing where the horse is now with a block of air
# then drawing the horse one block forward
# It's not Disney, but it works.

import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time


def drawCourse(x, y, z, track_length):
    # Our track is going to be made with stripes
    # to make it look a little neater
    # Draw 8 tracks altogether, in gravel and sand
    # At the end of the track draw some chequered wool

    # x and z are where we want to start drawing the track from
    # Don't make the track length too long or it will disappear into the distance.
    # This is a nice simple straight course, it makes the racing code fairly simple
    # A more advanced program could draw a looped track, but lets keep it
    # simple for now

    # Draw a couple of pillars at the end to make a finish archway
    arch_height = 6
    left_pillar_x = x
    # track is 8 wide so the right pillar is 9 blocks from the left one
    right_pillar_x = x + 9
    pillar_z = z + track_length + 1

    mc.setBlocks(
        left_pillar_x,
        y,
        pillar_z,
        left_pillar_x,
        y + arch_height,
        pillar_z,
        block.WOOD_PLANKS.id)

    mc.setBlocks(
        right_pillar_x,
        y,
        pillar_z,
        right_pillar_x,
        y + arch_height,
        pillar_z,
        block.WOOD_PLANKS.id)

# To make the track look pretty, we will alternate between gravel and sand
# This means our loop will count up in twos as we are drawing two tracks
# each time we go around the loop

    for track in range(1, 9, 2):
        # The track will be at ground level, which is our y position minus one
        # In this loop we need to work out what the x position of the tracks are
        # each time around the loop.  We use a variable to do this only once per loop
        # as several lines of code need this value

        # Can you see any other calculations that are done several times
        # that we could do once and use a variable to store the result?

        tx = x + track
        mc.setBlocks(tx, y - 1, z, tx, y - 1, z + track_length, block.GRAVEL.id)
        mc.setBlocks(tx + 1, y - 1, z, tx + 1, y - 1, z + track_length, block.SAND.id)

        # At the finish line we have a chequered pattern
        #  0 is white, 15 is black
        mc.setBlock(tx, y - 1, z + track_length + 1, block.WOOL.id, 0)
        mc.setBlock(tx, y - 1, z + track_length + 2, block.WOOL.id, 15)
        mc.setBlock(tx + 1, y - 1, z + track_length + 1, block.WOOL.id, 15)
        mc.setBlock(tx + 1, y - 1, z + track_length + 2, block.WOOL.id, 0)

        # Draw a chequered pattern between two the two end pillars, above the
        # ground at 6 and 7 blocks high
        mc.setBlock(tx, y + 7, z + track_length + 1, block.WOOL.id, 0)
        mc.setBlock(tx, y + 6, z + track_length + 1, block.WOOL.id, 15)
        mc.setBlock(tx + 1, y + 7, z + track_length + 1, block.WOOL.id, 15)
        mc.setBlock(tx + 1, y + 6, z + track_length + 1, block.WOOL.id, 0)


def readyHorses(x, y, start_line, total_horses):
    # Draw the horses at the start line
    # Lists start counting at item 0
    # We cheat a little by using the horse number in the list as its color
    # This saves us some coding
    # This is a trick that must be used carefully as it can get you into trouble!
    # If we have more than 15 horses for example, we run out of colours

    for horse in range(0, total_horses):
        mc.setBlock(x + horse, y, start_line, block.WOOL.id, horse)


def runRace(x, y, finish_line, horses):
    #  This is where we race the horses
    #  All the horses start at the starting line and race in a straight line towards the finish
    #  We will use a list to keep track of where our horses are in the race
    #  We will have 6 horses in the race
    # This is quite a lot of code in a single block
    # Ideally we would break it up into smaller ones
    # to help manage the code

    # At the start of the race there isn't a winner yet, so
    # we can use the Python "None" keyword for this

    winner = None
    # Our racetrack is on the ground level , Y=1, so our horses will be one above this Y=2
    # Our horses are running away from us , so we will be changing their Z
    # coordinate

    # Loop around until one of the horses is at the finish line
    # When a horse wins, make a note that the race has been won
    # allowing the rest of the horses to finish their moves

    # This isn't totally fair as we roll the dice for each horse
    # in strict order, so the first horse (white) has more chance of winning than the last (green)
    # but for now works well enough as often there is a clear winner

    # The horses move along the Z axis, away from where the player is standing
    # The maths library has a function called "max"
    # It tells us the largest number out of two more more numbers, the maximum
    # As our horses are moving towards the finish line, their Z coordinate is getting larger
    # if it bigger than the Z coordinate of  finish line, then one (or more)
    # horses has crossed the line

    race_won = False

    while (max(horses) <= finish_line):
        for horse in range(0, 6):
            # each horse will randomly move forward between 0 and three squares
            # Unlike a for loop, randint is inclusive of the end point

            moves = random.randint(0, 3)
            # for every move we have to animate the horse moving towards the finish
            # so replace where it is now with a block of air, then draw it forward one square
            # repeat this until we have reached the number of moves
            # It is a little jumpy, but then this is minecraft
            # print "horse  "+str(horse) +" moves = "+str(moves)
            for move in range(0, moves):
                # Where is our horse now ?
                horse_z = horses[horse]
                # Rub out the horse
                mc.setBlock(x + horse, y, horse_z, block.AIR)
                # now draw it one move towards the finish line
                # again we use the trick of the horse number also being its
                # color
                mc.setBlock(x + horse, y, horse_z + 1, block.WOOL.id, horse)
                # Update our list with where our horse is now, this time we use the short hand way
                # rather than writing out: horses[horse] = horses[horse] + 1
                horses[horse] += 1
                # Is this horse at the finish, has there already been a winner?
                if (horse_z >= finish_line) and (race_won is False):
                    # make a note of the winner and that the race has been won
                    # this will end our loop
                    race_won = True
                    winner = horse
                    print "Winner is :" + str(winner)
                # Wait a little bit, otherwise we won't see the race!
                time.sleep(0.1)

# Can you think of a slightly better way of doing this so there is less typing ?
# Or even better, using a list that stores the color of each horse

# Too many "if" and "else" lines can be hard to read
# Remember, "==" is used when we want to check two values are the same
# Only using one "=" when a programmer meant "==" is one of the more common mistakes
# and causes a lot of problems

# This code will break if you add more horses :-)
    if (winner == 0):
        mc.postToChat("White is the winner!")
    elif (winner == 1):
        mc.postToChat("Orange is the winner!")
    elif (winner == 2):
        mc.postToChat("Magenta is the winner!")
    elif (winner == 3):
        mc.postToChat("Blue is the winner!")
    elif (winner == 4):
        mc.postToChat("Yellow is the winner!")
    elif (winner == 5):
        mc.postToChat("Green is the winner!")


def main():
    # Start here
    # We actually wait longer than 5 seconds so the chat message disappears
    mc.postToChat("Race starting in 5 seconds...")
    x, y, z = mc.player.getTilePos()
    # If the track is too long, you won't be able to see the end on the Pi
    track_length = 22
    # Clean up the world so we have a nice flat space
    mc.setBlocks(x - 10, y, z - 10, x + 20, y + 20, z + track_length + 10, block.AIR.id)
    # Setup a grass floor
    mc.setBlocks(x - 12, y - 2, z - 12, x + 20, y - 1, z + track_length + 10, block.GRASS.id)
    # The start line is one block away from where we are standing
    start_line = z + 1
    total_horses = 6
    # This is a Python trick that we use to save typing
    # It stores the start_line for all the horses
    horses = [start_line] * total_horses

    finish_line = start_line + track_length
    # Draw the course starting at the same X co-ordinate as us
    drawCourse(x, y, start_line, track_length)
    # Draw the horses at the start line
    readyHorses(x + 1, y, start_line, total_horses)
    time.sleep(7)
    # Start the race
    runRace(x + 1, y, finish_line, horses)


mc = minecraft.Minecraft.create()
main()

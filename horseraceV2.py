#! /usr/bin/python
# Joe Deller 2014
# A second day at the Minecraft Races

# Level : Intermediate
# Uses  : Libraries, variables, loops, lists, methods, loops and logic

# Second version of the horse race program
# This time the horses will not race until we have
# clicked on a special stone block next to the start line

# TODO How about adding some steps and blocks at the side of the track
# to look like audience stands?
# How about adding some fence gates at the start of the track, then opening
# them , with setBlock (block.FENCE_GATE.id,4)
# Can you think what might go wrong with this?

# A more advanced version of this program would use threads to move the
# horses at the same time, rather than one after the other

import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time


def DrawCourse(x, y, z, track_length):
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
    # track is 8 blocks wide so the right pillar is 9 from the left one
    right_pillar_ = x + 9

    mc.setBlocks(
        left_pillar_x,
        y,
        z + track_length + 1,
        left_pillar_x,
        y + arch_height,
        z + track_length + 1,
        block.WOOD_PLANKS.id)

    mc.setBlocks(
        right_pillar_,
        y,
        z + track_length + 1,
        right_pillar_,
        y + arch_height,
        z + track_length + 1,
        block.WOOD_PLANKS.id)

# To make the track look pretty, we will alternate between gravel and sand
# This means our loop will count up in twos as we are drawing two tracks
# each time we go around the loop

    for track in range(1, 9, 2):
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


def readyHorses(x, y, start_line):
    # Draw all the horses at the start line
    # We cheat a little by using the horse number in the list as its color
    # This is a trick that must be used carefully as it can get you into
    # trouble!
    # A better way would be to have a list of colours 
    for horse in range(0, 6):
        mc.setBlock(x + horse, y, start_line, block.WOOL.id, horse)


def Race(x, y, start_line, finish_line):
    # This is where we race the horses
    # All the horses start at the starting line and race in a straight line
    # towards the finish

    #  We will use a list to keep track of where our horses are in the race
    #  We will have 6 horses in the race
    # A quick way of putting the information into our list
    horses = [start_line] * 6
    # At the start of the race there isn't a winner yet, so
    # we can use the Python "None" keyword for this
    winner = None


# Loop around until one of the horses is at the finish line
# This isn't totally fair as we work out how far each horse has travelled
# in strict order, so the first white horse
# has more chance of winning than the last green
# but for now works well enough as often there is a clear winner
# The horses move along the Z axis, away from where the player is standing

# Like a real race, several horses will cross the finish line close together
# but only the first one counts
# We will use a variable called race_won to keep track if we have a winner yet
# Variables used in this way are sometimes called "Flags"
# When they change, our code needs to take notice

    race_won = False

    while (max(horses) <= finish_line):
        for horse in range(0, 6):
            # each horse will randomly move forward between 0 and three squares
            # Instead of a dice, we use something from the random library
            # unlike a for loop, randint is inclusive of the end point
            moves = random.randint(0, 3)
            # For every move we have to animate the horse moving towards the finish, in the z direction
            # so replace where it is now with a block of air, then draw it forward one square
            # repeat this until we have reached the number of moves
            # print "horse  "+str(horse) +" moves = "+str(moves)
            for move in range(0, moves):
                # Where is our horse now ?
                horse_z = horses[horse]
                # Rub out the horse
                mc.setBlock(x + horse, y, horse_z, block.AIR)
                # now draw it one move towards the finish line
                # again we use the trick of the horse number also being it's
                # color
                mc.setBlock(x + horse, y, horse_z + 1, block.WOOL.id, horse)
                # Update our list with where our horse is now, this time we use the short hand way
                # rather than writing out: horses[horse] = horses[horse] + 1
                horses[horse] += 1
                # Now that we have moved, is this horse at or past  the finish?
                if (horse_z >= finish_line) and (race_won is False):
                    # make a note of the winner, not entirely fair as the first
                    # horse always moves first
                    race_won = True
                    winner = horse
                    print "Winner is :" + str(winner)
                # Wait a little bit, otherwise we won't see the race!
                time.sleep(0.1)
    # Unfortunately Minecraft does have a way for us to convert the color number
    # of a wool block back into a word.  We will make a list that matches
    # the known list of wool colors and use this to find the winning color
    # This is not without some possible problems.  If Minecraft were to ever change
    # its color numbers, then our code would report the wrong color
    # They shouldn't ever do this, but things like that do happen
    horse_colors = ["White", "Orange", "Magenta", "Blue", "Yellow", "Green"]
    winning_horse = horse_colors[winner]
    mc.postToChat(winning_horse + " is the winner!")


def CheckBlockIsHit(block_x, block_y, block_z):
        # Has our special starter stone been right clicked with the sword
    block_hits = mc.events.pollBlockHits()
    if(block_hits):
        for block_hit in block_hits:
            print "some thing hit at:" + str(block_hit.pos.x) + " " + str(block_hit.pos.y) + " " + str(block_hit.pos.z)
            # Was it our starter stone ?
            if(block_hit.pos.x == block_x and block_hit.pos.y == block_y and block_hit.pos.z == block_z):
                print "StartRace!"
                return True
            else:
                # The player hit something, but not the right thing so return false
                print "not the right block"
                return False


def main():
    # global x, y, z, track_length, start_line, finish_line, starting_block_x, start_race
    x, y, z = mc.player.getTilePos()
    track_length = 22
    # Clean up the world so we have a nice flat space
    mc.setBlocks(x - 10, y, z - 10, x + 20, y + 20, z + track_length + 10, block.AIR.id)
    # Setup a grass floor
    mc.setBlocks(x - 12, y - 2, z - 12, x + 20, y - 1, z + track_length + 10, block.GRASS.id)
    # The start line will be one block back from where we are standing
    start_line = z + 1
    finish_line = start_line + track_length
    # Draw a stone block right in front of where we are standing
    # We we right click it with our sword it will start the race
    starting_block_x = x
    mc.setBlock(starting_block_x, y, start_line, block.STONE.id)
    DrawCourse(x + 1, y, start_line, track_length)
    readyHorses(x + 4, y, start_line)
    start_race = False
    mc.postToChat("Right click the stone block with sword to start the race.")
    while (start_race is False):
        time.sleep(0.1)
        if (CheckBlockIsHit(starting_block_x, y, start_line)):
            start_race = True
    Race(x + 4, y, start_line, finish_line)


# Start here
mc = minecraft.Minecraft.create()
main()

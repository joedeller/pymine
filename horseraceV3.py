#! /usr/bin/python
# Joe Deller 2014

import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time


def DrawCourse(x, y, z, course_width, course_length):
    height = 6
    leftPostX = x - 1
    rightPostX = x + course_width + 1
    track_end = z + course_length

    mc.setBlocks(x, y - 1, z, x + course_width, y - 1, track_end, block.GRAVEL.id)
    track_end += 1

    leftPost = (leftPostX, y, track_end, leftPostX, y + height, track_end)
    rightPost = (rightPostX, y, track_end, rightPostX, y + height, track_end)

    mc.setBlocks(leftPost, block.WOOD_PLANKS.id)
    mc.setBlocks(rightPost, block.WOOD_PLANKS.id)

    time.sleep(1)

    for track in range(x, x + course_width + 1, 2):
        mc.setBlocks(track, y - 1, z, track, y - 1, track_end, block.SAND.id)

    colourA = 0
    for track in range(x, x + course_width + 1):
        mc.setBlock(track, y - 1, track_end, block.WOOL.id, colourA)
        mc.setBlock(track, y - 1, track_end + 1, block.WOOL.id, colourA ^15 )

        mc.setBlock(track, y + height, track_end, block.WOOL.id, colourA ^15 )
        mc.setBlock(track, y + height + 1, track_end, block.WOOL.id, colourA)
        # Use XOR to flip the colours between white (0) and black (15)
        colourA ^= 15



def readyHorses(x, y, start_line, horseCount):
    for horse in range(0, horseCount):
        mc.setBlock(x + horse, y, start_line, block.WOOL.id, horse)


def Race(x, y, start_line, finish_line, horseCount):
    horses = [start_line] * horseCount
    winner = None

    while max(horses) <= finish_line:
        for horse in range(0, horseCount):
            moves = random.randint(0, 3)
            # print "horse  "+str(horse) +" moves = "+str(moves)
            for move in range(0, moves):
                # Where is our horse now ?
                horse_z = horses[horse]
                # Rub out the horse and then move it forward one block at a time
                mc.setBlock(x + horse, y, horse_z, block.AIR)
                mc.setBlock(x + horse, y, horse_z + 1, block.WOOL.id, horse)
                horses[horse] += 1
                # Now that we have moved, is this horse at or past  the finish?
                if (horse_z >= finish_line) and (winner is None):
                    winner = horse
                    print "Winner is :" + str(winner)
                # Wait a little bit, otherwise we won't see the race!
                time.sleep(0.1)

    horse_colors = ["White", "Orange", "Magenta", "Blue", "Yellow", "Lime", "Pink", "Gray", "Lt Gray", "Cyan"]
    # Sanity check, list only has ten colours in it
    winning_horse = horse_colors[winner]
    mc.postToChat(winning_horse + " is the winner!")


def waitforstart(x, y, z):
    # Has our special starter stone been right clicked with the sword
    start_race = False
    while start_race == False:
        block_hits = mc.events.pollBlockHits()
        if (block_hits):
            for block_hit in block_hits:
                print "some thing hit at:" + str(block_hit.pos.x) + " " + str(block_hit.pos.y) + " " + str(
                    block_hit.pos.z)
                # Was it our starter stone ?
                if (block_hit.pos.x == x and block_hit.pos.y == y and block_hit.pos.z == z):
                    print "StartRace!"
                    start_race = True
                else:
                    # The player hit something, but not the right thing so return false
                    print "not the right block"
        time.sleep(0.1)


def main():
    x, y, z = mc.player.getTilePos()
    track_length = 22
    horseCount = 8  # Note that too many will make the code very slow and >9 will break the code

    # Clean up the world so we have a nice flat space
    mc.setBlocks(x - 10, y, z - 10, x + 20, y + 20, z + track_length + 10, block.AIR.id)
    # Setup a grass floor
    mc.setBlocks(x - 12, y - 2, z - 12, x + 20, y - 1, z + track_length + 10, block.GRASS.id)
    # The start line will be one block back from where we are standing
    start_line = z + 1
    finish_line = start_line + track_length
    # Draw a stone block right in front of where we are standing
    # We we right click it with our sword it will start the race
    mc.setBlock(x, y, start_line, block.STONE.id)
    # Draw the course one block to right of where we are standing
    DrawCourse(x + 1, y, start_line, horseCount + 1, track_length)
    # Draw the horses two blocks to the right
    horse_x = x + 2
    readyHorses(horse_x, y, start_line, horseCount)
    mc.postToChat("Right click the stone block with sword to start the race.")

    waitforstart(x, y, start_line)

    Race(horse_x, y, start_line, finish_line, horseCount)


# Start here
mc = minecraft.Minecraft.create()
main()

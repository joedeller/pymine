#! /usr/bin/python
# Joe Deller 2014

# Level : Advanced
# Uses  : Loops, files, lists, two dimensional arrays (lists)

# Draw a random maze.
# Once again the original code idea has come from Wikipedia and I have just adapted it
# into a Minecraft friendly format.  The mathematics required to draw the maze
# was written by someone else, you don't necessarily have to understand how
# it calculates the maze, only that it is calculating a maze

# The original printed different characters to the screen
# I have left much of the original code in and just commented out
# the parts that I didn't need
# The one small problem with this maze is there isn't an entrance or an exit....


# First our Minecraft connection
import mcpi.minecraft as minecraft
import mcpi.block as block
from random import shuffle, randrange

# The default is 12 wide by 14 deep
def make_maze(w=12, h=14):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    # ver = [["100"] * w + ['1'] for _ in range(h)] + [[]]
    # init array with --- * width
    # hor = [["111"] * w + ['1'] for _ in range(h + 1)]
    hor = [["|--"] * w + ['|'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "|  "
            if yy == y:
                ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))
    maze = []
    for (a, b) in zip(hor, ver):
        # row =(''.join(a + ['\n'] + b))
        row = (''.join(a))
        print row
        maze.append(row)
        row = (''.join(b))
        maze.append(row)
        print row
        # print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        # row =(''.join(a +  b))
        # maze.append(row)
        # print((a + ['\n'] + b))
        # print b

    # Make a note of where we are standing, so we can build our maze close by
    playerPos = mc.player.getTilePos()
    xStart = playerPos.x + 2
    yStart = playerPos.y
    zStart = playerPos.z - 14

    # clear some space and lay down some grass
    mc.setBlocks(
        xStart - 20,
        yStart,
        zStart - 20,
        xStart + 40,
        yStart + 20,
        zStart + 20,
        block.AIR)
    mc.setBlocks(
        xStart - 20,
        yStart - 2,
        zStart - 20,
        xStart + 40,
        yStart - 1,
        zStart + 20,
        block.GRASS.id)

    y = yStart
    z = zStart - w

    print "-------------------------"
    for row in maze:
        print row
        # Reset our X coordinate to the edge of the square for each floor and step back one from where we are standing
        # We don't want to build on top of our self
        x = xStart
        z = z + 1
        # each row has a series of blocks, working from left to right
        for maze_block in row:
            # print maze_block
            if (maze_block == " "):
                mc.setBlocks(x, y, z, x, y + 2, z, block.AIR.id)
            else:
                mc.setBlocks(x, y, z, x, y + 2, z, block.LEAVES.id)
                # Move to the right ready for the next block
            x = x + 1


mc = minecraft.Minecraft.create()
make_maze()

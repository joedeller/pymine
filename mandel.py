#!/usr/bin/python
# Joe Deller 2014
# A very simplified version of the Mandelbrot set

# Level : Intermediate
# Uses  : Libraries, variables, lists

# I have taken some example code for how to draw the Mandelbrot set from Wikipedia
# and made it compatible with the Pi.
# This isn't a true fractal program as we can't zoom in
# This is another example of where it isn't necessary to understand the code completely
# to be able to use it.
# If you know that fractals draw patterns in different colors, then
# it's just a question of converting the fractal code to draw blocks instead.


import mcpi.minecraft as minecraft
import mcpi.block as block

blockList = [block.STONE, block.DIRT, block.GRASS, block.SAND,
             block.WOOD, block.WOOD_PLANKS, block.LAPIS_LAZULI_BLOCK,
             block.COAL_ORE, block.IRON_ORE, block.WOOL, block.GLASS,
             block.WATER]


def chooseBlock(iterations):
    if (iterations > 10 ):
        return block.WATER
    else:
        return (blockList[iterations])


def drawMandelbrot(xPos, yPos, zPos, imgx, imgy, maxIt, xa, ya, xb, yb):
    for y in range(imgy):
        zy = y * (yb - ya) / (imgy - 1) + ya
        for x in range(imgx):
            zx = x * (xb - xa) / (imgx - 1) + xa
            # The next line uses something called a complex, or imaginary number
            # This is from a fairly advanced set of mathematics
            z = zx + zy * 1j
            c = z
            for i in range(maxIt):
                if abs(z) > 2.0: break
                z = z * z + c
            mc.setBlock(xPos + x, yPos, zPos + y, chooseBlock(i))


mc = minecraft.Minecraft.create()
x, y, z = mc.player.getTilePos()
mc.setBlocks(x -10, y, z, x + 40, y + 40, z + 50, block.AIR.id)
mc.setBlocks(x -10, y - 2, z, x + 40, y + -1, z + 50, block.GRASS.id)

# You can try different numbers and see what happens to the shape that is drawn
# Try changing by small amounts first.
# It's never going to be super detailed in Minecraft, but it does work, sort of


drawMandelbrot(x - 10,  y - 1, z - 10, 60, 60, 554, -2.0, -1.5, 1.0, 1.5)

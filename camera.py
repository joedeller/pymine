#! /usr/bin/python
# Joe Deller 2014

# Level : Beginner
# Uses  : Libraries, variables

# We can change the Minecraft camera from the normal player view
# to a fixed view, which we can move around without moving the player

import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()
mc.postToChat("Setting Camera to Fixed")
time.sleep(4)

playerPos = mc.player.getTilePos()

x = playerPos.x
y = playerPos.y
z = playerPos.z

# Tell Minecraft to use the fixed camera
mc.camera.setFixed()
time.sleep(1)

# Now let's move the camera up 12 blocks
# remember, a for loop counts up to, but not including the second number
for height in range(y, y + 13):
    mc.camera.setPos(x, height, z)
    time.sleep(0.1)

time.sleep(1)

# Lets move the camera backwards, 48 blocks

for depth in range(z, z + 49):
    mc.camera.setPos(x, y + 12, depth)
    time.sleep(0.1)

# to the right
for horizontal in range(x, x + 21):
    mc.camera.setPos(horizontal, y + 12, z + 48)
    time.sleep(0.1)

# forwards again
for depth in range(z + 48, z - 1, -1):
    mc.camera.setPos(x + 20, y + 12, depth)
    time.sleep(0.1)

# to the left
for horizontal in range(x + 20, x -1, -1):
    mc.camera.setPos(horizontal, y + 12, z)
    time.sleep(0.1)

# back down
for height in range(y + 12, y, -1):
    mc.camera.setPos(x, height, z)
    time.sleep(0.1)

# Reset back to normal
mc.postToChat("Setting Camera back to Normal")
mc.camera.setNormal()
mc.camera.setPos(x, y, z)

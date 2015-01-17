#! /usr/bin/python
# Joe Deller 2014
# Adding more information to a variable.
# Level : Beginner
# Uses  : Libraries, variables

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

message = "Hello Joe!"
message = "Is that Joe? " + message
mc.postToChat(message)

# This is called "prefixing " we add something to the beginning of our original message.
# In minecraft we will see "Is that Joe? Hello Joe!"

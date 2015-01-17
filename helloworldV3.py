#! /usr/bin/python
# Joe Deller 2014
# A simple example of using a variable.

# Level : Beginner
# Uses  : Libraries, variables

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

message = "Hello Joe!"
mc.postToChat(message)


# Once again we use round brackets to tell postToChat what it needs
# we have a variable called message and store "Hello Joe!" in it.

# The speech marks tell Python that everything inside the speech marks
# will be stored in the variable message.

# This time rather than the word "message" appearing in Minecraft
# the contents of what is stored in the variable called message
# are shown.

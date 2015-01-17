#! /usr/bin/python
# Joe Deller 2014
# Changing our message variable using some of Python's methods

# Level : Beginner
# Uses  : Libraries, variables, methods

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

# Our original message
message = "Hello World"

# Just like our Minecraft remote has lots of buttons that do things
# Python variables have buttons (methods) that can do things
# We sent Minecraft a message using a variable
# Some of the things we can do with the variable are:

# Change all the letters into CAPITAL letters (upper case)
# Change all the letters from CAPITAL letters into non capital (lower) case

# To start with we are going to change our message into CAPITALS
# but we are going to create another variable to store this version of the
# message

# Create a new variable that converts all the letters in our original
# message to UPPER CASE ones
shout = message.upper()
mc.postToChat(shout)

# We can convert back to lower case
# This time we don't create a new variable or change our shout variable
# the contents of shout are converted to lower case first
# then postToChat uses the lower case message

mc.postToChat(shout.lower())

message = "I feel back to front!"

# We can turn our message backwards
# Unfortunately there isn't a reverse() keyword
# but Python has another way. We will look at exactly what this does later on

# As you learn more about programming, you will see there is usually
# more than one way of doing things, some will better than others
# but not always, while some will generally always be not the best

# You will also find a some people who spend more time arguing about
# the best way than they do writing code

backwards = message[::-1]
mc.postToChat(backwards)

# What do you think might happen if we did this
mc.postToChat(backwards[::-1])

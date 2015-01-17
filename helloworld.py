#! /usr/bin/python
# Joe Deller 2014
# Our first Minecraft program written in the Python language
# Level : Beginner
# Uses  : Libraries



# When learning any programming language there is a tradition of writing
# your first program to simply say "Hello World!"

# The very first line of this program tells the Raspberry Pi we are
# running a python program.

# The first thing we need to do is tell our program about the
# Minecraft Library and to find the Minecraft Manual in that library
# Without this, our program won't know anything about Minecraft

# Most languages can use libraries as a way of extending the things
# they can do.  They let us reuse other peoples hard work
# so that we don't have to redo it ourselves.
# Some libraries contain lots of information, some only a little

# On the Raspberry pi, the Minecraft library is fairly small
# but has enough that we can do lots of things
# The people that write Minecraft wrote a special version for the Raspberry Pi
# and a library that lets us do things with it.

# import is a Python language keyword.  It tells Python to do a very
# specific job.  In this case to find the Minecraft library
import mcpi.minecraft as minecraft

# Now we have found our Minecraft instruction manual
# we are going to look for the part that tells us how to control minecraft
# Then we make something called an object, in this case our object
# is a bit like a Smart TV remote control
# We also give it a nickname as any easy way of remembering which remote
# we mean.  In this case, we've called the remote "mc"
mc = minecraft.Minecraft.create()

# Just as a remote control has lots of buttons that do things
# our Minecraft remote control is very similar, except we call the buttons
# "methods"

# When we want to do something, we press the right button and Minecraft will do something
# Much like a smart TV remote searching for a YouTube video, we sometimes type something before
# pressing another button on the remote.
# The button (method) we are going to press is the postToChat button
# This will show us a message in Minecraft
# but before we press it, we need to decide what to say

# Just like writing a story, we use speech marks to enclose our message
# That way the program knows exactly where our message starts and stops

# You might have noticed, but most of the program so far has a #
# at the start of the line
# This tells the computer that the line is a comment for a human to read
# and it will ignore it, except in very special cases

# Good comments can help other people understand your program
# They can help remind you what your program does
# Bad comments can help confuse them

# Enough already, lets do something!
mc.postToChat("Hello World!")

# Notice the round brackets ()
# This tells the program that everything inside them is meant for the postToChat
# button
# It is a bit like an envelope when you write a letter.
# You put your letter inside the envelope and then post it.

# In this first program, we only send one piece of information
# but as we start to do more complex things,
# some buttons need lots of information before they will work
# This program only has three lines that actually do anything.
# The other 71 are comments like this.
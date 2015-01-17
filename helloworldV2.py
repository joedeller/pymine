#! /usr/bin/python
# Joe Deller 2014
# The hello world program with most of the comments removed

# Level : Beginner
# Uses  : Libraries


# Add a your own message after hello world
# Don't forget to keep the message inside the speech marks ""
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("Hello World!")

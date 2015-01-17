#! /usr/bin/python
# Joe Deller 2014
# Asking questions

# Level : Beginner
# Uses  : Libraries, variables, input

# This time we will get Python to ask us a question
# We store the answer in a variable and then
# add what we typed to the end of a message.

# This way we can say hello to everyone.
# Later on we will look at connecting the Raspberry Pi to a network
# As a quick preview, this version of HelloWorld
# will tell us it's name and network address

import mcpi.minecraft as minecraft
import socket
mc = minecraft.Minecraft.create()
name = raw_input('What is your name? ')

mc.postToChat("Hello " + name + ". Nice to meet you.")
mc.postToChat("My name is " + socket.gethostname() + " and my address is " + socket.gethostbyname(socket.getfqdn()))

#Functions do 3 things:
# 1. name pieces of code the way variables name strings and numbers
# 2. take arguments the way your scripts take argv
# 3. Using #1 and #2, they let you make your own "mini-scripts" or "tiny commands"

#Create a function by using the word "def", which is short for define

#Make 4 functions that work like your scripts:

# this function is being named "print_two" and is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1; %r, arg2: %r" % (arg1, arg2)
	
# ok, that * args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one arguments
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takes no arguments
def print_none():
	print "I got nothin'."
	
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

#notice that the def lines end in a colon and have indenting exactly 4 spaces
#in print_two, the first indented line unpacks the arguments 
#can skip the unpacking by naming what we want inside the (), as done in print_two_again 

#"commands" from previous exercises are actually just functions 

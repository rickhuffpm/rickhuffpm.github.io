#Functions and Files

#bring in argv function from Python set 
from sys import argv

#set 2 variable arguments for argv
script, input_file = argv

#define a function named print_all
#f is our variable for the file's name 
def print_all(f):
	print f.read()
	
#define a function named rewind and issue a seek commend for file f
def rewind(f):
	f.seek(0)

#define a function named print_a_line, bring in the command line_count and file f.  Print.	
def print_a_line(line_count, f):
	print line_count,f.readline()

#use current_file f and command to open it and place its contents in variable input_file
current_file = open(input_file)

#a little text
print "First let's print the whole file:\n"

#use print_all command on the current file f
print_all(current_file)

#preare to print the lines from the beginning by rewind to the start of f's content 
print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

#incrementally print one line at a time using the count from current_line and adding 1
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#a shortcut for writing the addition of another line count is current_line = 1; current_line += 1, although this may need an equivalent of a For statement 

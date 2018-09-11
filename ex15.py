#add a feature/command to your script from the Python feature set
#argv is argument variable - it holds the arguments you pass to your Python script when you run it
from sys import argv

#unpack the arguments from argv and assign them to the variables you can work with (script, filename)
script, filename = argv

#create a variable so that when used it executes the open command
txt = open(filename)

#print a little line
print "Here's your file %r:" % filename

#call a function on txt and command it to open a file and read/print its text
#blank parenthesis means do the command with no parameters
print txt.read()

#print a little line  
print "Type the filename again:"

#set a new variable for the user to input the filename (again) after prompt "> "
file_again = raw_input("> ")

##create a variable so that when used it executes the open command with parameter file_again 
txt_again = open(file_again)

#print the content from the open and read file set in the txt_again variable 
print txt_again.read()

#Commands (aka methods or functions) to remember
#close - closes the file like File->Save..in your editor
#read - reads the contents of the file, which you can assign the result to a variable
#readline - reads just on line of a text file
#truncate - empties the file (be careful if you care about this file)
#write(stuff) - writes stuff to the file



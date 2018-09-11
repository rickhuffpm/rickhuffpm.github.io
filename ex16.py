#add the argument command feature to your script
from sys import argv

#unlock 2 variables as part of argv 
script, filename = argv

#print a warning to the user about the filename they mention in their argument (python ex16.py TEST.TXT)
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#request the user to enter one of the two options ^C or RETURN
raw_input("?")

#create a variable (target) to conduct a command to open the user's chosen filename in "write mode"
print "Opening the file..."
target = open(filename, 'w')

#command to truncate the variable (which is the chosen file), which means to empty the file
print "Truncating the file.  Goodbye!"
target.truncate()

#type a line to let user know next steps
print "Now I'm going to ask you for three lines."

#enable user to enter desired strings/text into each line of their chosen file 
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

#let the user know
print "I'm going to write these to the file."

#command to write each line, followed by a new line parameter, into the file 
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#let the user know their file will now close.
print "And finally, we close it."
#command the variable to close
target.close()

from sys import argv

first, second, third = argv

print "What is your fourth variable?"
	fourth = raw_input()
print "What is your fifth variable?"
	fifth = raw_input()
print "What is your sixth variable?"
	sixth = raw_input()
	
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third
print "Your fourth variable is:", fourth
print "Your fifth variable is:", fifth
print "Your sixth variable is:", sixth

print "For your script %r, these are the variables: %r, %r, %r, %r, %r, and %r." % (ScriptName, first, second, third, fourth, fifth, sixth)


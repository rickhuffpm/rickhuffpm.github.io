name = 'Richard Huff'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

#Try some variables to convert the inches and pounds to centimeters and kilos.  
#Do not just type in the measurements. Work out the math in Python.
	
inches = 12.0
centimeters = inches * 2.54

print "%d inches equals %d centimeters." % (inches, centimeters)





#print "108 inches equals", inches / foot, "feet"
#print "36 feet equals", foot / yard, "yards"


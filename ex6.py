#setting values for the following 4 variables:
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y= "Those who know %s and those who %s." % (binary, do_not)

#telling the computer to list the values for 2 variables:
print x
print y

#placing those 2 variables each within a string 
print "I said: %r." % x 
print "I also said: '%s'." % y

#setting a False value to a fifth variable with sarcasm
hilarious = False

#setting a value to a sixth variable
joke_evaluation = "Isn't that joke so funny?! %r"

#combining the sixth variable with the variable which has the False value 
print joke_evaluation % hilarious

#setting two string values to two new variables 
w = "This is the left side of..."
e = "a string with a right side."

#show how to combine two variables, each with string values, into one apparent string 
print w + e 
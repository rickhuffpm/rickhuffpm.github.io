
print "What sentence would you like to play with to help you learn functions? (sentence = )"

#sentence = raw_input("Start by establishing variable 'sentence'")
#print "Once you have entered your sentence, type 'sentence' to return the value which you will use in next steps."
#print "Use the break_words function on 'sentence' and place the value into a new variable 'words'"

def	break_words(stuff):
    #This function will break up words for us.
    words = stuff.split(' ')
    return words

#Once you have the values for the split words within variable 'words',
#	sort them and place the value in a new variable 'sorted_words' using "sorted()" function.
def sort_words(words):
	"""Sorts the words."""
	return sorted(words) 

#Use this function to pop off and print the first word from the original sentence.
def print_first_word(words):
    """Prints the first word after popping it off."""
	#update the line below so that the pop function works on the "words" variable
    word = words.pop(0)
    print word

#Use this function to pop off and print the last word from the original sentence.
def print_last_word(words):
    """Prints the last word after popping it off."""
	#update the line below so that the pop function works on the "words" variable
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

#    """Prints the first and last words of the original sentence."""
def print_first_and_last(sentence):
	words = break_words(sentence)
   	print_first_word(words)
	print_last_word(words)
	

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
	


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)



#In this exercise, we're going to interact with your .py file inside the 
#     python interpreter you used periodically to do calculations.
#	    You run that from the shell like this:
#	python
#		  It returns Python version information...and then >>> prompt
#	At the >>>, you can then type Python code in and it will run immediately

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

#	(Python version info...)

#	>>> import ex25

#			You are making a module to use, which has all your functions in it.
#     TIP: Use "from ex25 import *" (rather than just typing 'ex25') to call up every function in ex25

#	>>> sentence = "All good things come to those who wait."

#			You made a sentence to work with.

#	>>> words

#			Calling up your first function named ex25.break_words
#			The 'dot' or 'period' tells Python "There's a function called 
#			break_words inside ex25, and I want to run it.

#	['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
	
#	>>> sorted_words = ex25.sort_words(words)
#	>>> sorted_words 

#			You are just running the sort_words function on the resulting 'words' 
#			and placing the value in a variable named sorted_words and calling it
#			to get a sorted sentence.
 
#	['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word
	
#	>>> ex25.print_first_word(words)
#	[All]

def print_last_word(words):
	"""Prints the last words after popping it off."""
	word = words.pop(-1)
	print word
	
#	>>> ex25.print_last_word(words)
#	[wait.]

#	>>> words
#	['good', 'things', 'come', 'to', 'those', 'who']

#			Notice that the first and last words we just printed are now missing.
#			Now lets do the samething with the sorted sentence.

#	>>> ex25.print_first_word(sorted_words)
#	[All]

#	>>> ex25.print_last_word(sorted_words)
#	[who]

#	>>> sorted_words
#	['come', 'good', 'things', 'those', 'to', 'wait.']

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

#	>>> sorted_words = ex25.sort_sentence(sentence)
#	>>> sorted_words	
#	['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
#	>>> ex25.print_first_and_last(sentence)
#	[
#	All
#	wait.
#	]

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

#	>>> ex25.print_first_and_last_sorted(sentence)
#	[
#	All
#	who
#	]

def break_words(stuff):
   return stuff.split(' ')
	#return words
	
def sort_words(words):
    return sorted(words)
	
def print_first_words(words):
    print words.pop(0)
	#print word

def print_last_word(words):
    word = words.pop(-1)
    return word
	
	
def sort_sentence(sentence):
    words =  break_words(sentence)
    return sort_words(words)
	
def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_words(words)
    print_last_word(words)
	
def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_words(words)
    print_last_word(words)

'''	
inp = raw_input("Enter String:")
print "Sorted String is:"
print sort_sentence(inp)
print "First and Last word of the string:"
print print_first_and_last(inp)
print "First and last sorted words:"
print print_first_and_last_sorted(inp)	
'''
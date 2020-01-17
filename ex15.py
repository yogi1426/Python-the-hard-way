from sys import argv
script, filename = argv
txt= open(filename)

print "Here is your filename: %s" % filename
print txt.read()
print "type again"
file_again = raw_input("--->")
txt_again = open(file_again)
print txt_again.read()
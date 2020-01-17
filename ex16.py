from sys import argv
script, filename=argv
print "we're goimg to erase %r" % filename
print "If you dont want that, hit CTRL-C(^C)."
print "If you dont want that, hit Return."

raw_input("?")
print "opening the file......................"
target= open(filename,'w')
print "truncating the file. goodbye!"
target.truncate()

print "Now I'm going to ask you for three line."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally"
target.close()

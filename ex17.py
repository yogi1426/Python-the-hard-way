from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "Copying from %s to  %s" % (from_file, to_file)
in_file = open(from_file)
indata = in_file.read()
print "the input file is %d bytes long" % len(indata)
print "does the output file exists? %r" % exists(to_file)
print "ready, hit return to continue, CTRL-C to abort. "
raw_input()# to hit enter here
out_file=open(to_file, 'w')
out_file.write(indata)
print "alright, all done."
out_file.close()
in_file.close()
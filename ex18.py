def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
def print_one(arg1):
    print "arg1 %r" % arg1
def print_none():
    print "I got nthing"
	
	
in1 = raw_input("enter first name:")
in2 = raw_input("enter second name")

print_two(in1, in2)
print_two_again(in1, in2)
print_one(in1)
print_none()

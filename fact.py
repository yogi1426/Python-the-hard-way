

def init(num):
    if(num == 1):
        return 1;
    else:
        return num * init(num-1);
		
		
n = int(raw_input("> Enter number to check : "))

print "Factorial of %d is %d" % (n,init(n))


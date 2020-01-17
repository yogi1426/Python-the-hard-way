n = int(raw_input("> Enter number to check : "))

x = n
s = 0

while n != 0:
    a = n%10
    s = s + a*a*a
    n = n/10
	
if s == x:
    print "Armstrong Number:"
else:
    print "NOT an Armstrong Number"
	
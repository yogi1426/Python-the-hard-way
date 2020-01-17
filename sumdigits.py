n = int(raw_input(" > Enter number"))
s = 0
x = n
while n != 0:
    a = n%10
    s = s + a
    n = n/10
	
print "Sum of digits: %d" %s	


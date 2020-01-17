def fact(num):
    if(num == 1):
        return 1;
    else:
        return num * fact(num-1);
		
n = int(raw_input(" > Enter number"))
s = 0
x = n
while n != 0:
    a = n%10
    s = s + fact(a)
    n = n/10
	
print "Sum of factorial of digits: %d" %s
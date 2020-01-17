n = eval(input("> Enter number to check : "))

x = n
s = 0
i = 0
while n != 0:
    a = int(n%2)
    t = (pow(10,i))
    s = s + a*t
    n = int(n/2)
    i = i+1
print ("Binary of %d is %d" % (x,s))
while n != 0:
    a = int(n%8)
    t = pow(10,i)
    s = s + a*t
    n = int(n/8)
    i = i+1
	
print ("octal of %d is %d" % (x,s))

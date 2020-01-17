n = int(raw_input("> Enter number to check : "))

x = n
s = 0
b = n%10
while n != 0:
    a = n%10
    s = a
    n=n/10
	
sum = s + b

print "Sum of first and last digit..is %d" %sum

n = int(raw_input("> Enter number to check : "))

flag = 0
for i in range(2,n):
    if n%i == 0:
        flag = 1
        break;
	

if flag == 1:
    print "not a prime"
	
else:
    print "prime"
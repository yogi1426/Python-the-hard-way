m = int(raw_input("> Enter number 1. "))
n = int(raw_input("> Enter number 2 : "))

for i in range(m, n+1):
    x = i
    s=0
    while i != 0:
        a = i%10
        s = s + a*a*a
        i = i/10

    if s==x:
        print x
		
		
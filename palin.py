n = eval(input("> Enter number to check : "))

x = n
s = 0

while n != 0:
    a = int(n % 10)
   
    s = ( s*10 + a)
    n=int(n/10)



	
if s==x:
    print ("Palindrome Number")
	
else:
    print ("Not Palindrome Number")	


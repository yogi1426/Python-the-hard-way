s = raw_input("> ENter String:")

x = list(s)
c = 0
v = 0
for i in range(len(s)):

    if x[i]=='a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i]=='u':
        c = c+1
    	
    else:
        v = v+1
	
print "Number of vowels in String" , c
	
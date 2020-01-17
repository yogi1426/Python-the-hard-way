def palin(String1):

	str1 = list(String1)
	s1 = list(String1)
	s1.reverse()
	if str1==s1:
		return '1'
	else:
		return '0'
		
		
s = input("\n  Enter String\n ")
a = 0
l = s.split(' ')
n = len(l)
for i in range(n):
    m = palin(l[i])
    if m == '1':
        print (l[i])
   	
		
		

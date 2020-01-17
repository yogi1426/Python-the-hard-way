n = raw_input("\n > Enter String")
s = list(n.upper())
t = len(s)
m = int(raw_input("\n Enter number to shift\n")

for i in range(t):

    l = ord(str[i]) + m
    if l > 90:
        l = l - 26
        print chr(l)
    elif l < 65:
        l = l + 26
        print chr(l)	
		

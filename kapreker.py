m = raw_input("> Enter no. to check for Kapriker Number")
n = int(m)
sq = pow(n,2)

s1 = str(sq)

t = len(s1)
a=s1[0:t/2]
b=s1[t/2:t+1]

c = int(a)
d = int(b)

sum = c+d

if(sum == n):
    print "Kapriker Number"
else:
    print "Not a kapriker number"
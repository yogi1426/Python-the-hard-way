s = raw_input("\n > Enter String\n ")
str1 = list(s)
t = len(str1)

for i in range(t):
    if str1[i] >= 'a' and str1[i] <= 'z':
        print str1[i].upper()
    else:
        print str1[i].lower()

s = raw_input("\n > Enter String")
arr = s.split(' ')
t = len(arr)
for i in range(t):
    print "length of %s is %d " % (arr[i], len(arr[i]))

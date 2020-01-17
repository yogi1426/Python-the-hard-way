n = raw_input("\n > Enter numbers in an array seperated by space\n")

num = n.split()
t = len(num)
last = t-1
beg = 0
flag = '0'
target = raw_input("Enter Target Input")
while beg <= last:
    mid = (beg+last)/2
    if num[mid] > target:
        beg = mid + 1
    elif num[mid] < target:
        last = mid-1
    else:
        flag = '1'
        break;

if flag == '1':
    print "found"
else:
    print "Not Found"
	
	
def prime(n):
    flag = 0
    for i in range(2,n):
        if n%i == 0:
            flag = 1
            break
    if flag is 1:
        return -1
    else:
        return 1

def palin(n):
    x = n
    s = 0

    while n != 0:
        a = int(n % 10)
        s = s*10 + a
        n=int(n/10)
	
    if s==x: 
        return 1
    else:
        return -1

n = eval(input())
if (prime(n) is 1 and palin(n) is 1):
    print ("prime palindrome ")
else:
    print("not")

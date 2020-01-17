


size = eval(input("Enter Size\t"))
n = input(">>>>>>")
array = n.split()

sum = 0
for i in range(size):
    sum = sum + int(array[i])


print ("Sum is {}".format(sum))

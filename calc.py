print "Calculator:\n"
print "Welcome:\n"
print "Choose Options from below to do the calculations:\n\n"
print "1. Addition.\n 2. Substraction\n 3.Multiplication\n 4.Division\n 5. Modulous \n"
ch = raw_input("> ")

if ch == '1':
    print "Enter two numbers to add."
    a = raw_input(">First Number")
    b = raw_input(">Second Number")
    print "Sum of %d and %d is:" % a,b
    print "\t", a+b
	
elif ch == '2':
    print "Enter two numbers to Substract."
    a = raw_input(">First Number")
    b = raw_input(">Second Number")
    print "Difference of %d and %d is:" % a,b
    print "\t", a-b
	
elif ch == '3':
    print "Enter two numbers to Multiply."
    a = int(raw_input(">First Number"))
    b = int(raw_input(">Second Number"))
    print "PRODUCT of %d and %d is:" % (a, b)
    print "\t", a * b
	
elif ch == '4':
    print "Enter two numbers to Divide."
    a = int(raw_input(">First Number"))
    b = int(raw_input(">Second Number"))
    print "Dividend of %d and %d is:" % (a, b)
    print "\t", a/b
	
elif ch == '5':
    print "Enter two numbers to get Modulous."
    a = raw_input(">First Number")
    b = raw_input(">Second Number")
    print "Modulous of %d and %d is:" % a,b
    print "\t", a%b
	
else:
    print "The Choice was invalid"
	

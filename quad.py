a = float(raw_input("> Enter Coeff. of x^2")
b = float(raw_input("> Enter Coeff. of x")
c = float(raw_input("> Enter Constant")

d = float(b**2 - 4*a*c)

if d > 0:
    t = sqrt(d)
    x1 = (-b - t)/(2 * a)
    x2 = (+b + t)/(2 * a)
    print "roots are real and Imaginary", x1 "+" x2
	
elif d == 0:
    x1 = -b/(2 * a)
    x2 = x1
	print "ROots are real and unequal : %d + %d" %(x1, x2)
	
else:
    print "Roots are imaginary"
	

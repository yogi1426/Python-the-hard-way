def cheese_and_crackers(cheese_count, boxes_of_crackers):
  #"u have %d cheese" % cheese_count
	 print "you have %d boxes of crackrs" % boxes_of_crackers
	 print "Man thats enough for a party"
	 print "Get a blanket. \n"
	
	
print "we can just give the function numbers directly:"	
cheese_and_crackers(20, 30)

print "or, we can use variables from our script:"
amountcheese = 10
amountcrackers = 50
cheese_and_crackers(amountcheese, amountcrackers)
print "We can even do math inside:"
cheese_and_crackers(10 + 2, 5 + 6)
print "and we can combine"
cheese_and_crackers(amountcheese +100, amountcrackers +1000)
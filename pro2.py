i =  5
enter = int(raw_input("\n \n > What is your guess?"))

if i != enter:
    print "Your guess is wrong"
    if enter < i:
        print "The number is little higher.."
    else:
        print "the number is little lower.."

	
else:
    print "You guessed it correctly..congrats.."
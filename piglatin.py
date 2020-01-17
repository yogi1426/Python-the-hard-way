n = raw_input("\n > Enter String in Uppercase\n")

inp = list(n)
t=len(inp)

y = ' '
for i in range(t):
    if inp[i] == 'A' or inp[i] == 'E' or inp[i] == 'I' or inp[i] == 'O' or inp[i] == 'U':
        x =  inp[i:t+1]
        z=str(x)
        break
        
    else:
        y = y + inp[i]

print ''.join(x)+ y + "AY"
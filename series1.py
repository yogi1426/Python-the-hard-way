n = int(raw_input("\n Enter n\n"))
c=0
for i in range(2, n, 2):
    c = c+1
    if c%2==0:
        print -i
    
    else:
        print +i
    


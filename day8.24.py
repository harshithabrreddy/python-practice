#Enter the value of n:5
#E E E E E 
#D D D D D 
#C C C C C
#B B B B B
#A A A A A
n=int(input('Enter the value of n:'))
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(chr(i+64),end="")
    print()
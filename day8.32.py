#Enter the value of n:4
n=int(input('Enter the value of n:'))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(j+64),end="")
    print()
#Enter the value of n:4
#A
#B B
#C C C
n=int(input('Enter the value of n:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
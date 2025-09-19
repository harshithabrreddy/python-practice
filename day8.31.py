#Enter the value of n:4
#a
#a b
#a b c
n=int(input('Enter the value of n:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+96),end=" ")
    print()
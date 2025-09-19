#Enter the value of n:5
#A  A  A  A  A
#*  *  *  *  *
#C  C  C  C  C
#*  *  *  *  *
#E  E  E  E  E
n=int(input('Enter the value of n:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i%2==0):
            print("*",end=" ")
        else:
            print(chr(64+i),end=" ")
    print()
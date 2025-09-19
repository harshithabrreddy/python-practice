#Enter the value of n:5
#A B C D E 
#A B C D E
#A B C D E
n=int(input('Enter the value of n:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(j+64),end="")
    print()
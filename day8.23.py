# enter 
#A A A A
#B B B B
n=int(input('Enter the value of n:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(i+64),end="")
    print()


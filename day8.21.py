#Enter the  value of n:5
#   1
#  1 2
# 1 2 3
# 1 2 3 4
#1 2 3 4 5
# 1 2 3 4
#  1 2 3
#   1 2
#    1
n=int(input('Enter the value of n:'))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(f"{j} ",end="")
    print()
    for i in range(n-1,0,-1):
        print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(f"{j} ",end="")
print()

    

#Enter the value of n:5
#   *
#  **
# ***
n=int(input('Enter the value of n:')) 
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i) 
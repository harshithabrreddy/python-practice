#enter the value of n:5  
#     *
#    **
#   ***
#  ****
n=int(input('Enter the value of n:'))
for i in range(1,n+1):
    for j in range(n,i,-1):
      print(" " ,end="")
    for k in range (1,i+1):
      print("*",end="")
    print()

#another method
n=int(input('Enter the value of n:'))
for i in range(1,n+1):
   print(""*(n-i)+"*"*i)
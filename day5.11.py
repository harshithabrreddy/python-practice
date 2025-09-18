#check the  prime number or not
num=int(input('Enter the integer value:'))
factor=0
for i in range(num+1):
    if(num%i==0):
        factor+=1
res="Prime Number" if(factor==2)else"Not a Prime Number"
print(f"{num} is {res}")
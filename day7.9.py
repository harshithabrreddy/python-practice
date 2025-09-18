#even num and odd num without using loops and conditional statements
num=list(map(int,input("Enter the numbers:").split()))
even=list(filter(lambda i:i%2==0,num))
odd=list(filter(lambda i:i%2==0,num))
print(f"User Entered List:{num}")
print(f"Even List:{even}")
print(f"Odd List :{odd}")
num1 = int(input("Enter the a integer: "))
num2 = int(input("Enter the a integer: "))

# Compare and find the largest Number
if (num1 > num2):
    print(f"The largest number is {num1}")
else:
    print(f"The largest number is {num2}")
#ternary operator
res=num1 if(num1>num2) else num2 
print(f"{res} is largest number")    



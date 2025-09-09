num1 = int(input("Enter the a integer: "))
num2 = int(input("Enter the a integer: "))
num3= int (input("Enter the a integer:"))

# if-elif else
if(num1 > num2) and (num1>num3):
    print(f"{num1} is the largest number ")
elif(num2>num1 and num2>num3):
    print(f"{num2}is the largest number ")
else:
    print(f"{num3} is the largest number")
#ternary operator
largest=num1 if(num1>num2 and num1>num3 ) else num2 
res=num3 if (num3>num1 and num3>num2) else largest
print(f"{res} is  the largest number")    
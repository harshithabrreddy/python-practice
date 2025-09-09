a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# if-else 
if (a > b and a < c) or (a > c and a < b):
   print("a is a middle number")
elif (b > a and b < c) or (b > c and b < a):
    print("b is a middle number")
else:
    print("c is a middle number")
# Using ternary operator
middle = (a if (a > b and a < c) or (a > c and a < b) 
                  else (b if (b > a and b < c) or (b > c and b < a) 
                        else c))
print("Middle number :")
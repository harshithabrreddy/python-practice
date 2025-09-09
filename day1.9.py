a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# if-else
if a <= b and a <= c:
    print("a is a smallest number")
elif b <= a and b <= c:
    print("b is a smallest number")
else:
    print("c is a smallest number")

#  Ternary Operator 
smallest = a if (a <= b and a <= c) else (b if b <= c else c)
print("Smallest number:")



#
a=input(input("Enter the value of first integer:"))
b=input(input("Enter the value of second integer:"))
print(f"a={a}")
print(f"b={b}")
#first logic
a=a+b
b=a-b
a=a-b
print("After Swapping")
print(f"a={a}")
print(f"b={b}")
#second logic(temporary variable)
temp=a
a=b
b=temp
print("After Swapping")
print(f"a={a}")
print(f"b={b}")
#Third Logic
a,b=b,a
print("After swapping:")
print(f"a={a}")
print(f"b={b}")


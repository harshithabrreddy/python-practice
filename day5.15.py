# Swapping two integers in different ways
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("\nOriginal values: a =", a, ", b =", b)
# Using arithmetic operators
a = a + b
b = a - b
a = a * b
print("\nAfter swapping using arithmetic operators:")
print("a =", a, ", b =", b)
# Reset values for next method
a = int(input("\nEnter first number again: "))
b = int(input("Enter second number again: "))
#  Using a third variable
temp = a
a = b
b = temp
print("\nAfter swapping using a third variable:")
print("a =", a, ", b =", b)
# Reset values for next method
a = int(input("\nEnter first number again: "))
b = int(input("Enter second number again: "))
#  Without using a third variable (Python tuple unpacking)
a, b = b, a
print("\nAfter swapping without using a third variable (tuple unpacking):")
print("a =", a, ", b =", b)
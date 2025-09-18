# Python program to count even and odd numbers in a list
numbers = [10, 23, 45, 66, 78, 99, 100, 7]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Numbers in the list:", numbers)
print("Count of even numbers:", even_count)
print("Count of odd numbers:", odd_count)